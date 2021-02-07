# ----------------------------------------------------
# The below constants are autogenerated from WinBase.h
# ----------------------------------------------------

#
#  APISET contracts
#
FILE_BEGIN = 0
FILE_CURRENT = 1
FILE_END = 2
#
#  File creation flags must start at the high end since they
#  are combined with the attributes
#
#
#   These are flags supported through CreateFile (W7) and CreateFile2 (W8 and beyond)
#
FILE_FLAG_WRITE_THROUGH = 0x80000000
FILE_FLAG_OVERLAPPED = 0x40000000
FILE_FLAG_NO_BUFFERING = 0x20000000
FILE_FLAG_RANDOM_ACCESS = 0x10000000
FILE_FLAG_SEQUENTIAL_SCAN = 0x08000000
FILE_FLAG_DELETE_ON_CLOSE = 0x04000000
FILE_FLAG_BACKUP_SEMANTICS = 0x02000000
FILE_FLAG_POSIX_SEMANTICS = 0x01000000
FILE_FLAG_SESSION_AWARE = 0x00800000
FILE_FLAG_OPEN_REPARSE_POINT = 0x00200000
FILE_FLAG_OPEN_NO_RECALL = 0x00100000
FILE_FLAG_FIRST_PIPE_INSTANCE = 0x00080000
#
#   These are flags supported only through CreateFile2 (W8 and beyond)
#
#   Due to the multiplexing of file creation flags, file attribute flags and
#   security QoS flags into a single DWORD (dwFlagsAndAttributes) parameter for
#   CreateFile, there is no way to add any more flags to CreateFile. Additional
#   flags for the create operation must be added to CreateFile2 only
#
FILE_FLAG_OPEN_REQUIRING_OPLOCK = 0x00040000
#
#  Define possible return codes from the CopyFileEx callback routine
#
PROGRESS_CONTINUE = 0
PROGRESS_CANCEL = 1
PROGRESS_STOP = 2
PROGRESS_QUIET = 3
#
#  Define CopyFileEx callback routine state change values
#
CALLBACK_CHUNK_FINISHED = 0x00000000
CALLBACK_STREAM_SWITCH = 0x00000001
#
#  Define CopyFileEx option flags
#
COPY_FILE_FAIL_IF_EXISTS = 0x00000001
COPY_FILE_RESTARTABLE = 0x00000002
COPY_FILE_OPEN_SOURCE_FOR_WRITE = 0x00000004
COPY_FILE_ALLOW_DECRYPTED_DESTINATION = 0x00000008
#
#   Gap for private copyfile flags
#
COPY_FILE_COPY_SYMLINK = 0x00000800
COPY_FILE_NO_BUFFERING = 0x00001000
#
#   CopyFile2 flags
#
COPY_FILE_REQUEST_SECURITY_PRIVILEGES = 0x00002000
COPY_FILE_RESUME_FROM_PAUSE = 0x00004000
COPY_FILE_NO_OFFLOAD = 0x00040000
COPY_FILE_IGNORE_EDP_BLOCK = 0x00400000
COPY_FILE_IGNORE_SOURCE_ENCRYPTION = 0x00800000
#
#  Define ReplaceFile option flags
#
REPLACEFILE_WRITE_THROUGH = 0x00000001
REPLACEFILE_IGNORE_MERGE_ERRORS = 0x00000002
REPLACEFILE_IGNORE_ACL_ERRORS = 0x00000004
#
#  Define the NamedPipe definitions
#
#
#  Define the dwOpenMode values for CreateNamedPipe
#
PIPE_ACCESS_INBOUND = 0x00000001
PIPE_ACCESS_OUTBOUND = 0x00000002
PIPE_ACCESS_DUPLEX = 0x00000003
#
#  Define the Named Pipe End flags for GetNamedPipeInfo
#
PIPE_CLIENT_END = 0x00000000
PIPE_SERVER_END = 0x00000001
#
#  Define the dwPipeMode values for CreateNamedPipe
#
PIPE_WAIT = 0x00000000
PIPE_NOWAIT = 0x00000001
PIPE_READMODE_BYTE = 0x00000000
PIPE_READMODE_MESSAGE = 0x00000002
PIPE_TYPE_BYTE = 0x00000000
PIPE_TYPE_MESSAGE = 0x00000004
PIPE_ACCEPT_REMOTE_CLIENTS = 0x00000000
PIPE_REJECT_REMOTE_CLIENTS = 0x00000008
#
#  Define the well known values for CreateNamedPipe nMaxInstances
#
PIPE_UNLIMITED_INSTANCES = 255
#
#  Define the Security Quality of Service bits to be passed
#  into CreateFile
#
SECURITY_CONTEXT_TRACKING = 0x00040000
SECURITY_EFFECTIVE_ONLY = 0x00080000
SECURITY_SQOS_PRESENT = 0x00100000
SECURITY_VALID_SQOS_FLAGS = 0x001F0000
#
#  Fiber structures
#
#
#  FailFast Exception Flags
#
FAIL_FAST_GENERATE_EXCEPTION_ADDRESS = 0x1
FAIL_FAST_NO_HARD_ERROR_DLG = 0x2
#
#  Serial provider type.
#
#
#  Provider SubTypes
#
#
#  Provider capabilities flags.
#
#
#  Comm provider settable parameters.
#
#
#  Settable baud rates in the provider.
#
#
#  Settable Data Bits
#
#
#  Settable Stop and Parity bits.
#
#
#  Set dwProvSpec1 to COMMPROP_INITIALIZED to indicate that wPacketLength
#  is valid before a call to GetCommProperties().
#
#
#  DTR Control Flow Values.
#
DTR_CONTROL_DISABLE = 0x00
DTR_CONTROL_ENABLE = 0x01
DTR_CONTROL_HANDSHAKE = 0x02
#
#  RTS Control Flow Values
#
RTS_CONTROL_DISABLE = 0x00
RTS_CONTROL_ENABLE = 0x01
RTS_CONTROL_HANDSHAKE = 0x02
RTS_CONTROL_TOGGLE = 0x03
#
#
GMEM_FIXED = 0x0000
GMEM_MOVEABLE = 0x0002
GMEM_NOCOMPACT = 0x0010
GMEM_NODISCARD = 0x0020
GMEM_ZEROINIT = 0x0040
GMEM_MODIFY = 0x0080
GMEM_DISCARDABLE = 0x0100
GMEM_NOT_BANKED = 0x1000
GMEM_SHARE = 0x2000
GMEM_DDESHARE = 0x2000
GMEM_NOTIFY = 0x4000
GMEM_LOWER = GMEM_NOT_BANKED
GMEM_VALID_FLAGS = 0x7F72
GMEM_INVALID_HANDLE = 0x8000
GHND = GMEM_MOVEABLE  # | GMEM_ZEROINIT)
GPTR = GMEM_FIXED  # | GMEM_ZEROINIT)
GMEM_DISCARDED = 0x4000
GMEM_LOCKCOUNT = 0x00FF
#
#  Process dwCreationFlag values
#
DEBUG_PROCESS = 0x00000001
DEBUG_ONLY_THIS_PROCESS = 0x00000002
CREATE_SUSPENDED = 0x00000004
DETACHED_PROCESS = 0x00000008
CREATE_NEW_CONSOLE = 0x00000010
NORMAL_PRIORITY_CLASS = 0x00000020
IDLE_PRIORITY_CLASS = 0x00000040
HIGH_PRIORITY_CLASS = 0x00000080
REALTIME_PRIORITY_CLASS = 0x00000100
CREATE_NEW_PROCESS_GROUP = 0x00000200
CREATE_UNICODE_ENVIRONMENT = 0x00000400
CREATE_SEPARATE_WOW_VDM = 0x00000800
CREATE_SHARED_WOW_VDM = 0x00001000
CREATE_FORCEDOS = 0x00002000
BELOW_NORMAL_PRIORITY_CLASS = 0x00004000
ABOVE_NORMAL_PRIORITY_CLASS = 0x00008000
INHERIT_PARENT_AFFINITY = 0x00010000
INHERIT_CALLER_PRIORITY = 0x00020000  # Deprecated
CREATE_PROTECTED_PROCESS = 0x00040000
EXTENDED_STARTUPINFO_PRESENT = 0x00080000
PROCESS_MODE_BACKGROUND_BEGIN = 0x00100000
PROCESS_MODE_BACKGROUND_END = 0x00200000
CREATE_BREAKAWAY_FROM_JOB = 0x01000000
CREATE_PRESERVE_CODE_AUTHZ_LEVEL = 0x02000000
CREATE_DEFAULT_ERROR_MODE = 0x04000000
CREATE_NO_WINDOW = 0x08000000
PROFILE_USER = 0x10000000
PROFILE_KERNEL = 0x20000000
PROFILE_SERVER = 0x40000000
CREATE_IGNORE_SYSTEM_DEFAULT = 0x80000000
#
#  Thread dwCreationFlag values
#
# #define CREATE_SUSPENDED                  0x00000004
STACK_SIZE_PARAM_IS_A_RESERVATION = 0x00010000  # Threads only
#
#  Priority flags
#
THREAD_PRIORITY_NORMAL = 0
THREAD_MODE_BACKGROUND_BEGIN = 0x00010000
THREAD_MODE_BACKGROUND_END = 0x00020000
#
#  GetFinalPathNameByHandle
#
VOLUME_NAME_DOS = 0x0  # default
VOLUME_NAME_GUID = 0x1
VOLUME_NAME_NT = 0x2
VOLUME_NAME_NONE = 0x4
FILE_NAME_NORMALIZED = 0x0  # default
FILE_NAME_OPENED = 0x8
#
#  JIT Debugging Info. This structure is defined to have constant size in
#  both the emulated and native environment.
#
DRIVE_UNKNOWN = 0
DRIVE_NO_ROOT_DIR = 1
DRIVE_REMOVABLE = 2
DRIVE_FIXED = 3
DRIVE_REMOTE = 4
DRIVE_CDROM = 5
DRIVE_RAMDISK = 6
FILE_TYPE_UNKNOWN = 0x0000
FILE_TYPE_DISK = 0x0001
FILE_TYPE_CHAR = 0x0002
FILE_TYPE_PIPE = 0x0003
FILE_TYPE_REMOTE = 0x8000
NOPARITY = 0
ODDPARITY = 1
EVENPARITY = 2
MARKPARITY = 3
SPACEPARITY = 4
ONESTOPBIT = 0
ONE5STOPBITS = 1
TWOSTOPBITS = 2
IGNORE = 0  # Ignore signal
INFINITE = 0xFFFFFFFF  # Infinite timeout
#
#  Baud rates at which the communication device operates
#
CBR_110 = 110
CBR_300 = 300
CBR_600 = 600
CBR_1200 = 1200
CBR_2400 = 2400
CBR_4800 = 4800
CBR_9600 = 9600
CBR_14400 = 14400
CBR_19200 = 19200
CBR_38400 = 38400
CBR_56000 = 56000
CBR_57600 = 57600
CBR_115200 = 115200
CBR_128000 = 128000
CBR_256000 = 256000
#
#  Error Flags
#
CE_RXOVER = 0x0001  # Receive Queue overflow
CE_OVERRUN = 0x0002  # Receive Overrun Error
CE_RXPARITY = 0x0004  # Receive Parity Error
CE_FRAME = 0x0008  # Receive Framing error
CE_BREAK = 0x0010  # Break Detected
CE_TXFULL = 0x0100  # TX Queue is full
CE_PTO = 0x0200  # LPTx Timeout
CE_IOE = 0x0400  # LPTx I/O Error
CE_DNS = 0x0800  # LPTx Device not selected
CE_OOP = 0x1000  # LPTx Out-Of-Paper
CE_MODE = 0x8000  # Requested mode unsupported
IE_BADID = -1  # Invalid or unsupported id
IE_OPEN = -2  # Device Already Open
IE_NOPEN = -3  # Device Not Open
IE_MEMORY = -4  # Unable to allocate queues
IE_DEFAULT = -5  # Error in default parameters
IE_HARDWARE = -10  # Hardware Not Present
IE_BYTESIZE = -11  # Illegal Byte Size
IE_BAUDRATE = -12  # Unsupported BaudRate
#
#  Events
#
EV_RXCHAR = 0x0001  # Any Character received
EV_RXFLAG = 0x0002  # Received certain character
EV_TXEMPTY = 0x0004  # Transmitt Queue Empty
EV_CTS = 0x0008  # CTS changed state
EV_DSR = 0x0010  # DSR changed state
EV_RLSD = 0x0020  # RLSD changed state
EV_BREAK = 0x0040  # BREAK received
EV_ERR = 0x0080  # Line status error occurred
EV_RING = 0x0100  # Ring signal detected
EV_PERR = 0x0200  # Printer error occured
EV_RX80FULL = 0x0400  # Receive buffer is 80 percent full
EV_EVENT1 = 0x0800  # Provider specific event 1
EV_EVENT2 = 0x1000  # Provider specific event 2
#
#  Escape Functions
#
SETXOFF = 1  # Simulate XOFF received
SETXON = 2  # Simulate XON received
SETRTS = 3  # Set RTS high
CLRRTS = 4  # Set RTS low
SETDTR = 5  # Set DTR high
CLRDTR = 6  # Set DTR low
RESETDEV = 7  # Reset device if possible
SETBREAK = 8  # Set the device break line.
CLRBREAK = 9  # Clear the device break line.
#
#  PURGE function flags.
#
PURGE_TXABORT = 0x0001  # Kill the pending/current writes to the comm port.
PURGE_RXABORT = 0x0002  # Kill the pending/current reads to the comm port.
PURGE_TXCLEAR = 0x0004  # Kill the transmit queue if there.
PURGE_RXCLEAR = 0x0008  # Kill the typeahead buffer if there.
LPTx = 0x80  # Set if ID is for LPT device
#
#  Modem Status Flags
#
#
#  WaitSoundState() Constants
#
S_QUEUEEMPTY = 0
S_THRESHOLD = 1
S_ALLTHRESHOLD = 2
#
#  Accent Modes
#
S_NORMAL = 0
S_LEGATO = 1
S_STACCATO = 2
#
#  SetSoundNoise() Sources
#
S_PERIOD512 = 0  # Freq = N/512 high pitch, less coarse hiss
S_PERIOD1024 = 1  # Freq = N/1024
S_PERIOD2048 = 2  # Freq = N/2048 low pitch, more coarse hiss
S_PERIODVOICE = 3  # Source is frequency from voice channel (3)
S_WHITE512 = 4  # Freq = N/512 high pitch, less coarse hiss
S_WHITE1024 = 5  # Freq = N/1024
S_WHITE2048 = 6  # Freq = N/2048 low pitch, more coarse hiss
S_WHITEVOICE = 7  # Source is frequency from voice channel (3)
S_SERDVNA = -1  # Device not available
S_SEROFM = -2  # Out of memory
S_SERMACT = -3  # Music active
S_SERQFUL = -4  # Queue full
S_SERBDNT = -5  # Invalid note
S_SERDLN = -6  # Invalid note length
S_SERDCC = -7  # Invalid note count
S_SERDTP = -8  # Invalid tempo
S_SERDVL = -9  # Invalid volume
S_SERDMD = -10  # Invalid mode
S_SERDSH = -11  # Invalid shape
S_SERDPT = -12  # Invalid pitch
S_SERDFQ = -13  # Invalid frequency
S_SERDDR = -14  # Invalid duration
S_SERDSR = -15  # Invalid source
S_SERDST = -16  # Invalid state
NMPWAIT_WAIT_FOREVER = 0xffffffff
NMPWAIT_NOWAIT = 0x00000001
NMPWAIT_USE_DEFAULT_WAIT = 0x00000000
OF_READ = 0x00000000
OF_WRITE = 0x00000001
OF_READWRITE = 0x00000002
OF_SHARE_COMPAT = 0x00000000
OF_SHARE_EXCLUSIVE = 0x00000010
OF_SHARE_DENY_WRITE = 0x00000020
OF_SHARE_DENY_READ = 0x00000030
OF_SHARE_DENY_NONE = 0x00000040
OF_PARSE = 0x00000100
OF_DELETE = 0x00000200
OF_VERIFY = 0x00000400
OF_CANCEL = 0x00000800
OF_CREATE = 0x00001000
OF_PROMPT = 0x00002000
OF_EXIST = 0x00004000
OF_REOPEN = 0x00008000
OFS_MAXPATHNAME = 128
MAXINTATOM = 0xC000
#  GetBinaryType return values.
SCS_32BIT_BINARY = 0
SCS_DOS_BINARY = 1
SCS_WOW_BINARY = 2
SCS_PIF_BINARY = 3
SCS_POSIX_BINARY = 4
SCS_OS216_BINARY = 5
SCS_64BIT_BINARY = 6
#
#  Fiber begin
#
FIBER_FLAG_FLOAT_SWITCH = 0x1  # context switch floating point
#
#  Fiber end
#
#
#  UMS begin
#
#
#  UMS end
#
PROCESS_DEP_ENABLE = 0x00000001
PROCESS_DEP_DISABLE_ATL_THUNK_EMULATION = 0x00000002
#
#  Power Request APIs
#
# #if _WIN32_WINNT >= 0x0501 || defined(WINBASE_DECLARE_RESTORE_LAST_ERROR)
#
#  The following flags allows an application to change
#  the semantics of IO completion notification.
#
#
#  Don't queue an entry to an associated completion port if returning success
#  synchronously.
#
FILE_SKIP_COMPLETION_PORT_ON_SUCCESS = 0x1
#
#  Don't set the file handle event on IO completion.
#
FILE_SKIP_SET_EVENT_ON_HANDLE = 0x2
SEM_FAILCRITICALERRORS = 0x0001
SEM_NOGPFAULTERRORBOX = 0x0002
SEM_NOALIGNMENTFAULTEXCEPT = 0x0004
SEM_NOOPENFILEERRORBOX = 0x8000
HANDLE_FLAG_INHERIT = 0x00000001
HANDLE_FLAG_PROTECT_FROM_CLOSE = 0x00000002
HINSTANCE_ERROR = 32
GET_TAPE_MEDIA_INFORMATION = 0
GET_TAPE_DRIVE_INFORMATION = 1
SET_TAPE_MEDIA_INFORMATION = 0
SET_TAPE_DRIVE_INFORMATION = 1
#
#  Routines to convert back and forth between system time and file time
#
#
#  FORMAT_MESSAGE_ALLOCATE_BUFFER requires use of HeapFree
#
FORMAT_MESSAGE_ALLOCATE_BUFFER = 0x00000100
FORMAT_MESSAGE_IGNORE_INSERTS = 0x00000200
FORMAT_MESSAGE_FROM_STRING = 0x00000400
FORMAT_MESSAGE_FROM_HMODULE = 0x00000800
FORMAT_MESSAGE_FROM_SYSTEM = 0x00001000
FORMAT_MESSAGE_ARGUMENT_ARRAY = 0x00002000
FORMAT_MESSAGE_MAX_WIDTH_MASK = 0x000000FF
#
#  File Encryption API
#
#
#   Encryption Status Value
#
FILE_ENCRYPTABLE = 0
FILE_IS_ENCRYPTED = 1
FILE_SYSTEM_ATTR = 2
FILE_ROOT_DIR = 3
FILE_SYSTEM_DIR = 4
FILE_UNKNOWN = 5
FILE_SYSTEM_NOT_SUPPORT = 6
FILE_USER_DISALLOWED = 7
FILE_READ_ONLY = 8
FILE_DIR_DISALLOWED = 9
#
#  Currently defined recovery flags
#
EFS_USE_RECOVERY_KEYS = 0x1
#
#   OpenRaw flag values
#
CREATE_FOR_IMPORT = 1
CREATE_FOR_DIR = 2
OVERWRITE_HIDDEN = 4
EFSRPC_SECURE_ONLY = 8
EFS_DROP_ALTERNATE_STREAMS = 0x10
#
#  _l Compat Functions
#
#
#   Stream id structure
#
#
#   Stream Ids
#
BACKUP_INVALID = 0x00000000
BACKUP_DATA = 0x00000001
BACKUP_EA_DATA = 0x00000002
BACKUP_SECURITY_DATA = 0x00000003
BACKUP_ALTERNATE_DATA = 0x00000004
BACKUP_LINK = 0x00000005
BACKUP_PROPERTY_DATA = 0x00000006
BACKUP_OBJECT_ID = 0x00000007
BACKUP_REPARSE_DATA = 0x00000008
BACKUP_SPARSE_BLOCK = 0x00000009
BACKUP_TXFS_DATA = 0x0000000a
BACKUP_GHOSTED_FILE_EXTENTS = 0x0000000b
#
#   Stream Attributes
#
STREAM_NORMAL_ATTRIBUTE = 0x00000000
STREAM_MODIFIED_WHEN_READ = 0x00000001
STREAM_CONTAINS_SECURITY = 0x00000002
STREAM_CONTAINS_PROPERTIES = 0x00000004
STREAM_SPARSE_ATTRIBUTE = 0x00000008
STREAM_CONTAINS_GHOSTED_FILE_EXTENTS = 0x00000010
#
#  Dual Mode API below this line. Dual Mode Structures also included.
#
STARTF_USESHOWWINDOW = 0x00000001
STARTF_USESIZE = 0x00000002
STARTF_USEPOSITION = 0x00000004
STARTF_USECOUNTCHARS = 0x00000008
STARTF_USEFILLATTRIBUTE = 0x00000010
STARTF_RUNFULLSCREEN = 0x00000020  # ignored for non-x86 platforms
STARTF_FORCEONFEEDBACK = 0x00000040
STARTF_FORCEOFFFEEDBACK = 0x00000080
STARTF_USESTDHANDLES = 0x00000100
STARTF_USEHOTKEY = 0x00000200
STARTF_TITLEISLINKNAME = 0x00000800
STARTF_TITLEISAPPID = 0x00001000
STARTF_PREVENTPINNING = 0x00002000
STARTF_UNTRUSTEDSOURCE = 0x00008000
SHUTDOWN_NORETRY = 0x00000001
#
#  Supported process protection levels.
#
PROTECTION_LEVEL_WINTCB_LIGHT = 0x00000000
PROTECTION_LEVEL_WINDOWS = 0x00000001
PROTECTION_LEVEL_WINDOWS_LIGHT = 0x00000002
PROTECTION_LEVEL_ANTIMALWARE_LIGHT = 0x00000003
PROTECTION_LEVEL_LSA_LIGHT = 0x00000004
#
#  The following protection levels are supplied for testing only (no win32
#  callers need these).
#
PROTECTION_LEVEL_WINTCB = 0x00000005
PROTECTION_LEVEL_CODEGEN_LIGHT = 0x00000006
PROTECTION_LEVEL_AUTHENTICODE = 0x00000007
PROTECTION_LEVEL_PPL_APP = 0x00000008
PROTECTION_LEVEL_SAME = 0xFFFFFFFF
#
#  The following is only used as a value for ProtectionLevel
#  when querying ProcessProtectionLevelInfo in GetProcessInformation.
#
PROTECTION_LEVEL_NONE = 0xFFFFFFFE
PROCESS_NAME_NATIVE = 0x00000001
#
#  Extended process and thread attribute support
#
PROC_THREAD_ATTRIBUTE_NUMBER = 0x0000FFFF
PROC_THREAD_ATTRIBUTE_THREAD = 0x00010000  # Attribute may be used with thread creation
PROC_THREAD_ATTRIBUTE_INPUT = 0x00020000  # Attribute is input only
PROC_THREAD_ATTRIBUTE_ADDITIVE = 0x00040000  # Attribute may be "accumulated," e.g. bitmasks, counters, etc.
#
#  Define legacy creation mitigation policy options, which are straight
#  bitmasks.  Bits 0-5 are legacy bits.
#
PROCESS_CREATION_MITIGATION_POLICY_DEP_ENABLE = 0x01
PROCESS_CREATION_MITIGATION_POLICY_DEP_ATL_THUNK_ENABLE = 0x02
PROCESS_CREATION_MITIGATION_POLICY_SEHOP_ENABLE = 0x04
#
#  Define mandatory ASLR options.  Mandatory ASLR forcibly rebases images that
#  are not dynamic base compatible by acting as though there were an image base
#  collision at load time.
#
#  Note that 'require relocations' mode refuses load of images that do not have
#  a base relocation section.
#
PROCESS_CREATION_MITIGATION_POLICY_FORCE_RELOCATE_IMAGES_MASK = 0x00000003  # << 8)
PROCESS_CREATION_MITIGATION_POLICY_FORCE_RELOCATE_IMAGES_DEFER = 0x00000000  # << 8)
PROCESS_CREATION_MITIGATION_POLICY_FORCE_RELOCATE_IMAGES_ALWAYS_ON = 0x00000001  # << 8)
PROCESS_CREATION_MITIGATION_POLICY_FORCE_RELOCATE_IMAGES_ALWAYS_OFF = 0x00000002  # << 8)
PROCESS_CREATION_MITIGATION_POLICY_FORCE_RELOCATE_IMAGES_ALWAYS_ON_REQ_RELOCS = 0x00000003  # << 8)
#
#  Define heap terminate on corruption options.  Note that 'always off' does
#  not override the default opt-in for binaries with current subsystem versions
#  set in the image header.
#
#  Heap terminate on corruption is user mode enforced.
#
PROCESS_CREATION_MITIGATION_POLICY_HEAP_TERMINATE_MASK = 0x00000003  # << 12)
PROCESS_CREATION_MITIGATION_POLICY_HEAP_TERMINATE_DEFER = 0x00000000  # << 12)
PROCESS_CREATION_MITIGATION_POLICY_HEAP_TERMINATE_ALWAYS_ON = 0x00000001  # << 12)
PROCESS_CREATION_MITIGATION_POLICY_HEAP_TERMINATE_ALWAYS_OFF = 0x00000002  # << 12)
PROCESS_CREATION_MITIGATION_POLICY_HEAP_TERMINATE_RESERVED = 0x00000003  # << 12)
#
#  Define bottom up randomization (includes stack randomization) options,
#  i.e. randomization of the lowest user address.
#
PROCESS_CREATION_MITIGATION_POLICY_BOTTOM_UP_ASLR_MASK = 0x00000003  # << 16)
PROCESS_CREATION_MITIGATION_POLICY_BOTTOM_UP_ASLR_DEFER = 0x00000000  # << 16)
PROCESS_CREATION_MITIGATION_POLICY_BOTTOM_UP_ASLR_ALWAYS_ON = 0x00000001  # << 16)
PROCESS_CREATION_MITIGATION_POLICY_BOTTOM_UP_ASLR_ALWAYS_OFF = 0x00000002  # << 16)
PROCESS_CREATION_MITIGATION_POLICY_BOTTOM_UP_ASLR_RESERVED = 0x00000003  # << 16)
#
#  Define high entropy bottom up randomization.  Note that high entropy bottom
#  up randomization is effective if and only if bottom up ASLR is also enabled.
#
#  N.B.  High entropy mode is only meaningful for native 64-bit processes.  in
#        high entropy mode, up to 1TB of bottom up variance is enabled.
#
PROCESS_CREATION_MITIGATION_POLICY_HIGH_ENTROPY_ASLR_MASK = 0x00000003  # << 20)
PROCESS_CREATION_MITIGATION_POLICY_HIGH_ENTROPY_ASLR_DEFER = 0x00000000  # << 20)
PROCESS_CREATION_MITIGATION_POLICY_HIGH_ENTROPY_ASLR_ALWAYS_ON = 0x00000001  # << 20)
PROCESS_CREATION_MITIGATION_POLICY_HIGH_ENTROPY_ASLR_ALWAYS_OFF = 0x00000002  # << 20)
PROCESS_CREATION_MITIGATION_POLICY_HIGH_ENTROPY_ASLR_RESERVED = 0x00000003  # << 20)
#
#  Define handle checking enforcement options.  Handle checking enforcement
#  causes an exception to be raised immediately on a bad handle reference,
#  versus simply returning a failure status from the handle reference.
#
PROCESS_CREATION_MITIGATION_POLICY_STRICT_HANDLE_CHECKS_MASK = 0x00000003  # << 24)
PROCESS_CREATION_MITIGATION_POLICY_STRICT_HANDLE_CHECKS_DEFER = 0x00000000  # << 24)
PROCESS_CREATION_MITIGATION_POLICY_STRICT_HANDLE_CHECKS_ALWAYS_ON = 0x00000001  # << 24)
PROCESS_CREATION_MITIGATION_POLICY_STRICT_HANDLE_CHECKS_ALWAYS_OFF = 0x00000002  # << 24)
PROCESS_CREATION_MITIGATION_POLICY_STRICT_HANDLE_CHECKS_RESERVED = 0x00000003  # << 24)
#
#  Define win32k system call disable options.  Win32k system call disable
#  prevents a process from making Win32k calls.
#
PROCESS_CREATION_MITIGATION_POLICY_WIN32K_SYSTEM_CALL_DISABLE_MASK = 0x00000003  # << 28)
PROCESS_CREATION_MITIGATION_POLICY_WIN32K_SYSTEM_CALL_DISABLE_DEFER = 0x00000000  # << 28)
PROCESS_CREATION_MITIGATION_POLICY_WIN32K_SYSTEM_CALL_DISABLE_ALWAYS_ON = 0x00000001  # << 28)
PROCESS_CREATION_MITIGATION_POLICY_WIN32K_SYSTEM_CALL_DISABLE_ALWAYS_OFF = 0x00000002  # << 28)
PROCESS_CREATION_MITIGATION_POLICY_WIN32K_SYSTEM_CALL_DISABLE_RESERVED = 0x00000003  # << 28)
#
#  Define the extension point disable options.  Extension point disable allows
#  a process to opt-out of loading various arbitrary extension point DLLs.
#
#
#  Define dynamic code options.
#
#
#  Define Control Flow Guard (CFG) mitigation policy options.  Control Flow
#  Guard allows indirect control transfers to be checked at runtime.
#
#
#  Define module signature options.  When enabled, this option will
#  block mapping of non-microsoft binaries.
#
#
#  Define Font Disable Policy.  When enabled, this option will
#  block loading Non System Fonts.
#
#
#  Define remote image load options.  When enabled, this option will
#  block mapping of images from remote devices.
#
#
#  Define low IL image load options.  When enabled, this option will
#  block mapping of images that have the low mandatory label.
#
#
#  Define image load options to prefer System32 images compared to
#  the same images in application directory. When enabled, this option
#  will prefer loading images from system32 folder.
#
#
#  Define Loader Integrity Continuity mitigation policy options.  This mitigation
#  enforces OS signing levels for depenedent module loads.
#
#
#  Define the strict Control Flow Guard (CFG) mitigation policy options. This mitigation
#  requires all images that load in the process to be instrumented by CFG.
#
#
#  Define the module tampering mitigation policy options.
#
#
#  Define Attribute to disable creation of child process
#
PROCESS_CREATION_CHILD_PROCESS_RESTRICTED = 0x01
PROCESS_CREATION_CHILD_PROCESS_OVERRIDE = 0x02
PROCESS_CREATION_CHILD_PROCESS_RESTRICTED_UNLESS_SECURE = 0x04
#
#  Define Attribute to opt out of matching All Application Packages
#
PROCESS_CREATION_ALL_APPLICATION_PACKAGES_OPT_OUT = 0x01
#
#  Define Attribute for Desktop App Override
#
PROCESS_CREATION_DESKTOP_APP_BREAKAWAY_ENABLE_PROCESS_TREE = 0x01
PROCESS_CREATION_DESKTOP_APP_BREAKAWAY_DISABLE_PROCESS_TREE = 0x02
PROCESS_CREATION_DESKTOP_APP_BREAKAWAY_OVERRIDE = 0x04
ATOM_FLAG_GLOBAL = 0x2
#
#  for GetProcAddress
#
#
#  GetProcAddress only accepts GET_SYSTEM_WOW64_DIRECTORY_NAME_A_A,
#  GET_SYSTEM_WOW64_DIRECTORY_NAME_W_A, GET_SYSTEM_WOW64_DIRECTORY_NAME_T_A.
#  The others are if you want to use the strings in some other way.
#
BASE_SEARCH_PATH_ENABLE_SAFE_SEARCHMODE = 0x1
BASE_SEARCH_PATH_DISABLE_SAFE_SEARCHMODE = 0x10000
BASE_SEARCH_PATH_PERMANENT = 0x8000
DDD_RAW_TARGET_PATH = 0x00000001
DDD_REMOVE_DEFINITION = 0x00000002
DDD_EXACT_MATCH_ON_REMOVE = 0x00000004
DDD_NO_BROADCAST_SYSTEM = 0x00000008
DDD_LUID_BROADCAST_DRIVE = 0x00000010
#
#  TODO: Win7 for now, when we roll over the version number this needs to be updated.
#
MOVEFILE_REPLACE_EXISTING = 0x00000001
MOVEFILE_COPY_ALLOWED = 0x00000002
MOVEFILE_DELAY_UNTIL_REBOOT = 0x00000004
MOVEFILE_WRITE_THROUGH = 0x00000008
MOVEFILE_CREATE_HARDLINK = 0x00000010
MOVEFILE_FAIL_IF_NOT_TRACKABLE = 0x00000020
#
#  API call to create hard links.
#
#
#  API call to create hard links.
#
#
#  Event logging APIs
#
EVENTLOG_FULL_INFO = 0
#
#  Operation prefetch API.
#
OPERATION_API_VERSION = 1
#
#  OperationStart() parameters.
#
OPERATION_START_TRACE_CURRENT_THREAD = 0x1
#
#  OperationEnd() parameters.
#
OPERATION_END_DISCARD = 0x1
#
#
#  Security APIs
#
MAX_COMPUTERNAME_LENGTH = 15
# MAX_COMPUTERNAME_LENGTH = 31
#
#  Logon Support APIs
#
LOGON32_LOGON_INTERACTIVE = 2
LOGON32_LOGON_NETWORK = 3
LOGON32_LOGON_BATCH = 4
LOGON32_LOGON_SERVICE = 5
LOGON32_LOGON_UNLOCK = 7
LOGON32_LOGON_NETWORK_CLEARTEXT = 8
LOGON32_LOGON_NEW_CREDENTIALS = 9
LOGON32_PROVIDER_DEFAULT = 0
LOGON32_PROVIDER_WINNT35 = 1
LOGON32_PROVIDER_WINNT40 = 2
LOGON32_PROVIDER_WINNT50 = 3
LOGON32_PROVIDER_VIRTUAL = 4
#
#  LogonFlags
#
LOGON_WITH_PROFILE = 0x00000001
LOGON_NETCREDENTIALS_ONLY = 0x00000002
LOGON_ZERO_PASSWORD_BUFFER = 0x80000000
#
#  Thread pool API's
#
#
#   Private Namespaces support
#
#
#   Boundary descriptors support
#
#
#  Plug-and-Play API's
#
HW_PROFILE_GUIDLEN = 39  # 36-characters plus NULL terminator
MAX_PROFILE_LEN = 80
DOCKINFO_UNDOCKED = 0x1
DOCKINFO_DOCKED = 0x2
DOCKINFO_USER_SUPPLIED = 0x4
DOCKINFO_USER_UNDOCKED = DOCKINFO_USER_SUPPLIED  # | DOCKINFO_UNDOCKED)
DOCKINFO_USER_DOCKED = DOCKINFO_USER_SUPPLIED  # | DOCKINFO_DOCKED)
#  DOS and OS/2 Compatible Error Code definitions returned by the Win32 Base
#  API functions.
#
TC_NORMAL = 0
TC_HARDERR = 1
TC_GP_TRAP = 2
TC_SIGNAL = 3
#
#  Power Management APIs
#
#
#  Power Management APIs
#
AC_LINE_OFFLINE = 0x00
AC_LINE_ONLINE = 0x01
AC_LINE_BACKUP_POWER = 0x02
AC_LINE_UNKNOWN = 0xFF
BATTERY_FLAG_HIGH = 0x01
BATTERY_FLAG_LOW = 0x02
BATTERY_FLAG_CRITICAL = 0x04
BATTERY_FLAG_CHARGING = 0x08
BATTERY_FLAG_NO_BATTERY = 0x80
BATTERY_FLAG_UNKNOWN = 0xFF
BATTERY_PERCENTAGE_UNKNOWN = 0xFF
SYSTEM_STATUS_FLAG_POWER_SAVING_ON = 0x01
BATTERY_LIFE_UNKNOWN = 0xFFFFFFFF
#
#  Very Large Memory API Subset
#
ACTCTX_FLAG_PROCESSOR_ARCHITECTURE_VALID = 0x00000001
ACTCTX_FLAG_LANGID_VALID = 0x00000002
ACTCTX_FLAG_ASSEMBLY_DIRECTORY_VALID = 0x00000004
ACTCTX_FLAG_RESOURCE_NAME_VALID = 0x00000008
ACTCTX_FLAG_SET_PROCESS_DEFAULT = 0x00000010
ACTCTX_FLAG_APPLICATION_NAME_VALID = 0x00000020
ACTCTX_FLAG_SOURCE_IS_ASSEMBLYREF = 0x00000040
ACTCTX_FLAG_HMODULE_VALID = 0x00000080
DEACTIVATE_ACTCTX_FLAG_FORCE_EARLY_DEACTIVATION = 0x00000001
#  2600 stops here
FIND_ACTCTX_SECTION_KEY_RETURN_HACTCTX = 0x00000001
FIND_ACTCTX_SECTION_KEY_RETURN_FLAGS = 0x00000002
FIND_ACTCTX_SECTION_KEY_RETURN_ASSEMBLY_METADATA = 0x00000004
ACTIVATION_CONTEXT_BASIC_INFORMATION_DEFINED = 1
QUERY_ACTCTX_FLAG_USE_ACTIVE_ACTCTX = 0x00000004
QUERY_ACTCTX_FLAG_ACTCTX_IS_HMODULE = 0x00000008
QUERY_ACTCTX_FLAG_ACTCTX_IS_ADDRESS = 0x00000010
QUERY_ACTCTX_FLAG_NO_ADDREF = 0x80000000
#
#  switch (ulInfoClass)
#
#   case ActivationContextBasicInformation:
#     pvSubInstance == NULL
#     pvBuffer is of type PACTIVATION_CONTEXT_BASIC_INFORMATION
#
#   case ActivationContextDetailedInformation:
#     pvSubInstance == NULL
#     pvBuffer is of type PACTIVATION_CONTEXT_DETAILED_INFORMATION
#
#   case AssemblyDetailedInformationInActivationContext:
#     pvSubInstance is of type PULONG
#       *pvSubInstance < ACTIVATION_CONTEXT_DETAILED_INFORMATION::ulAssemblyCount
#     pvBuffer is of type PACTIVATION_CONTEXT_ASSEMBLY_DETAILED_INFORMATION
#
#   case FileInformationInAssemblyOfAssemblyInActivationContext:
#     pvSubInstance is of type PACTIVATION_CONTEXT_QUERY_INDEX
#       pvSubInstance->ulAssemblyIndex < ACTIVATION_CONTEXT_DETAILED_INFORMATION::ulAssemblyCount
#       pvSubInstance->ulFileIndexInAssembly < ACTIVATION_CONTEXT_ASSEMBLY_DETAILED_INFORMATION::ulFileCount
#     pvBuffer is of type PASSEMBLY_FILE_DETAILED_INFORMATION
#
#   case RunlevelInformationInActivationContext :
#     pvSubInstance == NULL
#     pvBuffer is of type PACTIVATION_CONTEXT_RUN_LEVEL_INFORMATION
#
#  String are placed after the structs.
#
#
#  NUMA Information routines.
#
#
#  Application restart and data recovery callback
#
#
#  Max length of commandline in characters (including the NULL character that can be registered for restart)
#
RESTART_MAX_CMD_LINE = 1024
#
#  Do not restart the process for termination due to application crashes
#
RESTART_NO_CRASH = 1
#
#  Do not restart the process for termination due to application hangs
#
RESTART_NO_HANG = 2
#
#  Do not restart the process for termination due to patch installations
#
RESTART_NO_PATCH = 4
#
#  Do not restart the process when the system is rebooted due to patch installations
#
RESTART_NO_REBOOT = 8
RECOVERY_DEFAULT_PING_INTERVAL = 5000
RECOVERY_MAX_PING_INTERVAL = 5  # * 60 * 1000)
FILE_RENAME_FLAG_REPLACE_IF_EXISTS = 0x00000001
FILE_RENAME_FLAG_POSIX_SEMANTICS = 0x00000002
FILE_RENAME_FLAG_SUPPRESS_PIN_STATE_INHERITANCE = 0x00000004
FILE_DISPOSITION_FLAG_DO_NOT_DELETE = 0x00000000
FILE_DISPOSITION_FLAG_DELETE = 0x00000001
FILE_DISPOSITION_FLAG_POSIX_SEMANTICS = 0x00000002
FILE_DISPOSITION_FLAG_FORCE_IMAGE_SECTION_CHECK = 0x00000004
FILE_DISPOSITION_FLAG_ON_CLOSE = 0x00000008
#  Structure and constants must match those in ntioapi_x.w
#
#   Flag definitions for FILE_STORAGE_INFO structure
#
#
#   If this flag is set then the partition is correctly aligned with the
#   physical sector size of the device for optimial performance.
#
STORAGE_INFO_FLAGS_ALIGNED_DEVICE = 0x00000001
STORAGE_INFO_FLAGS_PARTITION_ALIGNED_ON_DEVICE = 0x00000002
#
#   If this value is set for the Sector and Parition alignment
#   fields then it means the alignment is not known and the
#   alignment flags have no meaning
#
STORAGE_INFO_OFFSET_UNKNOWN = 0xffffffff
#
#   Structure definition for FileIdInfo
#
#
#   Structure definition for FileIdExtdDirectoryInfo
#
#
#  File Remote protocol info (FileRemoteProtocolInfo)
#
#  Protocol generic flags.
REMOTE_PROTOCOL_INFO_FLAG_LOOPBACK = 0x00000001
REMOTE_PROTOCOL_INFO_FLAG_OFFLINE = 0x00000002
REMOTE_PROTOCOL_INFO_FLAG_PERSISTENT_HANDLE = 0x00000004
#  Protocol specific SMB2 share capability flags.
RPI_FLAG_SMB2_SHARECAP_TIMEWARP = 0x00000002
RPI_FLAG_SMB2_SHARECAP_DFS = 0x00000008
RPI_FLAG_SMB2_SHARECAP_CONTINUOUS_AVAILABILITY = 0x00000010
RPI_FLAG_SMB2_SHARECAP_SCALEOUT = 0x00000020
RPI_FLAG_SMB2_SHARECAP_CLUSTER = 0x00000040
#  Protocol specific SMB2 server capability flags.
RPI_SMB2_FLAG_SERVERCAP_DFS = 0x00000001
RPI_SMB2_FLAG_SERVERCAP_LEASING = 0x00000002
RPI_SMB2_FLAG_SERVERCAP_LARGEMTU = 0x00000004
RPI_SMB2_FLAG_SERVERCAP_MULTICHANNEL = 0x00000008
RPI_SMB2_FLAG_SERVERCAP_PERSISTENT_HANDLES = 0x00000010
RPI_SMB2_FLAG_SERVERCAP_DIRECTORY_LEASING = 0x00000020
#
#   Flag values for the dwFlags parameter of the CreateSymbolicLink API
#
#   Request to create a directory symbolic link
SYMBOLIC_LINK_FLAG_DIRECTORY = 0x1
#   Specify this flag if you want to allow creation of symbolic links when the
#   process is not elevated.  As of now enabling DEVELOPER MODE on a system
#   is the only scenario that allow unprivileged symlink creation. There may
#   be future scenarios that this flag will enable in the future.
#
#   Also be aware that the behavior of this API with this flag set will likely
#   be different between a development environment and an and customers
#   environment so please be careful with the usage of this flag.
SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE = 0x2
#  ARM64_WORKAROUND : should this work for managed code?
#  ARM64_WORKAROUND : should this work for managed code?
MICROSOFT_WINBASE_H_DEFINE_INTERLOCKED_CPLUSPLUS_OVERLOADS = 0