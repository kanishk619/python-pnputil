from enum import IntEnum


class CR(IntEnum):
    SUCCESS = 0x00000000
    DEFAULT = 0x00000001
    OUT_OF_MEMORY = 0x00000002
    INVALID_POINTER = 0x00000003
    INVALID_FLAG = 0x00000004
    INVALID_DEVNODE = 0x00000005
    INVALID_DEVINST = INVALID_DEVNODE
    INVALID_RES_DES = 0x00000006
    INVALID_LOG_CONF = 0x00000007
    INVALID_ARBITRATOR = 0x00000008
    INVALID_NODELIST = 0x00000009
    DEVNODE_HAS_REQS = 0x0000000A
    DEVINST_HAS_REQS = DEVNODE_HAS_REQS
    INVALID_RESOURCEID = 0x0000000B
    DLVXD_NOT_FOUND = 0x0000000C  # WIN 95 ONLY
    NO_SUCH_DEVNODE = 0x0000000D
    NO_SUCH_DEVINST = NO_SUCH_DEVNODE
    NO_MORE_LOG_CONF = 0x0000000E
    NO_MORE_RES_DES = 0x0000000F
    ALREADY_SUCH_DEVNODE = 0x00000010
    ALREADY_SUCH_DEVINST = ALREADY_SUCH_DEVNODE
    INVALID_RANGE_LIST = 0x00000011
    INVALID_RANGE = 0x00000012
    FAILURE = 0x00000013
    NO_SUCH_LOGICAL_DEV = 0x00000014
    CREATE_BLOCKED = 0x00000015
    NOT_SYSTEM_VM = 0x00000016  # WIN 95 ONLY
    REMOVE_VETOED = 0x00000017
    APM_VETOED = 0x00000018
    INVALID_LOAD_TYPE = 0x00000019
    BUFFER_SMALL = 0x0000001A
    NO_ARBITRATOR = 0x0000001B
    NO_REGISTRY_HANDLE = 0x0000001C
    REGISTRY_ERROR = 0x0000001D
    INVALID_DEVICE_ID = 0x0000001E
    INVALID_DATA = 0x0000001F
    INVALID_API = 0x00000020
    DEVLOADER_NOT_READY = 0x00000021
    NEED_RESTART = 0x00000022
    NO_MORE_HW_PROFILES = 0x00000023
    DEVICE_NOT_THERE = 0x00000024
    NO_SUCH_VALUE = 0x00000025
    WRONG_TYPE = 0x00000026
    INVALID_PRIORITY = 0x00000027
    NOT_DISABLEABLE = 0x00000028
    FREE_RESOURCES = 0x00000029
    QUERY_VETOED = 0x0000002A
    CANT_SHARE_IRQ = 0x0000002B
    NO_DEPENDENT = 0x0000002C
    SAME_RESOURCES = 0x0000002D
    NO_SUCH_REGISTRY_KEY = 0x0000002E
    INVALID_MACHINENAME = 0x0000002F  # NT ONLY
    REMOTE_COMM_FAILURE = 0x00000030  # NT ONLY
    MACHINE_UNAVAILABLE = 0x00000031  # NT ONLY
    NO_CM_SERVICES = 0x00000032  # NT ONLY
    ACCESS_DENIED = 0x00000033  # NT ONLY
    CALL_NOT_IMPLEMENTED = 0x00000034
    INVALID_PROPERTY = 0x00000035
    DEVICE_INTERFACE_ACTIVE = 0x00000036
    NO_SUCH_DEVICE_INTERFACE = 0x00000037
    INVALID_REFERENCE_STRING = 0x00000038
    INVALID_CONFLICT_LIST = 0x00000039
    INVALID_INDEX = 0x0000003A
    INVALID_STRUCTURE_SIZE = 0x0000003B
    NUM_CR_RESULTS = 0x0000003C


