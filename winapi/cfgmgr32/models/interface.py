from winapi.guid import GUID
from winapi.setupapi.devpkey import DEVPKEY_DeviceInterface_FriendlyName, DEVPKEY_DeviceInterface_Enabled, \
    DEVPKEY_Device_InstanceId, DEVPKEY_DeviceInterface_ReferenceString
from .device import Device
from ..constants import CR
from ..interface_cache import InterfaceCache


__all__ = ['Interface']


class Interface(object):
    """
    This is a device interface object. When initialized, this will get all the available properties for the interface.
    """
    def __init__(self, device_interface_path: str, interface_class_guid: GUID = None):
        """

        :param device_interface_path: A string representing the device interface path.
        :param interface_class_guid: An interface class guid of the same the device. It is recommended to always set
            it also (Optional).
        """
        self.path = device_interface_path
        self.class_guid = str(interface_class_guid)
        self.device_instance_id = self.get_property(DEVPKEY_Device_InstanceId)
        self.status = self.get_property(DEVPKEY_DeviceInterface_Enabled)
        self.desc = self.get_property(DEVPKEY_DeviceInterface_FriendlyName)
        self.reference = self.get_property(DEVPKEY_DeviceInterface_ReferenceString)

        InterfaceCache.add_interface_to_cache(self.class_guid, self)

    def get_property(self, property_key):
        from ..api_wrappers import get_device_interface_property
        try:
            return self.convert(*get_device_interface_property(self.path, property_key))
        except AssertionError as e:
            if e.args[0].args[0] == CR.NO_SUCH_VALUE:
                return None
            raise e

    @property
    def device(self):
        from winapi.cfgmgr32.helper import get_device_via_instance_id
        return get_device_via_instance_id(self.device_instance_id)

    def convert(self, buf, _type):
        return Device.convert(buf, _type)

    def __str__(self):
        return f"<Interface: {self.path}>"

    def __repr__(self):
        return self.__str__()
