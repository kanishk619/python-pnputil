from ctypes import windll

from winapi.cfgmgr32.datatypes import *

__all__ = [
    'CM_Enumerate_Classes', 'CM_Get_Class_Property', 'CM_Get_Class_Property_Keys',
    'CM_Get_Depth', 'CM_Get_Device_ID', 'CM_Get_Device_ID_List', 'CM_Get_Device_ID_List_Size',
    'CM_Get_Device_ID_Size', 'CM_Get_Device_Interface_Alias', 'CM_Get_Device_Interface_List',
    'CM_Get_Device_Interface_List_Size', 'CM_Get_Device_Interface_Property',
    'CM_Get_Device_Interface_Property_Keys', 'CM_Get_DevNode_Property',
    'CM_Get_DevNode_Property_Keys', 'CM_Get_DevNode_Status', 'CM_Locate_DevNode'
]

cfgmgr32 = windll.cfgmgr32


class CM_Enumerate_Classes(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_enumerate_classes

    CM_Enumerate_Classes function
    =============================

    -description
    ------------

    The CM_Enumerate_Classes function, when called repeatedly, enumerates
    the local machine’s installed device classes by supplying each class’s
    GUID.

    -parameters
    -----------

    -param ulClassIndex [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied index into the machine’s list of device classes. For
    more information, see the Remarks section.

    -param ClassGuid [out]
    ~~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied address of a GUID structure (described in the Microsoft
    Windows SDK) to receive a device class’s GUID.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Beginning with Windows , callers can specify the following flags:

    CM_ENUMERATE_CLASSES_INSTALLER
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Enumerate device setup classes.

    CM_ENUMERATE_CLASSES_INTERFACE
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Enumerate device interface classes.

    Otherwise, should be set to zero.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    To enumerate the local machine’s device classes, call
    CM_Enumerate_Classes repeatedly, starting with a ulClassIndex value of
    zero and incrementing the index value with each subsequent call until
    the function returns CR_NO_SUCH_VALUE. Some index values might represent
    list entries containing invalid class data, in which case the function
    returns CR_INVALID_DATA. This return value can be ignored.

    The class GUIDs obtained from this function can be used as input to the
    device installation functions.

    Beginning with Windows  and later operating systems, callers can use
    the ulFlags member to specify which device classes CM_Enumerate_Classes
    should return. Prior to Windows , CM_Enumerate_Classes returned only
    device setup classes.

    -see-also
    ---------

    CM_Enumerate_Classes_Ex
    """

    def __new__(cls,
                ulClassIndex: ULONG = None,
                ClassGuid: POINTER(GUID) = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param ulClassIndex: ULONG [in]
        :param ClassGuid: POINTER(GUID) [out]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Enumerate_Classes
        func.argtypes = [
            ULONG,
            POINTER(GUID),
            ULONG
        ]
        func.restype = CONFIGRET
        return func(ulClassIndex, ClassGuid, ulFlags)


class CM_Get_Device_ID(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_idw

    CM_Get_Device_IDW function
    ==========================

    -description
    ------------

    The CM_Get_Device_ID function retrieves the device instance ID for a
    specified device instance on the local machine.

    -parameters
    -----------

    -param dnDevInst [in]
    ~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied device instance handle that is bound to the local
    machine.

    -param Buffer [out]
    ~~~~~~~~~~~~~~~~~~~

    Address of a buffer to receive a device instance ID string. The required
    buffer size can be obtained by calling CM_Get_Device_ID_Size, then
    incrementing the received value to allow room for the string’s
    terminating NULL.

    -param BufferLen [in]
    ~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied length, in characters, of the buffer specified by
    Buffer.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Not used, must be zero.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    The function appends a NULL terminator to the supplied device instance
    ID string, unless the buffer is too small to hold the string. In this
    case, the function supplies as much of the identifier string as will fit
    into the buffer, and then returns CR_BUFFER_SMALL.

    For information about device instance IDs, see Device Identification
    Strings.

    For information about using device instance handles that are bound to
    the local machine, see CM_Get_Child.

    -see-also
    ---------

    CM_Get_Child

    CM_Get_Device_ID_Ex
    """

    def __new__(cls,
                dnDevInst: DEVINST = None,
                Buffer: PWSTR = None,
                BufferLen: ULONG = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param dnDevInst: DEVINST [in]
        :param Buffer: PWSTR [out]
        :param BufferLen: ULONG [in]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_Device_IDW
        func.argtypes = [
            DEVINST,
            PWSTR,
            ULONG,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(dnDevInst, Buffer, BufferLen, ulFlags)


class CM_Get_Device_ID_List(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_listw

    CM_Get_Device_ID_ListW function
    ===============================

    -description
    ------------

    The CM_Get_Device_ID_List function retrieves a list of device instance
    IDs for the local computer’s device instances.

    -parameters
    -----------

    -param pszFilter [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied pointer to a character string that is either set to a
    subset of the computer’s device instance identifiers (IDs), or to NULL.
    See the following description of ulFlags.

    -param Buffer [out]
    ~~~~~~~~~~~~~~~~~~~

    Address of a buffer to receive a set of NULL-terminated device instance
    identifier strings. The end of the set is terminated by an extra NULL.
    The required buffer size should be obtained by calling
    CM_Get_Device_ID_List_Size.

    -param BufferLen [in]
    ~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied length, in characters, of the buffer specified by
    Buffer.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    One of the following caller-supplied bit flags that specifies search
    filters:

    CM_GETIDLIST_FILTER_BUSRELATIONS
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    If this flag is set, pszFilter must specify a device instance
    identifier. The function returns device instance IDs for the bus
    relations of the specified device instance.

    CM_GETIDLIST_FILTER_CLASS (Windows 7 and later versions of Windows)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    If this flag is set, pszFilter contains a string that specifies a device
    setup class GUID. The returned list contains device instances for which
    the property (referenced by the CM_DRP_CLASSGUID constant) matches the
    specified device setup class GUID.

    The CM_DRP_CLASSGUID constant is defined in Cfgmgr32.h.

    CM_GETIDLIST_FILTER_PRESENT (Windows 7 and later versions of Windows)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    If this flag is set, the returned list contains only device instances
    that are currently present on the system. This value can be combined
    with other ulFlags values, such as CM_GETIDLIST_FILTER_CLASS.

    CM_GETIDLIST_FILTER_TRANSPORTRELATIONS (Windows 7 and later versions of Windows)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    If this flag is set, pszFilter must specify the device instance
    identifier of a composite device node (devnode).

    The function returns the device instance identifiers of the devnodes
    that represent the transport relations of the specified composite
    devnode.

    For more information about composite devnodes and transport relations,
    see the following Remarks section.

    CM_GETIDLIST_DONOTGENERATE
    ^^^^^^^^^^^^^^^^^^^^^^^^^^

    Used only with CM_GETIDLIST_FILTER_SERVICE. If set, and if the device
    tree does not contain a devnode for the specified service, this flag
    prevents the function from creating a devnode for the service.

    CM_GETIDLIST_FILTER_EJECTRELATIONS
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    If this flag is set, pszFilter must specify a device instance
    identifier. The function returns device instance IDs for the ejection
    relations of the specified device instance.

    CM_GETIDLIST_FILTER_ENUMERATOR
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    If this flag is set, *pszFilter* must specify the name of a device
    enumerator, optionally followed by a device ID. The string format is
    *EnumeratorName*\\<*DeviceID*>, such as **ROOT** or **ROOT\*PNP0500**.

    If pszFilter supplies only an enumerator name, the function returns
    device instance IDs for the instances of each device associated with the
    enumerator. Enumerator names can be obtained by calling
    CM_Enumerate_Enumerators.

    If pszFilter supplies both an enumerator and a device ID, the function
    returns device instance IDs only for the instances of the specified
    device that is associated with the enumerator.

    CM_GETIDLIST_FILTER_NONE
    ^^^^^^^^^^^^^^^^^^^^^^^^

    If this flag is set, pszFilter is ignored, and a list of all devices on
    the system is returned.

    CM_GETIDLIST_FILTER_POWERRELATIONS
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    If this flag is set, pszFilter must specify a device instance
    identifier. The function returns device instance IDs for the power
    relations of the specified device instance.

    CM_GETIDLIST_FILTER_REMOVALRELATIONS
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    If this flag is set, pszFilter must specify a device instance
    identifier. The function returns device instance IDs for the removal
    relations of the specified device instance.

    CM_GETIDLIST_FILTER_SERVICE
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^

    If this flag is set, pszFilter must specify the name of a Microsoft
    Windows service (typically a driver). The function returns device
    instance IDs for the device instances controlled by the specified
    service.

    Note that if the device tree does not contain a devnode for the
    specified service, this function creates one by default. To inhibit this
    behavior, also set CM_GETIDLIST_DONOTGENERATE.

    If no search filter flag is specified, the function returns all device
    instance IDs for all device instances.

    - ulFlags.CM_GETIDLIST_DONOTGENERATE
    ''''''''''''''''''''''''''''''''''''

    Used only with CM_GETIDLIST_FILTER_SERVICE. If set, and if the device
    tree does not contain a devnode for the specified service, this flag
    prevents the function from creating a devnode for the service.

    - ulFlags.CM_GETIDLIST_FILTER_BUSRELATIONS
    ''''''''''''''''''''''''''''''''''''''''''

    If this flag is set, pszFilter must specify a device instance
    identifier. The function returns device instance IDs for the bus
    relations of the specified device instance.

    - ulFlags.CM_GETIDLIST_FILTER_CLASS (Windows 7 and later versions of Windows)
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    If this flag is set, pszFilter contains a string that specifies a device
    setup class GUID. The returned list contains device instances for which
    the property (referenced by the CM_DRP_CLASSGUID constant) matches the
    specified device setup class GUID.

    The CM_DRP_CLASSGUID constant is defined in Cfgmgr32.h.

    - ulFlags.CM_GETIDLIST_FILTER_EJECTRELATIONS
    ''''''''''''''''''''''''''''''''''''''''''''

    If this flag is set, pszFilter must specify a device instance
    identifier. The function returns device instance IDs for the ejection
    relations of the specified device instance.

    - ulFlags.CM_GETIDLIST_FILTER_ENUMERATOR
    ''''''''''''''''''''''''''''''''''''''''

    If this flag is set, pszFilter must specify the name of a device
    enumerator, optionally followed by a device ID. The string format is
    EnumeratorName\\<DeviceID>, such as ROOT or ROOT*PNP0500.

    If pszFilter supplies only an enumerator name, the function returns
    device instance IDs for the instances of each device associated with the
    enumerator. Enumerator names can be obtained by calling
    CM_Enumerate_Enumerators.

    If pszFilter supplies both an enumerator and a device ID, the function
    returns device instance IDs only for the instances of the specified
    device that is associated with the enumerator.

    - ulFlags.CM_GETIDLIST_FILTER_NONE
    ''''''''''''''''''''''''''''''''''

    If this flag is set, pszFilter is ignored, and a list of all devices on
    the system is returned.

    - ulFlags.CM_GETIDLIST_FILTER_POWERRELATIONS
    ''''''''''''''''''''''''''''''''''''''''''''

    If this flag is set, pszFilter must specify a device instance
    identifier. The function returns device instance IDs for the power
    relations of the specified device instance.

    - ulFlags.CM_GETIDLIST_FILTER_PRESENT (Windows 7 and later versions of Windows)
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    If this flag is set, the returned list contains only device instances
    that are currently present on the system. This value can be combined
    with other ulFlags values, such as CM_GETIDLIST_FILTER_CLASS.

    - ulFlags.CM_GETIDLIST_FILTER_REMOVALRELATIONS
    ''''''''''''''''''''''''''''''''''''''''''''''

    If this flag is set, pszFilter must specify a device instance
    identifier. The function returns device instance IDs for the removal
    relations of the specified device instance.

    - ulFlags.CM_GETIDLIST_FILTER_SERVICE
    '''''''''''''''''''''''''''''''''''''

    If this flag is set, pszFilter must specify the name of a Microsoft
    Windows service (typically a driver). The function returns device
    instance IDs for the device instances controlled by the specified
    service.

    Note that if the device tree does not contain a devnode for the
    specified service, this function creates one by default. To inhibit this
    behavior, also set CM_GETIDLIST_DONOTGENERATE.

    - ulFlags.CM_GETIDLIST_FILTER_TRANSPORTRELATIONS (Windows 7 and later versions of Windows)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    If this flag is set, pszFilter must specify the device instance
    identifier of a composite device node (devnode).

    The function returns the device instance identifiers of the devnodes
    that represent the transport relations of the specified composite
    devnode.

    For more information about composite devnodes and transport relations,
    see the following Remarks section.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    Starting with Windows 7, a device that supports multiple transport paths
    for packet-based data is referred to as a composite device and is
    represented by a composite devnode. A composite devnode logically
    represents the composite device to the user and applications as a single
    device, even though the composite devnode can have multiple paths to the
    physical device.

    Each active transport path to the physical device is represented by a
    transport devnode and is referred to as a transport relation for the
    composite device.

    The composite devnode (but not the related transport devnodes) exposes
    device interfaces to applications and the system. When an application
    uses these public device interfaces, the composite device routes the
    packet-based data to one or more of these transport devnodes, which then
    transport the data to the physical device.

    For example, if a physical cell phone is simultaneously connected to the
    computer on the USB and the Bluetooth buses, each bus enumerates a child
    transport devnode on that bus to represent the device’s physical
    connection.

    In this case, if you set the CM_GETIDLIST_FILTER_TRANSPORTRELATIONS
    flags in ulFlags and specify the device instance ID of the cell phone’s
    composite devnode in pszFilter, the function returns the device instance
    IDs for the two transport devnodes in the Buffer parameter.

    For more information about device instance IDs, see Device
    Identification Strings.

       The cfgmgr32.h header defines CM_Get_Device_ID_List as an
       alias which automatically selects the ANSI or Unicode version of this
       function based on the definition of the UNICODE preprocessor
       constant. Mixing usage of the encoding-neutral alias with code that
       not encoding-neutral can lead to mismatches that result in
       compilation or runtime errors. For more information, see `Conventions
       for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.

    -see-also
    ---------

    CM_Get_Device_ID_List_Size
    """

    def __new__(cls,
                pszFilter: PCWSTR = None,
                Buffer: PZZWSTR = None,
                BufferLen: ULONG = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param pszFilter: PCWSTR [in, optional]
        :param Buffer: PZZWSTR [out]
        :param BufferLen: ULONG [in]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_Device_ID_ListW
        func.argtypes = [
            PCWSTR,
            PZZWSTR,
            ULONG,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(pszFilter, Buffer, BufferLen, ulFlags)


class CM_Get_Device_ID_List_Size(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_list_sizew

    CM_Get_Device_ID_List_SizeW function
    ====================================

    -description
    ------------

    The CM_Get_Device_ID_List_Size function retrieves the buffer size
    required to hold a list of device instance IDs for the local machine’s
    device instances.

    -parameters
    -----------

    -param pulLen [out]
    ~~~~~~~~~~~~~~~~~~~

    Receives a value representing the required buffer size, in characters.

    -param pszFilter [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied pointer to a character string specifying a subset of the
    machine’s device instance identifiers, or NULL. See the following
    description of ulFlags.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    One of the optional, caller-supplied bit flags that specify search
    filters. If no flags are specified, the function supplies the buffer
    size required to hold all instance identifiers for all device instances.
    For a list of bit flags, see the ulFlags description for
    CM_Get_Device_ID_List.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    The CM_Get_Device_ID_List_Size function should be called to determine
    the buffer size required by CM_Get_Device_ID_List.

    The size value supplied in the location pointed to by pulLen is
    guaranteed to represent a buffer size large enough to hold all device
    instance identifier strings and terminating NULLs. The supplied value
    might actually represent a buffer size that is larger than necessary, so
    don’t assume the value represents the true length of the character
    strings that CM_Get_Device_ID_List will provide.

    For information about device instance IDs, see Device Identification
    Strings.

       The cfgmgr32.h header defines CM_Get_Device_ID_List_Size as
       an alias which automatically selects the ANSI or Unicode version of
       this function based on the definition of the UNICODE preprocessor
       constant. Mixing usage of the encoding-neutral alias with code that
       not encoding-neutral can lead to mismatches that result in
       compilation or runtime errors. For more information, see `Conventions
       for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.

    -see-also
    ---------

    CM_Get_Device_ID_List_Size_Ex
    """

    def __new__(cls,
                pulLen: PULONG = None,
                pszFilter: PCWSTR = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param pulLen: PULONG [out]
        :param pszFilter: PCWSTR [in, optional]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_Device_ID_List_SizeW
        func.argtypes = [
            PULONG,
            PCWSTR,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(pulLen, pszFilter, ulFlags)


class CM_Get_Device_ID_Size(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_size

    CM_Get_Device_ID_Size function
    ==============================

    -description
    ------------

    The CM_Get_Device_ID_Size function retrieves the buffer size required to
    hold a device instance ID for a device instance on the local machine.

    -parameters
    -----------

    -param pulLen [out]
    ~~~~~~~~~~~~~~~~~~~

    Receives a value representing the required buffer size, in characters.

    -param dnDevInst [in]
    ~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied device instance handle that is bound to the local
    machine.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Not used, must be zero.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    The CM_Get_Device_ID_Size function should be called to determine the
    buffer size required by CM_Get_Device_ID.

    The size value supplied in the location pointed to by pulLen is less
    than MAX_DEVICE_ID_LEN, and does not include the identifier string’s
    terminating NULL. If the specified device instance does not exist, the
    function supplies a size value of zero.

    For information about device instance IDs, see Device Identification
    Strings.

    For information about using device instance handles that are bound to
    the local machine, see CM_Get_Child.

    -see-also
    ---------

    CM_Get_Child

    CM_Get_Device_ID

    CM_Get_Device_ID_Size_Ex
    """

    def __new__(cls,
                pulLen: PULONG = None,
                dnDevInst: DEVINST = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param pulLen: PULONG [out]
        :param dnDevInst: DEVINST [in]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_Device_ID_Size
        func.argtypes = [
            PULONG,
            DEVINST,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(pulLen, dnDevInst, ulFlags)


class CM_Get_Device_Interface_Alias(object):
    """
    https://docs.microsoft.com/en-gb/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_aliasw

    CM_Get_Device_Interface_AliasW function
    =======================================

    -description
    ------------

    The CM_Get_Device_Interface_Alias function returns the alias of the
    specified device interface instance, if the alias exists.

    -parameters
    -----------

    -param pszDeviceInterface [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to the name of the device interface instance for which to
    retrieve an alias. The caller typically received this string from a call
    to CM_Get_Device_Interface_List, or in a PnP notification structure.

    -param AliasInterfaceGuid [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a GUID specifying the interface class of the alias to
    retrieve.

    -param pszAliasDeviceInterface [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Specifies a pointer to a buffer, that upon successful return, points to
    a string containing the name of the alias. The caller must free this
    string when it is no longer needed.

    A buffer is required. Otherwise, the call will fail.

    -param pulLength [in, out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Supplies the count of characters in pszAliasDeviceInterface and receives
    the number of characters required to hold the alias device interface.

    On input, this parameter must be greater than 0.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Reserved. Do not use.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

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

    CR_NO_SUCH_DEVICE_INTERFACE

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Possibly indicates that there is no alias of the specified interface
    class.

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

    CR_OUT_OF_MEMORY

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    There is not enough memory to complete the operation.

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

    CR_BUFFER_SMALL

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The buffer passed is too small.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -remarks
    --------

    Device interfaces are considered aliases if they are exposed by the same
    underlying device and have identical interface reference strings, but
    are of different interface classes.

    The pszDeviceInterface parameter specifies a device interface instance
    for a particular device, belonging to a particular interface class, with
    a particular reference string. CM_Get_Device_Interface_Alias returns
    another device interface instance for the same device and reference
    string, but of a different interface class, if it exists.

    For example, the function driver for a fault-tolerant volume could
    register and set two device interfaces, one of the fault-tolerant-volume
    interface class and one of the volume interface class. Another driver
    could call CM_Get_Device_Interface_Alias with the symbolic link for one
    of the interfaces and ask whether the other interface exists by
    specifying its interface class.

    Two device interfaces with NULL reference strings are aliases if they
    are exposed by the same underlying device and have different interface
    class GUIDs.
    """

    def __new__(cls,
                pszDeviceInterface: LPCWSTR = None,
                AliasInterfaceGuid: LPGUID = None,
                pszAliasDeviceInterface: LPWSTR = None,
                pulLength: PULONG = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param pszDeviceInterface: LPCWSTR [in]
        :param AliasInterfaceGuid: LPGUID [in]
        :param pszAliasDeviceInterface: LPWSTR [out]
        :param pulLength: PULONG [in, out]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_Device_Interface_AliasW
        func.argtypes = [
            LPCWSTR,
            LPGUID,
            LPWSTR,
            PULONG,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(pszDeviceInterface, AliasInterfaceGuid, pszAliasDeviceInterface, pulLength, ulFlags)


class CM_Get_Device_Interface_List(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_listw

    CM_Get_Device_Interface_ListW function
    ======================================

    -description
    ------------

    The CM_Get_Device_Interface_List function retrieves a list of device
    interface instances that belong to a specified device interface class.

    -parameters
    -----------

    -param InterfaceClassGuid [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Supplies a GUID that identifies a device interface class.

    -param pDeviceID [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied pointer to a NULL-terminated string that represents a
    device instance ID. If specified, the function retrieves device
    interfaces that are supported by the device for the specified class. If
    this value is NULL, or if it points to a zero-length string, the
    function retrieves all interfaces that belong to the specified class.

    -param Buffer [out]
    ~~~~~~~~~~~~~~~~~~~

    Caller-supplied pointer to a buffer that receives multiple,
    NULL-terminated Unicode strings, each representing the symbolic link
    name of an interface instance.

    -param BufferLen [in]
    ~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied value that specifies the length, in characters, of the
    buffer pointed to by Buffer. Call CM_Get_Device_Interface_List_Size to
    determine the required buffer size.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Contains one of the following caller-supplied flags:

    CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    The function provides a list containing device interfaces associated
    with all devices that match the specified GUID and device instance ID,
    if any.

    CM_GET_DEVICE_INTERFACE_LIST_PRESENT
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    The function provides a list containing device interfaces associated
    with devices that are currently active, and which match the specified
    GUID and device instance ID, if any.

    - ulFlags.CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES
    ''''''''''''''''''''''''''''''''''''''''''''''''''

    The function provides a list containing device interfaces associated
    with all devices that match the specified GUID and device instance ID,
    if any.

    - ulFlags.CM_GET_DEVICE_INTERFACE_LIST_PRESENT
    ''''''''''''''''''''''''''''''''''''''''''''''

    The function provides a list containing device interfaces associated
    with devices that are currently active, and which match the specified
    GUID and device instance ID, if any.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the error codes with the CR\_ prefix as defined in
    Cfgmgr32.h.

    The following table includes some of the more common error codes that
    this function might return.

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

    CR_BUFFER_SMALL

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The Buffer buffer is too small to hold the requested list of device
    interfaces.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -remarks
    --------

    Between calling CM_Get_Device_Interface_List_Size to get the size of the
    list and calling CM_Get_Device_Interface_List to get the list, a new
    device interface can be added to the system causing the size returned to
    no longer be valid.  Callers should be robust to that condition and
    retry getting the size and the list if CM_Get_Device_Interface_List
    returns CR_BUFFER_SMALL.

    Examples
    ^^^^^^^^

    This snippet illustrates retrying getting the size and the list as
    described in the Remarks section.

    ::

           CONFIGRET cr = CR_SUCCESS;
           PWSTR DeviceInterfaceList = NULL;
           ULONG DeviceInterfaceListLength = 0;

           do {
               cr = CM_Get_Device_Interface_List_Size(&DeviceInterfaceListLength,
                                                      (LPGUID)&GUID_DEVINTERFACE_VOLUME,
                                                      NULL,
                                                      CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES);

               if (cr != CR_SUCCESS)
               {
                   break;
               }

               if (DeviceInterfaceList != NULL) {
                   HeapFree(GetProcessHeap(),
                            0,
                            DeviceInterfaceList);
               }

               DeviceInterfaceList = (PWSTR)HeapAlloc(GetProcessHeap(),
                                                      HEAP_ZERO_MEMORY,
                                                      DeviceInterfaceListLength * sizeof(WCHAR));

               if (DeviceInterfaceList == NULL)
               {
                   cr = CR_OUT_OF_MEMORY;
                   break;
               }

               cr = CM_Get_Device_Interface_List((LPGUID)&GUID_DEVINTERFACE_VOLUME,
                                                 NULL,
                                                 DeviceInterfaceList,
                                                 DeviceInterfaceListLength,
                                                 CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES);
           } while (cr == CR_BUFFER_SMALL);

           if (cr != CR_SUCCESS)
           {
               goto Exit;
           }

    ..

       The cfgmgr32.h header defines CM_Get_Device_Interface_List as
       an alias which automatically selects the ANSI or Unicode version of
       this function based on the definition of the UNICODE preprocessor
       constant. Mixing usage of the encoding-neutral alias with code that
       not encoding-neutral can lead to mismatches that result in
       compilation or runtime errors. For more information, see `Conventions
       for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.

    -see-also
    ---------

    CM_Get_Device_Interface_List_Size
    """

    def __new__(cls,
                InterfaceClassGuid: LPGUID = None,
                pDeviceID: DEVINSTID_W = None,
                Buffer: PZZWSTR = None,
                BufferLen: ULONG = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param InterfaceClassGuid: LPGUID [in]
        :param pDeviceID: DEVINSTID_W [in, optional]
        :param Buffer: PZZWSTR [out]
        :param BufferLen: ULONG [in]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_Device_Interface_ListW
        func.argtypes = [
            LPGUID,
            DEVINSTID_W,
            PZZWSTR,
            ULONG,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(InterfaceClassGuid, pDeviceID, Buffer, BufferLen, ulFlags)


class CM_Get_Device_Interface_Property(object):
    """
    https://docs.microsoft.com/en-gb/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_propertyw

    CM_Get_Device_Interface_PropertyW function
    ==========================================

    -description
    ------------

    The CM_Get_Device_Interface_Property function retrieves a device
    property that is set for a device interface.

    -parameters
    -----------

    -param pszDeviceInterface [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a string that identifies the device interface instance to
    retrieve the property from.

    -param PropertyKey [in]
    ~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a DEVPROPKEY structure that represents the device interface
    property key of the device interface property to retrieve.

    -param PropertyType [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a DEVPROPTYPE-typed variable that receives the
    property-data-type identifier of the requested device interface
    property. The property-data-type identifier is a bitwise OR between a
    base-data-type identifier and, if the base-data type is modified, a
    property-data-type modifier.

    -param PropertyBuffer [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a buffer that receives the requested device interface
    property. CM_Get_Device_Interface_Property retrieves the requested
    property only if the buffer is large enough to hold all the property
    value data. The pointer can be NULL.

    -param PropertyBufferSize [in, out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size, in bytes, of the PropertyBuffer buffer. If PropertyBuffer is
    set to NULL, \ *PropertyBufferSize must be set to zero. As output, if
    the buffer is not large enough to hold all the property value data,
    CM_Get_Device_Interface_Property returns the size of the data, in bytes,
    in *\ PropertyBufferSize.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Reserved. Must be set to zero.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    CM_Get_Device_Interface_Property is part of the Unified Device Property
    Model.

    -see-also
    ---------

    SetupDiGetDeviceInterfaceProperty
    """

    def __new__(cls,
                pszDeviceInterface: LPCWSTR = None,
                PropertyKey: DEVPROPKEY = None,
                PropertyType: DEVPROPTYPE = None,
                PropertyBuffer: PBYTE = None,
                PropertyBufferSize: PULONG = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param pszDeviceInterface: LPCWSTR [in]
        :param PropertyKey: DEVPROPKEY [in]
        :param PropertyType: DEVPROPTYPE [out]
        :param PropertyBuffer: PBYTE [out]
        :param PropertyBufferSize: PULONG [in, out]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_Device_Interface_PropertyW
        func.argtypes = [
            LPCWSTR,
            DEVPROPKEY,
            DEVPROPTYPE,
            PBYTE,
            PULONG,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(pszDeviceInterface, PropertyKey, PropertyType, PropertyBuffer, PropertyBufferSize, ulFlags)


class CM_Get_Device_Interface_Property_Keys(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_property_keysw

    CM_Get_Device_Interface_Property_KeysW function
    ===============================================

    -description
    ------------

    The CM_Get_Device_Interface_Property_Keys function retrieves an array of
    device property keys that represent the device properties that are set
    for a device interface.

    -parameters
    -----------

    -param pszDeviceInterface [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a string that identifies the device interface instance to
    retrieve the property keys from.

    -param PropertyKeyArray [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a buffer that receives an array of DEVPROPKEY-typed values,
    where each value is a device property key that represents a device
    property that is set for the device interface. The pointer is optional
    and can be NULL

    -param PropertyKeyCount [in, out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size, in DEVPROPKEY-typed units, of the PropertyKeyArray buffer. If
    PropertyKeyArray is set to NULL, \ *PropertyKeyCount must be set to
    zero. As output, if PropertyKeyArray is not large enough to hold all the
    property key data, CM_Get_Device_Interface_Property_Keys returns the
    count of the keys, in *\ PropertyKeyCount.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Reserved. Must be set to zero.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    CM_Get_Device_Interface_Property_Keys is part of the Unified Device
    Property Model.

    -see-also
    ---------

    SetupDiGetDeviceInterfacePropertyKeys
    """

    def __new__(cls,
                pszDeviceInterface: LPCWSTR = None,
                PropertyKeyArray: DEVPROPKEY = None,
                PropertyKeyCount: PULONG = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param pszDeviceInterface: LPCWSTR [in]
        :param PropertyKeyArray: DEVPROPKEY [out, optional]
        :param PropertyKeyCount: PULONG [in, out]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_Device_Interface_Property_KeysW
        func.argtypes = [
            LPCWSTR,
            DEVPROPKEY,
            PULONG,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(pszDeviceInterface, PropertyKeyArray, PropertyKeyCount, ulFlags)


class CM_Get_DevNode_Property(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw

    CM_Get_DevNode_PropertyW function
    =================================

    -description
    ------------

    The CM_Get_DevNode_Property function retrieves a device instance
    property.

    -parameters
    -----------

    -param dnDevInst [in]
    ~~~~~~~~~~~~~~~~~~~~~

    Device instance handle that is bound to the local machine.

    -param PropertyKey [in]
    ~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a DEVPROPKEY structure that represents the device property
    key of the requested device instance property.

    -param PropertyType [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a DEVPROPTYPE-typed variable that receives the
    property-data-type identifier of the requested device instance property,
    where the property-data-type identifier is the bitwise OR between a
    base-data-type identifier and, if the base-data type is modified, a
    property-data-type modifier.

    -param PropertyBuffer [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a buffer that receives the requested device instance
    property. CM_Get_DevNode_Property retrieves the requested property only
    if the buffer is large enough to hold all the property value data. The
    pointer can be NULL.

    -param PropertyBufferSize [in, out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size, in bytes, of the PropertyBuffer buffer. If PropertyBuffer is
    set to NULL, \ *PropertyBufferSize must be set to zero. As output, if
    the buffer is not large enough to hold all the property value data,
    CM_Get_DevNode_Property returns the size of the data, in bytes, in
    *\ PropertyBufferSize.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Reserved. Must be set to zero.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    CM_Get_DevNode_Property is part of the Unified Device Property Model.

    -see-also
    ---------

    SetupDiGetDeviceProperty
    """

    def __new__(cls,
                dnDevInst: DEVINST = None,
                PropertyKey: DEVPROPKEY = None,
                PropertyType: DEVPROPTYPE = None,
                PropertyBuffer: PBYTE = None,
                PropertyBufferSize: PULONG = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param dnDevInst: DEVINST [in]
        :param PropertyKey: DEVPROPKEY [in]
        :param PropertyType: DEVPROPTYPE [out]
        :param PropertyBuffer: PBYTE [out]
        :param PropertyBufferSize: PULONG [in, out]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_DevNode_PropertyW
        func.argtypes = [
            DEVINST,
            DEVPROPKEY,
            DEVPROPTYPE,
            PBYTE,
            PULONG,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(dnDevInst, PropertyKey, PropertyType, PropertyBuffer, PropertyBufferSize, ulFlags)


class CM_Get_DevNode_Property_Keys(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_property_keys

    CM_Get_DevNode_Property_Keys function
    =====================================

    -description
    ------------

    The CM_Get_DevNode_Property_Keys function retrieves an array of the
    device property keys that represent the device properties that are set
    for a device instance.

    -parameters
    -----------

    -param dnDevInst [in]
    ~~~~~~~~~~~~~~~~~~~~~

    Device instance handle that is bound to the local machine.

    -param PropertyKeyArray [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a buffer that receives an array of DEVPROPKEY-typed values,
    where each value is a device property key that represents a device
    property that is set for the device instance. The pointer is optional
    and can be NULL.

    -param PropertyKeyCount [in, out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size, in DEVPROPKEY-typed units, of the PropertyKeyArray buffer. If
    PropertyKeyArray is set to NULL, \ *PropertyKeyCount must be set to
    zero. As output, If PropertyKeyArray is not large enough to hold all the
    property key data, CM_Get_DevNode_Property_Keys returns the count of the
    keys in *\ PropertyKeyCount.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Reserved. Must be set to zero.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    CM_Get_DevNode_Property_Keys is part of the Unified Device Property
    Model.

    -see-also
    ---------

    SetupDiGetDevicePropertyKeys
    """

    def __new__(cls,
                dnDevInst: DEVINST = None,
                PropertyKeyArray: DEVPROPKEY = None,
                PropertyKeyCount: PULONG = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param dnDevInst: DEVINST [in]
        :param PropertyKeyArray: DEVPROPKEY [out, optional]
        :param PropertyKeyCount: PULONG [in, out]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_DevNode_Property_Keys
        func.argtypes = [
            DEVINST,
            DEVPROPKEY,
            PULONG,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(dnDevInst, PropertyKeyArray, PropertyKeyCount, ulFlags)


class CM_Get_DevNode_Status(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_status

    CM_Get_DevNode_Status function
    ==============================

    -description
    ------------

    The CM_Get_DevNode_Status function obtains the status of a device
    instance from its device node (devnode) in the local machine’s device
    tree.

    -parameters
    -----------

    -param pulStatus [out]
    ~~~~~~~~~~~~~~~~~~~~~~

    Address of a location to receive status bit flags. The function can set
    any combination of the DN_-prefixed bit flags defined in Cfg.h.

    -param pulProblemNumber [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Address of a location to receive one of the CM_PROB\_-prefixed problem
    values defined in Cfg.h. Used only if DN_HAS_PROBLEM is set in
    pulStatus.

    -param dnDevInst [in]
    ~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied device instance handle that is bound to the local
    machine.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Not used, must be zero.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    For information about using device instance handles that are bound to
    the local machine, see CM_Get_Child.

    -see-also
    ---------

    CM_Get_Child

    CM_Get_DevNode_Status_Ex
    """

    def __new__(cls,
                pulStatus: PULONG = None,
                pulProblemNumber: PULONG = None,
                dnDevInst: DEVINST = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param pulStatus: PULONG [out]
        :param pulProblemNumber: PULONG [out]
        :param dnDevInst: DEVINST [in]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_DevNode_Status
        func.argtypes = [
            PULONG,
            PULONG,
            DEVINST,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(pulStatus, pulProblemNumber, dnDevInst, ulFlags)


class CM_Locate_DevNode(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_locate_devnodew

    CM_Locate_DevNodeW function
    ===========================

    -description
    ------------

    The CM_Locate_DevNode function obtains a device instance handle to the
    device node that is associated with a specified device instance ID on
    the local machine.

    -parameters
    -----------

    -param pdnDevInst [out]
    ~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a device instance handle that CM_Locate_DevNode retrieves.
    The retrieved handle is bound to the local machine.

    -param pDeviceID [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a NULL-terminated string representing a device instance ID.
    If this value is NULL, or if it points to a zero-length string, the
    function retrieves a device instance handle to the device at the root of
    the device tree.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    A variable of ULONG type that supplies one of the following flag values
    that apply if the caller supplies a device instance identifier:

    CM_LOCATE_DEVNODE_NORMAL
    ^^^^^^^^^^^^^^^^^^^^^^^^

    The function retrieves the device instance handle for the specified
    device only if the device is currently configured in the device tree.

    CM_LOCATE_DEVNODE_PHANTOM
    ^^^^^^^^^^^^^^^^^^^^^^^^^

    The function retrieves a device instance handle for the specified device
    if the device is currently configured in the device tree or the device
    is a nonpresent device that is not currently configured in the device
    tree.

    CM_LOCATE_DEVNODE_CANCELREMOVE
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    The function retrieves a device instance handle for the specified device
    if the device is currently configured in the device tree or in the
    process of being removed from the device tree. If the device is in the
    process of being removed, the function cancels the removal of the
    device.

    CM_LOCATE_DEVNODE_NOVALIDATION
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Not used.

    - ulFlags.CM_LOCATE_DEVNODE_CANCELREMOVE
    ''''''''''''''''''''''''''''''''''''''''

    The function retrieves a device instance handle for the specified device
    if the device is currently configured in the device tree or in the
    process of being removed from the device tree. If the device is in the
    process of being removed, the function cancels the removal of the
    device.

    - ulFlags.CM_LOCATE_DEVNODE_NORMAL
    ''''''''''''''''''''''''''''''''''

    The function retrieves the device instance handle for the specified
    device only if the device is currently configured in the device tree.

    - ulFlags.CM_LOCATE_DEVNODE_NOVALIDATION
    ''''''''''''''''''''''''''''''''''''''''

    Not used.

    - ulFlags.CM_LOCATE_DEVNODE_PHANTOM
    '''''''''''''''''''''''''''''''''''

    The function retrieves a device instance handle for the specified device
    if the device is currently configured in the device tree or the device
    is a nonpresent device that is not currently configured in the device
    tree.

    -returns
    --------

    If the operation succeeds, CM_Locate_DevNode returns CR_SUCCESS.
    Otherwise, the function returns one of the CR\_Xxx error codes that are
    defined in Cfgmgr32.h.

    -remarks
    --------

    For information about using device instance handles that are bound to
    the local machine, see CM_Get_Child.

       The cfgmgr32.h header defines CM_Locate_DevNode as an alias
       which automatically selects the ANSI or Unicode version of this
       function based on the definition of the UNICODE preprocessor
       constant. Mixing usage of the encoding-neutral alias with code that
       not encoding-neutral can lead to mismatches that result in
       compilation or runtime errors. For more information, see `Conventions
       for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.

    -see-also
    ---------

    CM_Get_Child

    CM_Locate_DevNode_Ex
    """

    def __new__(cls,
                pdnDevInst: PDEVINST = None,
                pDeviceID: DEVINSTID_W = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param pdnDevInst: PDEVINST [out]
        :param pDeviceID: DEVINSTID_W [in, optional]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Locate_DevNodeW
        func.argtypes = [
            PDEVINST,
            DEVINSTID_W,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(pdnDevInst, pDeviceID, ulFlags)


class CM_Get_Class_Property(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_class_propertyw

    CM_Get_Class_PropertyW function
    ===============================

    -description
    ------------

    The CM_Get_Class_Property function retrieves a device property that is
    set for a device interface class or device setup class.

    -parameters
    -----------

    -param ClassGUID [in]
    ~~~~~~~~~~~~~~~~~~~~~

    Pointer to the GUID that identifies the device interface class or device
    setup class for which to retrieve a device property that is set for the
    device class. For information about specifying the class type, see the
    ulFlags parameter.

    -param PropertyKey [in]
    ~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a DEVPROPKEY structure that represents the device property
    key of the requested device class property.

    -param PropertyType [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a DEVPROPTYPE-typed variable that receives the
    property-data-type identifier of the requested device class property,
    where the property-data-type identifier is the bitwise OR between a
    base-data-type identifier and, if the base data type is modified, a
    property-data-type modifier.

    -param PropertyBuffer [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a buffer that receives the requested device class property.
    CM_Get_Class_Property retrieves the requested property value only if the
    buffer is large enough to hold all the property value data. The pointer
    can be NULL.

    -param PropertyBufferSize [in, out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size, in bytes, of the PropertyBuffer buffer. If the PropertyBuffer
    parameter is set to NULL, \ *PropertyBufferSize must be set to zero. As
    output, if the buffer is not large enough to hold all the property value
    data, CM_Get_Class_Property returns the size of the data, in bytes, in
    *\ PropertyBufferSize.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Class property flags:

    CM_CLASS_PROPERTY_INSTALLER
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^

    ClassGUID specifies a device setup class. Do not combine with
    CM_CLASS_PROPERTY_INTERFACE.

    CM_CLASS_PROPERTY_INTERFACE
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^

    ClassGUID specifies a device interface class. Do not combine with
    CM_CLASS_PROPERTY_INSTALLER.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    CM_Get_Class_Property is part of the Unified Device Property Model.

    -see-also
    ---------

    SetupDiGetClassProperty
    """

    def __new__(cls,
                ClassGUID: LPCGUID = None,
                PropertyKey: DEVPROPKEY = None,
                PropertyType: DEVPROPTYPE = None,
                PropertyBuffer: PBYTE = None,
                PropertyBufferSize: PULONG = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param ClassGUID: LPCGUID [in]
        :param PropertyKey: DEVPROPKEY [in]
        :param PropertyType: DEVPROPTYPE [out]
        :param PropertyBuffer: PBYTE [out]
        :param PropertyBufferSize: PULONG [in, out]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_Class_PropertyW
        func.argtypes = [
            LPCGUID,
            DEVPROPKEY,
            DEVPROPTYPE,
            PBYTE,
            PULONG,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(ClassGUID, PropertyKey, PropertyType, PropertyBuffer, PropertyBufferSize, ulFlags)


class CM_Get_Class_Property_Keys(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_class_property_keys

    CM_Get_Class_Property_Keys function
    ===================================

    -description
    ------------

    The CM_Get_Class_Property_Keys function retrieves an array of the device
    property keys that represent the device properties that are set for a
    device interface class or device setup class.

    -parameters
    -----------

    -param ClassGUID [in]
    ~~~~~~~~~~~~~~~~~~~~~

    Pointer to the GUID that identifies the device interface class or device
    setup class for which to retrieve the property keys for. For information
    about specifying the class type, see the ulFlags parameter.

    -param PropertyKeyArray [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a buffer that receives an array of DEVPROPKEY-typed values,
    where each value is a device property key that represents a device
    property that is set for the device class. The pointer is optional and
    can be NULL.

    -param PropertyKeyCount [in, out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The size, in DEVPROPKEY-typed units, of the PropertyKeyArray buffer. If
    PropertyKeyArray is set to NULL, \ *PropertyKeyCount must be set to
    zero. As output, if PropertyKeyArray is not large enough to hold all the
    property key data, CM_Get_Class_Property_Keys returns the count of the
    keys, in *\ PropertyKeyCount.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Class property key flags:

    CM_CLASS_PROPERTY_INSTALLER
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^

    ClassGUID specifies a device setup class. Do not combine with
    CM_CLASS_PROPERTY_INTERFACE.

    CM_CLASS_PROPERTY_INTERFACE
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^

    ClassGUID specifies a device interface class. Do not combine with
    CM_CLASS_PROPERTY_INSTALLER.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    CM_Get_Class_Property_Keys is part of the Unified Device Property Model.

    -see-also
    ---------

    SetupDiGetClassPropertyKeys
    """

    def __new__(cls,
                ClassGUID: LPCGUID = None,
                PropertyKeyArray: DEVPROPKEY = None,
                PropertyKeyCount: PULONG = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param ClassGUID: LPCGUID [in]
        :param PropertyKeyArray: DEVPROPKEY [out, optional]
        :param PropertyKeyCount: PULONG [in, out]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_Class_Property_Keys
        func.argtypes = [
            LPCGUID,
            DEVPROPKEY,
            PULONG,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(ClassGUID, PropertyKeyArray, PropertyKeyCount, ulFlags)


class CM_Get_Device_Interface_List_Size(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_list_sizew

    CM_Get_Device_Interface_List_SizeW function
    ===========================================

    -description
    ------------

    The CM_Get_Device_Interface_List_Size function retrieves the buffer size
    that must be passed to the CM_Get_Device_Interface_List function.

    -parameters
    -----------

    -param pulLen [out]
    ~~~~~~~~~~~~~~~~~~~

    Caller-supplied pointer to a location that receives the required length,
    in characters, of a buffer to hold the multiple Unicode strings that
    will be returned by CM_Get_Device_Interface_List.

    -param InterfaceClassGuid [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Supplies a GUID that identifies a device interface class.

    -param pDeviceID [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied pointer to a NULL-terminated string that represents a
    device instance ID. If specified, the function retrieves the length of
    symbolic link names for the device interfaces that are supported by the
    device, for the specified class. If this value is NULL, or if it points
    to a zero-length string, the function retrieves the length of symbolic
    link names for all interfaces that belong to the specified class.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Contains one of the following caller-supplied flags:

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

    CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The function provides the size of a list that contains device interfaces
    associated with all devices that match the specified GUID and device
    instance ID, if any.

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

    CM_GET_DEVICE_INTERFACE_LIST_PRESENT

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The function provides the size of a list containing device interfaces
    associated with devices that are currently active, and which match the
    specified GUID and device instance ID, if any.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the error codes with the CR\_ prefix as defined in
    Cfgmgr32.h.

    -see-also
    ---------

    CM_Get_Device_Interface_List

    -remarks
    --------

       The cfgmgr32.h header defines
       CM_Get_Device_Interface_List_Size as an alias which automatically
       selects the ANSI or Unicode version of this function based on the
       definition of the UNICODE preprocessor constant. Mixing usage of the
       encoding-neutral alias with code that not encoding-neutral can lead
       to mismatches that result in compilation or runtime errors. For more
       information, see `Conventions for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.
    """

    def __new__(cls,
                pulLen: PULONG = None,
                InterfaceClassGuid: LPGUID = None,
                pDeviceID: DEVINSTID_W = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param pulLen: PULONG [out]
        :param InterfaceClassGuid: LPGUID [in]
        :param pDeviceID: DEVINSTID_W [in, optional]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_Device_Interface_List_SizeW
        func.argtypes = [
            PULONG,
            LPGUID,
            DEVINSTID_W,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(pulLen, InterfaceClassGuid, pDeviceID, ulFlags)


class CM_Get_Depth(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_depth

    CM_Get_Depth function
    =====================

    -description
    ------------

    The CM_Get_Depth function is used to obtain the depth of a specified
    device node (devnode) within the local machine’s device tree.

    -parameters
    -----------

    -param pulDepth [out]
    ~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied address of a location to receive a depth value, where
    zero represents the device tree’s root node, one represents the root
    node’s children, and so on.

    -param dnDevInst [in]
    ~~~~~~~~~~~~~~~~~~~~~

    Caller-supplied device instance handle that is bound to the local
    machine.

    -param ulFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Not used, must be zero.

    -returns
    --------

    If the operation succeeds, the function returns CR_SUCCESS. Otherwise,
    it returns one of the CR_-prefixed error codes defined in Cfgmgr32.h.

    -remarks
    --------

    For information about using device instance handles that are bound to
    the local machine, see CM_Get_Child.

    -see-also
    ---------

    CM_Get_Child

    CM_Get_Depth_Ex
    """

    def __new__(cls,
                pulDepth: PULONG = None,
                dnDevInst: DEVINST = None,
                ulFlags: ULONG = None
                ) -> CONFIGRET:
        """

        :param pulDepth: PULONG [out]
        :param dnDevInst: DEVINST [in]
        :param ulFlags: ULONG [in]
        :return: CONFIGRET
        """

        func = cfgmgr32.CM_Get_Depth
        func.argtypes = [
            PULONG,
            DEVINST,
            ULONG
        ]
        func.restype = CONFIGRET
        return func(pulDepth, dnDevInst, ulFlags)
