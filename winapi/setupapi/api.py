from ctypes import windll, POINTER

from winapi.common.datatypes import HWND, PDWORD, BOOL, PBYTE, LPSTR, \
    HDEVINFO, ULONG, DWORD, PCWSTR, PWSTR, PULONG, HANDLE
from winapi.guid import GUID
from winapi.setupapi.structs import *


__all__ = [
    'SetupDiBuildDriverInfoList', 'SetupDiEnumDriverInfo',
    'SetupDiGetDeviceProperty', 'SetupDiGetDeviceInterfaceDetail', 'SetupDiDestroyDeviceInfoList',
    'SetupDiGetDeviceInstanceId', 'SetupDiEnumDeviceInterfaces', 'SetupDiEnumDeviceInfo', 'SetupDiGetClassDevs',
    'SetupDiGetDeviceRegistryProperty', 'SetupDiGetDevicePropertyKeys', 'SetupGetInfPublishedName',
    'SetupGetInfDriverStoreLocation', 'SetupDiOpenDeviceInterfaceRegKey'
]


setupapi = windll.setupapi

PSTR = LPSTR
PSP_ALTPLATFORM_INFO = PULONG
ACCESS_MASK = DWORD     # typedef DWORD ACCESS_MASK;
REGSAM = ACCESS_MASK    # typedef ACCESS_MASK REGSAM;
HKEY = HANDLE           # typedef HKEY *PHKEY;
PSP_DEVINFO_DATA = POINTER(SP_DEVINFO_DATA)
PSP_DEVICE_INTERFACE_DATA = POINTER(SP_DEVICE_INTERFACE_DATA)
PSP_DEVICE_INTERFACE_DETAIL_DATA_W = POINTER(SP_DEVICE_INTERFACE_DETAIL_DATA_W)
DEVPROPTYPE = POINTER(ULONG),  # typedef ULONG DEVPROPTYPE, *PDEVPROPTYPE;
PSP_DRVINFO_DATA_W = POINTER(SP_DRVINFO_DATA_V2_W)


