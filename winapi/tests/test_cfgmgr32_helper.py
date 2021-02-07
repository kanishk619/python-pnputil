from ctypes import wstring_at
from unittest import TestCase

from winapi.cfgmgr32.api_wrappers import *
from winapi.cfgmgr32.helper import get_interfaces_via_device_instance_id, get_all_interfaces, \
    get_device_interfaces_with_properties, get_device_via_instance_id, all_devices
from winapi.cfgmgr32.interface_cache import InterfaceCache
from winapi.guid import GUID
from winapi.setupapi.devpkey import DEVPKEY_Device_Class, DEVPKEY_DeviceInterface_ClassGuid
from winapi.setupapi.devprop import DEVPROP_TYPE_STRING


class Test(TestCase):
    # below values are of Intel Management Engine interface
    interface_path = r'\\?\PCI#VEN_8086&DEV_02E0&SUBSYS_22B117AA&REV_00#3&11583659&0&B0#{e2d1ff34-3458-49a9-88da-8e6915ce9be5}'
    interface_class_guid = GUID.from_guid_string('{e2d1ff34-3458-49a9-88da-8e6915ce9be5}')
    device_instance_id = r'PCI\VEN_8086&DEV_02E0&SUBSYS_22B117AA&REV_00\3&11583659&0&B0'

    def test_locate_dev_node(self):
        res = locate_dev_node(device_instance_id=self.device_instance_id)
        self.assertGreaterEqual(res.value, 1)

    def test_get_device_interface_property(self):
        res = get_device_interface_property(self.interface_path, DEVPKEY_DeviceInterface_ClassGuid)
        self.assertEqual(GUID.from_buffer(res[0]), self.interface_class_guid)
        del res

    def test_get_device_interface_alias(self):
        res = get_device_interface_alias(device_interface=self.interface_path,
                                         alias_interface_guid=self.interface_class_guid)
        self.assertEqual(res, self.interface_path)
        del res

    def test_get_device_interface_list_size(self):
        res = get_device_interface_list_size(self.interface_class_guid)
        self.assertGreater(res, 1)
        del res

    def test_get_device_interface_list(self):
        InterfaceCache.get_instance().clear()
        res = [i for i in get_device_interface_list(interface_class_guid=self.interface_class_guid)]
        self.assertGreaterEqual(len(res), 1)
        del res

    def test_get_class_guid_interfaces(self):
        InterfaceCache.get_instance().clear()
        res = [i for i in get_device_interfaces_with_properties(interface_class_guid=self.interface_class_guid)]
        self.assertGreaterEqual(len(res), 1)
        del res

    def test_get_all_interfaces(self):
        InterfaceCache.get_instance().clear()
        res = [i for i in get_all_interfaces()]
        self.assertGreaterEqual(len(res), 1)
        del res

    def test_get_interfaces_via_instance_id(self):
        InterfaceCache.get_instance().clear()
        res = get_interfaces_via_device_instance_id(self.device_instance_id)
        self.assertGreaterEqual(len(res), 1)
        del res

    def test_get_device_property(self):
        dev_instance = locate_dev_node(self.device_instance_id)
        res = get_device_property(dev_instance, DEVPKEY_Device_Class)
        self.assertEqual(res[1], DEVPROP_TYPE_STRING)
        self.assertEqual(wstring_at(res[0]), "System")
        del res, dev_instance

    def test_get_device_id_size(self):
        dev_instance = locate_dev_node(self.device_instance_id)
        res = get_device_id_size(dev_instance)
        self.assertGreater(res, 1)
        del res, dev_instance

    def test_get_device_id(self):
        dev_instance = locate_dev_node(self.device_instance_id)
        res = get_device_id(dev_instance)
        self.assertEqual(self.device_instance_id, res)
        del res, dev_instance

    def test_get_device_id_list_size(self):
        res = get_device_id_list_size()
        self.assertGreater(res, 1)
        del res

    def test_get_device_id_list(self):
        res = [device_id for device_id in get_device_id_list()]
        self.assertTrue(len(res) >= 1)
        del res

    def test_enumerate_classes(self):
        res = [class_guid for class_guid in enumerate_classes()]
        assert len(res) >= 1, "enumerate_classes() failed"
        del res

    def test_get_device_via_instance_id(self):
        res = get_device_via_instance_id(self.device_instance_id)
        self.assertEqual(res.instance_id, self.device_instance_id)

    def test_all_devices(self):
        res = [d for d in all_devices()]
        self.assertGreaterEqual(len(res), 1)
