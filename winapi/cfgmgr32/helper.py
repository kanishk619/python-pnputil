from winapi.cfgmgr32.api_wrappers import get_device_interface_list, enumerate_classes, locate_dev_node, \
    get_device_id_list
from winapi.cfgmgr32.constants import CM_ENUMERATE_CLASSES_INTERFACE, CM_GETIDLIST_FILTER_NONE
from winapi.cfgmgr32.interface_cache import InterfaceCache
from winapi.cfgmgr32.models.device import Device
from winapi.cfgmgr32.models.interface import Interface
from winapi.guid import GUID


__all__ = ['get_device_interfaces_with_properties', 'get_all_interfaces', 'get_interfaces_via_device_instance_id',
           'get_device_via_instance_id', 'all_devices']


def get_device_interfaces_with_properties(interface_class_guid: GUID, **kwargs) -> dict:
    """
    `The function retrieves all interfaces available for the provided GUID.`

    :param interface_class_guid: A device interface class guid
    :return: A dictionary containing desc, present, reference, instance_id, path, class_guid keys
    """
    # Each call takes fair amount of time, hence we store result in cache
    # The issue as of now with cache is if first call is made with some arguments and next with different arguments,
    # result stored with the first set of arguments will retrieved, need to work in validating cache if argument changes
    # One way is to explicitly call InterfaceCache.get_instance().clear()
    if InterfaceCache.has_interface(interface_class_guid):
        for interface in InterfaceCache.get_interface(interface_class_guid):
            yield interface
    else:
        for interface_path in get_device_interface_list(interface_class_guid, **kwargs):
            yield Interface(interface_path, interface_class_guid=interface_class_guid)


def get_all_interfaces(**kwargs) -> dict:
    """
    `The function retrieves all device interfaces.`

    :return: Yields dict of all available interfaces.
    """
    for device_interface_class in enumerate_classes(ul_flags=CM_ENUMERATE_CLASSES_INTERFACE):
        for interface in get_device_interfaces_with_properties(device_interface_class, **kwargs):
            yield interface


def get_interfaces_via_device_instance_id(device_instance_id: str, **kwargs) -> dict:
    """
    `The function retrieves device interfaces via provided device instance id. To achieve this, a list of all interfaces
    is generated first and then the each interface is checked for matching device instance id as there isn't a direct
    way.`

    TODO: Implement a way to check instance_id in Interface cache

    :param device_instance_id: A device instance id, example: ACPI\LEN2068\4&1e507c5e&0
    :return: List of available interfaces for the provided instance id
    """
    available_interfaces = []
    for interface in get_all_interfaces(**kwargs):
        if interface.device_instance_id.lower() == device_instance_id.lower():
            available_interfaces.append(interface)
    return available_interfaces


def get_device_via_instance_id(device_instance_id: str) -> Device:
    """

    :param device_instance_id: A device instance id, example: ACPI\LEN2068\4&1e507c5e&0
    :return: winapi.cfgmgr32.models.Device
    """
    device_instance = locate_dev_node(device_instance_id)
    return Device(device_instance)


def all_devices(filter_keyword: str = None, flags=CM_GETIDLIST_FILTER_NONE) -> list[Device]:
    """

    :param filter_keyword: A string representing a value inline with the the provided flags
    :param flags: CM_GETIDLIST_* flags
    :return: winapi.cfgmgr32.models.Device
    """
    for device_instance_id in get_device_id_list(filter_keyword=filter_keyword, ul_flags=flags):
        yield get_device_via_instance_id(device_instance_id)