class SetupDiGetClassDevs(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw

    SetupDiGetClassDevsW function
    =============================

    -description
    ------------

    The SetupDiGetClassDevs function returns a handle to a device
    information set that contains requested device information elements for
    a local computer.

    -parameters
    -----------

    -param ClassGuid [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to the GUID for a device setup class or a device interface
    class. This pointer is optional and can be NULL. For more information
    about how to set ClassGuid, see the following Remarks section.

    -param Enumerator [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a NULL-terminated string that specifies:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    An identifier (ID) of a Plug and Play (PnP) enumerator. This ID can
    either be the value’s globally unique identifier (GUID) or symbolic
    name. For example, “PCI” can be used to specify the PCI PnP value. Other
    examples of symbolic names for PnP values include “USB,” “PCMCIA,” and
    “SCSI”.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    A PnP device instance ID. When specifying a PnP device instance ID,
    DIGCF_DEVICEINTERFACE must be set in the Flags parameter.

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    This pointer is optional and can be NULL. If an enumeration value is not
    used to select devices, set Enumerator to NULL

    For more information about how to set the Enumerator value, see the
    following Remarks section.

    -param hwndParent [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A handle to the top-level window to be used for a user interface that is
    associated with installing a device instance in the device information
    set. This handle is optional and can be NULL.

    -param Flags [in]
    ~~~~~~~~~~~~~~~~~

    A variable of type DWORD that specifies control options that filter the
    device information elements that are added to the device information
    set. This parameter can be a bitwise OR of zero or more of the following
    flags. For more information about combining these flags, see the
    following Remarks section.

    DIGCF_ALLCLASSES
    ^^^^^^^^^^^^^^^^

    Return a list of installed devices for all device setup classes or all
    device interface classes.

    DIGCF_DEVICEINTERFACE
    ^^^^^^^^^^^^^^^^^^^^^

    Return devices that support device interfaces for the specified device
    interface classes. This flag must be set in the Flags parameter if the
    Enumerator parameter specifies a device instance ID.

    DIGCF_DEFAULT
    ^^^^^^^^^^^^^

    Return only the device that is associated with the system default device
    interface, if one is set, for the specified device interface classes.

    DIGCF_PRESENT
    ^^^^^^^^^^^^^

    Return only devices that are currently present in a system.

    DIGCF_PROFILE
    ^^^^^^^^^^^^^

    Return only devices that are a part of the current hardware profile.

    -returns
    --------

    If the operation succeeds, SetupDiGetClassDevs returns a handle to a
    device information set that contains all installed devices that matched
    the supplied parameters. If the operation fails, the function returns
    INVALID_HANDLE_VALUE. To get extended error information, call
    GetLastError.

    -remarks
    --------

    The caller of SetupDiGetClassDevs must delete the returned device
    information set when it is no longer needed by calling
    SetupDiDestroyDeviceInfoList.

    Call SetupDiGetClassDevsEx to retrieve the devices for a class on a
    remote computer.

    .. raw:: html

       <h3>

    Device Setup Class Control Options

    .. raw:: html

       </h3>

    Use the following filtering options to control whether
    SetupDiGetClassDevs returns devices for all device setup classes or only
    for a specified device setup class:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    To return devices for all device setup classes, set the DIGCF_ALLCLASSES
    flag, and set the ClassGuid parameter to NULL.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    To return devices only for a specific device setup class, do not set
    DIGCF_ALLCLASSES, and use ClassGuid to supply the GUID of the device
    setup class.

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    In addition, you can use the following filtering options in combination
    with one another to further restrict which devices are returned:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    To return only devices that are present in the system, set the
    DIGCF_PRESENT flag.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    To return only devices that are part of the current hardware profile,
    set the DIGCF_PROFILE flag.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    To return devices only for a specific PnP enumerator, use the Enumerator
    parameter to supply the GUID or symbolic name of the enumerator. If
    Enumerator is NULL, SetupDiGetClassDevs returns devices for all PnP
    enumerators.

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    .. raw:: html

       <h3>

    Device Interface Class Control Options

    .. raw:: html

       </h3>

    Use the following filtering options to control whether
    SetupDiGetClassDevs returns devices that support any device interface
    class or only devices that support a specified device interface class:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    To return devices that support a device interface of any class, set the
    DIGCF_DEVICEINTERFACE flag, set the DIGCF_ALLCLASSES flag, and set
    ClassGuid to NULL. The function adds to the device information set a
    device information element that represents such a device and then adds
    to the device information element a device interface list that contains
    all the device interfaces that the device supports.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    To return only devices that support a device interface of a specified
    class, set the DIGCF_DEVICEINTERFACE flag and use the ClassGuid
    parameter to supply the class GUID of the device interface class. The
    function adds to the device information set a device information element
    that represents such a device and then adds a device interface of the
    specified class to the device interface list for that device information
    element.

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    In addition, you can use the following filtering options to control
    whether SetupDiGetClassDevs returns only devices that support the system
    default interface for device interface classes:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    To return only the device that supports the system default interface, if
    one is set, for a specified device interface class, set the
    DIGCF_DEVICEINTERFACE flag, set the DIGCF_DEFAULT flag, and use
    ClassGuid to supply the class GUID of the device interface class. The
    function adds to the device information set a device information element
    that represents such a device and then adds the system default interface
    to the device interface list for that device information element.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    To return a device that supports a system default interface for an
    unspecified device interface class, set the DIGCF_DEVICEINTERFACE flag,
    set the DIGCF_ALLCLASSES flag, set the DIGCF_DEFAULT flag, and set
    ClassGuid to NULL. The function adds to the device information set a
    device information element that represents such a device and then adds
    the system default interface to the device interface list for that
    device information element.

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    You can also use the following options in combination with the other
    options to further restrict which devices are returned:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    To return only devices that are present in the system, set the
    DIGCF_PRESENT flag.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    To return only devices that are part of the current hardware profile,
    set the DIGCF_PROFILE flag.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    To return only a specific device, set the DIGCF_DEVICEINTERFACE flag and
    use the Enumerator parameter to supply the device instance ID of the
    device. To include all possible devices, set Enumerator to NULL.

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    Examples
    ^^^^^^^^

    The following are some examples of how to use the SetupDiGetClassDevs
    function.

    Example 1: Build a list of all devices in the system, including devices
    that are not currently present.

    ::

       Handle = SetupDiGetClassDevs(NULL, NULL, NULL, DIGCF_ALLCLASSES);

    Example 2: Build a list of all devices that are present in the system.

    ::

       Handle = SetupDiGetClassDevs(NULL, NULL, NULL, DIGCF_ALLCLASSES | DIGCF_PRESENT);

    Example 3: Build a list of all devices that are present in the system
    that are from the network adapter device setup class.

    ::

       Handle = SetupDiGetClassDevs(&GUID_DEVCLASS_NET, NULL, NULL, DIGCF_PRESENT);

    Example 4: Build a list of all devices that are present in the system
    that have enabled an interface from the storage volume device interface
    class.

    ::

       Handle = SetupDiGetClassDevs(&GUID_DEVINTERFACE_VOLUME, NULL, NULL, DIGCF_PRESENT | DIGCF_DEVICEINTERFACE);

    Example 5: Build a list of all devices that are present in the system
    but do not belong to any known device setup class (Windows Vista and
    later versions of Windows).

    .. container:: alert

       Note  You cannot set the ClassGuid parameter to GUID_DEVCLASS_UNKNOWN
       to detect devices with an unknown setup class. Instead, you must
       follow this example.

    .. container::

        

    ::

       DeviceInfoSet = SetupDiGetClassDevs(
                                           NULL,
                                           NULL,
                                           NULL,
                                           DIGCF_ALLCLASSES | DIGCF_PRESENT);

       ZeroMemory(&DeviceInfoData, sizeof(SP_DEVINFO_DATA));
       DeviceInfoData.cbSize = sizeof(SP_DEVINFO_DATA);
       DeviceIndex = 0;

       while (SetupDiEnumDeviceInfo(
                                    DeviceInfoSet,
                                    DeviceIndex,
                                    &DeviceInfoData)) {
           DeviceIndex++;

           if (!SetupDiGetDeviceProperty(
                                         DeviceInfoSet,
                                         &DeviceInfoData,
                                         &DEVPKEY_Device_Class,
                                         &PropType,
                                         (PBYTE)&DevGuid,
                                         sizeof(GUID),
                                         &Size,
                                         0) || PropType != DEVPROP_TYPE_GUID) {

               Error = GetLastError();

               if (Error == ERROR_NOT_FOUND) {
                   \\
                   \\ This device has an unknown device setup class.
                   \\
                   }
               }
           }

       if (DeviceInfoSet) {
           SetupDiDestroyDeviceInfoList(DeviceInfoSet);
           }

    ..

       [!NOTE] The setupapi.h header defines SetupDiGetClassDevs as an alias
       which automatically selects the ANSI or Unicode version of this
       function based on the definition of the UNICODE preprocessor
       constant. Mixing usage of the encoding-neutral alias with code that
       not encoding-neutral can lead to mismatches that result in
       compilation or runtime errors. For more information, see `Conventions
       for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.

    -see-also
    ---------

    Device Information Set

    Device Instance IDs

    SetupDiCreateDeviceInfoList

    SetupDiDestroyDeviceInfoList

    SetupDiEnumDeviceInterfaces

    SetupDiGetClassDevsEx
    """

    def __new__(cls,
                ClassGuid: POINTER(GUID) = None,
                Enumerator: PCWSTR = None,
                hwndParent: HWND = None,
                Flags: DWORD = None
                ) -> HDEVINFO:
        """

        :param ClassGuid: POINTER(GUID) [in, optional]
        :param Enumerator: PCWSTR [in, optional]
        :param hwndParent: HWND [in, optional]
        :param Flags: DWORD [in]
        :return: HDEVINFO
        """

        func = setupapi.SetupDiGetClassDevsW
        func.argtypes = [
            POINTER(GUID),
            PCWSTR,
            HWND,
            DWORD
        ]
        func.restype = HDEVINFO
        return func(ClassGuid, Enumerator, hwndParent, Flags)


class SetupDiDestroyDeviceInfoList(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdidestroydeviceinfolist

    SetupDiDestroyDeviceInfoList function
    =====================================

    -description
    ------------

    The SetupDiDestroyDeviceInfoList function deletes a device information
    set and frees all associated memory.

    -parameters
    -----------

    -param DeviceInfoSet [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A handle to the device information set to delete.

    -returns
    --------

    The function returns TRUE if it is successful. Otherwise, it returns
    FALSE and the logged error can be retrieved with a call to GetLastError.

    -see-also
    ---------

    SetupDiCreateDeviceInfoList

    SetupDiGetClassDevs
    """

    def __new__(cls,
                DeviceInfoSet: HDEVINFO = None
                ) -> BOOL:
        """

        :param DeviceInfoSet: HDEVINFO [in]
        :return: BOOL
        """

        func = setupapi.SetupDiDestroyDeviceInfoList
        func.argtypes = [
            HDEVINFO
        ]
        func.restype = BOOL
        return func(DeviceInfoSet)


class SetupDiEnumDeviceInterfaces(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces

    SetupDiEnumDeviceInterfaces function
    ====================================

    -description
    ------------

    The SetupDiEnumDeviceInterfaces function enumerates the device
    interfaces that are contained in a device information set.

    -parameters
    -----------

    -param DeviceInfoSet [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a device information set that contains the device
    interfaces for which to return information. This handle is typically
    returned by SetupDiGetClassDevs.

    -param DeviceInfoData [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to an SP_DEVINFO_DATA structure that specifies a device
    information element in DeviceInfoSet. This parameter is optional and can
    be NULL. If this parameter is specified, SetupDiEnumDeviceInterfaces
    constrains the enumeration to the interfaces that are supported by the
    specified device. If this parameter is NULL, repeated calls to
    SetupDiEnumDeviceInterfaces return information about the interfaces that
    are associated with all the device information elements in
    DeviceInfoSet. This pointer is typically returned by
    SetupDiEnumDeviceInfo.

    -param InterfaceClassGuid [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a GUID that specifies the device interface class for the
    requested interface.

    -param MemberIndex [in]
    ~~~~~~~~~~~~~~~~~~~~~~~

    A zero-based index into the list of interfaces in the device information
    set. The caller should call this function first with MemberIndex set to
    zero to obtain the first interface. Then, repeatedly increment
    MemberIndex and retrieve an interface until this function fails and
    GetLastError returns ERROR_NO_MORE_ITEMS.

    If DeviceInfoData specifies a particular device, the MemberIndex is
    relative to only the interfaces exposed by that device.

    -param DeviceInterfaceData [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a caller-allocated buffer that contains, on successful
    return, a completed SP_DEVICE_INTERFACE_DATA structure that identifies
    an interface that meets the search parameters. The caller must set
    DeviceInterfaceData.cbSize to sizeof(SP_DEVICE_INTERFACE_DATA) before
    calling this function.

    -returns
    --------

    SetupDiEnumDeviceInterfaces returns TRUE if the function completed
    without error. If the function completed with an error, FALSE is
    returned and the error code for the failure can be retrieved by calling
    GetLastError.

    -remarks
    --------

    Repeated calls to this function return an SP_DEVICE_INTERFACE_DATA
    structure for a different device interface. This function can be called
    repeatedly to get information about interfaces in a device information
    set that are associated with a particular device information element or
    that are associated with all device information elements.

    DeviceInterfaceData points to a structure that identifies a requested
    device interface. To get detailed information about an interface, call
    SetupDiGetDeviceInterfaceDetail. The detailed information includes the
    name of the device interface that can be passed to a Win32 function such
    as CreateFile (described in Microsoft Windows SDK documentation) to get
    a handle to the interface.

    See System Defined Device Interface Classes for a list of available
    device interface classes.

    -see-also
    ---------

    SetupDiEnumDeviceInfo

    SetupDiGetClassDevs

    SetupDiGetDeviceInterfaceDetail
    """

    def __new__(cls,
                DeviceInfoSet: HDEVINFO = None,
                DeviceInfoData: PSP_DEVINFO_DATA = None,
                InterfaceClassGuid: POINTER(GUID) = None,
                MemberIndex: DWORD = None,
                DeviceInterfaceData: PSP_DEVICE_INTERFACE_DATA = None
                ) -> BOOL:
        """

        :param DeviceInfoSet: HDEVINFO [in]
        :param DeviceInfoData: PSP_DEVINFO_DATA [in, optional]
        :param InterfaceClassGuid: POINTER(GUID) [in]
        :param MemberIndex: DWORD [in]
        :param DeviceInterfaceData: PSP_DEVICE_INTERFACE_DATA [out]
        :return: BOOL
        """

        func = setupapi.SetupDiEnumDeviceInterfaces
        func.argtypes = [
            HDEVINFO,
            PSP_DEVINFO_DATA,
            POINTER(GUID),
            DWORD,
            PSP_DEVICE_INTERFACE_DATA
        ]
        func.restype = BOOL
        return func(DeviceInfoSet, DeviceInfoData, InterfaceClassGuid, MemberIndex, DeviceInterfaceData)


class SetupDiGetDeviceInterfaceDetail(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacedetailw

    SetupDiGetDeviceInterfaceDetailW function
    =========================================

    -description
    ------------

    The SetupDiGetDeviceInterfaceDetail function returns details about a
    device interface.

    -parameters
    -----------

    -param DeviceInfoSet [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to the device information set that contains the interface for
    which to retrieve details. This handle is typically returned by
    SetupDiGetClassDevs.

    -param DeviceInterfaceData [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to an SP_DEVICE_INTERFACE_DATA structure that specifies the
    interface in DeviceInfoSet for which to retrieve details. A pointer of
    this type is typically returned by SetupDiEnumDeviceInterfaces.

    -param DeviceInterfaceDetailData [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to an SP_DEVICE_INTERFACE_DETAIL_DATA structure to receive
    information about the specified interface. This parameter is optional
    and can be NULL. This parameter must be NULL if
    DeviceInterfaceDetailSize is zero. If this parameter is specified, the
    caller must set DeviceInterfaceDetailData.cbSize to
    sizeof(SP_DEVICE_INTERFACE_DETAIL_DATA) before calling this function.
    The cbSize member always contains the size of the fixed part of the data
    structure, not a size reflecting the variable-length string at the end.

    -param DeviceInterfaceDetailDataSize [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size of the DeviceInterfaceDetailData buffer. The buffer must be at
    least (offsetof(SP_DEVICE_INTERFACE_DETAIL_DATA, DevicePath) +
    sizeof(TCHAR)) bytes, to contain the fixed part of the structure and a
    single NULL to terminate an empty MULTI_SZ string.

    This parameter must be zero if DeviceInterfaceDetailData is NULL.

    -param RequiredSize [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a variable of type DWORD that receives the required size of
    the DeviceInterfaceDetailData buffer. This size includes the size of the
    fixed part of the structure plus the number of bytes required for the
    variable-length device path string. This parameter is optional and can
    be NULL.

    -param DeviceInfoData [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a buffer that receives information about the device that
    supports the requested interface. The caller must set
    DeviceInfoData.cbSize to sizeof(SP_DEVINFO_DATA). This parameter is
    optional and can be NULL.

    -returns
    --------

    SetupDiGetDeviceInterfaceDetail returns TRUE if the function completed
    without error. If the function completed with an error, FALSE is
    returned and the error code for the failure can be retrieved by calling
    GetLastError.

    -remarks
    --------

    Using this function to get details about an interface is typically a
    two-step process:

    .. raw:: html

       <ol>

    .. raw:: html

       <li>

    Get the required buffer size. Call SetupDiGetDeviceInterfaceDetail with
    a NULLDeviceInterfaceDetailData pointer, a DeviceInterfaceDetailDataSize
    of zero, and a valid RequiredSize variable. In response to such a call,
    this function returns the required buffer size at RequiredSize and fails
    with GetLastError returning ERROR_INSUFFICIENT_BUFFER.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Allocate an appropriately sized buffer and call the function again to
    get the interface details.

    .. raw:: html

       </li>

    .. raw:: html

       </ol>

    The interface detail returned by this function consists of a device path
    that can be passed to Win32 functions such as CreateFile. Do not attempt
    to parse the device path symbolic name. The device path can be reused
    across system starts.

    SetupDiGetDeviceInterfaceDetail can be used to get just the
    DeviceInfoData. If the interface exists but DeviceInterfaceDetailData is
    NULL, this function fails, GetLastError returns
    ERROR_INSUFFICIENT_BUFFER, and the DeviceInfoData structure is filled
    with information about the device that exposes the interface.

       [!NOTE] The setupapi.h header defines SetupDiGetDeviceInterfaceDetail
       as an alias which automatically selects the ANSI or Unicode version
       of this function based on the definition of the UNICODE preprocessor
       constant. Mixing usage of the encoding-neutral alias with code that
       not encoding-neutral can lead to mismatches that result in
       compilation or runtime errors. For more information, see `Conventions
       for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.

    -see-also
    ---------

    SetupDiEnumDeviceInterfaces

    SetupDiGetClassDevs
    """

    def __new__(cls,
                DeviceInfoSet: HDEVINFO = None,
                DeviceInterfaceData: PSP_DEVICE_INTERFACE_DATA = None,
                DeviceInterfaceDetailData: PSP_DEVICE_INTERFACE_DETAIL_DATA_W = None,
                DeviceInterfaceDetailDataSize: DWORD = None,
                RequiredSize: PDWORD = None,
                DeviceInfoData: PSP_DEVINFO_DATA = None
                ) -> BOOL:
        """

        :param DeviceInfoSet: HDEVINFO [in]
        :param DeviceInterfaceData: PSP_DEVICE_INTERFACE_DATA [in]
        :param DeviceInterfaceDetailData: PSP_DEVICE_INTERFACE_DETAIL_DATA_W [out, optional]
        :param DeviceInterfaceDetailDataSize: DWORD [in]
        :param RequiredSize: PDWORD [out, optional]
        :param DeviceInfoData: PSP_DEVINFO_DATA [out, optional]
        :return: BOOL
        """

        func = setupapi.SetupDiGetDeviceInterfaceDetailW
        func.argtypes = [
            HDEVINFO,
            PSP_DEVICE_INTERFACE_DATA,
            PSP_DEVICE_INTERFACE_DETAIL_DATA_W,
            DWORD,
            PDWORD,
            PSP_DEVINFO_DATA
        ]
        func.restype = BOOL
        return func(DeviceInfoSet, DeviceInterfaceData, DeviceInterfaceDetailData, DeviceInterfaceDetailDataSize,
                    RequiredSize, DeviceInfoData)


class SetupDiGetDeviceRegistryProperty(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceregistrypropertyw

    SetupDiGetDeviceRegistryPropertyW function
    ==========================================

    -description
    ------------

    The SetupDiGetDeviceRegistryProperty function retrieves a specified Plug
    and Play device property.

    -parameters
    -----------

    -param DeviceInfoSet [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A handle to a device information set that contains a device information
    element that represents the device for which to retrieve a Plug and Play
    property.

    -param DeviceInfoData [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to an SP_DEVINFO_DATA structure that specifies the device
    information element in DeviceInfoSet.

    -param Property [in]
    ~~~~~~~~~~~~~~~~~~~~

    One of the following values that specifies the property to be retrieved:

    SPDRP_ADDRESS
    ^^^^^^^^^^^^^

    The function retrieves the device’s address.

    SPDRP_BUSNUMBER
    ^^^^^^^^^^^^^^^

    The function retrieves the device’s bus number.

    SPDRP_BUSTYPEGUID
    ^^^^^^^^^^^^^^^^^

    The function retrieves the GUID for the device’s bus type.

    SPDRP_CAPABILITIES
    ^^^^^^^^^^^^^^^^^^

    The function retrieves a bitwise OR of the following CM_DEVCAP\_Xxx
    flags in a DWORD. The device capabilities that are represented by these
    flags correspond to the device capabilities that are represented by the
    members of the DEVICE_CAPABILITIES structure. The CM_DEVCAP_Xxx
    constants are defined in Cfgmgr32.h.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    CM_DEVCAP_Xxx flag

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    Corresponding DEVICE_CAPABILITIES structure member

    .. raw:: html

       </th>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_LOCKSUPPORTED

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    LockSupported

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_EJECTSUPPORTED

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    EjectSupported

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_REMOVABLE

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Removable

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_DOCKDEVICE

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    DockDevice

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_UNIQUEID

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    UniqueID

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_SILENTINSTALL

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    SilentInstall

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_RAWDEVICEOK

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    RawDeviceOK

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_SURPRISEREMOVALOK

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    SurpriseRemovalOK

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_HARDWAREDISABLED

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    HardwareDisabled

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_NONDYNAMIC

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    NonDynamic

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

     

    SPDRP_CHARACTERISTICS
    ^^^^^^^^^^^^^^^^^^^^^

    The function retrieves a bitwise OR of a device’s characteristics flags
    in a DWORD. For a description of these flags, which are defined in Wdm.h
    and Ntddk.h, see the DeviceCharacteristics parameter of the
    IoCreateDevice function.

    SPDRP_CLASS
    ^^^^^^^^^^^

    The function retrieves a REG_SZ string that contains the device setup
    class of a device.

    SPDRP_CLASSGUID
    ^^^^^^^^^^^^^^^

    The function retrieves a REG_SZ string that contains the GUID that
    represents the device setup class of a device.

    SPDRP_COMPATIBLEIDS
    ^^^^^^^^^^^^^^^^^^^

    The function retrieves a REG_MULTI_SZ string that contains the list of
    compatible IDs for a device. For information about compatible IDs, see
    Device Identification Strings.

    SPDRP_CONFIGFLAGS
    ^^^^^^^^^^^^^^^^^

    The function retrieves a bitwise OR of a device’s configuration flags in
    a DWORD value. The configuration flags are represented by the
    CONFIGFLAG\_Xxx bitmasks that are defined in Regstr.h.

    SPDRP_DEVICE_POWER_DATA
    ^^^^^^^^^^^^^^^^^^^^^^^

    (Windows XP and later) The function retrieves a CM_POWER_DATA structure
    that contains the device’s power management information.

    SPDRP_DEVICEDESC
    ^^^^^^^^^^^^^^^^

    The function retrieves a REG_SZ string that contains the description of
    a device.

    SPDRP_DEVTYPE
    ^^^^^^^^^^^^^

    The function retrieves a DWORD value that represents the device’s type.
    For more information, see Specifying Device Types.

    SPDRP_DRIVER
    ^^^^^^^^^^^^

    The function retrieves a string that identifies the device’s software
    key (sometimes called the driver key). For more information about driver
    keys, see Registry Trees and Keys for Devices and Drivers.

    SPDRP_ENUMERATOR_NAME
    ^^^^^^^^^^^^^^^^^^^^^

    The function retrieves a REG_SZ string that contains the name of the
    device’s enumerator.

    SPDRP_EXCLUSIVE
    ^^^^^^^^^^^^^^^

    The function retrieves a DWORD value that indicates whether a user can
    obtain exclusive use of the device. The returned value is one if
    exclusive use is allowed, or zero otherwise. For more information, see
    IoCreateDevice.

    SPDRP_FRIENDLYNAME
    ^^^^^^^^^^^^^^^^^^

    The function retrieves a REG_SZ string that contains the friendly name
    of a device.

    SPDRP_HARDWAREID
    ^^^^^^^^^^^^^^^^

    The function retrieves a REG_MULTI_SZ string that contains the list of
    hardware IDs for a device. For information about hardware IDs, see
    Device Identification Strings.

    SPDRP_INSTALL_STATE
    ^^^^^^^^^^^^^^^^^^^

    (Windows XP and later) The function retrieves a DWORD value that
    indicates the installation state of a device. The installation state is
    represented by one of the CM_INSTALL_STATE\_Xxx values that are defined
    in Cfgmgr32.h. The CM_INSTALL_STATE\_Xxx values correspond to the
    DEVICE_INSTALL_STATE enumeration values.

    SPDRP_LEGACYBUSTYPE
    ^^^^^^^^^^^^^^^^^^^

    The function retrieves the device’s legacy bus type as an INTERFACE_TYPE
    value (defined in Wdm.h and Ntddk.h).

    SPDRP_LOCATION_INFORMATION
    ^^^^^^^^^^^^^^^^^^^^^^^^^^

    The function retrieves a REG_SZ string that contains the hardware
    location of a device.

    SPDRP_LOCATION_PATHS
    ^^^^^^^^^^^^^^^^^^^^

    (Windows Server 2003 and later) The function retrieves a REG_MULTI_SZ
    string that represents the location of the device in the device tree.

    SPDRP_LOWERFILTERS
    ^^^^^^^^^^^^^^^^^^

    The function retrieves a REG_MULTI_SZ string that contains the names of
    a device’s lower-filter drivers.

    SPDRP_MFG
    ^^^^^^^^^

    The function retrieves a REG_SZ string that contains the name of the
    device manufacturer.

    SPDRP_PHYSICAL_DEVICE_OBJECT_NAME
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    The function retrieves a REG_SZ string that contains the name that is
    associated with the device’s PDO. For more information, see
    IoCreateDevice.

    SPDRP_REMOVAL_POLICY
    ^^^^^^^^^^^^^^^^^^^^

    (Windows XP and later) The function retrieves the device’s current
    removal policy as a DWORD that contains one of the
    CM_REMOVAL_POLICY\_Xxx values that are defined in Cfgmgr32.h.

    SPDRP_REMOVAL_POLICY_HW_DEFAULT
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    (Windows XP and later) The function retrieves the device’s
    hardware-specified default removal policy as a DWORD that contains one
    of the CM_REMOVAL_POLICY\_Xxx values that are defined in Cfgmgr32.h.

    SPDRP_REMOVAL_POLICY_OVERRIDE
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    (Windows XP and later) The function retrieves the device’s override
    removal policy (if it exists) from the registry, as a DWORD that
    contains one of the CM_REMOVAL_POLICY\_Xxx values that are defined in
    Cfgmgr32.h.

    SPDRP_SECURITY
    ^^^^^^^^^^^^^^

    The function retrieves a SECURITY_DESCRIPTOR structure for a device.

    SPDRP_SECURITY_SDS
    ^^^^^^^^^^^^^^^^^^

    The function retrieves a REG_SZ string that contains the device’s
    security descriptor. For information about security descriptor strings,
    see Security Descriptor Definition Language (Windows). For information
    about the format of security descriptor strings, see Security Descriptor
    Definition Language (Windows).

    SPDRP_SERVICE
    ^^^^^^^^^^^^^

    The function retrieves a REG_SZ string that contains the service name
    for a device.

    SPDRP_UI_NUMBER
    ^^^^^^^^^^^^^^^

    The function retrieves a DWORD value set to the value of the UINumber
    member of the device’s DEVICE_CAPABILITIES structure.

    SPDRP_UI_NUMBER_DESC_FORMAT
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^

    The function retrieves a format string (REG_SZ) used to display the
    UINumber value.

    SPDRP_UPPERFILTERS
    ^^^^^^^^^^^^^^^^^^

    The function retrieves a REG_MULTI_SZ string that contains the names of
    a device’s upper filter drivers.

    -param PropertyRegDataType [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a variable that receives the data type of the property that
    is being retrieved. This is one of the standard registry data types.
    This parameter is optional and can be NULL.

    -param PropertyBuffer [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a buffer that receives the property that is being
    retrieved. If this parameter is set to NULL, and PropertyBufferSize is
    also set to zero, the function returns the required size for the buffer
    in RequiredSize.

    -param PropertyBufferSize [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size, in bytes, of the PropertyBuffer buffer.

    -param RequiredSize [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a variable of type DWORD that receives the required size,
    in bytes, of the PropertyBuffer buffer that is required to hold the data
    for the requested property. This parameter is optional and can be NULL.

    - Property.SPDRP_ADDRESS
    ''''''''''''''''''''''''

    The function retrieves the device’s address.

    - Property.SPDRP_BUSNUMBER
    ''''''''''''''''''''''''''

    The function retrieves the device’s bus number.

    - Property.SPDRP_BUSTYPEGUID
    ''''''''''''''''''''''''''''

    The function retrieves the GUID for the device’s bus type.

    - Property.SPDRP_CAPABILITIES
    '''''''''''''''''''''''''''''

    The function retrieves a bitwise OR of the following CM_DEVCAP\_Xxx
    flags in a DWORD. The device capabilities that are represented by these
    flags correspond to the device capabilities that are represented by the
    members of the DEVICE_CAPABILITIES structure. The CM_DEVCAP_Xxx
    constants are defined in Cfgmgr32.h.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    CM_DEVCAP_Xxx flag

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    Corresponding DEVICE_CAPABILITIES structure member

    .. raw:: html

       </th>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_LOCKSUPPORTED

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    LockSupported

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_EJECTSUPPORTED

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    EjectSupported

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_REMOVABLE

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Removable

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_DOCKDEVICE

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    DockDevice

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_UNIQUEID

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    UniqueID

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_SILENTINSTALL

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    SilentInstall

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_RAWDEVICEOK

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    RawDeviceOK

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_SURPRISEREMOVALOK

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    SurpriseRemovalOK

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_HARDWAREDISABLED

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    HardwareDisabled

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    CM_DEVCAP_NONDYNAMIC

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    NonDynamic

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

     

    - Property.SPDRP_CHARACTERISTICS
    ''''''''''''''''''''''''''''''''

    The function retrieves a bitwise OR of a device’s characteristics flags
    in a DWORD. For a description of these flags, which are defined in Wdm.h
    and Ntddk.h, see the DeviceCharacteristics parameter of the
    IoCreateDevice function.

    - Property.SPDRP_CLASS
    ''''''''''''''''''''''

    The function retrieves a REG_SZ string that contains the device setup
    class of a device.

    - Property.SPDRP_CLASSGUID
    ''''''''''''''''''''''''''

    The function retrieves a REG_SZ string that contains the GUID that
    represents the device setup class of a device.

    - Property.SPDRP_COMPATIBLEIDS
    ''''''''''''''''''''''''''''''

    The function retrieves a REG_MULTI_SZ string that contains the list of
    compatible IDs for a device. For information about compatible IDs, see
    Device Identification Strings.

    - Property.SPDRP_CONFIGFLAGS
    ''''''''''''''''''''''''''''

    The function retrieves a bitwise OR of a device’s configuration flags in
    a DWORD value. The configuration flags are represented by the
    CONFIGFLAG\_Xxx bitmasks that are defined in Regstr.h.

    - Property.SPDRP_DEVICEDESC
    '''''''''''''''''''''''''''

    The function retrieves a REG_SZ string that contains the description of
    a device.

    - Property.SPDRP_DEVICE_POWER_DATA
    ''''''''''''''''''''''''''''''''''

    (Windows XP and later) The function retrieves a CM_POWER_DATA structure
    that contains the device’s power management information.

    - Property.SPDRP_DEVTYPE
    ''''''''''''''''''''''''

    The function retrieves a DWORD value that represents the device’s type.
    For more information, see Specifying Device Types.

    - Property.SPDRP_DRIVER
    '''''''''''''''''''''''

    The function retrieves a string that identifies the device’s software
    key (sometimes called the driver key). For more information about driver
    keys, see Registry Trees and Keys for Devices and Drivers.

    - Property.SPDRP_ENUMERATOR_NAME
    ''''''''''''''''''''''''''''''''

    The function retrieves a REG_SZ string that contains the name of the
    device’s enumerator.

    - Property.SPDRP_EXCLUSIVE
    ''''''''''''''''''''''''''

    The function retrieves a DWORD value that indicates whether a user can
    obtain exclusive use of the device. The returned value is one if
    exclusive use is allowed, or zero otherwise. For more information, see
    IoCreateDevice.

    - Property.SPDRP_FRIENDLYNAME
    '''''''''''''''''''''''''''''

    The function retrieves a REG_SZ string that contains the friendly name
    of a device.

    - Property.SPDRP_HARDWAREID
    '''''''''''''''''''''''''''

    The function retrieves a REG_MULTI_SZ string that contains the list of
    hardware IDs for a device. For information about hardware IDs, see
    Device Identification Strings.

    - Property.SPDRP_INSTALL_STATE
    ''''''''''''''''''''''''''''''

    (Windows XP and later) The function retrieves a DWORD value that
    indicates the installation state of a device. The installation state is
    represented by one of the CM_INSTALL_STATE\_Xxx values that are defined
    in Cfgmgr32.h. The CM_INSTALL_STATE\_Xxx values correspond to the
    DEVICE_INSTALL_STATE enumeration values.

    - Property.SPDRP_LEGACYBUSTYPE
    ''''''''''''''''''''''''''''''

    The function retrieves the device’s legacy bus type as an INTERFACE_TYPE
    value (defined in Wdm.h and Ntddk.h).

    - Property.SPDRP_LOCATION_INFORMATION
    '''''''''''''''''''''''''''''''''''''

    The function retrieves a REG_SZ string that contains the hardware
    location of a device.

    - Property.SPDRP_LOCATION_PATHS
    '''''''''''''''''''''''''''''''

    (Windows Server 2003 and later) The function retrieves a REG_MULTI_SZ
    string that represents the location of the device in the device tree.

    - Property.SPDRP_LOWERFILTERS
    '''''''''''''''''''''''''''''

    The function retrieves a REG_MULTI_SZ string that contains the names of
    a device’s lower-filter drivers.

    - Property.SPDRP_MFG
    ''''''''''''''''''''

    The function retrieves a REG_SZ string that contains the name of the
    device manufacturer.

    - Property.SPDRP_PHYSICAL_DEVICE_OBJECT_NAME
    ''''''''''''''''''''''''''''''''''''''''''''

    The function retrieves a REG_SZ string that contains the name that is
    associated with the device’s PDO. For more information, see
    IoCreateDevice.

    - Property.SPDRP_REMOVAL_POLICY
    '''''''''''''''''''''''''''''''

    (Windows XP and later) The function retrieves the device’s current
    removal policy as a DWORD that contains one of the
    CM_REMOVAL_POLICY\_Xxx values that are defined in Cfgmgr32.h.

    - Property.SPDRP_REMOVAL_POLICY_HW_DEFAULT
    ''''''''''''''''''''''''''''''''''''''''''

    (Windows XP and later) The function retrieves the device’s
    hardware-specified default removal policy as a DWORD that contains one
    of the CM_REMOVAL_POLICY\_Xxx values that are defined in Cfgmgr32.h.

    - Property.SPDRP_REMOVAL_POLICY_OVERRIDE
    ''''''''''''''''''''''''''''''''''''''''

    (Windows XP and later) The function retrieves the device’s override
    removal policy (if it exists) from the registry, as a DWORD that
    contains one of the CM_REMOVAL_POLICY\_Xxx values that are defined in
    Cfgmgr32.h.

    - Property.SPDRP_SECURITY
    '''''''''''''''''''''''''

    The function retrieves a SECURITY_DESCRIPTOR structure for a device.

    - Property.SPDRP_SECURITY_SDS
    '''''''''''''''''''''''''''''

    The function retrieves a REG_SZ string that contains the device’s
    security descriptor. For information about security descriptor strings,
    see Security Descriptor Definition Language (Windows). For information
    about the format of security descriptor strings, see Security Descriptor
    Definition Language (Windows).

    - Property.SPDRP_SERVICE
    ''''''''''''''''''''''''

    The function retrieves a REG_SZ string that contains the service name
    for a device.

    - Property.SPDRP_UI_NUMBER
    ''''''''''''''''''''''''''

    The function retrieves a DWORD value set to the value of the UINumber
    member of the device’s DEVICE_CAPABILITIES structure.

    - Property.SPDRP_UI_NUMBER_DESC_FORMAT
    ''''''''''''''''''''''''''''''''''''''

    The function retrieves a format string (REG_SZ) used to display the
    UINumber value.

    - Property.SPDRP_UPPERFILTERS
    '''''''''''''''''''''''''''''

    The function retrieves a REG_MULTI_SZ string that contains the names of
    a device’s upper filter drivers.

    -returns
    --------

    SetupDiGetDeviceRegistryProperty returns TRUE if the call was
    successful. Otherwise, it returns FALSE and the logged error can be
    retrieved by making a call to GetLastError.
    SetupDiGetDeviceRegistryProperty returns the ERROR_INVALID_DATA error
    code if the requested property does not exist for a device or if the
    property data is not valid.

    -see-also
    ---------

    IoGetDeviceProperty

    SetupDiGetClassRegistryProperty

    SetupDiSetClassRegistryProperty

    SetupDiSetDeviceRegistryProperty

    -remarks
    --------

       [!NOTE] The setupapi.h header defines
       SetupDiGetDeviceRegistryProperty as an alias which automatically
       selects the ANSI or Unicode version of this function based on the
       definition of the UNICODE preprocessor constant. Mixing usage of the
       encoding-neutral alias with code that not encoding-neutral can lead
       to mismatches that result in compilation or runtime errors. For more
       information, see `Conventions for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.
    """

    def __new__(cls,
                DeviceInfoSet: HDEVINFO = None,
                DeviceInfoData: PSP_DEVINFO_DATA = None,
                Property: DWORD = None,
                PropertyRegDataType: PDWORD = None,
                PropertyBuffer: PBYTE = None,
                PropertyBufferSize: DWORD = None,
                RequiredSize: PDWORD = None
                ) -> BOOL:
        """

        :param DeviceInfoSet: HDEVINFO [in]
        :param DeviceInfoData: PSP_DEVINFO_DATA [in]
        :param Property: DWORD [in]
        :param PropertyRegDataType: PDWORD [out, optional]
        :param PropertyBuffer: PBYTE [out, optional]
        :param PropertyBufferSize: DWORD [in]
        :param RequiredSize: PDWORD [out, optional]
        :return: BOOL
        """

        func = setupapi.SetupDiGetDeviceRegistryPropertyW
        func.argtypes = [
            HDEVINFO,
            PSP_DEVINFO_DATA,
            DWORD,
            PDWORD,
            PBYTE,
            DWORD,
            PDWORD
        ]
        func.restype = BOOL
        return func(DeviceInfoSet, DeviceInfoData, Property, PropertyRegDataType, PropertyBuffer, PropertyBufferSize,
                    RequiredSize)


class SetupDiEnumDeviceInfo(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinfo

    SetupDiEnumDeviceInfo function
    ==============================

    -description
    ------------

    The SetupDiEnumDeviceInfo function returns a SP_DEVINFO_DATA structure
    that specifies a device information element in a device information set.

    -parameters
    -----------

    -param DeviceInfoSet [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A handle to the device information set for which to return an
    SP_DEVINFO_DATA structure that represents a device information element.

    -param MemberIndex [in]
    ~~~~~~~~~~~~~~~~~~~~~~~

    A zero-based index of the device information element to retrieve.

    -param DeviceInfoData [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to an SP_DEVINFO_DATA structure to receive information about
    an enumerated device information element. The caller must set
    DeviceInfoData.cbSize to sizeof(SP_DEVINFO_DATA).

    -returns
    --------

    The function returns TRUE if it is successful. Otherwise, it returns
    FALSE and the logged error can be retrieved with a call to GetLastError.

    -remarks
    --------

    Repeated calls to this function return a device information element for
    a different device. This function can be called repeatedly to get
    information about all devices in the device information set.

    To enumerate device information elements, an installer should initially
    call SetupDiEnumDeviceInfo with the MemberIndex parameter set to 0. The
    installer should then increment MemberIndex and call
    SetupDiEnumDeviceInfo until there are no more values (the function fails
    and a call to GetLastError returns ERROR_NO_MORE_ITEMS).

    Call SetupDiEnumDeviceInterfaces to get a context structure for a device
    interface element (versus a device information element).

    -see-also
    ---------

    SP_DEVINFO_DATA

    SetupDiCreateDeviceInfo

    SetupDiDeleteDeviceInfo

    SetupDiEnumDeviceInterfaces

    SetupDiOpenDeviceInfo
    """

    def __new__(cls,
                DeviceInfoSet: HDEVINFO = None,
                MemberIndex: DWORD = None,
                DeviceInfoData: PSP_DEVINFO_DATA = None
                ) -> BOOL:
        """

        :param DeviceInfoSet: HDEVINFO [in]
        :param MemberIndex: DWORD [in]
        :param DeviceInfoData: PSP_DEVINFO_DATA [out]
        :return: BOOL
        """

        func = setupapi.SetupDiEnumDeviceInfo
        func.argtypes = [
            HDEVINFO,
            DWORD,
            PSP_DEVINFO_DATA
        ]
        func.restype = BOOL
        return func(DeviceInfoSet, MemberIndex, DeviceInfoData)


class SetupDiGetDevicePropertyKeys(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertykeys

    SetupDiGetDevicePropertyKeys function
    =====================================

    -description
    ------------

    The SetupDiGetDevicePropertyKeys function retrieves an array of the
    device property keys that represent the device properties that are set
    for a device instance.

    -parameters
    -----------

    -param DeviceInfoSet [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A handle to a device information set. This device information set
    contains the device instance for which this function retrieves an array
    of device property keys. The property keys represent the device
    properties that are set for the device instance.

    -param DeviceInfoData [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to an SP_DEVINFO_DATA structure that represents the device
    instance for which to retrieve the requested array of device property
    keys.

    -param PropertyKeyArray [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a buffer that receives an array of DEVPROPKEY-typed values,
    where each value is a device property key that represents a device
    property that is set for the device instance. The pointer is optional
    and can be NULL. For more information, see the Remarks section later in
    this topic.

    -param PropertyKeyCount [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size, in DEVPROPKEY-typed values, of the PropertyKeyArray buffer. If
    PropertyKeyArray is set to NULL, PropertyKeyCount must be set to zero.

    -param RequiredPropertyKeyCount [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a DWORD-typed variable that receives the number of
    requested device property keys. The pointer is optional and can be set
    to NULL.

    -param Flags [in]
    ~~~~~~~~~~~~~~~~~

    This parameter must be set to zero.

    -returns
    --------

    SetupDiGetDevicePropertyKeys returns TRUE if it is successful.
    Otherwise, it returns FALSE, and the logged error can be retrieved by
    calling GetLastError.

    The following table includes some of the more common error codes that
    this function might log.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    Return code

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    Description

    .. raw:: html

       </th>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INVALID_FLAGS

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The value of Flags is not zero.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INVALID_HANDLE

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The device information set that is specified by DevInfoSet is not valid.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INVALID_PARAMETER

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    A supplied parameter is not valid. One possibility is that the device
    information element is not valid.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INVALID_DATA

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    An internal data value is not valid.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INVALID_USER_BUFFER

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    A user buffer is not valid. One possibility is that PropertyKeyArray is
    NULL and PropertKeyCount is not zero.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_NO_SUCH_DEVINST

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The device instance that is specified by DevInfoData does not exist.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INSUFFICIENT_BUFFER

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The PropertyKeyArray buffer is too small to hold all the requested
    property keys.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_NOT_ENOUGH_MEMORY

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    There was not enough system memory available to complete the operation.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -remarks
    --------

    SetupDiGetDevicePropertyKeys is part of the unified device property
    model.

    If the ProperKeyArray buffer is not large enough to hold all the
    requested property keys, SetupDiGetDevicePropertyKeys does not retrieve
    any property keys and returns ERROR_INSUFFICIENT_BUFFER. If the caller
    supplied a RequiredPropertyKeyCount pointer,
    SetupDiGetDevicePropertyKeys sets the value of
    \*RequiredPropertyKeyCount to the required size, in DEVPROPKEY-typed
    values, of the PropertyKeyArray buffer.

    To retrieve a device instance property, call SetupDiGetDeviceProperty,
    and to set a device instance property, call SetupDiSetDeviceProperty.

    -see-also
    ---------

    SetupDiGetDeviceProperty

    SetupDiSetDeviceProperty
    """

    def __new__(cls,
                DeviceInfoSet: HDEVINFO = None,
                DeviceInfoData: PSP_DEVINFO_DATA = None,
                PropertyKeyArray: DEVPROPKEY = None,
                PropertyKeyCount: DWORD = None,
                RequiredPropertyKeyCount: PDWORD = None,
                Flags: DWORD = None
                ) -> BOOL:
        """

        :param DeviceInfoSet: HDEVINFO [in]
        :param DeviceInfoData: PSP_DEVINFO_DATA [in]
        :param PropertyKeyArray: DEVPROPKEY [out, optional]
        :param PropertyKeyCount: DWORD [in]
        :param RequiredPropertyKeyCount: PDWORD [out, optional]
        :param Flags: DWORD [in]
        :return: BOOL
        """

        func = setupapi.SetupDiGetDevicePropertyKeys
        func.argtypes = [
            HDEVINFO,
            PSP_DEVINFO_DATA,
            DEVPROPKEY,
            DWORD,
            PDWORD,
            DWORD
        ]
        func.restype = BOOL
        return func(DeviceInfoSet, DeviceInfoData, PropertyKeyArray, PropertyKeyCount, RequiredPropertyKeyCount, Flags)


class SetupDiGetDeviceProperty(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw

    SetupDiGetDevicePropertyW function
    ==================================

    -description
    ------------

    The SetupDiGetDeviceProperty function retrieves a device instance
    property.

    -parameters
    -----------

    -param DeviceInfoSet [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A handle to a device information set that contains a device instance for
    which to retrieve a device instance property.

    -param DeviceInfoData [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to the SP_DEVINFO_DATA structure that represents the device
    instance for which to retrieve a device instance property.

    -param PropertyKey [in]
    ~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a DEVPROPKEY structure that represents the device property
    key of the requested device instance property.

    -param PropertyType [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a DEVPROPTYPE-typed variable that receives the
    property-data-type identifier of the requested device instance property,
    where the property-data-type identifier is the bitwise OR between a
    base-data-type identifier and, if the base-data type is modified, a
    property-data-type modifier.

    -param PropertyBuffer [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a buffer that receives the requested device instance
    property. SetupDiGetDeviceProperty retrieves the requested property only
    if the buffer is large enough to hold all the property value data. The
    pointer can be NULL. If the pointer is set to NULL and RequiredSize is
    supplied, SetupDiGetDeviceProperty returns the size of the property, in
    bytes, in \*RequiredSize.

    -param PropertyBufferSize [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size, in bytes, of the PropertyBuffer buffer. If PropertyBuffer is
    set to NULL, PropertyBufferSize must be set to zero.

    -param RequiredSize [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a DWORD-typed variable that receives the size, in bytes, of
    either the device instance property if the property is retrieved or the
    required buffer size if the buffer is not large enough. This pointer can
    be set to NULL.

    -param Flags [in]
    ~~~~~~~~~~~~~~~~~

    This parameter must be set to zero.

    -returns
    --------

    SetupDiGetDeviceProperty returns TRUE if it is successful. Otherwise, it
    returns FALSE, and the logged error can be retrieved by calling
    GetLastError.

    The following table includes some of the more common error codes that
    this function might log.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    Return code

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    Description

    .. raw:: html

       </th>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INVALID_FLAGS

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The value of Flags is not zero.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INVALID_HANDLE

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The device information set that is specified by DevInfoSet is not valid.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INVALID_PARAMETER

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    A supplied parameter is not valid. One possibility is that the device
    information element is not valid.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INVALID_REG_PROPERTY

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The property key that is supplied by PropertyKey is not valid.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INVALID_DATA

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    An unspecified internal data value was not valid.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INVALID_USER_BUFFER

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    A user buffer is not valid. One possibility is that PropertyBuffer is
    NULL and PropertBufferSize is not zero.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_NO_SUCH_DEVINST

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The device instance that is specified by DevInfoData does not exist.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INSUFFICIENT_BUFFER

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The PropertyBuffer buffer is too small to hold the requested property
    value, or an internal data buffer that was passed to a system call was
    too small.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_NOT_ENOUGH_MEMORY

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    There was not enough system memory available to complete the operation.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_NOT_FOUND

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The requested device property does not exist.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_ACCESS_DENIED

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The caller does not have Administrator privileges.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -remarks
    --------

    SetupDiGetDeviceProperty is part of the unified device property model.

    SetupAPI supports only a Unicode version of SetupDiGetDeviceProperty.

    To obtain the device property keys that represent the device properties
    that are set for a device instance, call SetupDiGetDevicePropertyKeys.

    To set a device instance property, call SetupDiSetDeviceProperty.

    -see-also
    ---------

    SetupDiGetDevicePropertyKeys

    SetupDiSetDeviceProperty
    """

    def __new__(cls,
                DeviceInfoSet: HDEVINFO = None,
                DeviceInfoData: PSP_DEVINFO_DATA = None,
                PropertyKey: POINTER(DEVPROPKEY) = None,
                PropertyType: DEVPROPTYPE = None,
                PropertyBuffer: PBYTE = None,
                PropertyBufferSize: DWORD = None,
                RequiredSize: PDWORD = None,
                Flags: DWORD = None
                ) -> BOOL:
        """

        :param DeviceInfoSet: HDEVINFO [in]
        :param DeviceInfoData: PSP_DEVINFO_DATA [in]
        :param PropertyKey: POINTER(DEVPROPKEY) [in]
        :param PropertyType: DEVPROPTYPE [out]
        :param PropertyBuffer: PBYTE [out, optional]
        :param PropertyBufferSize: DWORD [in]
        :param RequiredSize: PDWORD [out, optional]
        :param Flags: DWORD [in]
        :return: BOOL
        """

        func = setupapi.SetupDiGetDevicePropertyW
        func.argtypes = [
            HDEVINFO,
            PSP_DEVINFO_DATA,
            POINTER(DEVPROPKEY),
            DEVPROPTYPE,
            PBYTE,
            DWORD,
            PDWORD,
            DWORD
        ]
        func.restype = BOOL
        return func(DeviceInfoSet, DeviceInfoData, PropertyKey, PropertyType, PropertyBuffer, PropertyBufferSize,
                    RequiredSize, Flags)


class SetupDiGetDeviceInstanceId(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinstanceidw

    SetupDiGetDeviceInstanceIdW function
    ====================================

    -description
    ------------

    The SetupDiGetDeviceInstanceId function retrieves the device instance ID
    that is associated with a device information element.

    -parameters
    -----------

    -param DeviceInfoSet [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A handle to the device information set that contains the device
    information element that represents the device for which to retrieve a
    device instance ID.

    -param DeviceInfoData [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to an SP_DEVINFO_DATA structure that specifies the device
    information element in DeviceInfoSet.

    -param DeviceInstanceId [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to the character buffer that will receive the NULL-terminated
    device instance ID for the specified device information element. For
    information about device instance IDs, see Device Identification
    Strings.

    -param DeviceInstanceIdSize [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size, in characters, of the DeviceInstanceId buffer.

    -param RequiredSize [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to the variable that receives the number of characters
    required to store the device instance ID.

    -returns
    --------

    The function returns TRUE if it is successful. Otherwise, it returns
    FALSE and the logged error can be retrieved by making a call to
    GetLastError.

    -see-also
    ---------

    SP_DEVINFO_DATA

    SetupDiCreateDevRegKey

    SetupDiCreateDeviceInfo

    SetupDiOpenDevRegKey

    SetupDiOpenDeviceInfo

    -remarks
    --------

       [!NOTE] The setupapi.h header defines SetupDiGetDeviceInstanceId as
       an alias which automatically selects the ANSI or Unicode version of
       this function based on the definition of the UNICODE preprocessor
       constant. Mixing usage of the encoding-neutral alias with code that
       not encoding-neutral can lead to mismatches that result in
       compilation or runtime errors. For more information, see `Conventions
       for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.
    """

    def __new__(cls,
                DeviceInfoSet: HDEVINFO = None,
                DeviceInfoData: PSP_DEVINFO_DATA = None,
                DeviceInstanceId: PWSTR = None,
                DeviceInstanceIdSize: DWORD = None,
                RequiredSize: PDWORD = None
                ) -> BOOL:
        """

        :param DeviceInfoSet: HDEVINFO [in]
        :param DeviceInfoData: PSP_DEVINFO_DATA [in]
        :param DeviceInstanceId: PWSTR [out, optional]
        :param DeviceInstanceIdSize: DWORD [in]
        :param RequiredSize: PDWORD [out, optional]
        :return: BOOL
        """

        func = setupapi.SetupDiGetDeviceInstanceIdW
        func.argtypes = [
            HDEVINFO,
            PSP_DEVINFO_DATA,
            PWSTR,
            DWORD,
            PDWORD
        ]
        func.restype = BOOL
        return func(DeviceInfoSet, DeviceInfoData, DeviceInstanceId, DeviceInstanceIdSize, RequiredSize)


class SetupGetInfDriverStoreLocation(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupgetinfdriverstorelocationw

    SetupGetInfDriverStoreLocationW function
    ========================================

    -description
    ------------

    The SetupGetInfDriverStoreLocation function retrieves the fully
    qualified file name (directory path and file name) of an INF file in the
    driver store that corresponds to a specified INF file in the system INF
    file directory or a specified INF file in the driver store.

    -parameters
    -----------

    -param FileName [in]
    ~~~~~~~~~~~~~~~~~~~~

    A pointer to a NULL-terminated string that contains the name, and
    optionally the full directory path, of an INF file in the system INF
    file directory. Alternatively, this parameter is a pointer to a
    NULL-terminated string that contains the fully qualified file name
    (directory path and file name) of an INF file in the driver store.

    For more information about how to specify the INF file, see the
    following Remarks section.

    -param AlternatePlatformInfo [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Reserved for system use.

    -param LocaleName [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Reserved for system use.

    -param ReturnBuffer [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a buffer in which the function returns a NULL-terminated
    string that contains the fully qualified file name of the specified INF
    file. This parameter can be set to NULL. The maximum supported path size
    is MAX_PATH. For information about how to determine the required size of
    the buffer, see the following Remarks section.

    -param ReturnBufferSize [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size, in characters, of the buffer supplied by ReturnBuffer.

    -param RequiredSize [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a DWORD-typed variable that receives the size, in
    characters, of the ReturnBuffer buffer. This parameter is optional and
    can be set to NULL.

    -returns
    --------

    If SetupGetInfDriverStoreLocation succeeds, the function returns TRUE;
    otherwise, the function returns FALSE. To obtain extended error
    information, call GetLastError.

    If the size, in characters, of the fully qualified file name of the
    requested INF file, including a null-terminator, is greater than
    ReturnBufferSize, the function will fail, and a call to GetLastError
    will return ERROR_INSUFFICIENT_BUFFER.

    -remarks
    --------

    To determine the size of the return buffer that is required to contain
    the fully qualified file name of the specified INF file in the driver
    store, call SetupGetInfDriverStoreLocation and set ReturnBuffer to NULL,
    ReturnBufferSize to zero, and supply RequiredSize.
    SetupGetInfDriverStoreLocation will return the required buffer size in
    RequiredSize.

    When device installation preinstalls a driver package in the driver
    store, it creates two copies of the driver package INF file. Device
    installation installs one copy in the system INF directory and assigns
    that copy of the INF file a unique published file name of the form
    OEMnnn.inf. Device installation installs a second copy of the INF file
    in the driver store and assigns that copy the original INF file name.

    SetupGetInfDriverStoreLocation returns the fully qualified file name of
    the INF file in the driver store that matches the INF file, if any, that
    is supplied by FileName. Filename must specify the file name, and
    optionally the directory path, of an INF file in the system INF
    directory. Alternatively, Filename must specify the fully qualified file
    name of an INF file in the driver store.

    For example, assume that the INF file for a driver package is Myinf.inf,
    and that for this driver package, device installation installs the INF
    file OEM1.inf in the system INF directory
    C::raw-latex:`\Windows`:raw-latex:`\inf`. Further assume that device
    installation installs the corresponding INF file copy
    C::raw-latex:`\windows`:raw-latex:`\system32`:raw-latex:`\driverstore`:raw-latex:`\filerepository`:raw-latex:`\myinf`\_12345678:raw-latex:`\myinf`.inf
    in the driver store. In this case, the function returns
    C::raw-latex:`\windows`:raw-latex:`\system32`:raw-latex:`\driverstore`:raw-latex:`\filerepository`:raw-latex:`\myinf`\_12345678:raw-latex:`\myinf`.inf
    if FileName supplies one of the following strings: OEM1.inf,
    C::raw-latex:`\Windows`:raw-latex:`\inf`:raw-latex:`\OEM`1.inf, or
    C::raw-latex:`\windows`:raw-latex:`\system32`:raw-latex:`\driverstore`:raw-latex:`\filerepository`:raw-latex:`\myinf`\_12345678:raw-latex:`\myinf`.inf.

    Class installers and co-installers can use
    SetupGetInfDriverStoreLocation to access files in a driver package that
    is preinstalled in the driver store. To determine the path of the driver
    package in the driver store, the installer does the following:

    .. raw:: html

       <ol>

    .. raw:: html

       <li>

    Call SetupDiGetDriverInfoDetail to retrieve a SP_DRVINFO_DETAIL_DATA
    structure for a driver. The InfFileName member of this structure
    contains the fully qualified file name of the driver INF file in the
    system INF directory.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Call SetupGetInfDriverStoreLocation and supply the fully qualified file
    name of the driver INF file that was retrieved by calling
    SetupDiGetDriverInfoDetail. SetupGetInfDriverStoreLocation will return
    the fully qualified file name of the driver INF file in the driver
    store. The directory path part of the fully qualified file name of the
    INF file is the path of the driver package files.

    .. raw:: html

       </li>

    .. raw:: html

       </ol>

    .. container:: alert

       Note  SetupGetInfDriverStoreLocation does not process the contents of
       the INF file that is specified in FileName. You cannot use this
       function to perform a content-specific search for an INF file in the
       driver store.

    .. container::

        

    Call the SetupGetInfPublishedName function to retrieve the fully
    qualified file name of an INF file in the system INF file directory that
    corresponds to a specified INF file in the system INF file directory or
    a specified file in the driver store.

       [!NOTE] The setupapi.h header defines SetupGetInfDriverStoreLocation
       as an alias which automatically selects the ANSI or Unicode version
       of this function based on the definition of the UNICODE preprocessor
       constant. Mixing usage of the encoding-neutral alias with code that
       not encoding-neutral can lead to mismatches that result in
       compilation or runtime errors. For more information, see `Conventions
       for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.

    -see-also
    ---------

    SP_ALTPLATFORM_INFO

    SP_DRVINFO_DETAIL_DATA

    SetupDiGetDriverInfoDetail

    SetupGetInfPublishedName
    """

    def __new__(cls,
                FileName: PCWSTR = None,
                AlternatePlatformInfo: PSP_ALTPLATFORM_INFO = None,
                LocaleName: PCWSTR = None,
                ReturnBuffer: PWSTR = None,
                ReturnBufferSize: DWORD = None,
                RequiredSize: PDWORD = None
                ) -> BOOL:
        """

        :param FileName: PCWSTR [in]
        :param AlternatePlatformInfo: PSP_ALTPLATFORM_INFO [in, optional]
        :param LocaleName: PCWSTR [in, optional]
        :param ReturnBuffer: PWSTR [out]
        :param ReturnBufferSize: DWORD [in]
        :param RequiredSize: PDWORD [out, optional]
        :return: BOOL
        """

        func = setupapi.SetupGetInfDriverStoreLocationW
        func.argtypes = [
            PCWSTR,
            PSP_ALTPLATFORM_INFO,
            PCWSTR,
            PWSTR,
            DWORD,
            PDWORD
        ]
        func.restype = BOOL
        return func(FileName, AlternatePlatformInfo, LocaleName, ReturnBuffer, ReturnBufferSize, RequiredSize)


class SetupGetInfPublishedName(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupgetinfpublishednamew

    SetupGetInfPublishedNameW function
    ==================================

    -description
    ------------

    The SetupGetInfPublishedName function retrieves the fully qualified file
    name (directory path and file name) of an INF file in the system INF
    file directory that corresponds to a specified INF file in the driver
    store or a specified INF file in the system INF file directory.

    -parameters
    -----------

    -param DriverStoreLocation [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a NULL-terminated string that contains the fully qualified
    file name (directory path and file name) of an INF file in the driver
    store. Alternatively, this parameter is a pointer to a NULL-terminated
    string that contains the name, and optionally the full directory path,
    of an INF file in the system INF file directory. For more information
    about how to specify the INF file, see the following Remarks section.

    -param ReturnBuffer [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to the buffer in which SetupGetInfPublishedName returns a
    NULL-terminated string that contains the fully qualified file name of
    the specified INF file in the system INF directory. The maximum path
    size is MAX_PATH. This pointer can be set to NULL. For information about
    how to determine the required size of the return buffer, see the
    following Remarks section.

    -param ReturnBufferSize [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size, in characters, of the buffer supplied by ReturnBuffer.

    -param RequiredSize [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a DWORD-typed variable that receives the size, in
    characters, of the ReturnBuffer buffer. This parameter is optional and
    can be set to NULL.

    -returns
    --------

    If SetupGetInfPublishedName succeeds, the function returns TRUE;
    otherwise, the function returns FALSE. To obtain extended error
    information, call GetLastError.

    If the size, in characters, of the fully qualified file name of the
    requested INF file, including a null-terminator, is greater than
    ReturnBufferSize, the function will fail, and a call to GetLastError
    will return ERROR_INSUFFICIENT_BUFFER.

    -remarks
    --------

    To determine the size of the return buffer that is required to contain
    the fully qualified file name of the specified INF file in the system
    INF directory, call SetupGetInfPublishedName and set ReturnBuffer to
    NULL, ReturnBufferSize to zero, and supply RequiredSize.
    SetupGetInfPublishedName will return the required buffer size in
    RequiredSize.

    When device installation preinstalls a driver package in the driver
    store, it creates two copies of the driver package INF file. Device
    installation adds one copy to the system INF directory and assigns that
    copy of the INF file a unique published file name of the form
    OEMnnn.inf. Device installation adds a second copy of the INF file to
    the driver store and assigns that copy the original INF file name.

    SetupGetInfPublishedName returns the fully qualified file name of the
    INF file in the system INF file directory that matches the INF file, if
    any, that is supplied by DriverStoreLocation. DriverStoreLocation must
    specify the fully qualified file name of an INF file in the driver store
    or must specify the file name, and optionally the directory path, of an
    INF file in the system INF directory. For example, assume that the INF
    file for a driver package is myinf.inf, and that for this driver
    package, device installation installs the INF file OEM1.inf in the
    system INF directory C::raw-latex:`\Windows`:raw-latex:`\inf`. Further
    assume that device installation installs the corresponding INF file copy
    C::raw-latex:`\windows`:raw-latex:`\system32`:raw-latex:`\driverstore`:raw-latex:`\filerepository`:raw-latex:`\myinf`\_12345678:raw-latex:`\myinf`.inf
    in the driver store. In this case, the function returns
    C::raw-latex:`\Windows`:raw-latex:`\inf`:raw-latex:`\OEM`1.inf if
    DriverStoreLocation supplies one of the following strings:
    C::raw-latex:`\windows`:raw-latex:`\system32`:raw-latex:`\driverstore`:raw-latex:`\filerepository`:raw-latex:`\myinf`\_12345678:raw-latex:`\myinf`.inf,
    OEM1.inf, or
    C::raw-latex:`\Windows`:raw-latex:`\inf`:raw-latex:`\OEM`1.inf.

    Call the SetupGetInfDriverStoreLocation function to retrieve the fully
    qualified file name of an INF file in the driver store that corresponds
    to a specified INF file in the system INF file directory or a specified
    file in the driver store.

       [!NOTE] The setupapi.h header defines SetupGetInfPublishedName as an
       alias which automatically selects the ANSI or Unicode version of this
       function based on the definition of the UNICODE preprocessor
       constant. Mixing usage of the encoding-neutral alias with code that
       not encoding-neutral can lead to mismatches that result in
       compilation or runtime errors. For more information, see `Conventions
       for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.

    -see-also
    ---------

    SetupGetInfDriverStoreLocation
    """

    def __new__(cls,
                DriverStoreLocation: PCWSTR = None,
                ReturnBuffer: PWSTR = None,
                ReturnBufferSize: DWORD = None,
                RequiredSize: PDWORD = None
                ) -> BOOL:
        """

        :param DriverStoreLocation: PCWSTR [in]
        :param ReturnBuffer: PWSTR [out]
        :param ReturnBufferSize: DWORD [in]
        :param RequiredSize: PDWORD [out, optional]
        :return: BOOL
        """

        func = setupapi.SetupGetInfPublishedNameW
        func.argtypes = [
            PCWSTR,
            PWSTR,
            DWORD,
            PDWORD
        ]
        func.restype = BOOL
        return func(DriverStoreLocation, ReturnBuffer, ReturnBufferSize, RequiredSize)


class SetupDiOpenDeviceInterfaceRegKey(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfaceregkey

    SetupDiOpenDeviceInterfaceRegKey function
    =========================================

    -description
    ------------

    The SetupDiOpenDeviceInterfaceRegKey function opens the registry subkey
    that is used by applications and drivers to store information that is
    specific to a device interface.

    -parameters
    -----------

    -param DeviceInfoSet [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a device information set that contains the device interface
    for which to open a registry subkey.

    -param DeviceInterfaceData [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to an SP_DEVICE_INTERFACE_DATA structure that specifies the
    device interface. This pointer can be returned by
    SetupDiCreateDeviceInterface or SetupDiEnumDeviceInterfaces.

    -param Reserved
    ~~~~~~~~~~~~~~~

    Reserved. Must be zero.

    -param samDesired [in]
    ~~~~~~~~~~~~~~~~~~~~~~

    The requested registry security access to the registry subkey. For
    information about registry security access values of type REGSAM, see
    the Microsoft Windows SDK documentation.

    -returns
    --------

    SetupDiOpenDeviceInterfaceRegKey returns a handle to the opened registry
    key. If the function fails, it returns INVALID_HANDLE_VALUE. To get
    extended error information, call GetLastError.

    -remarks
    --------

    Depending on the value that is passed in the samDesired parameter, it
    might be necessary for the caller of this function to be a member of the
    Administrators group.

    Close the handle returned from by function by calling RegCloseKey.

    -see-also
    ---------

    SetupDiCreateDeviceInterface

    SetupDiCreateDeviceInterfaceRegKey

    SetupDiEnumDeviceInterfaces
    """

    def __new__(cls,
                DeviceInfoSet: HDEVINFO = None,
                DeviceInterfaceData: PSP_DEVICE_INTERFACE_DATA = None,
                Reserved: DWORD = None,
                samDesired: REGSAM = None
                ) -> HKEY:
        """

        :param DeviceInfoSet: HDEVINFO [in]
        :param DeviceInterfaceData: PSP_DEVICE_INTERFACE_DATA [in]
        :param Reserved: DWORD Reserved. Must be zero.
        :param samDesired: REGSAM [in]
        :return: HKEY
        """

        func = setupapi.SetupDiOpenDeviceInterfaceRegKey
        func.argtypes = [
            HDEVINFO,
            PSP_DEVICE_INTERFACE_DATA,
            DWORD,
            REGSAM
        ]
        func.restype = HKEY
        return func(DeviceInfoSet, DeviceInterfaceData, Reserved, samDesired)


class SetupDiBuildDriverInfoList(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdibuilddriverinfolist

    SetupDiBuildDriverInfoList function
    ===================================

    -description
    ------------

    The SetupDiBuildDriverInfoList function builds a list of drivers that is
    associated with a specific device or with the global class driver list
    for a device information set.

    -parameters
    -----------

    -param DeviceInfoSet [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A handle to the device information set to contain the driver list,
    either globally for all device information elements or specifically for
    a single device information element. The device information set must not
    contain remote device information elements.

    -param DeviceInfoData [in, out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to an SP_DEVINFO_DATA structure for the device information
    element in DeviceInfoSet that represents the device for which to build a
    driver list. This parameter is optional and can be NULL. If this
    parameter is specified, the list is associated with the specified
    device. If this parameter is NULL, the list is associated with the
    global class driver list for DeviceInfoSet.

    If the class of this device is updated because of building a compatible
    driver list, DeviceInfoData.ClassGuid is updated upon return.

    -param DriverType [in]
    ~~~~~~~~~~~~~~~~~~~~~~

    The type of driver list to build. Must be one of the following values:

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    Value

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    Meaning

    .. raw:: html

       </th>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    SPDIT_CLASSDRIVER

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Build a list of class drivers. If DeviceInfoData is NULL, this driver
    list type must be specified.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    SPDIT_COMPATDRIVER

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Build a list of compatible drivers. DeviceInfoData must not be NULL if
    this driver list type is specified.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -returns
    --------

    The function returns TRUE if it is successful. Otherwise, it returns
    FALSE and the logged error can be retrieved by making a call to
    GetLastError.

    -remarks
    --------

    The device information set should be for a local computer because
    SetupDiBuildDriverInfoList searches for drivers only on a local
    computer. If the device information set is for a remote computer, the
    function returns TRUE but does not actually update the existing driver
    list for the device information set or, if supplied, the driver list for
    the device information element.

    The caller can set Flags in the SP_DEVINSTALL_PARAMS that are associated
    with the device information set or with a specific device
    (DeviceInfoData) to control how the list is built. For example, the
    caller can set the DI_FLAGSEX_ALLOWEXCLUDEDDRVS flag to include drivers
    that are marked Exclude From Select.

    A driver is “Exclude From Select” if either it is marked
    ExcludeFromSelect in the INF file or it is a driver for a device whose
    whole setup class is marked NoInstallClass or NoUseClass in the class
    installer INF file. Drivers for PnP devices are typically “Exclude From
    Select”; PnP devices should not be manually installed. To build a list
    of driver files for a PnP device a caller of SetupDiBuildDriverInfoList
    must set this flag.

    The DriverPath in the SP_DEVINSTALL_PARAMS contains either a path of a
    directory that contain INF files or a path of a specific INF file. If
    DI_ENUMSINGLEINF is set, DriverPath contains a path of a single INF
    file. If DriverPath is NULL, this function builds the driver list from
    the default INF file location, %SystemRoot%:raw-latex:`\inf`.

    After this function has built the specified driver list, the caller can
    enumerate the elements of the list by calling SetupDiEnumDriverInfo.

    If the driver list is associated with a device instance (that is,
    DeviceInfoData is specified), the resulting list is composed of drivers
    that have the same class as the device instance with which they are
    associated. If this is a global class driver list (that is, DriverType
    is SPDIT_CLASSDRIVER and DeviceInfoData is not specified), the class
    that is used when building the list is the class associated with the
    device information set. If the device information set has no associated
    class, drivers of all classes are used when building the list.

    Another thread can terminate the building of a driver list by a call to
    SetupDiCancelDriverInfoSearch.

    The DeviceInfoSet must only contain elements on the local computer. This
    function only searches for local drivers.

    -see-also
    ---------

    SetupDiCancelDriverInfoSearch

    SetupDiDestroyDriverInfoList

    SetupDiEnumDriverInfo
    """

    def __new__(cls,
                DeviceInfoSet: HDEVINFO = None,
                DeviceInfoData: PSP_DEVINFO_DATA = None,
                DriverType: DWORD = None
                ) -> BOOL:
        """

        :param DeviceInfoSet: HDEVINFO [in]
        :param DeviceInfoData: PSP_DEVINFO_DATA [in, out]
        :param DriverType: DWORD [in]
        :return: BOOL
        """

        func = setupapi.SetupDiBuildDriverInfoList
        func.argtypes = [
            HDEVINFO,
            PSP_DEVINFO_DATA,
            DWORD
        ]
        func.restype = BOOL
        return func(DeviceInfoSet, DeviceInfoData, DriverType)


class SetupDiEnumDriverInfo(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdienumdriverinfoW

    SetupDiEnumDriverInfoW function
    ===============================

    -description
    ------------

    The SetupDiEnumDriverInfo function enumerates the members of a driver
    list.

    -parameters
    -----------

    -param DeviceInfoSet [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A handle to the device information set that contains the driver list to
    enumerate.

    -param DeviceInfoData [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to an SP_DEVINFO_DATA structure that specifies a device
    information element in DeviceInfoSet. This parameter is optional and can
    be NULL. If this parameter is specified, SetupDiEnumDriverInfo
    enumerates a driver list for the specified device. If this parameter is
    NULL, SetupDiEnumDriverInfo enumerates the global class driver list that
    is associated with DeviceInfoSet (this list is of type
    SPDIT_CLASSDRIVER).

    -param DriverType [in]
    ~~~~~~~~~~~~~~~~~~~~~~

    The type of driver list to enumerate, which must be one of the following
    values:

    SPDIT_CLASSDRIVER
    ^^^^^^^^^^^^^^^^^

    Enumerate a class driver list. This driver list type must be specified
    if DeviceInfoData is not specified.

    SPDIT_COMPATDRIVER
    ^^^^^^^^^^^^^^^^^^

    Enumerate a list of compatible drivers for the specified device. This
    driver list type can be specified only if DeviceInfoData is also
    specified.

    -param MemberIndex [in]
    ~~~~~~~~~~~~~~~~~~~~~~~

    The zero-based index of the driver information member to retrieve.

    -param DriverInfoData [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a caller-initialized SP_DRVINFO_DATA structure that
    receives information about the enumerated driver. The caller must set
    DriverInfoData.cbSize to sizeof(SP_DRVINFO_DATA) before calling
    SetupDiEnumDriverInfo. If the cbSize member is not properly set,
    SetupDiEnumDriverInfo will return FALSE.

    - DriverType.SPDIT_CLASSDRIVER
    ''''''''''''''''''''''''''''''

    Enumerate a class driver list. This driver list type must be specified
    if DeviceInfoData is not specified.

    - DriverType.SPDIT_COMPATDRIVER
    '''''''''''''''''''''''''''''''

    Enumerate a list of compatible drivers for the specified device. This
    driver list type can be specified only if DeviceInfoData is also
    specified.

    -returns
    --------

    The function returns TRUE if it is successful. Otherwise, it returns
    FALSE and the logged error can be retrieved with a call to GetLastError.

    -remarks
    --------

    To enumerate driver information set members, an installer should first
    call SetupDiEnumDriverInfo with the MemberIndex parameter set to 0. It
    should then increment MemberIndex and call SetupDiEnumDriverInfo until
    there are no more values. When there are no more values, the function
    fails and a call to GetLastError returns ERROR_NO_MORE_ITEMS.

    If you do not properly initialize the cbSize member of the
    SP_DRVINFO_DATA structure that is supplied by the pointer
    DriverInfoData, the function will fail and log the error
    ERROR_INVALID_USER_BUFFER.

    To build a list of drivers associated with a specific device or with the
    global class driver list for a device information set first use
    SetupDiBuildDriverInfoList then pass that list to SetupDiEnumDriverInfo.

       [!NOTE] The setupapi.h header defines SetupDiEnumDriverInfo as an
       alias which automatically selects the ANSI or Unicode version of this
       function based on the definition of the UNICODE preprocessor
       constant. Mixing usage of the encoding-neutral alias with code that
       not encoding-neutral can lead to mismatches that result in
       compilation or runtime errors. For more information, see `Conventions
       for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.

    -see-also
    ---------

    SetupDiBuildDriverInfoList
    """

    def __new__(cls,
                DeviceInfoSet: HDEVINFO = None,
                DeviceInfoData: PSP_DEVINFO_DATA = None,
                DriverType: DWORD = None,
                MemberIndex: DWORD = None,
                DriverInfoData: PSP_DRVINFO_DATA_W = None
                ) -> BOOL:
        """

        :param DeviceInfoSet: HDEVINFO [in]
        :param DeviceInfoData: PSP_DEVINFO_DATA [in, optional]
        :param DriverType: DWORD [in]
        :param MemberIndex: DWORD [in]
        :param DriverInfoData: PSP_DRVINFO_DATA_W [out]
        :return: BOOL
        """

        func = setupapi.SetupDiEnumDriverInfoW
        func.argtypes = [
            HDEVINFO,
            PSP_DEVINFO_DATA,
            DWORD,
            DWORD,
            PSP_DRVINFO_DATA_W
        ]
        func.restype = BOOL
        return func(DeviceInfoSet, DeviceInfoData, DriverType, MemberIndex, DriverInfoData)
