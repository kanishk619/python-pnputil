from ctypes import (
    GetLastError, WinError, resize, byref, sizeof, wstring_at,
)

from winapi.common.constants import n
from winapi.common.winerror_h import ERROR_INVALID_USER_BUFFER, ERROR_INSUFFICIENT_BUFFER, ERROR_FILE_NOT_FOUND
from winapi.common.datatypes import BYTE, HDEVINFO, DWORD, ULONG, WCHAR
from winapi.guid import GUID
from winapi.setupapi.api import *
from winapi.setupapi.constants import *
from winapi.setupapi.models.device import Device
from winapi.setupapi.structs import DEVPROPKEY, SP_DEVICE_INTERFACE_DATA, SP_DEVINFO_DATA, \
    SP_DEVICE_INTERFACE_DETAIL_DATA_W
from winapi.utils import IS_PYTHON_64


__all__ = [
    'get_device_interface_detail', 'get_device_property', 'get_device_property_keys', 'enumerate_device_interfaces',
    'get_inf_driver_store_location'
]


class Error(Exception):
    def __init__(self, message):
        super().__init__(message)


def get_device_interface_detail(
        device_info_set: HDEVINFO,
        device_interface_data: SP_DEVICE_INTERFACE_DATA,
        with_device=False) -> tuple[SP_DEVICE_INTERFACE_DETAIL_DATA_W, Device]:
    """
    `This returns SP_DEVICE_INTERFACE_DETAIL_DATA buffer from where DevicePath can be accessed via str(buffer)`

    :param device_info_set: HDEVINFO
    :param device_interface_data: SP_DEVICE_INTERFACE_DATA obj
    :param with_device: boolean, default=False. If true, a device object is also returned
    :return: tuple(SP_DEVICE_INTERFACE_DETAIL_DATA, None/Device)
    """
    buffer_size = ULONG()  # allocate space to retrieve size of device path

    # This call will retrieve the size required for the buffer to store the devicepath later
    res = SetupDiGetDeviceInterfaceDetail(
        device_info_set,
        byref(device_interface_data),
        None,  # This parameter must be NULL if DeviceInterfaceDetailSize is zero
        0,  # This parameter must be zero if DeviceInterfaceDetailData is NULL.
        byref(buffer_size),
        None
    )
    assert all([res == 0, GetLastError() == ERROR_INSUFFICIENT_BUFFER]), WinError()

    device_interface_detail_data = SP_DEVICE_INTERFACE_DETAIL_DATA_W()
    if IS_PYTHON_64:
        device_interface_detail_data.cbSize = sizeof(SP_DEVICE_INTERFACE_DETAIL_DATA_W)
    else:
        device_interface_detail_data.cbSize = 6  # if ERROR_INVALID_USER_BUFFER is raised, reduce or increase this

    resize(device_interface_detail_data, buffer_size.value)  # re-adjust buffer size of idd

    device_info_data = SP_DEVINFO_DATA()
    device_info_data.cbSize = sizeof(SP_DEVINFO_DATA)

    res = SetupDiGetDeviceInterfaceDetail(
        device_info_set,
        byref(device_interface_data),
        byref(device_interface_detail_data),
        buffer_size,
        None,
        byref(device_info_data)
    )
    assert all([res == 1, GetLastError() != ERROR_INVALID_USER_BUFFER]), WinError()
    if with_device:
        return device_interface_detail_data, Device(device_info_set, device_info_data)
    else:
        return device_interface_detail_data, None


