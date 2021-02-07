from ctypes import create_unicode_buffer, byref, wstring_at, sizeof

from winapi.cfgmgr32.api import *
from winapi.cfgmgr32.constants import CR, CM_GETIDLIST_FILTER_NONE, CM_ENUMERATE_CLASSES_INTERFACE, \
    CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES, CM_GET_DEVICE_INTERFACE_LIST_PRESENT, CM_LOCATE_DEVNODE_NOVALIDATION
from winapi.cfgmgr32.datatypes import *
from winapi.setupapi.devpkey import *
from winapi.utils import unicode_buffer_to_string_array

__all__ = [
    'enumerate_classes', 'get_device_id', 'get_device_id_list', 'get_device_id_list_size', 'get_device_id_size',
    'get_device_interface_alias', 'get_device_interface_list', 'get_device_interface_list_size',
    'get_device_interface_property', 'get_device_property', 'locate_dev_node'
]


def locate_dev_node(device_instance_id: str) -> DEVINST:
    """
    `The function retrieves device instance.`

    :param device_instance_id: A string representing a device instance ID. If this value is NULL, or if it points to a
        zero-length string, the function retrieves a device instance handle to the device at the root of the device
        tree.
    :return: A device instance
    """
    device_instance = DEVINST()
    r = CM_Locate_DevNode(
        byref(device_instance),
        device_instance_id,
        CM_LOCATE_DEVNODE_NOVALIDATION
    )
    assert r == CR.SUCCESS, WindowsError(r, CR(r).name)
    return device_instance


def get_device_interface_property(device_interface: str, key: DEVPROPKEY) -> tuple[bytes, int]:
    """
    `The function retrieves a device property that is set for a device interface.`

    :param device_interface: The device interface instance path
    :param key: The device interface property key
    :return: c_type unicode buffer
    """
    property_type = ULONG(0)
    buffer_size = ULONG(0)
    r = CM_Get_Device_Interface_Property(
        device_interface,
        byref(key),
        byref(property_type),
        None,
        byref(buffer_size),
        0
    )

    assert r == CR.BUFFER_SMALL, WindowsError(r, CR(r).name)

    property_buffer = (BYTE * buffer_size.value)()
    r = CM_Get_Device_Interface_Property(
        device_interface,
        byref(key),
        byref(property_type),
        property_buffer,
        byref(buffer_size),
        0
    )
    if r == CR.NO_SUCH_VALUE: return None, property_type.value
    assert r == CR.SUCCESS, WindowsError(r, CR(r).name)
    return property_buffer, property_type.value


def get_device_interface_alias(device_interface: str, alias_interface_guid: GUID) -> str:
    """
    `The function returns the alias of the specified device interface instance, if the alias exists.`

    :param device_interface: A string representing device interface instance for which to retrieve an alias. The caller
        typically received this string from a call to get_device_interface_list, or in a PnP notification structure.
    :param alias_interface_guid: A GUID object specifying the interface class of the alias to retrieve.
    :return: A string containing the name of the alias. The caller must free this string when it is no longer needed.
    """
    buf_len = ULONG(0)
    r = CM_Get_Device_Interface_Alias(
        device_interface,
        byref(alias_interface_guid),
        (WCHAR * 1)(),
        byref(buf_len),
        0
    )
    assert r == CR.BUFFER_SMALL, WindowsError(r, CR(r).name)

    alias_device_interface = (WCHAR * buf_len.value)()
    r = CM_Get_Device_Interface_Alias(
        device_interface,
        byref(alias_interface_guid),
        alias_device_interface,
        byref(buf_len),
        0
    )
    assert r == CR.SUCCESS, WindowsError(r, CR(r).name)
    return wstring_at(alias_device_interface)


def get_device_interface_list_size(interface_class_guid: GUID,
                                   device_id: str = None,
                                   ul_flags=CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES) -> int:
    """
    `The function retrieves the buffer size that must be passed to the get_device_interface_list function.`

    :param interface_class_guid: Device interface class GUID
    :param device_id: Caller-supplied string that represents a device instance ID. If specified, the function
        retrieves the length of symbolic link names for the device interfaces that are supported by the device, for
        the specified class. If this value is NULL, or if it points to a zero-length string, the function retrieves
        the length of symbolic link names for all interfaces that belong to the specified class.
    :param ul_flags: CM_GET_DEVICE_INTERFACE_LIST_PRESENT or CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES (default)
    :return: Size requred for creating buffer to store the device interface list
    """
    list_size = ULONG(0)
    r = CM_Get_Device_Interface_List_Size(
        list_size,
        interface_class_guid,
        device_id if device_id else None,
        ul_flags
    )
    assert r == CR.SUCCESS, WindowsError(r, CR(r).name)
    return list_size.value


def get_device_interface_list(interface_class_guid: GUID,
                              device_id: str = None,
                              present=False) -> list[str]:
    """
    `The function retrieves a list of device interface instances that belong to a specified device interface class.`

    :param interface_class_guid: Device interface class GUID.
    :param device_id: Caller-supplied string that represents a device instance ID. If specified, the function retrieves
        device interfaces that are supported by the device for the specified class. If this value is NULL, or if it
        points to a zero-length string, the function retrieves all interfaces that belong to the specified class.
    :param present: If set to true, only available device instances will be retrieved.
    :return: A list of device interfaces based on the ul_flags
    """
    ul_flags = CM_GET_DEVICE_INTERFACE_LIST_PRESENT if present else CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES
    buffer_len = get_device_interface_list_size(interface_class_guid, device_id, ul_flags)
    buffer = create_unicode_buffer(buffer_len)
    r = CM_Get_Device_Interface_List(
        interface_class_guid,
        device_id if device_id else None,
        buffer,
        buffer_len,
        ul_flags
    )
    assert r == CR.SUCCESS, WindowsError(r, CR(r).name)
    return unicode_buffer_to_string_array(buffer)


