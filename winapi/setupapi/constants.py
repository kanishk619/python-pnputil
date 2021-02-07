from enum import IntEnum

ERROR_NO_MORE_ITEMS = 259


class DIGCF(IntEnum):
    DEFAULT = 0x00000001  # only valid with DIGCF.DEVICEINTERFACE
    PRESENT = 0x00000002
    ALLCLASSES = 0x00000004
    PROFILE = 0x00000008
    DEVICEINTERFACE = 0x00000010


class DEVPROP(IntEnum):
    """
    https://github.com/tpn/winsdk-10/blob/master/Include/10.0.10240.0/shared/devpropdef.h
    """
    TYPEMOD_ARRAY = 0x00001000  # array of fixed-sized data elements
    TYPEMOD_LIST = 0x00002000  # list of variable-sized data elements
    TYPE_EMPTY = 0x00000000  # nothing, no property data
    TYPE_NULL = 0x00000001  # null property data
    TYPE_SBYTE = 0x00000002  # 8-bit signed int (SBYTE)
    TYPE_BYTE = 0x00000003  # 8-bit unsigned int (BYTE)
    TYPE_INT16 = 0x00000004  # 16-bit signed int (SHORT)
    TYPE_UINT16 = 0x00000005  # 16-bit unsigned int (USHORT)
    TYPE_INT32 = 0x00000006  # 32-bit signed int (LONG)
    TYPE_UINT32 = 0x00000007  # 32-bit unsigned int (ULONG)
    TYPE_INT64 = 0x00000008  # 64-bit signed int (LONG64)
    TYPE_UINT64 = 0x00000009  # 64-bit unsigned int (ULONG64)
    TYPE_FLOAT = 0x0000000A  # 32-bit floating-point (FLOAT)
    TYPE_DOUBLE = 0x0000000B  # 64-bit floating-point (DOUBLE)
    TYPE_DECIMAL = 0x0000000C  # 128-bit data (DECIMAL)
    TYPE_GUID = 0x0000000D  # 128-bit unique identifier (GUID)
    TYPE_CURRENCY = 0x0000000E  # 64 bit signed int currency value (CURRENCY)
    TYPE_DATE = 0x0000000F  # date (DATE)
    TYPE_FILETIME = 0x00000010  # file time (FILETIME)
    TYPE_BOOL = 0x00000011  # 8-bit boolean (BOOLEAN)
    TYPE_STRING = 0x00000012  # null-terminated string
    TYPE_STRING_LIST = (TYPE_STRING | TYPEMOD_LIST)  # multi-sz string list
    TYPE_SECURITY_DESCRIPTOR = 0x00000013  # self-relative binary SECURITY_DESCRIPTOR
    TYPE_SECURITY_DESCRIPTOR_STRING = 0x00000014  # security descriptor string (SDDL format)
    TYPE_DEVPROPKEY = 0x00000015  # device property key (DEVPROPKEY)
    TYPE_DEVPROPTYPE = 0x00000016  # device property type (DEVPROPTYPE)
    TYPE_BINARY = (TYPE_BYTE | TYPEMOD_ARRAY)  # custom binary data
    TYPE_ERROR = 0x00000017  # 32-bit Win32 system error code
    TYPE_NTSTATUS = 0x00000018  # 32-bit NTSTATUS code
    TYPE_STRING_INDIRECT = 0x00000019  # string resource (@[path\]<dllname>,-<strId>)
    TYPE_BOOLEAN = TYPE_BOOL


class DN(IntEnum):
    """
    https://github.com/tpn/winsdk-10/blob/master/Include/10.0.16299.0/shared/cfg.h
    """
    ROOT_ENUMERATED = 0x00000001  # Was enumerated by ROOT
    DRIVER_LOADED = 0x00000002  # Has Register_Device_Driver
    ENUM_LOADED = 0x00000004  # Has Register_Enumerator
    STARTED = 0x00000008  # Is currently configured
    MANUAL = 0x00000010  # Manually installed
    NEED_TO_ENUM = 0x00000020  # May need reenumeration
    NOT_FIRST_TIME = 0x00000040  # Has received a config
    HARDWARE_ENUM = 0x00000080  # Enum generates hardware ID
    LIAR = 0x00000100  # Lied about can reconfig once
    HAS_MARK = 0x00000200  # Not CM_Create_DevInst lately
    HAS_PROBLEM = 0x00000400  # Need device installer
    FILTERED = 0x00000800  # Is filtered
    MOVED = 0x00001000  # Has been moved
    DISABLEABLE = 0x00002000  # Can be disabled
    REMOVABLE = 0x00004000  # Can be removed
    PRIVATE_PROBLEM = 0x00008000  # Has a private problem
    MF_PARENT = 0x00010000  # Multi function parent
    MF_CHILD = 0x00020000  # Multi function child
    WILL_BE_REMOVED = 0x00040000  # DevInst is being removed

    #
    # Windows 4 OPK2 Flags
    #
    NOT_FIRST_TIMEE = 0x00080000  # S: Has received a config enumerate
    STOP_FREE_RES = 0x00100000  # S: When child is stopped, free resources
    REBAL_CANDIDATE = 0x00200000  # S: Don't skip during rebalance
    BAD_PARTIAL = 0x00400000  # S: This devnode's log_confs do not have same resources
    NT_ENUMERATOR = 0x00800000  # S: This devnode's is an NT enumerator
    NT_DRIVER = 0x01000000  # S: This devnode's is an NT driver
    #
    # Windows 4.1 Flags
    #
    NEEDS_LOCKING = 0x02000000  # S: Devnode need lock resume processing
    ARM_WAKEUP = 0x04000000  # S: Devnode can be the wakeup device
    APM_ENUMERATOR = 0x08000000  # S: APM aware enumerator
    APM_DRIVER = 0x10000000  # S: APM aware driver
    SILENT_INSTALL = 0x20000000  # S: Silent install
    NO_SHOW_IN_DM = 0x40000000  # S: No show in device manager
    BOOT_LOG_PROB = 0x80000000  # S: Had a problem during preassignment of boot log conf

    #
    # Windows NT Flags
    #
    # These are overloaded on top of unused Win 9X flags
    #

    # if NTDDI_VERSION >= NTDDI_WIN2K

    NEED_RESTART = LIAR  # System needs to be restarted for this Devnode to work properly

    # endif

    # if NTDDI_VERSION >= NTDDI_WINXP

    DRIVER_BLOCKED = NOT_FIRST_TIME  # One or more drivers are blocked from loading for this Devnode
    LEGACY_DRIVER = MOVED  # This device is using a legacy driver
    CHILD_WITH_INVALID_ID = HAS_MARK  # One or more children have invalid IDs

    # endif

    # if NTDDI_VERSION >= NTDDI_WIN8

    DEVICE_DISCONNECTED = NEEDS_LOCKING  # The function driver for a device reported that the device is not connected.  Typically this means a wireless device is out of range.

    # endif

    # if NTDDI_VERSION >= NTDDI_WIN10

    QUERY_REMOVE_PENDING = MF_PARENT  # Device is part of a set of related devices collectively pending query-removal
    QUERY_REMOVE_ACTIVE = MF_CHILD  # Device is actively engaged in a query-remove IRP


SPDIT_NODRIVER = 0x00000000
SPDIT_CLASSDRIVER = 0x00000001
SPDIT_COMPATDRIVER = 0x00000002
