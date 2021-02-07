from ctypes import sizeof, wstring_at, addressof

from winapi.common.datatypes import DWORD, ULONG_PTR, WCHAR, Structure
from .datatypes import DWORDLONG, DEVPROPGUID, DEVPROPID
from winapi.guid import GUID
from winapi.kernel32.structs import FILETIME


__all__ = [
    'SP_DEVINFO_DATA', 'SP_DEVICE_INTERFACE_DETAIL_DATA_W', 'SP_DEVICE_INTERFACE_DATA', 'DEVPROPKEY',
    'SP_DRVINFO_DATA', 'SP_DRVINFO_DATA_V2_W'
]


class SP_DEVINFO_DATA(Structure):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data

    typedef struct _SP_DEVINFO_DATA {
      DWORD     cbSize;
      GUID      ClassGuid;
      DWORD     DevInst;
      ULONG_PTR Reserved;
    } SP_DEVINFO_DATA, *PSP_DEVINFO_DATA;

    SP_DEVINFO_DATA structure
    =========================

    -description
    ------------

    An SP_DEVINFO_DATA structure defines a device instance that is a member
    of a device information set.

    -struct-fields
    --------------

    -field cbSize
    ~~~~~~~~~~~~~

    The size, in bytes, of the SP_DEVINFO_DATA structure. For more
    information, see the following Remarks section.

    -field ClassGuid
    ~~~~~~~~~~~~~~~~

    The GUID of the device’s setup class.

    -field DevInst
    ~~~~~~~~~~~~~~

    An opaque handle to the device instance (also known as a handle to the
    devnode).

    Some functions, such as SetupDiXxx functions, take the whole
    SP_DEVINFO_DATA structure as input to identify a device in a device
    information set. Other functions, such as CM\_Xxx functions like
    CM_Get_DevNode_Status, take this DevInst handle as input.

    -field Reserved
    ~~~~~~~~~~~~~~~

    Reserved. For internal use only.

    -remarks
    --------

    An SP_DEVINFO_DATA structure identifies a device in a device information
    set. For example, when Windows sends a DIF_INSTALLDEVICE request to a
    class installer and co-installers, it includes a handle to a device
    information set and a pointer to an SP_DEVINFO_DATA that specifies the
    particular device. In addition to DIF requests, this structure is also
    used in some SetupDiXxx functions.

    SetupDiXxx functions that take an SP_DEVINFO_DATA structure as a
    parameter verify that the cbSize member of the supplied structure is
    equal to the size, in bytes, of the structure. If the cbSize member is
    not set correctly for an input parameter, the function will fail and set
    an error code of ERROR_INVALID_PARAMETER. If the cbSize member is not
    set correctly for an output parameter, the function will fail and set an
    error code of ERROR_INVALID_USER_BUFFER.

    -see-also
    ---------

    SP_DEVINFO_LIST_DETAIL_DATA
    """
    _fields_ = [
        ("cbSize", DWORD),
        ("ClassGuid", GUID),
        ("DevInst", DWORD),
        ("Reserved", ULONG_PTR)
    ]

    def __str__(self):
        return '<SP_DEVINFO_DATA: DevInst(%s), ClassGuid(%s)>' % (self.DevInst, self.ClassGuid)


class SP_DEVICE_INTERFACE_DATA(Structure):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/ns-setupapi-sp_device_interface_data

    typedef struct _SP_DEVICE_INTERFACE_DATA {
      DWORD     cbSize;
      GUID      InterfaceClassGuid;
      DWORD     Flags;
      ULONG_PTR Reserved;
    } SP_DEVICE_INTERFACE_DATA, *PSP_DEVICE_INTERFACE_DATA;

    SP_DEVICE_INTERFACE_DATA structure
    ==================================

    -description
    ------------

    An SP_DEVICE_INTERFACE_DATA structure defines a device interface in a
    device information set.

    -struct-fields
    --------------

    -field cbSize
    ~~~~~~~~~~~~~

    The size, in bytes, of the SP_DEVICE_INTERFACE_DATA structure. For more
    information, see the Remarks section.

    -field InterfaceClassGuid
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    The GUID for the class to which the device interface belongs.

    -field Flags
    ~~~~~~~~~~~~

    Can be one or more of the following:

    SPINT_ACTIVE
    ^^^^^^^^^^^^

    The interface is active (enabled).

    SPINT_DEFAULT
    ^^^^^^^^^^^^^

    The interface is the default interface for the device class.

    SPINT_REMOVED
    ^^^^^^^^^^^^^

    The interface is removed.

    -field Reserved
    ~~~~~~~~~~~~~~~

    Reserved. Do not use.

    -remarks
    --------

    A SetupAPI function that takes an instance of the
    SP_DEVICE_INTERFACE_DATA structure as a parameter verifies whether the
    cbSize member of the supplied structure is equal to the size, in bytes,
    of the structure. If the cbSize member is not set correctly, the
    function will fail and set an error code of ERROR_INVALID_USER_BUFFER.

    -see-also
    ---------

    SP_DEVICE_INTERFACE_DETAIL_DATA

    SetupDiCreateDeviceInterface

    SetupDiEnumDeviceInterfaces

    SetupDiGetDeviceInterfaceAlias

    SetupDiOpenDeviceInterface

    SetupDiSetDeviceInterfaceDefault
    """
    _fields_ = [
        ("cbSize", DWORD),
        ("InterfaceClassGuid", GUID),
        ("Flags", DWORD),
        ("Reserved", ULONG_PTR)
    ]

    def __str__(self):
        return '<SP_DEVICE_INTERFACE_DATA: InterfaceClassGuid(%s)>' % str(self.InterfaceClassGuid)