# --------------------------------------------------------------
#  General size definitions
# --------------------------------------------------------------
MAX_DEVICE_ID_LEN = 200
MAX_DEVNODE_ID_LEN = MAX_DEVICE_ID_LEN
MAX_GUID_STRING_LEN = 39  # 38 chars + terminator null
MAX_CLASS_NAME_LEN = 32
MAX_PROFILE_LEN = 80
MAX_CONFIG_VALUE = 9999
MAX_INSTANCE_VALUE = 9999
MAX_MEM_REGISTERS = 9  # Win95 compatibility--not applicable to 32-bit ConfigMgr
MAX_IO_PORTS = 20  # Win95 compatibility--not applicable to 32-bit ConfigMgr
MAX_IRQS = 7  # Win95 compatibility--not applicable to 32-bit ConfigMgr
MAX_DMA_CHANNELS = 7  # Win95 compatibility--not applicable to 32-bit ConfigMgr
CONFIGMG_VERSION = 0x0400
# --------------------------------------------------------------
#  Data types
# --------------------------------------------------------------
#
#  Standardized Return Value data type
#
#
#  Device Instance Handle data type
#
#
#  Device Instance Identifier data type
#  The device instance ID specifies the registry path, relative to the
#  Enum key , for a device instance.  For example:  \Root\*PNP0500\0000.
#
#
#  Logical Configuration Handle data type
#
#
#  Resource Descriptor Handle data type
#
#
#  Resource ID data type (may take any of the ResType_* values)
#
#
#  Priority data type (may take any of the LCPRI_* values)
#
#
#  Range List Handle data type
#
#
#  Range Element Handle data type
#
#
#  Machine Handle data type
#
#
#  Conflict List data types
#
CM_CDMASK_DEVINST = 0x00000001  # mask to retrieve CD_dnDevInst attribute for conflict
CM_CDMASK_RESDES = 0x00000002  # mask to retrieve CD_rdResDes attribute for conflict
CM_CDMASK_FLAGS = 0x00000004  # mask to retrieve CD_ulFlags attribute for conflict
CM_CDMASK_DESCRIPTION = 0x00000008  # mask to retrieve CD_szDescription attribute for conflict
CM_CDMASK_VALID = 0x0000000F  # valid bits
CM_CDFLAGS_DRIVER = 0x00000001  # CD_ulFlags: CD_szDescription reports back legacy driver name
CM_CDFLAGS_ROOT_OWNED = 0x00000002  # CD_ulFlags: Root owned device
CM_CDFLAGS_RESERVED = 0x00000004  # CD_ulFlags: Specified range is not available for use
#
#  use 1 byte packing for the data structures
#
# --------------------------------------------------------------
#  Memory resource
# --------------------------------------------------------------
#
#  Define the attribute flags for memory ranges.  Each bit flag is
#  identified by a constant bitmask.  Following the bitmask definition,
#  are the two possible values.
#
mMD_MemoryType = 0x1  # Bitmask, whether memory is writable
MD_MemoryType = mMD_MemoryType  # compatibility
MD_ROM = 0x0  # Memory range is read-only
MD_RAM = 0x1  # Memory range may be written to
mMD_32_24 = 0x2  # Bitmask, memory is 24 or 32-bit
MD_32_24 = mMD_32_24  # compatibility
MD_24 = 0x0  # Memory range is 24-bit
MD_32 = 0x2  # Memory range is 32-bit
mMD_Prefetchable = 0x4  # Bitmask,whether memory prefetchable
MD_Prefetchable = mMD_Prefetchable  # compatibility
MD_Pref = mMD_Prefetchable  # compatibility
MD_PrefetchDisallowed = 0x0  # Memory range is not prefetchable
MD_PrefetchAllowed = 0x4  # Memory range is prefetchable
mMD_Readable = 0x8  # Bitmask,whether memory is readable
MD_Readable = mMD_Readable  # compatibility
MD_ReadAllowed = 0x0  # Memory range is readable
MD_ReadDisallowed = 0x8  # Memory range is write-only
mMD_CombinedWrite = 0x10  # Bitmask,supports write-behind
MD_CombinedWrite = mMD_CombinedWrite  # compatibility
MD_CombinedWriteDisallowed = 0x0  # no combined-write caching
MD_CombinedWriteAllowed = 0x10  # supports combined-write caching
mMD_Cacheable = 0x20  # Bitmask,whether memory is cacheable
MD_NonCacheable = 0x0  # Memory range is non-cacheable
MD_Cacheable = 0x20  # Memory range is cacheable
MD_WINDOW_DECODE = 0x40  # Memory range is bridge window decode.
MD_MEMORY_BAR = 0x80  # Memory BAR resource.
#
#  MEM_RANGE Structure
#
#
#  MEM_DES structure
#
#
#  MEM_RESOURCE structure
#
#
#  Define the size of each range structure
#
# --------------------------------------------------------------
#  Large Memory Resource
# --------------------------------------------------------------
#
#  Note that large memory ranges use the same attribute flags as memory ranges.
#
#
#  MEM_LARGE_RANGE Structure
#
#
#  MEM_LARGE_DES structure
#
#
#  MEM_LARGE_RESOURCE structure
#
#
#  Define the size of each range structure
#
# --------------------------------------------------------------
#  I/O Port Resource
# --------------------------------------------------------------
#
#  Define the attribute flags for port resources.  Each bit flag is
#  identified by a constant bitmask.  Following the bitmask definition,
#  are the two possible values.
#
IOD_PortType = 0x1  # Bitmask,whether port is IO or memory
IOD_Memory = 0x0  # Port resource really uses memory
IOD_IO = 0x1  # Port resource uses IO ports
IOD_DECODE = 0x00fc  # decode flags
IOD_10_BIT_DECODE = 0x0004
IOD_12_BIT_DECODE = 0x0008
IOD_16_BIT_DECODE = 0x0010
IOD_POSITIVE_DECODE = 0x0020
IOD_PASSIVE_DECODE = 0x0040
IOD_WINDOW_DECODE = 0x0080
IOD_PORT_BAR = 0x0100
#
#  these are for compatiblity
#
IO_ALIAS_10_BIT_DECODE = 0x00000004
IO_ALIAS_12_BIT_DECODE = 0x00000010
IO_ALIAS_16_BIT_DECODE = 0x00000000
IO_ALIAS_POSITIVE_DECODE = 0x000000FF
#
#  IO_RANGE structure
#
#
#  IO_DES structure
#
#
#  IO_RESOURCE
#
IOA_Local = 0xff
#
#  Define the size of each range structure
#
# --------------------------------------------------------------
#  DMA Resource
# --------------------------------------------------------------
#
#  Define the attribute flags for a DMA resource range.  Each bit flag is
#  identified with a constant bitmask.  Following the bitmask definition
#  are the possible values.
#
mDD_Width = 0x3  # Bitmask, width of the DMA channel:
DD_BYTE = 0x0  # 8-bit DMA channel
DD_WORD = 0x1  # 16-bit DMA channel
DD_DWORD = 0x2  # 32-bit DMA channel
DD_BYTE_AND_WORD = 0x3  # 8-bit and 16-bit DMA channel
mDD_BusMaster = 0x4  # Bitmask, whether bus mastering is supported
DD_NoBusMaster = 0x0  # no bus mastering
DD_BusMaster = 0x4  # bus mastering
mDD_Type = 0x18  # Bitmask, specifies type of DMA
DD_TypeStandard = 0x00  # standard DMA
DD_TypeA = 0x08  # Type-A DMA
DD_TypeB = 0x10  # Type-B DMA
DD_TypeF = 0x18  # Type-F DMA
#
#  DMA_RANGE structure
#
#
#  DMA_DES structure
#
#
#  DMA_RESOURCE
#
#
#  Define the size of each range structure
#
# --------------------------------------------------------------
#  Interrupt Resource
# --------------------------------------------------------------
#
#  Define the attribute flags for an interrupt resource range.  Each bit flag
#  is identified with a constant bitmask.  Following the bitmask definition
#  are the possible values.
#
mIRQD_Share = 0x1  # Bitmask,whether the IRQ may be shared:
IRQD_Exclusive = 0x0  # The IRQ may not be shared
IRQD_Share = 0x1  # The IRQ may be shared
IRQD_Share_Bit = 0  # compatibility
IRQD_Level_Bit = 1  # compatibility
#
#  ** NOTE: 16-bit ConfigMgr uses fIRQD_Level_Bit being set to indicate that the
#  ** interrupt is _level-sensitive_.  For 32-bit ConfigMgr, if this bit is set,
#  ** then the interrupt is _edge-sensitive_.
#
mIRQD_Edge_Level = 0x2  # Bitmask,whether edge or level triggered:
IRQD_Level = 0x0  # The IRQ is level-sensitive
IRQD_Edge = 0x2  # The IRQ is edge-sensitive
#
#  IRQ_RANGE
#
#
#  IRQ_DES structure
#
#
#  IRQ_RESOURCE structure
#
#
#  Define the size of each range structure
#
#
#  Flags for resource descriptor APIs indicating the width of certain
#  variable-size resource descriptor structure fields, where applicable.
#
CM_RESDES_WIDTH_DEFAULT = 0x00000000  # 32 or 64-bit IRQ_RESOURCE / IRQ_DES, based on client
CM_RESDES_WIDTH_32 = 0x00000001  # 32-bit IRQ_RESOURCE / IRQ_DES
CM_RESDES_WIDTH_64 = 0x00000002  # 64-bit IRQ_RESOURCE / IRQ_DES
CM_RESDES_WIDTH_BITS = 0x00000003
# --------------------------------------------------------------
#  Device Private Resource
# --------------------------------------------------------------
#
#  DEVICEPRIVATE_RANGE structure
#
#
#  DEVPRIVATE_DES structure
#
#
#  DEVPRIVATE_RESOURCE
#
#
#  Define the size of each range structure
#
# --------------------------------------------------------------
#  Class-Specific Resource
# --------------------------------------------------------------
# --------------------------------------------------------------
#  PC Card Configuration Resource
# --------------------------------------------------------------
#
#  Define the attribute flags for a PC Card configuration resource descriptor.
#  Each bit flag is identified with a constant bitmask.  Following the bitmask
#  definition are the possible values.
#
mPCD_IO_8_16 = 0x1  # Bitmask, whether I/O is 8 or 16 bits
PCD_IO_8 = 0x0  # I/O is 8-bit
PCD_IO_16 = 0x1  # I/O is 16-bit
mPCD_MEM_8_16 = 0x2  # Bitmask, whether MEM is 8 or 16 bits
PCD_MEM_8 = 0x0  # MEM is 8-bit
PCD_MEM_16 = 0x2  # MEM is 16-bit
mPCD_MEM_A_C = 0xC  # Bitmask, whether MEMx is Attribute or Common
PCD_MEM1_A = 0x4  # MEM1 is Attribute
PCD_MEM2_A = 0x8  # MEM2 is Attribute
PCD_IO_ZW_8 = 0x10  # zero wait on 8 bit I/O
PCD_IO_SRC_16 = 0x20  # iosrc 16
PCD_IO_WS_16 = 0x40  # wait states on 16 bit io
mPCD_MEM_WS = 0x300  # Bitmask, for additional wait states on memory windows
PCD_MEM_WS_ONE = 0x100  # 1 wait state
PCD_MEM_WS_TWO = 0x200  # 2 wait states
PCD_MEM_WS_THREE = 0x300  # 3 wait states
PCD_MEM_A = 0x4  # MEM is Attribute
PCD_ATTRIBUTES_PER_WINDOW = 0x8000
PCD_IO1_16 = 0x00010000  # I/O window 1 is 16-bit
PCD_IO1_ZW_8 = 0x00020000  # I/O window 1 zero wait on 8 bit I/O
PCD_IO1_SRC_16 = 0x00040000  # I/O window 1 iosrc 16
PCD_IO1_WS_16 = 0x00080000  # I/O window 1 wait states on 16 bit io
PCD_IO2_16 = 0x00100000  # I/O window 2 is 16-bit
PCD_IO2_ZW_8 = 0x00200000  # I/O window 2 zero wait on 8 bit I/O
PCD_IO2_SRC_16 = 0x00400000  # I/O window 2 iosrc 16
PCD_IO2_WS_16 = 0x00800000  # I/O window 2 wait states on 16 bit io
mPCD_MEM1_WS = 0x03000000  # MEM window 1 Bitmask, for additional wait states on memory windows
PCD_MEM1_WS_ONE = 0x01000000  # MEM window 1, 1 wait state
PCD_MEM1_WS_TWO = 0x02000000  # MEM window 1, 2 wait states
PCD_MEM1_WS_THREE = 0x03000000  # MEM window 1, 3 wait states
PCD_MEM1_16 = 0x04000000  # MEM window 1 is 16-bit
mPCD_MEM2_WS = 0x30000000  # MEM window 2 Bitmask, for additional wait states on memory windows
PCD_MEM2_WS_ONE = 0x10000000  # MEM window 2, 1 wait state
PCD_MEM2_WS_TWO = 0x20000000  # MEM window 2, 2 wait states
PCD_MEM2_WS_THREE = 0x30000000  # MEM window 2, 3 wait states
PCD_MEM2_16 = 0x40000000  # MEM window 2 is 16-bit
PCD_MAX_MEMORY = 2
PCD_MAX_IO = 2
# --------------------------------------------------------------
#  MF (multifunction) PCCard Configuration Resource
# --------------------------------------------------------------
mPMF_AUDIO_ENABLE = 0x8  # Bitmask, whether audio is enabled or not
PMF_AUDIO_ENABLE = 0x8  # Audio is enabled
# --------------------------------------------------------------
#  Bus Number Resource
# --------------------------------------------------------------
#
#  Define the attribute flags for a Bus Number resource descriptor.
#  Each bit flag is identified with a constant bitmask.  Following the bitmask
#  definition are the possible values.
#
#  Currently unused.
#
#
#  BUSNUMBER_RANGE
#
#
#  BUSNUMBER_DES structure
#
#
#  BUSNUMBER_RESOURCE structure
#
#
#  Define the size of each range structure
#
# --------------------------------------------------------------
#  Connection (Resource Hub) Resource
# --------------------------------------------------------------
#
#  CONNECTION_DES structure
#
#
#  CONNECTION_RESOURCE
#
# --------------------------------------------------------------
#  Hardware Profile Information
# --------------------------------------------------------------
#
#  Define flags relating to hardware profiles
#
CM_HWPI_NOT_DOCKABLE = 0x00000000  # machine is not dockable
CM_HWPI_UNDOCKED = 0x00000001  # hw profile for docked config
CM_HWPI_DOCKED = 0x00000002  # hw profile for undocked config
#
#  HWPROFILEINFO structure
#
#
#  revert back to normal default packing
#
# --------------------------------------------------------------
#  Miscellaneous
# --------------------------------------------------------------
#
#  Resource types
#
ResType_All = 0x00000000  # Return all resource types
ResType_None = 0x00000000  # Arbitration always succeeded
ResType_Mem = 0x00000001  # Physical address resource
ResType_IO = 0x00000002  # Physical I/O address resource
ResType_DMA = 0x00000003  # DMA channels resource
ResType_IRQ = 0x00000004  # IRQ resource
ResType_DoNotUse = 0x00000005  # Used as spacer to sync subsequent ResTypes w/NT
ResType_BusNumber = 0x00000006  # bus number resource
ResType_MemLarge = 0x00000007  # Memory resources >= 4GB
ResType_MAX = 0x00000007  # Maximum known (arbitrated) ResType
ResType_Ignored_Bit = 0x00008000  # Ignore this resource
ResType_ClassSpecific = 0x0000FFFF  # class-specific resource
ResType_Reserved = 0x00008000  # reserved for internal use
ResType_DevicePrivate = 0x00008001  # device private data
ResType_PcCardConfig = 0x00008002  # PC Card configuration data
ResType_MfCardConfig = 0x00008003  # MF Card configuration data
ResType_Connection = 0x00008004  # Connection (Resource Hub) resource
#
#  Flags specifying options for ranges that conflict with ranges already in
#  the range list (CM_Add_Range)
#
CM_ADD_RANGE_ADDIFCONFLICT = 0x00000000  # merg with conflicting range
CM_ADD_RANGE_DONOTADDIFCONFLICT = 0x00000001  # error if range conflicts
CM_ADD_RANGE_BITS = 0x00000001
#
#  Logical Config Flags (specified in call to CM_Get_First_Log_Conf
#
BASIC_LOG_CONF = 0x00000000  # Specifies the req list.
FILTERED_LOG_CONF = 0x00000001  # Specifies the filtered req list.
ALLOC_LOG_CONF = 0x00000002  # Specifies the Alloc Element.
BOOT_LOG_CONF = 0x00000003  # Specifies the RM Alloc Element.
FORCED_LOG_CONF = 0x00000004  # Specifies the Forced Log Conf
OVERRIDE_LOG_CONF = 0x00000005  # Specifies the Override req list.
NUM_LOG_CONF = 0x00000006  # Number of Log Conf type
LOG_CONF_BITS = 0x00000007  # The bits of the log conf type.
PRIORITY_EQUAL_FIRST = 0x00000008  # Same priority, new one first
PRIORITY_EQUAL_LAST = 0x00000000  # Same priority, new one last
PRIORITY_BIT = 0x00000008
#
#  Registry disposition values
#  (specified in call to CM_Open_DevNode_Key and CM_Open_Class_Key)
#
RegDisposition_OpenAlways = 0x00000000  # open if exists else create
RegDisposition_OpenExisting = 0x00000001  # open key only if exists
RegDisposition_Bits = 0x00000001
#
#  ulFlags values for CM API routines
#
#
#  Flags for CM_Add_ID
#
CM_ADD_ID_HARDWARE = 0x00000000
CM_ADD_ID_COMPATIBLE = 0x00000001
CM_ADD_ID_BITS = 0x00000001
#
#  Flags for CM_Create_DevNode
#
CM_CREATE_DEVNODE_NORMAL = 0x00000000  # install later
CM_CREATE_DEVNODE_NO_WAIT_INSTALL = 0x00000001  # NOT SUPPORTED ON NT
CM_CREATE_DEVNODE_PHANTOM = 0x00000002
CM_CREATE_DEVNODE_GENERATE_ID = 0x00000004
CM_CREATE_DEVNODE_DO_NOT_INSTALL = 0x00000008
CM_CREATE_DEVNODE_BITS = 0x0000000F
CM_CREATE_DEVINST_NORMAL = CM_CREATE_DEVNODE_NORMAL
CM_CREATE_DEVINST_NO_WAIT_INSTALL = CM_CREATE_DEVNODE_NO_WAIT_INSTALL
CM_CREATE_DEVINST_PHANTOM = CM_CREATE_DEVNODE_PHANTOM
CM_CREATE_DEVINST_GENERATE_ID = CM_CREATE_DEVNODE_GENERATE_ID
CM_CREATE_DEVINST_DO_NOT_INSTALL = CM_CREATE_DEVNODE_DO_NOT_INSTALL
CM_CREATE_DEVINST_BITS = CM_CREATE_DEVNODE_BITS
#
#  Flags for CM_Delete_Class_Key
#
CM_DELETE_CLASS_ONLY = 0x00000000
CM_DELETE_CLASS_SUBKEYS = 0x00000001
CM_DELETE_CLASS_INTERFACE = 0x00000002
CM_DELETE_CLASS_BITS = 0x00000003
#
#  Flags for CM_Enumerate_Classes
#
CM_ENUMERATE_CLASSES_INSTALLER = 0x00000000
CM_ENUMERATE_CLASSES_INTERFACE = 0x00000001
CM_ENUMERATE_CLASSES_BITS = 0x00000001
#
#  Detection reason flags (specified in call to CM_Run_Detection)
#
CM_DETECT_NEW_PROFILE = 0x00000001  # detection for new hw profile
CM_DETECT_CRASHED = 0x00000002  # Previous detection crashed
CM_DETECT_HWPROF_FIRST_BOOT = 0x00000004
CM_DETECT_RUN = 0x80000000
CM_DETECT_BITS = 0x80000007
#
#  Flags for CM_Disable_DevNode
#
CM_DISABLE_POLITE = 0x00000000  # Ask the driver
CM_DISABLE_ABSOLUTE = 0x00000001  # Don't ask the driver
CM_DISABLE_HARDWARE = 0x00000002  # Don't ask the driver, and won't be restarteable
CM_DISABLE_UI_NOT_OK = 0x00000004  # Don't popup any veto API
CM_DISABLE_PERSIST = 0x00000008  # Persists through restart by setting CONFIGFLAG_DISABLED in the registry
CM_DISABLE_BITS = 0x0000000F  # The bits for the disable function
#
#  Flags for CM_Get_Device_ID_List, CM_Get_Device_ID_List_Size
#
CM_GETIDLIST_FILTER_NONE = 0x00000000
CM_GETIDLIST_FILTER_ENUMERATOR = 0x00000001
CM_GETIDLIST_FILTER_SERVICE = 0x00000002
CM_GETIDLIST_FILTER_EJECTRELATIONS = 0x00000004
CM_GETIDLIST_FILTER_REMOVALRELATIONS = 0x00000008
CM_GETIDLIST_FILTER_POWERRELATIONS = 0x00000010
CM_GETIDLIST_FILTER_BUSRELATIONS = 0x00000020
CM_GETIDLIST_DONOTGENERATE = 0x10000040
CM_GETIDLIST_FILTER_BITS = 0x1000007F
CM_GETIDLIST_FILTER_TRANSPORTRELATIONS = 0x00000080
CM_GETIDLIST_FILTER_PRESENT = 0x00000100
CM_GETIDLIST_FILTER_CLASS = 0x00000200
# CM_GETIDLIST_FILTER_BITS = 0x100003FF
#
#  Flags for CM_Get_Device_Interface_List, CM_Get_Device_Interface_List_Size
#
CM_GET_DEVICE_INTERFACE_LIST_PRESENT = 0x00000000  # only currently 'live' device interfaces
CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES = 0x00000001  # all registered device interfaces, live or not
CM_GET_DEVICE_INTERFACE_LIST_BITS = 0x00000001
#
#  Registry properties (specified in call to CM_Get_DevInst_Registry_Property or CM_Get_Class_Registry_Property,
#  some are allowed in calls to CM_Set_DevInst_Registry_Property and CM_Set_Class_Registry_Property)
#  CM_DRP_xxxx values should be used for CM_Get_DevInst_Registry_Property / CM_Set_DevInst_Registry_Property
#  CM_CRP_xxxx values should be used for CM_Get_Class_Registry_Property / CM_Set_Class_Registry_Property
#  DRP/CRP values that overlap must have a 1:1 correspondence with each other
#
CM_DRP_DEVICEDESC = 0x00000001  # DeviceDesc REG_SZ property (RW)
CM_DRP_HARDWAREID = 0x00000002  # HardwareID REG_MULTI_SZ property (RW)
CM_DRP_COMPATIBLEIDS = 0x00000003  # CompatibleIDs REG_MULTI_SZ property (RW)
CM_DRP_UNUSED0 = 0x00000004  # unused
CM_DRP_SERVICE = 0x00000005  # Service REG_SZ property (RW)
CM_DRP_UNUSED1 = 0x00000006  # unused
CM_DRP_UNUSED2 = 0x00000007  # unused
CM_DRP_CLASS = 0x00000008  # Class REG_SZ property (RW)
CM_DRP_CLASSGUID = 0x00000009  # ClassGUID REG_SZ property (RW)
CM_DRP_DRIVER = 0x0000000A  # Driver REG_SZ property (RW)
CM_DRP_CONFIGFLAGS = 0x0000000B  # ConfigFlags REG_DWORD property (RW)
CM_DRP_MFG = 0x0000000C  # Mfg REG_SZ property (RW)
CM_DRP_FRIENDLYNAME = 0x0000000D  # FriendlyName REG_SZ property (RW)
CM_DRP_LOCATION_INFORMATION = 0x0000000E  # LocationInformation REG_SZ property (RW)
CM_DRP_PHYSICAL_DEVICE_OBJECT_NAME = 0x0000000F  # PhysicalDeviceObjectName REG_SZ property (R)
CM_DRP_CAPABILITIES = 0x00000010  # Capabilities REG_DWORD property (R)
CM_DRP_UI_NUMBER = 0x00000011  # UiNumber REG_DWORD property (R)
CM_DRP_UPPERFILTERS = 0x00000012  # UpperFilters REG_MULTI_SZ property (RW)
CM_CRP_UPPERFILTERS = CM_DRP_UPPERFILTERS  # UpperFilters REG_MULTI_SZ property (RW)
CM_DRP_LOWERFILTERS = 0x00000013  # LowerFilters REG_MULTI_SZ property (RW)
CM_CRP_LOWERFILTERS = CM_DRP_LOWERFILTERS  # LowerFilters REG_MULTI_SZ property (RW)
CM_DRP_BUSTYPEGUID = 0x00000014  # Bus Type Guid, GUID, (R)
CM_DRP_LEGACYBUSTYPE = 0x00000015  # Legacy bus type, INTERFACE_TYPE, (R)
CM_DRP_BUSNUMBER = 0x00000016  # Bus Number, DWORD, (R)
CM_DRP_ENUMERATOR_NAME = 0x00000017  # Enumerator Name REG_SZ property (R)
CM_DRP_SECURITY = 0x00000018  # Security - Device override (RW)
CM_CRP_SECURITY = CM_DRP_SECURITY  # Class default security (RW)
CM_DRP_SECURITY_SDS = 0x00000019  # Security - Device override (RW)
CM_CRP_SECURITY_SDS = CM_DRP_SECURITY_SDS  # Class default security (RW)
CM_DRP_DEVTYPE = 0x0000001A  # Device Type - Device override (RW)
CM_CRP_DEVTYPE = CM_DRP_DEVTYPE  # Class default Device-type (RW)
CM_DRP_EXCLUSIVE = 0x0000001B  # Exclusivity - Device override (RW)
CM_CRP_EXCLUSIVE = CM_DRP_EXCLUSIVE  # Class default (RW)
CM_DRP_CHARACTERISTICS = 0x0000001C  # Characteristics - Device Override (RW)
CM_CRP_CHARACTERISTICS = CM_DRP_CHARACTERISTICS  # Class default (RW)
CM_DRP_ADDRESS = 0x0000001D  # Device Address (R)
CM_DRP_UI_NUMBER_DESC_FORMAT = 0x0000001E  # UINumberDescFormat REG_SZ property (RW)
CM_DRP_DEVICE_POWER_DATA = 0x0000001F  # CM_POWER_DATA REG_BINARY property (R)
CM_DRP_REMOVAL_POLICY = 0x00000020  # CM_DEVICE_REMOVAL_POLICY REG_DWORD (R)
CM_DRP_REMOVAL_POLICY_HW_DEFAULT = 0x00000021  # CM_DRP_REMOVAL_POLICY_HW_DEFAULT REG_DWORD (R)
CM_DRP_REMOVAL_POLICY_OVERRIDE = 0x00000022  # CM_DRP_REMOVAL_POLICY_OVERRIDE REG_DWORD (RW)
CM_DRP_INSTALL_STATE = 0x00000023  # CM_DRP_INSTALL_STATE REG_DWORD (R)
CM_DRP_LOCATION_PATHS = 0x00000024  # CM_DRP_LOCATION_PATHS REG_MULTI_SZ (R)
CM_DRP_BASE_CONTAINERID = 0x00000025  # Base ContainerID REG_SZ property (R)
CM_DRP_MIN = 0x00000001  # First device register
CM_CRP_MIN = CM_DRP_MIN  # First class register
CM_DRP_MAX = 0x00000025  # Last device register
CM_CRP_MAX = CM_DRP_MAX  # Last class register
#
#  Capabilities bits (the capability value is returned from calling
#  CM_Get_DevInst_Registry_Property with CM_DRP_CAPABILITIES property)
#
CM_DEVCAP_LOCKSUPPORTED = 0x00000001
CM_DEVCAP_EJECTSUPPORTED = 0x00000002
CM_DEVCAP_REMOVABLE = 0x00000004
CM_DEVCAP_DOCKDEVICE = 0x00000008
CM_DEVCAP_UNIQUEID = 0x00000010
CM_DEVCAP_SILENTINSTALL = 0x00000020
CM_DEVCAP_RAWDEVICEOK = 0x00000040
CM_DEVCAP_SURPRISEREMOVALOK = 0x00000080
CM_DEVCAP_HARDWAREDISABLED = 0x00000100
CM_DEVCAP_NONDYNAMIC = 0x00000200
CM_DEVCAP_SECUREDEVICE = 0x00000400
#
#  Removal policies (retrievable via CM_Get_DevInst_Registry_Property with
#  the CM_DRP_REMOVAL_POLICY, CM_DRP_REMOVAL_POLICY_OVERRIDE, or
#  CM_DRP_REMOVAL_POLICY_HW_DEFAULT properties)
#
CM_REMOVAL_POLICY_EXPECT_NO_REMOVAL = 1
CM_REMOVAL_POLICY_EXPECT_ORDERLY_REMOVAL = 2
CM_REMOVAL_POLICY_EXPECT_SURPRISE_REMOVAL = 3
#
#  Device install states (retrievable via CM_Get_DevInst_Registry_Property with
#  the CM_DRP_INSTALL_STATE properties)
#
CM_INSTALL_STATE_INSTALLED = 0
CM_INSTALL_STATE_NEEDS_REINSTALL = 1
CM_INSTALL_STATE_FAILED_INSTALL = 2
CM_INSTALL_STATE_FINISH_INSTALL = 3
#
#  Flags for CM_Locate_DevNode
#
CM_LOCATE_DEVNODE_NORMAL = 0x00000000
CM_LOCATE_DEVNODE_PHANTOM = 0x00000001
CM_LOCATE_DEVNODE_CANCELREMOVE = 0x00000002
CM_LOCATE_DEVNODE_NOVALIDATION = 0x00000004
CM_LOCATE_DEVNODE_BITS = 0x00000007
CM_LOCATE_DEVINST_NORMAL = CM_LOCATE_DEVNODE_NORMAL
CM_LOCATE_DEVINST_PHANTOM = CM_LOCATE_DEVNODE_PHANTOM
CM_LOCATE_DEVINST_CANCELREMOVE = CM_LOCATE_DEVNODE_CANCELREMOVE
CM_LOCATE_DEVINST_NOVALIDATION = CM_LOCATE_DEVNODE_NOVALIDATION
CM_LOCATE_DEVINST_BITS = CM_LOCATE_DEVNODE_BITS
#
#  Flags for CM_Open_Class_Key
#
CM_OPEN_CLASS_KEY_INSTALLER = 0x00000000
CM_OPEN_CLASS_KEY_INTERFACE = 0x00000001
CM_OPEN_CLASS_KEY_BITS = 0x00000001
#
#  Flags for CM_Query_And_Remove_SubTree
#
CM_REMOVE_UI_OK = 0x00000000
CM_REMOVE_UI_NOT_OK = 0x00000001
CM_REMOVE_NO_RESTART = 0x00000002
CM_REMOVE_BITS = 0x00000003
#
#  Backward compatibility--do not use
#  (use above CM_REMOVE_* flags instead)
#
CM_QUERY_REMOVE_UI_OK = CM_REMOVE_UI_OK
CM_QUERY_REMOVE_UI_NOT_OK = CM_REMOVE_UI_NOT_OK
#
#  Flags for CM_Reenumerate_DevNode
#
CM_REENUMERATE_NORMAL = 0x00000000
CM_REENUMERATE_SYNCHRONOUS = 0x00000001
CM_REENUMERATE_RETRY_INSTALLATION = 0x00000002
CM_REENUMERATE_ASYNCHRONOUS = 0x00000004
CM_REENUMERATE_BITS = 0x00000007
#
#  Flags for CM_Register_Device_Driver
#
CM_REGISTER_DEVICE_DRIVER_STATIC = 0x00000000
CM_REGISTER_DEVICE_DRIVER_DISABLEABLE = 0x00000001
CM_REGISTER_DEVICE_DRIVER_REMOVABLE = 0x00000002
CM_REGISTER_DEVICE_DRIVER_BITS = 0x00000003
#
#  Registry Branch Locations (for CM_Open_DevNode_Key)
#
CM_REGISTRY_HARDWARE = 0x00000000
CM_REGISTRY_SOFTWARE = 0x00000001
CM_REGISTRY_USER = 0x00000100
CM_REGISTRY_CONFIG = 0x00000200
CM_REGISTRY_BITS = 0x00000301
#
#  Flags for CM_Set_DevNode_Problem
#
CM_SET_DEVNODE_PROBLEM_NORMAL = 0x00000000  # only set problem if currently no problem
CM_SET_DEVNODE_PROBLEM_OVERRIDE = 0x00000001  # override current problem with new problem
CM_SET_DEVNODE_PROBLEM_BITS = 0x00000001
CM_SET_DEVINST_PROBLEM_NORMAL = CM_SET_DEVNODE_PROBLEM_NORMAL
CM_SET_DEVINST_PROBLEM_OVERRIDE = CM_SET_DEVNODE_PROBLEM_OVERRIDE
CM_SET_DEVINST_PROBLEM_BITS = CM_SET_DEVNODE_PROBLEM_BITS
#
#  Flags for CM_Set_HW_Prof_Flags
#
CM_SET_HW_PROF_FLAGS_UI_NOT_OK = 0x00000001  # Don't popup any veto UI
CM_SET_HW_PROF_FLAGS_BITS = 0x00000001
#
#  Re-enable and configuration actions (specified in call to CM_Setup_DevInst)
#
CM_SETUP_DEVNODE_READY = 0x00000000  # Reenable problem devinst
CM_SETUP_DEVINST_READY = CM_SETUP_DEVNODE_READY
CM_SETUP_DOWNLOAD = 0x00000001  # Get info about devinst
CM_SETUP_WRITE_LOG_CONFS = 0x00000002
CM_SETUP_PROP_CHANGE = 0x00000003
CM_SETUP_DEVNODE_RESET = 0x00000004  # Reset problem devinst without starting
CM_SETUP_DEVINST_RESET = CM_SETUP_DEVNODE_RESET
CM_SETUP_DEVNODE_CONFIG = 0x00000005  # Configure devinst without (re)starting
CM_SETUP_DEVINST_CONFIG = CM_SETUP_DEVNODE_CONFIG
CM_SETUP_DEVNODE_CONFIG_CLASS = 0x00000006  # Configure devinst class without (re)starting
CM_SETUP_DEVINST_CONFIG_CLASS = CM_SETUP_DEVNODE_CONFIG_CLASS
CM_SETUP_DEVNODE_CONFIG_EXTENSIONS = 0x00000007  # Configure devinst extensions without (re)starting
CM_SETUP_DEVINST_CONFIG_EXTENSIONS = CM_SETUP_DEVNODE_CONFIG_EXTENSIONS
CM_SETUP_DEVNODE_CONFIG_RESET = 0x00000008  # Reset devinst configuration without (re)starting
CM_SETUP_DEVINST_CONFIG_RESET = CM_SETUP_DEVNODE_CONFIG_RESET
CM_SETUP_BITS = 0x0000000F
#
#  Flags for CM_Query_Arbitrator_Free_Data and
#  CM_Query_Arbitrator_Free_Data_Size.
#
CM_QUERY_ARBITRATOR_RAW = 0x00000000
CM_QUERY_ARBITRATOR_TRANSLATED = 0x00000001
CM_QUERY_ARBITRATOR_BITS = 0x00000001
#
#  Flags for CM_Get_DevNode_Custom_Property
#
CM_CUSTOMDEVPROP_MERGE_MULTISZ = 0x00000001
CM_CUSTOMDEVPROP_BITS = 0x00000001
#
#  Name attibute bitmasks
#
CM_NAME_ATTRIBUTE_NAME_RETRIEVED_FROM_DEVICE = 0x1
CM_NAME_ATTRIBUTE_USER_ASSIGNED_NAME = 0x2
#
#  Flags for CM_Get_Class_Property_Keys_Ex, CM_Get_Class_Property_Ex,
#  and CM_Set_Class_Property_Ex
#
CM_CLASS_PROPERTY_INSTALLER = 0x00000000
CM_CLASS_PROPERTY_INTERFACE = 0x00000001
CM_CLASS_PROPERTY_BITS = 0x00000001
#
#  Device notification registration handle
#
#
#  Device notification flags for registration filters
#
CM_NOTIFY_FILTER_FLAG_ALL_INTERFACE_CLASSES = 0x00000001
CM_NOTIFY_FILTER_FLAG_ALL_DEVICE_INSTANCES = 0x00000002
CM_NOTIFY_FILTER_VALID_FLAGS = CM_NOTIFY_FILTER_FLAG_ALL_INTERFACE_CLASSES  # |\
#
#  Device notification filter types
#
#
#  Device notification filter structure
#
#
#  Device notification event action types
#
#
#  Device notification event data structure
#
#
#  Device notification event callback definiton
#
# --------------------------------------------------------------
#  Function prototypes
# --------------------------------------------------------------
CM_GLOBAL_STATE_CAN_DO_UI = 0x00000001  # Can do UI
CM_GLOBAL_STATE_ON_BIG_STACK = 0x00000002  # Not used (reserved)
CM_GLOBAL_STATE_SERVICES_AVAILABLE = 0x00000004  # CM APIs available?
CM_GLOBAL_STATE_SHUTTING_DOWN = 0x00000008  # CM shutting down
CM_GLOBAL_STATE_DETECTION_PENDING = 0x00000010  # Not used (reserved)
CM_GLOBAL_STATE_REBOOT_REQUIRED = 0x00000020  # system reboot is required
#
#  CONFIGRET to Win32 error mapping routine
#
#
#  Configuration Manager CONFIGRET return status codes
#
CR_SUCCESS = 0x00000000
CR_DEFAULT = 0x00000001
CR_OUT_OF_MEMORY = 0x00000002
CR_INVALID_POINTER = 0x00000003
CR_INVALID_FLAG = 0x00000004
CR_INVALID_DEVNODE = 0x00000005
CR_INVALID_DEVINST = CR_INVALID_DEVNODE
CR_INVALID_RES_DES = 0x00000006
CR_INVALID_LOG_CONF = 0x00000007
CR_INVALID_ARBITRATOR = 0x00000008
CR_INVALID_NODELIST = 0x00000009
CR_DEVNODE_HAS_REQS = 0x0000000A
CR_DEVINST_HAS_REQS = CR_DEVNODE_HAS_REQS
CR_INVALID_RESOURCEID = 0x0000000B
CR_DLVXD_NOT_FOUND = 0x0000000C  # WIN 95 ONLY
CR_NO_SUCH_DEVNODE = 0x0000000D
CR_NO_SUCH_DEVINST = CR_NO_SUCH_DEVNODE
CR_NO_MORE_LOG_CONF = 0x0000000E
CR_NO_MORE_RES_DES = 0x0000000F
CR_ALREADY_SUCH_DEVNODE = 0x00000010
CR_ALREADY_SUCH_DEVINST = CR_ALREADY_SUCH_DEVNODE
CR_INVALID_RANGE_LIST = 0x00000011
CR_INVALID_RANGE = 0x00000012
CR_FAILURE = 0x00000013
CR_NO_SUCH_LOGICAL_DEV = 0x00000014
CR_CREATE_BLOCKED = 0x00000015
CR_NOT_SYSTEM_VM = 0x00000016  # WIN 95 ONLY
CR_REMOVE_VETOED = 0x00000017
CR_APM_VETOED = 0x00000018
CR_INVALID_LOAD_TYPE = 0x00000019
CR_BUFFER_SMALL = 0x0000001A
CR_NO_ARBITRATOR = 0x0000001B
CR_NO_REGISTRY_HANDLE = 0x0000001C
CR_REGISTRY_ERROR = 0x0000001D
CR_INVALID_DEVICE_ID = 0x0000001E
CR_INVALID_DATA = 0x0000001F
CR_INVALID_API = 0x00000020
CR_DEVLOADER_NOT_READY = 0x00000021
CR_NEED_RESTART = 0x00000022
CR_NO_MORE_HW_PROFILES = 0x00000023
CR_DEVICE_NOT_THERE = 0x00000024
CR_NO_SUCH_VALUE = 0x00000025
CR_WRONG_TYPE = 0x00000026
CR_INVALID_PRIORITY = 0x00000027
CR_NOT_DISABLEABLE = 0x00000028
CR_FREE_RESOURCES = 0x00000029
CR_QUERY_VETOED = 0x0000002A
CR_CANT_SHARE_IRQ = 0x0000002B
CR_NO_DEPENDENT = 0x0000002C
CR_SAME_RESOURCES = 0x0000002D
CR_NO_SUCH_REGISTRY_KEY = 0x0000002E
CR_INVALID_MACHINENAME = 0x0000002F  # NT ONLY
CR_REMOTE_COMM_FAILURE = 0x00000030  # NT ONLY
CR_MACHINE_UNAVAILABLE = 0x00000031  # NT ONLY
CR_NO_CM_SERVICES = 0x00000032  # NT ONLY
CR_ACCESS_DENIED = 0x00000033  # NT ONLY
CR_CALL_NOT_IMPLEMENTED = 0x00000034
CR_INVALID_PROPERTY = 0x00000035
CR_DEVICE_INTERFACE_ACTIVE = 0x00000036
CR_NO_SUCH_DEVICE_INTERFACE = 0x00000037
CR_INVALID_REFERENCE_STRING = 0x00000038
CR_INVALID_CONFLICT_LIST = 0x00000039
CR_INVALID_INDEX = 0x0000003A
CR_INVALID_STRUCTURE_SIZE = 0x0000003B
NUM_CR_RESULTS = 0x0000003C
