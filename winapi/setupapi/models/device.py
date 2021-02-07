from ctypes import wstring_at, byref
from struct import unpack

from winapi.common.datatypes import HDEVINFO
from winapi.guid import GUID
from winapi.kernel32.structs import FILETIME
from winapi.setupapi.constants import DN
from winapi.setupapi.devpkey import DEVPKEY_Device_DeviceDesc, DEVPKEY_NAME, DEVPKEY_Device_Service, \
    DEVPKEY_Device_Class, DEVPKEY_Device_ClassGuid, DEVPKEY_Device_Driver, DEVPKEY_Device_Manufacturer, \
    DEVPKEY_Device_LocationInfo, DEVPKEY_Device_PDOName, DEVPKEY_Device_ExtendedConfigurationIds, DEVPKEY_Device_Model, \
    DEVPKEY_Device_DriverProvider, DEVPKEY_Device_HardwareIds, DEVPKEY_Device_CompatibleIds, \
    DEVPKEY_Device_DriverVersion, DEVPKEY_Device_SecuritySDS, DEVPKEY_Device_LocationPaths, DEVPKEY_Device_InstanceId, \
    DEVPKEY_Device_FriendlyName, DEVPKEY_Device_ContainerId, DEVPKEY_Device_ModelId, DEVPKEY_Device_IsPresent, \
    DEVPKEY_Device_DevNodeStatus, DEVPKEY_Device_Stack, DEVPKEY_Device_BiosDeviceName, DEVPKEY_Device_FirmwareVersion, \
    DEVPKEY_Device_InstallDate, DEVPKEY_Device_DriverDate, DEVPKEY_Device_DriverDesc, DEVPKEY_Device_DriverInfPath, \
    DEVPKEY_Device_DriverInfSection, DEVPKEY_Device_FirmwareRevision
from winapi.setupapi.devprop import DEVPROP_TYPE_BOOL, DEVPROP_TYPE_STRING_LIST, DEVPROP_TYPE_STRING, \
    DEVPROP_TYPE_STRING_INDIRECT, DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING, DEVPROP_TYPE_GUID, DEVPROP_TYPE_NULL, \
    DEVPROP_TYPE_SBYTE, DEVPROP_TYPE_EMPTY, DEVPROP_TYPE_BINARY, DEVPROP_TYPE_UINT32, DEVPROP_TYPE_ERROR, \
    DEVPROP_TYPE_NTSTATUS, DEVPROP_TYPE_FILETIME
from winapi.setupapi.structs import SP_DEVINFO_DATA

__all__ = ['DeviceInitError', 'Device']


class DeviceInitError(WindowsError):
    pass