def enumerate_device_interfaces(device_info_set: HDEVINFO, guid: GUID) -> SP_DEVICE_INTERFACE_DATA:
    """
    `This function yields SP_DEVICE_INTERFACE_DATA obj`

    :param device_info_set: HDEVINFO obj
    :param guid: GUID obj
    """
    device_interface_data = SP_DEVICE_INTERFACE_DATA()
    device_interface_data.cbSize = sizeof(SP_DEVICE_INTERFACE_DATA)

    member_index = 0

    while True:
        res = SetupDiEnumDeviceInterfaces(
            device_info_set,
            None,
            byref(guid),
            member_index,
            byref(device_interface_data)
        )
        if GetLastError() == ERROR_NO_MORE_ITEMS:
            break
        assert res == bool(1), WinError()
        member_index += 1

        yield device_interface_data


def get_device_property(
        device_info_set: HDEVINFO,
        device_info_data: SP_DEVINFO_DATA,
        key: DEVPROPKEY) -> [(BYTE * n)(), int]:
    """
    `Get specific property value and type by providing property key`

    :param device_info_set: HDEVINFO
    :param device_info_data: SP_DEVINFO_DATA obj
    :param key: DEVPROPKEY obj
    :return: tuple(c_byte_Array, property_type)
    """
    buffer_size = DWORD()
    property_type = ULONG()

    # First call to get size of buffer required to store the value
    r = SetupDiGetDeviceProperty(
        device_info_set,
        byref(device_info_data),
        byref(key),
        byref(property_type),
        None,
        0,
        byref(buffer_size),
        0
    )

    if GetLastError() == 1168: return None, property_type.value
    assert all([r == 0, GetLastError() == ERROR_INSUFFICIENT_BUFFER]), WinError()

    property_buffer = (BYTE * buffer_size.value)()
    # actual call to populate the above buffer with value
    r = SetupDiGetDeviceProperty(
        device_info_set,
        byref(device_info_data),
        byref(key),
        byref(property_type),
        property_buffer,
        buffer_size,
        None,
        0
    )

    if GetLastError() == 1168: return None, property_type.value
    assert all([r == 1, GetLastError() == 0]), WinError()

    return property_buffer, property_type.value


def get_device_property_keys(
        device_info_set: HDEVINFO,
        device_info_data: SP_DEVICE_INTERFACE_DATA) -> (DEVPROPKEY * n):
    """
    Get all available property keys for a device
    :param device_info_set: HDEVINFO
    :param device_info_data: SP_DEVICE_INTERFACE_DATA obj
    :return: c_byte_Array(n)
    """
    required_property_key_count = DWORD()
    # First call to get number of property keys for a device
    r = SetupDiGetDevicePropertyKeys(
        device_info_set,
        byref(device_info_data),
        None,
        0,
        required_property_key_count,
        0
    )
    assert all([r == 0, GetLastError() == ERROR_INSUFFICIENT_BUFFER])

    property_key_array = (DEVPROPKEY * required_property_key_count.value)()
    # actual call to populate the above array with property keys
    r = SetupDiGetDevicePropertyKeys(
        device_info_set,
        byref(device_info_data),
        property_key_array,
        len(property_key_array),
        None,
        0
    )
    assert all([r == 1, GetLastError() == 0])
    return property_key_array


def get_inf_driver_store_location(inf_file_name: str) -> str:
    """
    `The function retrieves INF file's driver store location`

    :param inf_file_name: A string representing the inf filename (oemXX.inf)
    :return: The inf file driver store path (C:\windows\System32\DriverStore\FileRepository\abcd\oemXX.inf)
    """
    if not inf_file_name: return None
    required_size = ULONG(0)
    r = SetupGetInfDriverStoreLocation(
        inf_file_name,
        None,
        None,
        None,
        0,
        required_size
    )
    assert r == 0, GetLastError()
    inf_path_buffer = (WCHAR * required_size.value)()
    r = SetupGetInfDriverStoreLocation(
        inf_file_name,
        None,
        None,
        inf_path_buffer,
        sizeof(inf_path_buffer),
        None
    )

    if r == 0 and GetLastError() == ERROR_FILE_NOT_FOUND:
        return None

    assert r == 1, GetLastError()
    return wstring_at(inf_path_buffer)
