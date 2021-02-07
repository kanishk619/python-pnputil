from ctypes import WinError, sizeof, byref

from winapi.common.constants import INVALID_HANDLE_VALUE
from winapi.common.datatypes import ULONG
from winapi.guid import GUID
from winapi.setupapi.api import SetupDiGetClassDevs, SetupDiDestroyDeviceInfoList, SetupDiEnumDeviceInfo
from winapi.setupapi.constants import DIGCF
from winapi.setupapi.api_wrappers import enumerate_device_interfaces, get_device_interface_detail
from winapi.setupapi.models import Device
from winapi.setupapi.models.device import DeviceInitError
from winapi.setupapi.structs import SP_DEVINFO_DATA


__all__ = ['resolve_device_interfaces_via_guid', 'all_devices']


def resolve_device_interfaces_via_guid(guid: GUID, present=False) -> list:
    """
    Resolve device GUID to device symbolic link. winapi.cfgmgr32.helper.get_device_interface_list is faster

    :param present: Only list interfaces which are present
    :param guid: GUID obj
    :return: List of interfaces available for the device GUID
    """
    if not isinstance(guid, GUID):
        raise TypeError("parameter must be instance of GUID")

    device_info_set = SetupDiGetClassDevs(
        byref(guid),
        None,
        None,
        DIGCF.DEVICEINTERFACE | (DIGCF.PRESENT if present else 0x0)
    )

    assert device_info_set != INVALID_HANDLE_VALUE, WinError()

    device_interfaces = []
    for device_interface_data in enumerate_device_interfaces(device_info_set, guid):
        device_interface_detail_data, d = get_device_interface_detail(device_info_set, device_interface_data)
        device_interfaces.append(device_interface_detail_data)
    SetupDiDestroyDeviceInfoList(device_info_set)
    return device_interfaces


def all_devices(class_guid: str = None, flags=DIGCF.ALLCLASSES) -> Device:
    """
    Yields all available devices based on flags
    :param class_guid: GUID string for a device setup class or a device interface class.
    :param flags: DICGF flags, default: DIGCF_ALLCLASSES
    """
    class_guid = GUID.from_guid_string(class_guid) if class_guid else None
    device_info_set = SetupDiGetClassDevs(
        class_guid,
        None,
        None,
        flags
    )
    assert device_info_set != INVALID_HANDLE_VALUE, WinError()

    device_info_data = SP_DEVINFO_DATA()
    device_info_data.cbSize = sizeof(SP_DEVINFO_DATA)
    device_index = ULONG(0)

    while SetupDiEnumDeviceInfo(device_info_set, device_index, byref(device_info_data)):
        device_index.value += 1
        try:
            yield Device(device_info_set, device_info_data)
        except DeviceInitError:
            continue

    SetupDiDestroyDeviceInfoList(device_info_set)