class Device(object):
    def __init__(self, device_info_set: HDEVINFO, device_info_data: SP_DEVINFO_DATA) -> object:
        """
        Automatically retrieves the properties and parse them and sets the instance attributes accordingly
        :param device_info_set:
        :param device_info_data:
        """
        self.__info_set = device_info_set
        self.__info_data = device_info_data
        self.__name = None
        self.__friendly_name = None
        self.__desc = None
        self.__service = None
        self.__class_name = None
        self.__class_guid = None
        self.__manufacturer = None
        self.__location_info = None
        self.__location_paths = None
        self.__pdo_name = None
        self.__extended_config_ids = None
        self.__model = None
        self.__model_id = None
        self.__hw_ids = None
        self.__compat_ids = None
        self.__sds = None
        self.__instance_id = None
        self.__container_id = None
        self.__is_present = None
        self.__status = None
        self.__stack = None
        self.__bios_name = None
        self.__fw_version = None
        self.__fw_revision = None
        self.__install_date = None
        self.__driver = None
        self.__driver_version = None
        self.__driver_date = None
        self.__driver_desc = None
        self.__driver_inf_path = None
        self.__driver_inf_section = None
        self.__driver_provider = None
        self.__interfaces = None
        self.__driver_inf_driver_store_location = None

    @property
    def name(self):
        if not self.__name:
            self.__name = self.get_property(DEVPKEY_NAME)
        return self.__name

    @property
    def friendly_name(self):
        if not self.__friendly_name:
            self.__friendly_name = self.get_property(DEVPKEY_Device_FriendlyName)
        return self.__friendly_name

    @property
    def desc(self):
        if not self.__desc:
            self.__desc = self.get_property(DEVPKEY_Device_DeviceDesc)
        return self.__desc

    @property
    def service(self):
        if not self.__service:
            self.__service = self.get_property(DEVPKEY_Device_Service)
        return self.__service

    @property
    def class_name(self):
        if not self.__class_name:
            self.__class_name = self.get_property(DEVPKEY_Device_Class)
        return self.__class_name

    @property
    def class_guid(self):
        if not self.__class_guid:
            self.__class_guid = self.get_property(DEVPKEY_Device_ClassGuid)
        return self.__class_guid

    @property
    def manufacturer(self):
        if not self.__manufacturer:
            self.__manufacturer = self.get_property(DEVPKEY_Device_Manufacturer)
        return self.__manufacturer

    @property
    def location_info(self):
        if not self.__location_info:
            self.__location_info = self.get_property(DEVPKEY_Device_LocationInfo)
        return self.__location_info

    @property
    def location_paths(self):
        if not self.__location_paths:
            self.__location_paths = self.get_property(DEVPKEY_Device_LocationPaths)
        return self.__location_paths

    @property
    def pdo_name(self):
        if not self.__pdo_name:
            self.__pdo_name = self.get_property(DEVPKEY_Device_PDOName)
        return self.__pdo_name

    @property
    def extended_config_ids(self):
        if not self.__extended_config_ids:
            self.__extended_config_ids = self.get_property(DEVPKEY_Device_ExtendedConfigurationIds)
        return self.__extended_config_ids

    @property
    def model(self):
        if not self.__model:
            self.__model = self.get_property(DEVPKEY_Device_Model)
        return self.__model

    @property
    def model_id(self):
        if not self.__model_id:
            self.__model_id = self.get_property(DEVPKEY_Device_ModelId)
        return self.__model_id

    @property
    def hw_ids(self):
        if not self.__hw_ids:
            self.__hw_ids = self.get_property(DEVPKEY_Device_HardwareIds)
        return self.__hw_ids

    @property
    def compat_ids(self):
        if not self.__compat_ids:
            self.__compat_ids = self.get_property(DEVPKEY_Device_CompatibleIds)
        return self.__compat_ids

    @property
    def sds(self):
        if not self.__sds:
            self.__sds = self.get_property(DEVPKEY_Device_SecuritySDS)
        return self.__sds

    @property
    def instance_id(self):
        if not self.__instance_id:
            self.__instance_id = self.get_property(DEVPKEY_Device_InstanceId)
        return self.__instance_id

    @property
    def container_id(self):
        if not self.__container_id:
            self.__container_id = self.get_property(DEVPKEY_Device_ContainerId)
        return self.__container_id

    @property
    def is_present(self):
        if not self.__is_present:
            self.__is_present = self.get_property(DEVPKEY_Device_IsPresent)
        return self.__is_present

    @property
    def status(self, code=False):
        if not self.__status:
            status_code = self.get_property(DEVPKEY_Device_DevNodeStatus)
            if code: return status_code[0]
            try:
                status = ''
                for code in DN:
                    res = status_code[0] & code
                    if res:
                        if code in [DN.DRIVER_LOADED, DN.STARTED]:
                            status = 'Started'
                            break
                        elif code in [DN.DISABLEABLE, DN.REMOVABLE]:
                            status = 'Stopped'
                            break
            except TypeError:
                status = 'Disconnected'
            self.__status = status
        return self.__status

    @property
    def stack(self):
        if not self.__stack:
            self.__stack = self.get_property(DEVPKEY_Device_Stack)
        return self.__stack

    @property
    def bios_name(self):
        if not self.__bios_name:
            self.__bios_name = self.get_property(DEVPKEY_Device_BiosDeviceName)
        return self.__bios_name

    @property
    def fw_version(self):
        if not self.__fw_version:
            self.__fw_version = self.get_property(DEVPKEY_Device_FirmwareVersion)
        return self.__fw_version

    @property
    def fw_revision(self):
        if not self.__fw_revision:
            self.__fw_revision = self.get_property(DEVPKEY_Device_FirmwareRevision)
        return self.__fw_revision

    @property
    def install_date(self):
        if not self.__install_date:
            self.__install_date = self.get_property(DEVPKEY_Device_InstallDate)
        return self.__install_date

    @property
    def driver(self):
        if not self.__driver:
            self.__driver = self.get_property(DEVPKEY_Device_Driver)
        return self.__driver

    @property
    def driver_version(self):
        if not self.__driver_version:
            self.__driver_version = self.get_property(DEVPKEY_Device_DriverVersion)
        return self.__driver_version

    @property
    def driver_date(self):
        if not self.__driver_date:
            self.__driver_date = self.get_property(DEVPKEY_Device_DriverDate)
        return self.__driver_date

    @property
    def driver_desc(self):
        if not self.__driver_desc:
            self.__driver_desc = self.get_property(DEVPKEY_Device_DriverDesc)
        return self.__driver_desc

    @property
    def driver_inf_path(self):
        if not self.__driver_inf_path:
            self.__driver_inf_path = self.get_property(DEVPKEY_Device_DriverInfPath)
        return self.__driver_inf_path

    @property
    def driver_inf_section(self):
        if not self.__driver_inf_section:
            self.__driver_inf_section = self.get_property(DEVPKEY_Device_DriverInfSection)
        return self.__driver_inf_section

    @property
    def driver_provider(self):
        if not self.__driver_provider:
            self.__driver_provider = self.get_property(DEVPKEY_Device_DriverProvider)
        return self.__driver_provider

    @property
    def driver_inf_driver_store_location(self):
        from winapi.setupapi.api_wrappers import get_inf_driver_store_location
        if not self.__driver_inf_driver_store_location:
            self.__driver_inf_driver_store_location = get_inf_driver_store_location(self.driver_inf_path)
        return self.__driver_inf_driver_store_location

    @property
    def interfaces(self):
        from winapi.setupapi.helper import resolve_device_interfaces_via_guid
        return resolve_device_interfaces_via_guid(self.instance_id)

    def get_property(self, _property):
        from winapi.setupapi.api_wrappers import get_device_property
        return self.convert(*get_device_property(self.__info_set, self.__info_data, _property))

    @staticmethod
    def convert(buf, _type):
        if buf is None:
            return
        if any([_type == DEVPROP_TYPE_STRING, _type == DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING,
                _type == DEVPROP_TYPE_STRING_INDIRECT]):
            return wstring_at(byref(buf))
        elif _type == DEVPROP_TYPE_STRING_LIST:
            return [i for i in bytes(buf).decode("utf-16").strip("\x00").strip().split("\x00") if i != ""]
        elif _type == DEVPROP_TYPE_GUID:
            return GUID.from_buffer(buf)
        elif _type == DEVPROP_TYPE_BOOL:
            # return buf[0] != 0
            return bool(bytes(buf)[0])
        elif _type == DEVPROP_TYPE_NULL:
            return None
        elif _type == DEVPROP_TYPE_SBYTE:
            return buf[0]
        elif _type == DEVPROP_TYPE_EMPTY:
            raise AttributeError()
        elif _type == DEVPROP_TYPE_BINARY:
            pass
        elif any([_type == DEVPROP_TYPE_UINT32, _type == DEVPROP_TYPE_ERROR, _type == DEVPROP_TYPE_NTSTATUS]):
            return unpack("L", buf)
        elif _type == DEVPROP_TYPE_FILETIME:
            return FILETIME.from_buffer(buf)

    def __del__(self):
        del self.__info_data
        del self.__info_set

    def __str__(self):
        return '<Device: %s, %s, %s, %s>' % (self.name, self.driver_inf_path, self.driver_provider, self.class_name)