class SP_DEVICE_INTERFACE_DETAIL_DATA_W(Structure):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/ns-setupapi-sp_device_interface_detail_data_w

    typedef struct _SP_DEVICE_INTERFACE_DETAIL_DATA_W {
      DWORD cbSize;
      WCHAR DevicePath[ANYSIZE_ARRAY];
    } SP_DEVICE_INTERFACE_DETAIL_DATA_W, *PSP_DEVICE_INTERFACE_DETAIL_DATA_W;

    SP_DEVICE_INTERFACE_DETAIL_DATA_W structure
    ===========================================

    -description
    ------------

    An SP_DEVICE_INTERFACE_DETAIL_DATA structure contains the path for a
    device interface.

    -struct-fields
    --------------

    -field cbSize
    ~~~~~~~~~~~~~

    The size, in bytes, of the SP_DEVICE_INTERFACE_DETAIL_DATA structure.
    For more information, see the following Remarks section.

    -field DevicePath
    ~~~~~~~~~~~~~~~~~

    A NULL-terminated string that contains the device interface path. This
    path can be passed to Win32 functions such as CreateFile.

    -remarks
    --------

    An SP_DEVICE_INTERFACE_DETAIL_DATA structure identifies the path for a
    device interface in a device information set.

    SetupDiXxx functions that take an SP_DEVICE_INTERFACE_DETAIL_DATA
    structure as a parameter verify that the cbSize member of the supplied
    structure is equal to the size, in bytes, of the structure. If the
    cbSize member is not set correctly for an input parameter, the function
    will fail and set an error code of ERROR_INVALID_PARAMETER. If the
    cbSize member is not set correctly for an output parameter, the function
    will fail and set an error code of ERROR_INVALID_USER_BUFFER.

       [!NOTE] The setupapi.h header defines SP_DEVICE_INTERFACE_DETAIL_DATA
       as an alias which automatically selects the ANSI or Unicode version
       of this function based on the definition of the UNICODE preprocessor
       constant. Mixing usage of the encoding-neutral alias with code that
       not encoding-neutral can lead to mismatches that result in
       compilation or runtime errors. For more information, see `Conventions
       for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.

    -see-also
    ---------

    SetupDiGetDeviceInterfaceDetail
    """
    _fields_ = [
        ("cbSize", DWORD),
        ("DevicePath", WCHAR)
    ]

    def __str__(self):
        return wstring_at(addressof(self) + sizeof(DWORD))


class DEVPROPKEY(Structure):
    """
    https://docs.microsoft.com/en-us/windows-hardware/drivers/install/devpropkey

    struct DEVPROPKEY {
      DEVPROPGUID fmtid;
      DEVPROPID   pid;
    };

    DEVPROPKEY structure
    ====================

    In Windows Vista and later versions of Windows, the DEVPROPKEY structure
    represents a device property key for a device property in the `unified
    device property
    model <./unified-device-property-model--windows-vista-and-later-.md>`__.

    Syntax
    ------

    .. code:: managedcplusplus

       struct DEVPROPKEY {
         DEVPROPGUID fmtid;
         DEVPROPID   pid;
       };

    Members
    -------

    | **fmtid**
    | A DEVPROPGUID-typed value that specifies a property category.

    The DEVPROPGUID data type is defined as:

    .. code:: cpp

       typedef GUID  DEVPROPGUID, *PDEVPROPGUID;

    | **pid**
    | A DEVPROPID-typed value that uniquely identifies the property within
      the property category. For internal system reasons, a property
      identifier must be greater than or equal to two.

    The DEVPROPID data type is defined as:

    .. code:: cpp

       typedef ULONG DEVPROPID, *PDEVPROPID;

    Remarks
    -------

    The DEVPROPKEY structure is part of the `unified device property
    model <./unified-device-property-model--windows-vista-and-later-.md>`__.

    The basic set of system-supplied device property keys are defined in
    *Devpkey.h*.

    The `DEFINE_DEVPROPKEY <./define-devpropkey.md>`__ macro creates an
    instance of a DEVPROPKEY structure that represents a device property
    key.

    Requirements
    ------------

    .. raw:: html

       <table>

    .. raw:: html

       <colgroup>

    .. raw:: html

       <col width="50%" />

    .. raw:: html

       <col width="50%" />

    .. raw:: html

       </colgroup>

    .. raw:: html

       <tbody>

    .. raw:: html

       <tr class="odd">

    .. raw:: html

       <td align="left">

    .. raw:: html

       <p>

    Header

    .. raw:: html

       </p>

    .. raw:: html

       </td>

    .. raw:: html

       <td align="left">

    Devpropdef.h (include Devpropdef.h)

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </tbody>

    .. raw:: html

       </table>

    See also
    --------

    `DEFINE_DEVPROPKEY <./define-devpropkey.md>`__
    """
    _fields_ = [
        ("fmtid", DEVPROPGUID),
        ("pid", DEVPROPID)
    ]

    def __init__(self, *args):
        if len(args) == 12:
            args = (GUID(args[0], args[1], args[2], args[3:11]), args[-1])
        elif type(args[0]) == str and len(args) == 2:
            args = (GUID.from_guid_string(args[0]), args[1])
        super().__init__(*args)

    def __eq__(self, other):
        return all([self.fmtid == other.fmtid, self.pid == other.pid])

    def __str__(self):
        return '<DEVPROPKEY: fmtid(%s), pid(%s)>' % (str(self.fmtid), self.pid)


class SP_DRVINFO_DATA_V2_W(Structure):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/ns-setupapi-sp_drvinfo_data_v2_w

    typedef struct _SP_DRVINFO_DATA_V2_W {
      DWORD     cbSize;
      DWORD     DriverType;
      ULONG_PTR Reserved;
      WCHAR     Description[LINE_LEN];
      WCHAR     MfgName[LINE_LEN];
      WCHAR     ProviderName[LINE_LEN];
      FILETIME  DriverDate;
      DWORDLONG DriverVersion;
    } SP_DRVINFO_DATA_V2_W, *PSP_DRVINFO_DATA_V2_W;

    SP_DRVINFO_DATA_V2_W structure
    ==============================

    -description
    ------------

    An SP_DRVINFO_DATA structure contains information about a driver. This
    structure is a member of a driver information list that can be
    associated with a particular device instance or globally with a device
    information set.

    -struct-fields
    --------------

    -field cbSize
    ~~~~~~~~~~~~~

    The size, in bytes, of the SP_DRVINFO_DATA structure. For more
    information, see the Remarks section in this topic.

    -field DriverType
    ~~~~~~~~~~~~~~~~~

    The type of driver represented by this structure. Must be one of the
    following values:

    SPDIT_CLASSDRIVER
    ^^^^^^^^^^^^^^^^^

    This structure represents a class driver.

    SPDIT_COMPATDRIVER
    ^^^^^^^^^^^^^^^^^^

    This structure represents a compatible driver.

    -field Reserved
    ~~~~~~~~~~~~~~~

    Reserved. For internal use only.

    -field Description
    ~~~~~~~~~~~~~~~~~~

    A NULL-terminated string that describes the device supported by this
    driver.

    -field MfgName
    ~~~~~~~~~~~~~~

    A NULL-terminated string that contains the name of the manufacturer of
    the device supported by this driver.

    -field ProviderName
    ~~~~~~~~~~~~~~~~~~~

    A NULL-terminated string giving the provider of this driver. This is
    typically the name of the organization that creates the driver or INF
    file. ProviderName can be an empty string.

    -field DriverDate
    ~~~~~~~~~~~~~~~~~

    Date of the driver. From the DriverVer entry in the INF file. See the
    INF DDInstall Section for more information about the DriverVer entry.

    -field DriverVersion
    ~~~~~~~~~~~~~~~~~~~~

    Version of the driver. From the DriverVer entry in the INF file.

    -field DriverType.SPDIT_CLASSDRIVER
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This structure represents a class driver.

    -field DriverType.SPDIT_COMPATDRIVER
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This structure represents a compatible driver.

    -remarks
    --------

    In SetupAPI.h, this structure equates to either SP_DRVINFO_DATA_V1 or
    SP_DRVINFO_DATA_V2, based on whether you include the following line in
    your source code:

    ::

       #define  USE_SP_DRVINFO_DATA_V1 1

    Define this identifier only if your component must run on Windows 98 or
    Millennium Edition, or on Windows NT. If your component is run only in
    Windows 2000 and later versions of Windows, do not define the
    identifier. If the identifier is not defined, SP_DRVINFO_DATA_V2 is
    used.

    SP_DRVINFO_DATA_V1 does not contain DriverDate and DriverVersion
    members.

    SetupDiXxx functions that take an SP_DRVINFO_DATA structure as a
    parameter verify that the cbSize member of the supplied structure is
    equal to the size, in bytes, of the structure. If the cbSize member is
    not set correctly for an input parameter, the function will fail and set
    an error code of ERROR_INVALID_PARAMETER. If the cbSize member is not
    set correctly for an output parameter, the function will fail and set an
    error code of ERROR_INVALID_USER_BUFFER.

       [!NOTE] The setupapi.h header defines SP_DRVINFO_DATA_V2 as an alias
       which automatically selects the ANSI or Unicode version of this
       function based on the definition of the UNICODE preprocessor
       constant. Mixing usage of the encoding-neutral alias with code that
       not encoding-neutral can lead to mismatches that result in
       compilation or runtime errors. For more information, see `Conventions
       for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.

    -see-also
    ---------

    SetupDiEnumDriverInfo

    SetupDiGetDriverInstallParams

    SetupDiGetSelectedDriver

    SetupDiSetDriverInstallParams

    SetupDiSetSelectedDriver
    """

    LINE_LEN = 256      # define LINE_LEN 256 // Windows 9x-compatible maximum for

    _fields_ = [
        ("cbSize", DWORD),
        ("DriverType", DWORD),
        ("Reserved", ULONG_PTR),
        ("Description", (WCHAR * LINE_LEN)),
        ("MfgName", (WCHAR * LINE_LEN)),
        ("ProviderName", (WCHAR * LINE_LEN)),
        ("DriverDate", FILETIME),
        ("DriverVersion", DWORDLONG)
    ]


SP_DRVINFO_DATA = SP_DRVINFO_DATA_V2_W
