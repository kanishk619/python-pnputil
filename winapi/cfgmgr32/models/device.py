from winapi.common.datatypes import DEVINST
from winapi.setupapi.models import Device as _Device
from winapi.setupapi.models import DeviceInitError


__all__ = ['DeviceInitError', 'Device']


class Device(_Device):
    def __init__(self, dev_inst: DEVINST):
        super(Device, self).__init__(None, None)
        self.__dev_inst = dev_inst

    def get_property(self, _property):
        from ..api_wrappers import get_device_property
        try:
            return self.convert(*get_device_property(self.__dev_inst, _property))
        except AssertionError as e:
            return None

    def __del__(self):
        del self.__dev_inst

    @property
    def interfaces(self):
        from ..helper import get_interfaces_via_device_instance_id
        return get_interfaces_via_device_instance_id(device_instance_id=self.instance_id)