def get_device_property(device_instance: DEVINST, key: DEVPROPKEY) -> tuple[bytes, int]:
    """
    `The function retrieves a device instance property.`

    :param device_instance: A string representing device instance, can be acquired from locate_dev_node.
    :param key: DEVPROPKEY structure that represents the device property key of the requested device instance property.
    :return: tuple(property_value_buffer, property_type)
    """
    buffer_size = DWORD()
    property_type = ULONG()

    r = CM_Get_DevNode_Property(
        device_instance,
        byref(key),
        byref(property_type),
        None,
        byref(buffer_size),
        0
    )
    assert r == CR.BUFFER_SMALL, WindowsError(r, CR(r).name)

    property_buffer = (BYTE * buffer_size.value)()
    r = CM_Get_DevNode_Property(
        device_instance,
        byref(key),
        byref(property_type),
        property_buffer,
        byref(buffer_size),
        0
    )
    if r == CR.NO_SUCH_VALUE: return None, property_type.value
    assert r == CR.SUCCESS, WindowsError(r, CR(r).name)
    return property_buffer, property_type.value


def get_device_id_size(dev_inst: DEVINST) -> int:
    """
    `The function retrieves the buffer size required to hold a device instance ID for a device instance on the
    local machine.`

    :param dev_inst: A device instance
    :return: The size required for the buffer to hold the device instance id for the provided device instance
    """
    buffer_size = ULONG()
    r = CM_Get_Device_ID_Size(
        byref(buffer_size),
        dev_inst,
        0
    )
    assert r == CR.SUCCESS, WindowsError(r, CR(r).name)
    return buffer_size.value


def get_device_id(dev_inst: DEVINST) -> str:
    """
    `The function retrieves the device instance ID for a specified device instance on a local machine.`

    :param dev_inst: A device instance
    :return: A device instance id for the provided device instance
    """
    buffer_size = get_device_id_size(dev_inst)
    buffer = create_unicode_buffer(buffer_size + 1)  # Extra padding for null termination
    r = CM_Get_Device_ID(
        dev_inst,
        buffer,
        buffer_size,
        0
    )
    assert r == CR.SUCCESS, WindowsError(r, CR(r).name)
    return wstring_at(buffer)


def get_device_id_list_size(filter_keyword=None, ul_flags=CM_GETIDLIST_FILTER_NONE) -> int:
    """
    `The function retrieves the buffer size required to hold a list of device instance IDs for the local machine's
    device instances.`

    :param filter_keyword: Caller-supplied string specifying a subset of the machine's device instance identifiers, or NULL.
        See the following description of ulFlags.
    :param ul_flags: One of the optional, caller-supplied bit flags that specify search filters. If no flags are
        specified, the function supplies the buffer size required to hold all instance identifiers for all device
        instances. For a list of bit flags, see the ulFlags description for CM_Get_Device_ID_List.
    :return: The size of the buffer required to store device id list
    """
    list_size = ULONG(0)
    r = CM_Get_Device_ID_List_Size(
        list_size,
        filter_keyword,
        ul_flags,
    )
    assert r == CR.SUCCESS, WindowsError(r, CR(r).name)
    return list_size.value


def get_device_id_list(filter_keyword=None, ul_flags=CM_GETIDLIST_FILTER_NONE) -> list[str]:
    """
    `The function retrieves a list of device instance IDs for the local computer's device instances.`

    :param filter_keyword: Caller-supplied string specifying a subset of the machine's device instance identifiers,
        or NULL. See the following description of ulFlags.
    :param ul_flags: One of the optional, caller-supplied bit flags that specify search filters. If no flags are
        specified, the function supplies the buffer size required to hold all instance identifiers for all device
        instances. For a list of bit flags, see the ulFlags description for CM_Get_Device_ID_List.
    :return: The size of the device id list
    """
    list_size = get_device_id_list_size(filter_keyword, ul_flags)
    buffer = create_unicode_buffer(list_size)
    r = CM_Get_Device_ID_List(
        filter_keyword if filter_keyword else None,
        buffer,
        sizeof(buffer),
        ul_flags
    )
    assert r == CR.SUCCESS, WindowsError(r, CR(r).name)
    return unicode_buffer_to_string_array(buffer)


def enumerate_classes(class_guid: GUID = None, ul_flags=CM_ENUMERATE_CLASSES_INTERFACE) -> GUID:
    """
    `The function yields the local machine's installed device classes.`

    :param class_guid: A device setup/interface class guid. If none, all interfaces will be returned
    :param ul_flags: CM_ENUMERATE_CLASSES_INTERFACE or CM_ENUMERATE_CLASSES_INSTALLER
    """
    class_guid = class_guid if class_guid else GUID()
    index = ULONG(0)
    while (r := CM_Enumerate_Classes(index, byref(class_guid), ul_flags)) != CR.NO_SUCH_VALUE:
        index.value += 1
        assert r == CR.SUCCESS, WindowsError(r, CR(r).name)
        yield class_guid
