import ctypes

from winapi.common.datatypes import LPCWSTR, DWORD, POINTER, HANDLE, BOOL, UINT, LPVOID, INT, LPSTR, LPBOOL
from winapi.kernel32.datatypes import LPCWCH, LPCCH, HGLOBAL
from winapi.kernel32.structs import *

__all__ = [
    'GlobalAlloc', 'GetSystemTime', 'CreateFile', 'GetLocalTime', 'CloseHandle', 'SystemTimeToFileTime', 'LockFile',
    'FileTimeToLocalFileTime', 'FileTimeToSystemTime', 'WideCharToMultiByte', 'GlobalLock', 'GlobalUnlock',
    'SystemTimeToTzSpecificLocalTime', 'GetFileInformationByHandle'
]

kernel32 = ctypes.windll.kernel32
SIZE_T = ctypes.c_size_t
void = None
VOID = void


class CreateFile(object):
    """
    CreateFileW function
    ====================

    -description
    ------------

    Creates or opens a file or I/O device. The most commonly used I/O
    devices are as follows: file, file stream, directory, physical disk,
    volume, console buffer, tape drive, communications resource, mailslot,
    and pipe. The function returns a handle that can be used to access the
    file or device for various types of I/O depending on the file or device
    and the flags and attributes specified.

    To perform this operation as a transacted operation, which results in a
    handle that can be used for transacted I/O, use the CreateFileTransacted
    function.

    -parameters
    -----------

    -param lpFileName [in]
    ~~~~~~~~~~~~~~~~~~~~~~

    The name of the file or device to be created or opened. You may use
    either forward slashes (/) or backslashes (\) in this name.

    In the ANSI version of this function, the name is limited to MAX_PATH
    characters. To extend this limit to 32,767 wide characters, use this
    Unicode version of the function and prepend â€œ\\\?\\â€ to the path. For
    more information, see Naming Files, Paths, and Namespaces.

    For information on special device names, see Defining an MS-DOS Device
    Name.

    To create a file stream, specify the name of the file, a colon, and then
    the name of the stream. For more information, see File Streams.

    .. container:: alert

       Tip Starting with Windows 10, version 1607, for the unicode version
       of this function (CreateFileW), you can opt-in to remove the MAX_PATH
       limitation without prepending â€œ\\?". See theâ€Maximum Path Length
       Limitation" section of Naming Files, Paths, and Namespaces for
       details.

    .. container::

    -param dwDesiredAccess [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The requested access to the file or device, which can be summarized as
    read, write, both or neither zero).

    The most commonly used values are GENERIC_READ, GENERIC_WRITE, or both
    (GENERIC_READ \| GENERIC_WRITE). For more information, see Generic
    Access Rights, File Security and Access Rights, File Access Rights
    Constants, and ACCESS_MASK.

    If this parameter is zero, the application can query certain metadata
    such as file, directory, or device attributes without accessing that
    file or device, even if GENERIC_READ access would have been denied.

    You cannot request an access mode that conflicts with the sharing mode
    that is specified by the dwShareMode parameter in an open request that
    already has an open handle.

    For more information, see the Remarks section of this topic and Creating
    and Opening Files.

    -param dwShareMode [in]
    ~~~~~~~~~~~~~~~~~~~~~~~

    The requested sharing mode of the file or device, which can be read,
    write, both, delete, all of these, or none (refer to the following
    table). Access requests to attributes or extended attributes are not
    affected by this flag.

    If this parameter is zero and CreateFile succeeds, the file or device
    cannot be shared and cannot be opened again until the handle to the file
    or device is closed. For more information, see the Remarks section.

    You cannot request a sharing mode that conflicts with the access mode
    that is specified in an existing request that has an open handle.
    CreateFile would fail and the GetLastError function would return
    ERROR_SHARING_VIOLATION.

    To enable a process to share a file or device while another process has
    the file or device open, use a compatible combination of one or more of
    the following values. For more information about valid combinations of
    this parameter with the dwDesiredAccess parameter, see Creating and
    Opening Files.

    .. container:: alert

       Note The sharing options for each open handle remain in effect until
       that handle is closed, regardless of process context.

    .. container::

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

    0

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x00000000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Prevents other processes from opening a file or device if they request
    delete, read, or write access.

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

    FILE_SHARE_DELETE

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x00000004

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Enables subsequent open operations on a file or device to request delete
    access.

    Otherwise, other processes cannot open the file or device if they
    request delete access.

    If this flag is not specified, but the file or device has been opened
    for delete access, the function fails.

    .. container:: alert

       Note Delete access allows both delete and rename operations.

    .. container::

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

    FILE_SHARE_READ

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x00000001

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Enables subsequent open operations on a file or device to request read
    access.

    Otherwise, other processes cannot open the file or device if they
    request read access.

    If this flag is not specified, but the file or device has been opened
    for read access, the function fails.

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

    FILE_SHARE_WRITE

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x00000002

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Enables subsequent open operations on a file or device to request write
    access.

    Otherwise, other processes cannot open the file or device if they
    request write access.

    If this flag is not specified, but the file or device has been opened
    for write access or has a file mapping with write access, the function
    fails.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -param lpSecurityAttributes [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a SECURITY_ATTRIBUTES structure that contains two separate
    but related data members: an optional security descriptor, and a Boolean
    value that determines whether the returned handle can be inherited by
    child processes.

    This parameter can be NULL.

    If this parameter is NULL, the handle returned by CreateFile cannot be
    inherited by any child processes the application may create and the file
    or device associated with the returned handle gets a default security
    descriptor.

    The lpSecurityDescriptor member of the structure specifies a
    SECURITY_DESCRIPTOR for a file or device. If this member is NULL, the
    file or device associated with the returned handle is assigned a default
    security descriptor.

    CreateFile ignores the lpSecurityDescriptor member when opening an
    existing file or device, but continues to use the bInheritHandle member.

    The bInheritHandlemember of the structure specifies whether the returned
    handle can be inherited.

    For more information, see the Remarks section.

    -param dwCreationDisposition [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    An action to take on a file or device that exists or does not exist.

    For devices other than files, this parameter is usually set to
    OPEN_EXISTING.

    For more information, see the Remarks section.

    This parameter must be one of the following values, which cannot be
    combined:

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

    CREATE_ALWAYS

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    2

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Creates a new file, always.

    If the specified file exists and is writable, the function overwrites
    the file, the function succeeds, and last-error code is set to
    ERROR_ALREADY_EXISTS (183).

    If the specified file does not exist and is a valid path, a new file is
    created, the function succeeds, and the last-error code is set to zero.

    For more information, see the Remarks section of this topic.

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

    CREATE_NEW

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    1

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Creates a new file, only if it does not already exist.

    If the specified file exists, the function fails and the last-error code
    is set to ERROR_FILE_EXISTS (80).

    If the specified file does not exist and is a valid path to a writable
    location, a new file is created.

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

    OPEN_ALWAYS

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    4

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Opens a file, always.

    If the specified file exists, the function succeeds and the last-error
    code is set to ERROR_ALREADY_EXISTS (183).

    If the specified file does not exist and is a valid path to a writable
    location, the function creates a file and the last-error code is set to
    zero.

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

    OPEN_EXISTING

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    3

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Opens a file or device, only if it exists.

    If the specified file or device does not exist, the function fails and
    the last-error code is set to ERROR_FILE_NOT_FOUND (2).

    For more information about devices, see the Remarks section.

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

    TRUNCATE_EXISTING

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    5

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Opens a file and truncates it so that its size is zero bytes, only if it
    exists.

    If the specified file does not exist, the function fails and the
    last-error code is set to ERROR_FILE_NOT_FOUND (2).

    The calling process must open the file with the GENERIC_WRITE bit set as
    part of the dwDesiredAccess parameter.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -param dwFlagsAndAttributes [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The file or device attributes and flags, FILE_ATTRIBUTE_NORMAL being the
    most common default value for files.

    This parameter can include any combination of the available file
    attributes (FILE_ATTRIBUTE_\*). All other file attributes override
    FILE_ATTRIBUTE_NORMAL.

    This parameter can also contain combinations of flags (FILE_FLAG\_\ *)
    for control of file or device caching behavior, access modes, and other
    special-purpose flags. These combine with any FILE_ATTRIBUTE\_*\
    values.

    This parameter can also contain Security Quality of Service (SQOS)
    information by specifying the SECURITY_SQOS_PRESENT flag. Additional
    SQOS-related flags information is presented in the table following the
    attributes and flags tables.

    .. container:: alert

       Note When CreateFile opens an existing file, it generally combines
       the file flags with the file attributes of the existing file, and
       ignores any file attributes supplied as part of dwFlagsAndAttributes.
       Special cases are detailed in Creating and Opening Files.

    .. container::

    Some of the following file attributes and flags may only apply to files
    and not necessarily all other types of devices that CreateFile can open.
    For additional information, see the Remarks section of this topic and
    Creating and Opening Files.

    For more advanced access to file attributes, see SetFileAttributes. For
    a complete list of all file attributes with their values and
    descriptions, see File Attribute Constants.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    Attribute

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

    FILE_ATTRIBUTE_ARCHIVE

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    32 (0x20)

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file should be archived. Applications use this attribute to mark
    files for backup or removal.

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

    FILE_ATTRIBUTE_ENCRYPTED

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    16384 (0x4000)

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file or directory is encrypted. For a file, this means that all data
    in the file is encrypted. For a directory, this means that encryption is
    the default for newly created files and subdirectories. For more
    information, see File Encryption.

    This flag has no effect if FILE_ATTRIBUTE_SYSTEM is also specified.

    This flag is not supported on Home, Home Premium, Starter, or ARM
    editions of Windows.

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

    FILE_ATTRIBUTE_HIDDEN

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    2 (0x2)

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file is hidden. Do not include it in an ordinary directory listing.

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

    FILE_ATTRIBUTE_NORMAL

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    128 (0x80)

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file does not have other attributes set. This attribute is valid
    only if used alone.

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

    FILE_ATTRIBUTE_OFFLINE

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    4096 (0x1000)

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The data of a file is not immediately available. This attribute
    indicates that file data is physically moved to offline storage. This
    attribute is used by Remote Storage, the hierarchical storage management
    software. Applications should not arbitrarily change this attribute.

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

    FILE_ATTRIBUTE_READONLY

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    1 (0x1)

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file is read only. Applications can read the file, but cannot write
    to or delete it.

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

    FILE_ATTRIBUTE_SYSTEM

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    4 (0x4)

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file is part of or used exclusively by an operating system.

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

    FILE_ATTRIBUTE_TEMPORARY

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    256 (0x100)

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file is being used for temporary storage.

    For more information, see the Caching Behavior section of this topic.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    Flag

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

    FILE_FLAG_BACKUP_SEMANTICS

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x02000000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file is being opened or created for a backup or restore operation.
    The system ensures that the calling process overrides file security
    checks when the process has SE_BACKUP_NAME and SE_RESTORE_NAME
    privileges. For more information, see Changing Privileges in a Token.

    You must set this flag to obtain a handle to a directory. A directory
    handle can be passed to some functions instead of a file handle. For
    more information, see the Remarks section.

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

    FILE_FLAG_DELETE_ON_CLOSE

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x04000000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file is to be deleted immediately after all of its handles are
    closed, which includes the specified handle and any other open or
    duplicated handles.

    If there are existing open handles to a file, the call fails unless they
    were all opened with the FILE_SHARE_DELETE share mode.

    Subsequent open requests for the file fail, unless the FILE_SHARE_DELETE
    share mode is specified.

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

    FILE_FLAG_NO_BUFFERING

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x20000000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file or device is being opened with no system caching for data reads
    and writes. This flag does not affect hard disk caching or memory mapped
    files.

    There are strict requirements for successfully working with files opened
    with CreateFile using the FILE_FLAG_NO_BUFFERING flag, for details see
    File Buffering.

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

    FILE_FLAG_OPEN_NO_RECALL

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x00100000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file data is requested, but it should continue to be located in
    remote storage. It should not be transported back to local storage. This
    flag is for use by remote storage systems.

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

    FILE_FLAG_OPEN_REPARSE_POINT

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x00200000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Normal reparse point processing will not occur; CreateFile will attempt
    to open the reparse point. When a file is opened, a file handle is
    returned, whether or not the filter that controls the reparse point is
    operational.

    This flag cannot be used with the CREATE_ALWAYS flag.

    If the file is not a reparse point, then this flag is ignored.

    For more information, see the Remarks section.

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

    FILE_FLAG_OVERLAPPED

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x40000000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file or device is being opened or created for asynchronous I/O.

    When subsequent I/O operations are completed on this handle, the event
    specified in the OVERLAPPED structure will be set to the signaled state.

    If this flag is specified, the file can be used for simultaneous read
    and write operations.

    If this flag is not specified, then I/O operations are serialized, even
    if the calls to the read and write functions specify an OVERLAPPED
    structure.

    For information about considerations when using a file handle created
    with this flag, see the Synchronous and Asynchronous I/O Handles section
    of this topic.

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

    FILE_FLAG_POSIX_SEMANTICS

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x01000000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Access will occur according to POSIX rules. This includes allowing
    multiple files with names, differing only in case, for file systems that
    support that naming. Use care when using this option, because files
    created with this flag may not be accessible by applications that are
    written for MS-DOS or 16-bit Windows.

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

    FILE_FLAG_RANDOM_ACCESS

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x10000000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Access is intended to be random. The system can use this as a hint to
    optimize file caching.

    This flag has no effect if the file system does not support cached I/O
    and FILE_FLAG_NO_BUFFERING.

    For more information, see the Caching Behavior section of this topic.

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

    FILE_FLAG_SESSION_AWARE

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x00800000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The file or device is being opened with session awareness. If this flag
    is not specified, then per-session devices (such as a device using
    RemoteFX USB Redirection) cannot be opened by processes running in
    session 0. This flag has no effect for callers not in session 0. This
    flag is supported only on server editions of Windows.

    Windows Server 2008 R2 and Windows Server 2008: This flag is not
    supported before Windows Server 2012.

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

    FILE_FLAG_SEQUENTIAL_SCAN

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x08000000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Access is intended to be sequential from beginning to end. The system
    can use this as a hint to optimize file caching.

    This flag should not be used if read-behind (that is, reverse scans)
    will be used.

    This flag has no effect if the file system does not support cached I/O
    and FILE_FLAG_NO_BUFFERING.

    For more information, see the Caching Behavior section of this topic.

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

    FILE_FLAG_WRITE_THROUGH

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x80000000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Write operations will not go through any intermediate cache, they will
    go directly to disk.

    For additional information, see the Caching Behavior section of this
    topic.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    The dwFlagsAndAttributes parameter can also specify SQOS information.
    For more information, see Impersonation Levels. When the calling
    application specifies the SECURITY_SQOS_PRESENT flag as part of
    dwFlagsAndAttributes, it can also contain one or more of the following
    values.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    Security flag

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

    SECURITY_ANONYMOUS

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Impersonates a client at the Anonymous impersonation level.

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

    SECURITY_CONTEXT_TRACKING

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The security tracking mode is dynamic. If this flag is not specified,
    the security tracking mode is static.

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

    SECURITY_DELEGATION

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Impersonates a client at the Delegation impersonation level.

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

    SECURITY_EFFECTIVE_ONLY

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Only the enabled aspects of the clientâ€™s security context are available
    to the server. If you do not specify this flag, all aspects of the
    clientâ€™s security context are available.

    This allows the client to limit the groups and privileges that a server
    can use while impersonating the client.

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

    SECURITY_IDENTIFICATION

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Impersonates a client at the Identification impersonation level.

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

    SECURITY_IMPERSONATION

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Impersonate a client at the impersonation level. This is the default
    behavior if no other flags are specified along with the
    SECURITY_SQOS_PRESENT flag.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -param hTemplateFile [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A valid handle to a template file with the GENERIC_READ access right.
    The template file supplies file attributes and extended attributes for
    the file that is being created.

    This parameter can be NULL.

    When opening an existing file, CreateFile ignores this parameter.

    When opening a new encrypted file, the file inherits the discretionary
    access control list from its parent directory. For additional
    information, see File Encryption.

    -returns
    --------

    If the function succeeds, the return value is an open handle to the
    specified file, device, named pipe, or mail slot.

    If the function fails, the return value is INVALID_HANDLE_VALUE. To get
    extended error information, call GetLastError.

    -remarks
    --------

    CreateFile was originally developed specifically for file interaction
    but has since been expanded and enhanced to include most other types of
    I/O devices and mechanisms available to Windows developers. This section
    attempts to cover the varied issues developers may experience when using
    CreateFile in different contexts and with different I/O types. The text
    attempts to use the word file only when referring specifically to data
    stored in an actual file on a file system. However, some uses of file
    may be referring more generally to an I/O object that supports file-like
    mechanisms. This liberal use of the term file is particularly prevalent
    in constant names and parameter names because of the previously
    mentioned historical reasons.

    When an application is finished using the object handle returned by
    CreateFile, use the CloseHandle function to close the handle. This not
    only frees up system resources, but can have wider influence on things
    like sharing the file or device and committing data to disk. Specifics
    are noted within this topic as appropriate.

    Windows Server 2003 and Windows XP: A sharing violation occurs if an
    attempt is made to open a file or directory for deletion on a remote
    computer when the value of the dwDesiredAccess parameter is the DELETE
    access flag (0x00010000) ORâ€™ed with any other access flag, and the
    remote file or directory has not been opened with FILE_SHARE_DELETE. To
    avoid the sharing violation in this scenario, open the remote file or
    directory with the DELETE access right only, or call DeleteFile without
    first opening the file or directory for deletion.

    Some file systems, such as the NTFS file system, support compression or
    encryption for individual files and directories. On volumes that have a
    mounted file system with this support, a new file inherits the
    compression and encryption attributes of its directory.

    You cannot use CreateFile to control compression, decompression, or
    decryption on a file or directory. For more information, see Creating
    and Opening Files, File Compression and Decompression, and File
    Encryption.

    Windows Server 2003 and Windows XP: For backward compatibility purposes,
    CreateFile does not apply inheritance rules when you specify a security
    descriptor in lpSecurityAttributes. To support inheritance, functions
    that later query the security descriptor of this file may heuristically
    determine and report that inheritance is in effect. For more
    information, see Automatic Propagation of Inheritable ACEs.

    As stated previously, if the lpSecurityAttributes parameter is NULL, the
    handle returned by CreateFile cannot be inherited by any child processes
    your application may create. The following information regarding this
    parameter also applies:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    If the bInheritHandle member variable is not FALSE, which is any nonzero
    value, then the handle can be inherited. Therefore it is critical this
    structure member be properly initialized to FALSE if you do not intend
    the handle to be inheritable.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    The access control lists (ACL) in the default security descriptor for a
    file or directory are inherited from its parent directory.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    The target file system must support security on files and directories
    for the lpSecurityDescriptor member to have an effect on them, which can
    be determined by using GetVolumeInformation.

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    In Windows 8 and Windows Server 2012, this function is supported by the
    following technologies.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    Technology

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    Supported

    .. raw:: html

       </th>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    Server Message Block (SMB) 3.0 protocol

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    SMB 3.0 Transparent Failover (TFO)

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    See remarks

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    SMB 3.0 with Scale-out File Shares (SO)

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    See remarks

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    Cluster Shared Volume File System (CsvFS)

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    Resilient File System (ReFS)

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    Note that CreateFile with supersede disposition will fail if performed
    on a file where there is already an open alternate data stream.

    .. raw:: html

       <h3>

    Symbolic Link Behavior

    .. raw:: html

       </h3>

    If the call to this function creates a file, there is no change in
    behavior. Also, consider the following information regarding
    FILE_FLAG_OPEN_REPARSE_POINT:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    If FILE_FLAG_OPEN_REPARSE_POINT is specified:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    If an existing file is opened and it is a symbolic link, the handle
    returned is a handle to the symbolic link.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    If TRUNCATE_EXISTING or FILE_FLAG_DELETE_ON_CLOSE are specified, the
    file affected is a symbolic link.

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    If FILE_FLAG_OPEN_REPARSE_POINT is not specified:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    If an existing file is opened and it is a symbolic link, the handle
    returned is a handle to the target.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    If CREATE_ALWAYS, TRUNCATE_EXISTING, or FILE_FLAG_DELETE_ON_CLOSE are
    specified, the file affected is the target.

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    .. raw:: html

       <h3>

    Caching Behavior

    .. raw:: html

       </h3>

    Several of the possible values for the dwFlagsAndAttributes parameter
    are used by CreateFile to control or affect how the data associated with
    the handle is cached by the system. They are:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    FILE_FLAG_NO_BUFFERING

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    FILE_FLAG_RANDOM_ACCESS

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    FILE_FLAG_SEQUENTIAL_SCAN

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    FILE_FLAG_WRITE_THROUGH

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    FILE_ATTRIBUTE_TEMPORARY

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    If none of these flags is specified, the system uses a default
    general-purpose caching scheme. Otherwise, the system caching behaves as
    specified for each flag.

    Some of these flags should not be combined. For instance, combining
    FILE_FLAG_RANDOM_ACCESS with FILE_FLAG_SEQUENTIAL_SCAN is
    self-defeating.

    Specifying the FILE_FLAG_SEQUENTIAL_SCAN flag can increase performance
    for applications that read large files using sequential access.
    Performance gains can be even more noticeable for applications that read
    large files mostly sequentially, but occasionally skip forward over
    small ranges of bytes. If an application moves the file pointer for
    random access, optimum caching performance most likely will not occur.
    However, correct operation is still guaranteed.

    The flags FILE_FLAG_WRITE_THROUGH and FILE_FLAG_NO_BUFFERING are
    independent and may be combined.

    If FILE_FLAG_WRITE_THROUGH is used but FILE_FLAG_NO_BUFFERING is not
    also specified, so that system caching is in effect, then the data is
    written to the system cache but is flushed to disk without delay.

    If FILE_FLAG_WRITE_THROUGH and FILE_FLAG_NO_BUFFERING are both
    specified, so that system caching is not in effect, then the data is
    immediately flushed to disk without going through the Windows system
    cache. The operating system also requests a write-through of the hard
    diskâ€™s local hardware cache to persistent media.

    .. container:: alert

       Note Not all hard disk hardware supports this write-through
       capability.

    .. container::

    Proper use of the FILE_FLAG_NO_BUFFERING flag requires special
    application considerations. For more information, see File Buffering.

    A write-through request via FILE_FLAG_WRITE_THROUGH also causes NTFS to
    flush any metadata changes, such as a time stamp update or a rename
    operation, that result from processing the request. For this reason, the
    FILE_FLAG_WRITE_THROUGH flag is often used with the
    FILE_FLAG_NO_BUFFERING flag as a replacement for calling the
    FlushFileBuffers function after each write, which can cause unnecessary
    performance penalties. Using these flags together avoids those
    penalties. For general information about the caching of files and
    metadata, see File Caching.

    When FILE_FLAG_NO_BUFFERING is combined with FILE_FLAG_OVERLAPPED, the
    flags give maximum asynchronous performance, because the I/O does not
    rely on the synchronous operations of the memory manager. However, some
    I/O operations take more time, because data is not being held in the
    cache. Also, the file metadata may still be cached (for example, when
    creating an empty file). To ensure that the metadata is flushed to disk,
    use the FlushFileBuffers function.

    Specifying the FILE_ATTRIBUTE_TEMPORARY attribute causes file systems to
    avoid writing data back to mass storage if sufficient cache memory is
    available, because an application deletes a temporary file after a
    handle is closed. In that case, the system can entirely avoid writing
    the data. Although it does not directly control data caching in the same
    way as the previously mentioned flags, the FILE_ATTRIBUTE_TEMPORARY
    attribute does tell the system to hold as much as possible in the system
    cache without writing and therefore may be of concern for certain
    applications.

    .. raw:: html

       <h3>

    Files

    .. raw:: html

       </h3>

    If you rename or delete a file and then restore it shortly afterward,
    the system searches the cache for file information to restore. Cached
    information includes its short/long name pair and creation time.

    If you call CreateFile on a file that is pending deletion as a result of
    a previous call to DeleteFile, the function fails. The operating system
    delays file deletion until all handles to the file are closed.
    GetLastError returns ERROR_ACCESS_DENIED.

    The dwDesiredAccess parameter can be zero, allowing the application to
    query file attributes without accessing the file if the application is
    running with adequate security settings. This is useful to test for the
    existence of a file without opening it for read and/or write access, or
    to obtain other statistics about the file or directory. See Obtaining
    and Setting File Information and GetFileInformationByHandle.

    If CREATE_ALWAYS and FILE_ATTRIBUTE_NORMAL are specified, CreateFile
    fails and sets the last error to ERROR_ACCESS_DENIED if the file exists
    and has the FILE_ATTRIBUTE_HIDDEN or FILE_ATTRIBUTE_SYSTEM attribute. To
    avoid the error, specify the same attributes as the existing file.

    When an application creates a file across a network, it is better to use
    GENERIC_READ \| GENERIC_WRITE for dwDesiredAccess than to use
    GENERIC_WRITE alone. The resulting code is faster, because the
    redirector can use the cache manager and send fewer SMBs with more data.
    This combination also avoids an issue where writing to a file across a
    network can occasionally return ERROR_ACCESS_DENIED.

    For more information, see Creating and Opening Files.

    .. raw:: html

       <h3>

    Synchronous and Asynchronous I/O Handles

    .. raw:: html

       </h3>

    CreateFile provides for creating a file or device handle that is either
    synchronous or asynchronous. A synchronous handle behaves such that I/O
    function calls using that handle are blocked until they complete, while
    an asynchronous file handle makes it possible for the system to return
    immediately from I/O function calls, whether they completed the I/O
    operation or not. As stated previously, this synchronous versus
    asynchronous behavior is determined by specifying FILE_FLAG_OVERLAPPED
    within the dwFlagsAndAttributes parameter. There are several
    complexities and potential pitfalls when using asynchronous I/O; for
    more information, see Synchronous and Asynchronous I/O.

    .. raw:: html

       <h3>

    File Streams

    .. raw:: html

       </h3>

    On NTFS file systems, you can use CreateFile to create separate streams
    within a file. For more information, see File Streams.

    .. raw:: html

       <h3>

    Directories

    .. raw:: html

       </h3>

    An application cannot create a directory by using CreateFile, therefore
    only the OPEN_EXISTING value is valid for dwCreationDisposition for this
    use case. To create a directory, the application must call
    CreateDirectory or CreateDirectoryEx.

    To open a directory using CreateFile, specify the
    FILE_FLAG_BACKUP_SEMANTICS flag as part of dwFlagsAndAttributes.
    Appropriate security checks still apply when this flag is used without
    SE_BACKUP_NAME and SE_RESTORE_NAME privileges.

    When using CreateFile to open a directory during defragmentation of a
    FAT or FAT32 file system volume, do not specify the MAXIMUM_ALLOWED
    access right. Access to the directory is denied if this is done. Specify
    the GENERIC_READ access right instead.

    For more information, see About Directory Management.

    .. raw:: html

       <h3>

    Physical Disks and Volumes

    .. raw:: html

       </h3>

    Direct access to the disk or to a volume is restricted. For more
    information, see â€œChanges to the file system and to the storage stack to
    restrict direct disk access and direct volume access in Windows Vista
    and in Windows Server 2008â€ in the Help and Support Knowledge Base at
    http://support.microsoft.com/kb/942448.

    Windows Server 2003 and Windows XP: Direct access to the disk or to a
    volume is not restricted in this manner.

    You can use the CreateFile function to open a physical disk drive or a
    volume, which returns a direct access storage device (DASD) handle that
    can be used with the DeviceIoControl function. This enables you to
    access the disk or volume directly, for example such disk metadata as
    the partition table. However, this type of access also exposes the disk
    drive or volume to potential data loss, because an incorrect write to a
    disk using this mechanism could make its contents inaccessible to the
    operating system. To ensure data integrity, be sure to become familiar
    with DeviceIoControl and how other APIs behave differently with a direct
    access handle as opposed to a file system handle.

    The following requirements must be met for such a call to succeed:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    The caller must have administrative privileges. For more information,
    see Running with Special Privileges.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    The dwCreationDisposition parameter must have the OPEN_EXISTINGflag.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    When opening a volume or floppy disk, the dwShareMode parameter must
    have the FILE_SHARE_WRITEflag.

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    .. container:: alert

       Note The dwDesiredAccess parameter can be zero, allowing the
       application to query device attributes without accessing a device.
       This is useful for an application to determine the size of a floppy
       disk drive and the formats it supports without requiring a floppy
       disk in a drive, for instance. It can also be used for reading
       statistics without requiring higher-level data read/write permission.

    .. container::

    When opening a physical drive x:, the lpFileName string should be the
    following form: â€œ\\.:raw-latex:`\PhysicalDrive`Xâ€. Hard disk numbers
    start at zero. The following table shows some examples of physical drive
    strings.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    String

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

       <td>

    â€œ\\.:raw-latex:`\PhysicalDrive0`â€

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Opens the first physical drive.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    â€œ\\.:raw-latex:`\PhysicalDrive2`â€

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Opens the third physical drive.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    To obtain the physical drive identifier for a volume, open a handle to
    the volume and call the DeviceIoControl function with
    IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS. This control code returns the disk
    number and offset for each of the volumeâ€™s one or more extents; a volume
    can span multiple physical disks.

    For an example of opening a physical drive, see Calling DeviceIoControl.

    When opening a volume or removable media drive (for example, a floppy
    disk drive or flash memory thumb drive), the lpFileName string should be
    the following form: â€œ\\.\\X:â€. Do not use a trailing backslash (), which
    indicates the root directory of a drive. The following table shows some
    examples of drive strings.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    String

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

       <td>

    â€œ\\.:raw-latex:`\A`:â€

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Opens floppy disk drive A.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    â€œ\\.:raw-latex:`\C`:â€

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Opens the C: volume.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    "\.:raw-latex:`\C`:"

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Opens the file system of the C: volume.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    You can also open a volume by referring to its volume name. For more
    information, see Naming a Volume.

    A volume contains one or more mounted file systems. Volume handles can
    be opened as noncached at the discretion of the particular file system,
    even when the noncached option is not specified in CreateFile. You
    should assume that all Microsoft file systems open volume handles as
    noncached. The restrictions on noncached I/O for files also apply to
    volumes.

    A file system may or may not require buffer alignment even though the
    data is noncached. However, if the noncached option is specified when
    opening a volume, buffer alignment is enforced regardless of the file
    system on the volume. It is recommended on all file systems that you
    open volume handles as noncached, and follow the noncached I/O
    restrictions.

    .. container:: alert

       Note To read or write to the last few sectors of the volume, you must
       call DeviceIoControl and specify FSCTL_ALLOW_EXTENDED_DASD_IO. This
       signals the file system driver not to perform any I/O boundary checks
       on partition read or write calls. Instead, boundary checks are
       performed by the device driver.

    .. container::

    .. raw:: html

       <h3>

    Changer Device

    .. raw:: html

       </h3>

    The IOCTL_CHANGER_\* control codes for DeviceIoControl accept a handle
    to a changer device. To open a changer device, use a file name of the
    following form: â€œ\\.:raw-latex:`\Changer`xâ€ where x is a number that
    indicates which device to open, starting with zero. To open changer
    device zero in an application that is written in C or C++, use the
    following file name: â€œ\\\.\Changer0â€.

    .. raw:: html

       <h3>

    Tape Drives

    .. raw:: html

       </h3>

    You can open tape drives by using a file name of the following form:
    â€œ\\.:raw-latex:`\TAPE`xâ€ where x is a number that indicates which drive
    to open, starting with tape drive zero. To open tape drive zero in an
    application that is written in C or C++, use the following file name:
    â€œ\\\.\TAPE0â€.

    For more information, see Backup.

    .. raw:: html

       <h3>

    Communications Resources

    .. raw:: html

       </h3>

    The CreateFile function can create a handle to a communications
    resource, such as the serial port COM1. For communications resources,
    the dwCreationDisposition parameter must be OPEN_EXISTING, the
    dwShareMode parameter must be zero (exclusive access), and the
    hTemplateFile parameter must be NULL. Read, write, or read/write access
    can be specified, and the handle can be opened for overlapped I/O.

    To specify a COM port number greater than 9, use the following syntax:
    â€œ\\.:raw-latex:`\COM10`â€. This syntax works for all port numbers and
    hardware that allows COM port numbers to be specified.

    For more information about communications, see Communications.

    .. raw:: html

       <h3>

    Consoles

    .. raw:: html

       </h3>

    The CreateFile function can create a handle to console input
    (CONIN\ :math:`). If the process has an open handle to it as a result of inheritance or  duplication, it can also create a handle to the active screen buffer (CONOUT`).
    The calling process must be attached to an inherited console or one
    allocated by the AllocConsole function. For console handles, set the
    CreateFile parameters as follows.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    Parameters

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    Value

    .. raw:: html

       </th>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    lpFileName

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Use the CONIN$ value to specify console input.

    Use the CONOUT$ value to specify console output.

    CONIN$ gets a handle to the console input buffer, even if the
    SetStdHandle function redirects the standard input handle. To get the
    standard input handle, use the GetStdHandlefunction.

    CONOUT$ gets a handle to the active screen buffer, even if
    SetStdHandleredirects the standard output handle. To get the standard
    output handle, use GetStdHandle.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    dwDesiredAccess

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    GENERIC_READ \| GENERIC_WRITE is preferred, but either one can limit
    access.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    dwShareMode

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    When opening
    CONIN\ :math:`, specify  <b>FILE_SHARE_READ</b>. When opening CONOUT`,
    specify FILE_SHARE_WRITE.

    If the calling process inherits the console, or if a child process
    should be able to access the console, this parameter must be
    FILE_SHARE_READ \| FILE_SHARE_WRITE.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    lpSecurityAttributes

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    If you want the console to be inherited, the bInheritHandle member of
    the SECURITY_ATTRIBUTES structure must be TRUE.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    dwCreationDisposition

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    You should specify OPEN_EXISTING when using CreateFile to open the
    console.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    dwFlagsAndAttributes

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Ignored.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    hTemplateFile

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Ignored.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    The following table shows various settings of dwDesiredAccess and
    lpFileName.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    lpFileName

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    dwDesiredAccess

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    Result

    .. raw:: html

       </th>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    â€œCONâ€

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    GENERIC_READ

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Opens console for input.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    â€œCONâ€

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    GENERIC_WRITE

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Opens console for output.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    â€œCONâ€

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    GENERIC_READ \| GENERIC_WRITE

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Causes CreateFile to fail; GetLastError returns ERROR_FILE_NOT_FOUND.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    .. raw:: html

       <h3>

    Mailslots

    .. raw:: html

       </h3>

    If CreateFileopens the client end of a mailslot, the function returns
    INVALID_HANDLE_VALUE if the mailslot client attempts to open a local
    mailslot before the mailslot server has created it with the
    CreateMailSlot function.

    For more information, see Mailslots.

    .. raw:: html

       <h3>

    Pipes

    .. raw:: html

       </h3>

    If CreateFile opens the client end of a named pipe, the function uses
    any instance of the named pipe that is in the listening state. The
    opening process can duplicate the handle as many times as required, but
    after it is opened, the named pipe instance cannot be opened by another
    client. The access that is specified when a pipe is opened must be
    compatible with the access that is specified in the dwOpenModeparameter
    of the CreateNamedPipe function.

    If the CreateNamedPipe function was not successfully called on the
    server prior to this operation, a pipe will not exist and CreateFile
    will fail with ERROR_FILE_NOT_FOUND.

    If there is at least one active pipe instance but there are no available
    listener pipes on the server, which means all pipe instances are
    currently connected, CreateFile fails with ERROR_PIPE_BUSY.

    For more information, see Pipes.

    Examples
    ^^^^^^^^

    Example file operations are shown in the following topics:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    Appending One File to Another File

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Canceling Pending I/O Operations

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Creating a Child Process with Redirected Input and Output

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Creating and Using a Temporary File

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    FSCTL_RECALL_FILE

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    GetFinalPathNameByHandle

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Locking and Unlocking Byte Ranges in Files

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Obtaining a File Name From a File Handle

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Obtaining File System Recognition Information

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Opening a File for Reading or Writing

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Retrieving the Last-Write Time

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    SetFileInformationByHandle

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Testing for the End of a File

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Using Fibers

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Using Streams

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Walking a Buffer of Change Journal Records

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Wow64DisableWow64FsRedirection

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Wow64EnableWow64FsRedirection

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    Physical device I/O is demonstrated in the following topics:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    Calling DeviceIoControl

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Configuring a Communications Resource

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Monitoring Communications Events

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Processing a Request to Remove a Device

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    An example using named pipes is located at Named Pipe Client.

    Working with a mailslot is shown in Writing to a Mailslot.

    A tape backup code snippet can found at Creating a Backup Application.

    .. container:: code

    ..

       The fileapi.h header defines CreateFile as an alias which
       automatically selects the ANSI or Unicode version of this function
       based on the definition of the UNICODE preprocessor constant. Mixing
       usage of the encoding-neutral alias with code that not
       encoding-neutral can lead to mismatches that result in compilation or
       runtime errors. For more information, see `Conventions for Function
       Prototypes </windows/win32/intl/conventions-for-function-prototypes>`__.

    -see-also
    ---------

    About Directory Management

    About Volume Management

    Backup

    CloseHandle

    Communications

    CreateDirectory

    CreateDirectoryEx

    CreateFileTransacted

    CreateMailSlot

    CreateNamedPipe

    Creating, Deleting, and Maintaining Files

    DeleteFile

    Device Input and Output Control (IOCTL)

    DeviceIoControl

    File Compression and Decompression

    File Encryption

    File Management Functions

    File Security and Access Rights

    File Streams

    Functions

    GetLastError

    I/O Completion Ports

    I/O Concepts

    Mailslots

    Obtaining and Setting File Information

    Overview Topics

    Pipes

    ReadFile

    ReadFileEx

    Running with Special Privileges

    SetFileAttributes

    WriteFile

    WriteFileEx
    """

    def __new__(cls, *args, **kwargs):
        """
        HANDLE CreateFileW(
            LPCWSTR               lpFileName,
            DWORD                 dwDesiredAccess,
            DWORD                 dwShareMode,
            LPSECURITY_ATTRIBUTES lpSecurityAttributes,
            DWORD                 dwCreationDisposition,
            DWORD                 dwFlagsAndAttributes,
            HANDLE                hTemplateFile
        );
        https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew
        """
        func = kernel32.CreateFileW
        func.argtypes = [
            LPCWSTR,
            DWORD,
            DWORD,
            POINTER(SECURITY_ATTRIBUTES),
            DWORD,
            DWORD,
            HANDLE
        ]
        func.restype = HANDLE
        return func(*args)


class GetFileInformationByHandle(object):
    """
    GetFileInformationByHandle function
    ===================================

    -description
    ------------

    Retrieves file information for the specified file.

    For a more advanced version of this function, see
    GetFileInformationByHandleEx.

    To set file information using a file handle, see
    SetFileInformationByHandle.

    -parameters
    -----------

    -param hFile [in]
    ~~~~~~~~~~~~~~~~~

    A handle to the file that contains the information to be retrieved.

    This handle should not be a pipe handle.

    -param lpFileInformation [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a BY_HANDLE_FILE_INFORMATION structure that receives the
    file information.

    -returns
    --------

    If the function succeeds, the return value is nonzero and file
    information data is contained in the buffer pointed to by the
    lpFileInformation parameter.

    If the function fails, the return value is zero. To get extended error
    information, call GetLastError.

    -remarks
    --------

    Depending on the underlying network features of the operating system and
    the type of server connected to, the GetFileInformationByHandle function
    may fail, return partial information, or full information for the given
    file.

    You can compare the VolumeSerialNumber and FileIndex members returned in
    the BY_HANDLE_FILE_INFORMATION structure to determine if two paths map
    to the same target; for example, you can compare two file paths and
    determine if they map to the same directory.

    IIn Windows and Windows Server2012, this function is supported by the
    following technologies.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    Technology

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    Supported

    .. raw:: html

       </th>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    Server Message Block (SMB) 3.0 protocol

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    SMB 3.0 Transparent Failover (TFO)

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    SMB 3.0 with Scale-out File Shares (SO)

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    Cluster Shared Volume File System (CsvFS)

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    Resilient File System (ReFS)

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>



    .. raw:: html

       <h3>

    Transacted Operations

    .. raw:: html

       </h3>

    If there is a transaction bound to the thread at the time of the call,
    then the function returns the compressed file size of the isolated file
    view. For more information, see About Transactional NTFS.

    -see-also
    ---------

    File Management Functions

    GetFileInformationByHandleEx

    SetFileInformationByHandle
    """

    def __new__(cls, *args, **kwargs):
        """
        BOOL GetFileInformationByHandle(
            HANDLE                       hFile,
            LPBY_HANDLE_FILE_INFORMATION lpFileInformation
        );
        https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfileinformationbyhandle
        """
        func = kernel32.GetFileInformationByHandle
        func.argtypes = [
            HANDLE,
            POINTER(BY_HANDLE_FILE_INFORMATION)
        ]
        func.restype = BOOL
        return func(*args)


class CloseHandle(object):
    """
    CloseHandle function
    ====================

    -description
    ------------

    Closes an open object handle.

    -parameters
    -----------

    -param hObject [in]
    ~~~~~~~~~~~~~~~~~~~

    A valid handle to an open object.

    -returns
    --------

    If the function succeeds, the return value is nonzero.

    If the function fails, the return value is zero. To get extended error
    information, call GetLastError.

    If the application is running under a debugger, the function will throw
    an exception if it receives either a handle value that is not valid or a
    pseudo-handle value. This can happen if you close a handle twice, or if
    you call CloseHandle on a handle returned by the FindFirstFile function
    instead of calling the FindClose function.

    -remarks
    --------

    The CloseHandle function closes handles to the following objects:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    Access token

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Communications device

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Console input

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Console screen buffer

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Event

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    File

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    File mapping

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    I/O completion port

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Job

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Mailslot

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Memory resource notification

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Mutex

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Named pipe

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Pipe

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Process

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Semaphore

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Thread

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Transaction

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    Waitable timer

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    The documentation for the functions that create these objects indicates
    that CloseHandle should be used when you are finished with the object,
    and what happens to pending operations on the object after the handle is
    closed. In general, CloseHandle invalidates the specified object handle,
    decrements the objectâ€™s handle count, and performs object retention
    checks. After the last handle to an object is closed, the object is
    removed from the system. For a summary of the creator functions for
    these objects, see Kernel Objects.

    Generally, an application should call CloseHandle once for each handle
    it opens. It is usually not necessary to call CloseHandle if a function
    that uses a handle fails with ERROR_INVALID_HANDLE, because this error
    usually indicates that the handle is already invalidated. However, some
    functions use ERROR_INVALID_HANDLE to indicate that the object itself is
    no longer valid. For example, a function that attempts to use a handle
    to a file on a network might fail with ERROR_INVALID_HANDLE if the
    network connection is severed, because the file object is no longer
    available. In this case, the application should close the handle.

    If a handle is transacted, all handles bound to a transaction should be
    closed before the transaction is committed. If a transacted handle was
    opened by calling CreateFileTransacted with the
    FILE_FLAG_DELETE_ON_CLOSE flag, the file is not deleted until the
    application closes the handle and calls CommitTransaction. For more
    information about transacted objects, see Working With Transactions.

    Closing a thread handle does not terminate the associated thread or
    remove the thread object. Closing a process handle does not terminate
    the associated process or remove the process object. To remove a thread
    object, you must terminate the thread, then close all handles to the
    thread. For more information, see Terminating a Thread. To remove a
    process object, you must terminate the process, then close all handles
    to the process. For more information, see Terminating a Process.

    Closing a handle to a file mapping can succeed even when there are file
    views that are still open. For more information, see Closing a File
    Mapping Object.

    Do not use the CloseHandle function to close a socket. Instead, use the
    closesocket function, which releases all resources associated with the
    socket including the handle to the socket object. For more information,
    see Socket Closure.

    Do not use the CloseHandle function to close a handle to an open
    registry key. Instead, use the RegCloseKey function. CloseHandle does
    not close the handle to the registry key, but does not return an error
    to indicate this failure.

    Examples
    ^^^^^^^^

    .. code:: cpp

       dwPriorityClass = 0;
       hProcess = OpenProcess( PROCESS_ALL_ACCESS, FALSE, pe32.th32ProcessID );
       if( hProcess == NULL )
           printError( TEXT("OpenProcess") );
       else
       {
           dwPriorityClass = GetPriorityClass( hProcess );
           if( !dwPriorityClass )
           printError( TEXT("GetPriorityClass") );
           CloseHandle( hProcess );
       }

    To see this example in context, see Taking a Snapshot and Viewing
    Processes.

    .. container:: code

    -see-also
    ---------

    CreateFile

    CreateFileTransacted

    DeleteFile

    FindClose

    FindFirstFile

    Handle and Object Functions

    Kernel Objects

    Object Interface
    """

    def __new__(cls, *args, **kwargs):
        """
        BOOL CloseHandle(
            HANDLE hObject
        );
        https://docs.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-closehandle
        """
        func = kernel32.CloseHandle
        func.argtypes = [
            HANDLE
        ]
        func.restype = BOOL
        return func(*args)


class LockFile(object):
    """
    LockFileEx function
    ===================

    -description
    ------------

    Locks the specified file for exclusive access by the calling process.
    This function can operate either synchronously or asynchronously and can
    request either an exclusive or a shared lock.

    -parameters
    -----------

    -param hFile [in]
    ~~~~~~~~~~~~~~~~~

    A handle to the file. The handle must have been created with either the
    GENERIC_READ or GENERIC_WRITE access right. For more information, see
    File Security and Access Rights.

    -param dwFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    This parameter may be one or more of the following values.

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

    LOCKFILE_EXCLUSIVE_LOCK

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x00000002

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The function requests an exclusive lock. Otherwise, it requests a shared
    lock.

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

    LOCKFILE_FAIL_IMMEDIATELY

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x00000001

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The function returns immediately if it is unable to acquire the
    requested lock. Otherwise, it waits.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -param dwReserved
    ~~~~~~~~~~~~~~~~~

    Reserved parameter; must be set to zero.

    -param nNumberOfBytesToLockLow [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The low-order 32 bits of the length of the byte range to lock.

    -param nNumberOfBytesToLockHigh [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The high-order 32 bits of the length of the byte range to lock.

    -param lpOverlapped [in, out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to an OVERLAPPED structure that the function uses with the
    locking request. This structure, which is required, contains the file
    offset of the beginning of the lock range. You must initialize the
    hEvent member to a valid handle or zero.

    -returns
    --------

    If the function succeeds, the return value is nonzero (TRUE).

    If the function fails, the return value is zero (FALSE). To get extended
    error information, call GetLastError.

    -remarks
    --------

    Locking a region of a file is used to acquire shared or exclusive access
    to the specified region using this file handle. If the file handle is
    inherited by a process created by the locking process, the child process
    is not granted access to the locked region. If the locking process opens
    the file a second time, it cannot access the specified region through
    this second handle until it unlocks the region.

    Locking a portion of a file for exclusive access denies all other
    processes both read and write access to the specified region of the
    file. Locking a region that goes beyond the current end-of-file position
    is not an error.

    Locking a portion of a file for shared access denies all processes write
    access to the specified region of the file, including the process that
    first locks the region. All processes can read the locked region.

    Locking a region of a file does not prevent reading from a mapped file
    view.

    The LockFileEx function operates asynchronously if the file handle was
    opened for asynchronous I/O, unless the LOCKFILE_FAIL_IMMEDIATELY flag
    is specified. If an exclusive lock is requested for a range of a file
    that already has a shared or exclusive lock, the function returns the
    error ERROR_IO_PENDING. The system will signal the event specified in
    the OVERLAPPED structure after the lock is granted. To determine when
    the lock has been granted, use the GetOverlappedResult function or one
    of the wait functions. For more information, see Synchronous and
    Asynchronous I/O.

    If the file handle was not opened for asynchronous I/O and the lock is
    not available, this call waits until the lock is granted or an error
    occurs, unless the LOCKFILE_FAIL_IMMEDIATELY flag is specified.

    Exclusive locks cannot overlap an existing locked region of a file.
    Shared locks can overlap a locked region provided locks held on that
    region are shared locks. A shared lock can overlap an exclusive lock if
    both locks were created using the same file handle. When a shared lock
    overlaps an exclusive lock, the only possible access is a read by the
    owner of the locks. If the same range is locked with an exclusive and a
    shared lock, two unlock operations are necessary to unlock the region;
    the first unlock operation unlocks the exclusive lock, the second unlock
    operation unlocks the shared lock.

    If a process terminates with a portion of a file locked or closes a file
    that has outstanding locks, the locks are unlocked by the operating
    system. However, the time it takes for the operating system to unlock
    these locks depends upon available system resources. Therefore, it is
    recommended that your process explicitly unlock all files it has locked
    when it terminates. If this is not done, access to these files may be
    denied if the operating system has not yet unlocked them.

    In Windows and Windows Server2012, this function is supported by the
    following technologies.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    Technology

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    Supported

    .. raw:: html

       </th>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    Server Message Block (SMB) 3.0 protocol

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    SMB 3.0 Transparent Failover (TFO)

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    SMB 3.0 with Scale-out File Shares (SO)

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    Cluster Shared Volume File System (CsvFS)

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    Resilient File System (ReFS)

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Yes

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -see-also
    ---------

    CreateFile

    File Management Functions

    LockFile

    OVERLAPPED

    UnlockFile

    UnlockFileEx
    """

    def __new__(cls, *args, **kwargs):
        """
        BOOL LockFileEx(
            HANDLE       hFile,
            DWORD        dwFlags,
            DWORD        dwReserved,
            DWORD        nNumberOfBytesToLockLow,
            DWORD        nNumberOfBytesToLockHigh,
            LPOVERLAPPED lpOverlapped
        );
        https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-lockfileex
        """
        func = kernel32.LockFileEx
        func.argtypes = [
            HANDLE,
            DWORD,
            DWORD,
            DWORD,
            DWORD,
            POINTER(OVERLAPPED)
        ]
        func.restype = BOOL
        return func(*args)


class FileTimeToSystemTime(object):
    """
    FileTimeToSystemTime function
    =============================

    -description
    ------------

    Converts a file time to system time format. System time is based on
    Coordinated Universal Time (UTC).

    -parameters
    -----------

    -param lpFileTime [in]
    ~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a FILETIME structure containing the file time to be
    converted to system (UTC) date and time format.

    This value must be less than 0x8000000000000000. Otherwise, the function
    fails.

    -param lpSystemTime [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a SYSTEMTIME structure to receive the converted file time.

    -returns
    --------

    If the function succeeds, the return value is nonzero.

    If the function fails, the return value is zero. To get extended error
    information, call GetLastError.

    -see-also
    ---------

    DosDateTimeToFileTime

    FILETIME

    File Times

    FileTimeToDosDateTime

    SYSTEMTIME

    SystemTimeToFileTime

    Time Functions
    """

    def __new__(cls, *args, **kwargs):
        """
        BOOL FileTimeToSystemTime(
            const FILETIME *lpFileTime,
            LPSYSTEMTIME   lpSystemTime
        );
        https://docs.microsoft.com/en-us/windows/win32/api/timezoneapi/nf-timezoneapi-filetimetosystemtime
        """
        func = kernel32.FileTimeToSystemTime
        func.argtypes = [
            POINTER(FILETIME),
            POINTER(SYSTEMTIME)
        ]
        func.restype = BOOL
        return func(*args)


class GetSystemTime(object):
    """
    GetSystemTime function
    ======================

    -description
    ------------

    Retrieves the current system date and time in Coordinated Universal Time
    (UTC) format.

    To retrieve the current system date and time in local time, use the
    GetLocalTime function.

    -parameters
    -----------

    -param lpSystemTime [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a SYSTEMTIME structure to receive the current system date
    and time. The lpSystemTime parameter must not be NULL. Using NULL will
    result in an access violation.

    -remarks
    --------

    To set the current system date and time, use the SetSystemTime function.

    Examples
    ^^^^^^^^

    For an example, see SYSTEMTIME.

    .. container:: code

    -see-also
    ---------

    GetLocalTime

    GetSystemTimeAdjustment

    GetSystemTimeAsFileTime

    SYSTEMTIME

    SetSystemTime

    System Time

    Time Functions
    """

    def __new__(cls, *args, **kwargs):
        """
        void GetSystemTime(
            LPSYSTEMTIME lpSystemTime
        );
        https://docs.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtime
        """
        func = kernel32.GetSystemTime
        func.argtypes = [
            POINTER(SYSTEMTIME)
        ]
        func.restype = None
        return func(*args)


class GetLocalTime(object):
    """
    GetLocalTime function
    =====================

    -description
    ------------

    Retrieves the current local date and time.

    To retrieve the current date and time in Coordinated Universal Time
    (UTC) format, use the GetSystemTime function.

    -parameters
    -----------

    -param lpSystemTime [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a SYSTEMTIME structure to receive the current local date
    and time.

    -remarks
    --------

    To set the current local date and time, use the SetLocalTime function.

    Examples
    ^^^^^^^^

    For an example, see SYSTEMTIME.

    .. container:: code

    -see-also
    ---------

    GetSystemTime

    Local Time

    SYSTEMTIME

    SetLocalTime

    Time Functions
    """

    def __new__(cls, *args, **kwargs):
        """
        void GetLocalTime(
            LPSYSTEMTIME lpSystemTime
        );
        https://docs.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlocaltime
        """
        func = kernel32.GetLocalTime
        func.argtypes = [
            POINTER(SYSTEMTIME)
        ]
        func.restype = None
        return func(*args)


class SystemTimeToFileTime(object):
    """
    SystemTimeToFileTime function
    =============================

    -description
    ------------

    Converts a system time to file time format. System time is based on
    Coordinated Universal Time (UTC).

    -parameters
    -----------

    -param lpSystemTime [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a SYSTEMTIME structure that contains the system time to be
    converted from UTC to file time format.

    The wDayOfWeek member of the SYSTEMTIME structure is ignored.

    -param lpFileTime [out]
    ~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a FILETIME structure to receive the converted system time.

    -returns
    --------

    If the function succeeds, the return value is nonzero.

    If the function fails, the return value is zero. To get extended error
    information, call GetLastError.

       A False return value can indicate that the passed SYSTEMTIME
       structure represents an invalid date. Certain situations, such as the
       additional day added in a leap year, can result in application logic
       unexpectedly creating an invalid date. For more information on
       avoiding these issues, see `leap year
       readiness <https://techcommunity.microsoft.com/t5/azure-developer-community-blog/it-s-2020-is-your-code-ready-for-leap-day/ba-p/1157279>`__.

    -see-also
    ---------

    DosDateTimeToFileTime

    FILETIME

    FileTimeToDosDateTime

    FileTimeToSystemTime

    SYSTEMTIME

    System Time

    Time Functions
    """

    def __new__(cls, *args, **kwargs):
        """
        BOOL SystemTimeToFileTime(
            const SYSTEMTIME *lpSystemTime,
            LPFILETIME       lpFileTime
        );
        https://docs.microsoft.com/en-us/windows/win32/api/timezoneapi/nf-timezoneapi-systemtimetofiletime
        """
        func = kernel32.SystemTimeToFileTime
        func.argtypes = [
            POINTER(SYSTEMTIME),
            POINTER(FILETIME)
        ]
        func.restype = BOOL
        return func(*args)


class FileTimeToLocalFileTime(object):
    """
    FileTimeToLocalFileTime function
    ================================

    -description
    ------------

    Converts a file time to a local file time.

    -parameters
    -----------

    -param lpFileTime [in]
    ~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a FILETIME structure containing the UTC-based file time to
    be converted into a local file time.

    -param lpLocalFileTime [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a FILETIME structure to receive the converted local file
    time. This parameter cannot be the same as the lpFileTime parameter.

    -returns
    --------

    If the function succeeds, the return value is nonzero.

    If the function fails, the return value is zero. To get extended error
    information, call GetLastError.

    -remarks
    --------

    To account for daylight saving time when converting a file time to a
    local time, use the following sequence of functions in place of using
    FileTimeToLocalFileTime:

    .. raw:: html

       <ol>

    .. raw:: html

       <li>

    FileTimeToSystemTime

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    SystemTimeToTzSpecificLocalTime

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    SystemTimeToFileTime

    .. raw:: html

       </li>

    .. raw:: html

       </ol>

    -see-also
    ---------

    FILETIME

    File Times

    LocalFileTimeToFileTime

    Time Functions
    """

    def __new__(cls, *args, **kwargs):
        """
        BOOL FileTimeToLocalFileTime(
            const FILETIME *lpFileTime,
            LPFILETIME     lpLocalFileTime
        );
        https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-filetimetolocalfiletime
        """
        func = kernel32.FileTimeToLocalFileTime
        func.argtypes = [
            POINTER(FILETIME),
            POINTER(FILETIME)
        ]
        func.restype = BOOL
        return func(*args)


class SystemTimeToTzSpecificLocalTime(object):
    """
    SystemTimeToTzSpecificLocalTime function
    ========================================

    -description
    ------------

    Converts a time in Coordinated Universal Time (UTC) to a specified time
    zoneâ€™s corresponding local time.

    -parameters
    -----------

    -param lpTimeZoneInformation [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a TIME_ZONE_INFORMATION structure that specifies the time
    zone of interest.

    If lpTimeZone is NULL, the function uses the currently active time zone.

    -param lpUniversalTime [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a SYSTEMTIME structure that specifies the UTC time to be
    converted. The function converts this universal time to the specified
    time zoneâ€™s corresponding local time.

    -param lpLocalTime [out]
    ~~~~~~~~~~~~~~~~~~~~~~~~

    A pointer to a SYSTEMTIME structure that receives the local time.

    -returns
    --------

    If the function succeeds, the return value is nonzero, and the function
    sets the members of the SYSTEMTIME structure pointed to by lpLocalTime
    to the appropriate local time values.

    If the function fails, the return value is zero. To get extended error
    information, call GetLastError.

    -remarks
    --------

    The SystemTimeToTzSpecificLocalTime function takes into account whether
    daylight saving time (DST) is in effect for the local time to which the
    system time is to be converted.

    The SystemTimeToTzSpecificLocalTime function may calculate the local
    time incorrectly under the following conditions:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    The time zone uses a different UTC offset for the old and new years.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    The UTC time to be converted and the calculated local time are in
    different years.

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    Examples
    ^^^^^^^^

    For an example, see Retrieving the Last-Write Time.

    .. container:: code

    -see-also
    ---------

    GetSystemTime

    GetTimeZoneInformation

    SYSTEMTIME

    System Time

    TIME_ZONE_INFORMATION

    Time Functions

    TzSpecificLocalTimeToSystemTime
    """

    def __new__(cls, *args, **kwargs):
        """
        BOOL SystemTimeToTzSpecificLocalTime(
            const TIME_ZONE_INFORMATION *lpTimeZoneInformation,
            const SYSTEMTIME            *lpUniversalTime,
            LPSYSTEMTIME                lpLocalTime
        );
        https://docs.microsoft.com/en-us/windows/win32/api/timezoneapi/nf-timezoneapi-systemtimetotzspecificlocaltime
        """
        func = kernel32.SystemTimeToTzSpecificLocalTime
        func.argtypes = [
            POINTER(TIME_ZONE_INFORMATION),
            POINTER(SYSTEMTIME),
            POINTER(SYSTEMTIME)
        ]
        func.restype = BOOL
        return func(*args)


class GlobalAlloc(object):
    """
    GlobalAlloc function
    ====================

    -description
    ------------

    Allocates the specified number of bytes from the heap.

    .. container:: alert

       Note  The global functions have greater overhead and provide fewer
       features than other memory management functions. New applications
       should use the heap functions unless documentation states that a
       global function should be used. For more information, see Global and
       Local Functions.

    .. container::

        

    -parameters
    -----------

    -param uFlags [in]
    ~~~~~~~~~~~~~~~~~~

    The memory allocation attributes. If zero is specified, the default is
    GMEM_FIXED. This parameter can be one or more of the following values,
    except for the incompatible combinations that are specifically noted.

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

    GHND

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x0042

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Combines GMEM_MOVEABLE and GMEM_ZEROINIT.

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

    GMEM_FIXED

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x0000

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Allocates fixed memory. The return value is a pointer.

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

    GMEM_MOVEABLE

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x0002

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Allocates movable memory. Memory blocks are never moved in physical
    memory, but they can be moved within the default heap.

    The return value is a handle to the memory object. To translate the
    handle into a pointer, use the GlobalLock function.

    This value cannot be combined with GMEM_FIXED.

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

    GMEM_ZEROINIT

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x0040

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Initializes memory contents to zero.

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

    GPTR

    .. raw:: html

       </dt>

    .. raw:: html

       <dt>

    0x0040

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Combines GMEM_FIXED and GMEM_ZEROINIT.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

     

    The following values are obsolete, but are provided for compatibility
    with 16-bit Windows. They are ignored.

    .. raw:: html

       <dl>

    .. raw:: html

       <dd>

    GMEM_DDESHARE

    .. raw:: html

       </dd>

    .. raw:: html

       <dd>

    GMEM_DISCARDABLE

    .. raw:: html

       </dd>

    .. raw:: html

       <dd>

    GMEM_LOWER

    .. raw:: html

       </dd>

    .. raw:: html

       <dd>

    GMEM_NOCOMPACT

    .. raw:: html

       </dd>

    .. raw:: html

       <dd>

    GMEM_NODISCARD

    .. raw:: html

       </dd>

    .. raw:: html

       <dd>

    GMEM_NOT_BANKED

    .. raw:: html

       </dd>

    .. raw:: html

       <dd>

    GMEM_NOTIFY

    .. raw:: html

       </dd>

    .. raw:: html

       <dd>

    GMEM_SHARE

    .. raw:: html

       </dd>

    .. raw:: html

       </dl>

    -param dwBytes [in]
    ~~~~~~~~~~~~~~~~~~~

    The number of bytes to allocate. If this parameter is zero and the
    uFlags parameter specifies GMEM_MOVEABLE, the function returns a handle
    to a memory object that is marked as discarded.

    -returns
    --------

    If the function succeeds, the return value is a handle to the newly
    allocated memory object.

    If the function fails, the return value is NULL. To get extended error
    information, call GetLastError.

    -remarks
    --------

    Windows memory management does not provide a separate local heap and
    global heap. Therefore, the GlobalAlloc and LocalAlloc functions are
    essentially the same.

    The movable-memory flags GHND and GMEM_MOVABLE add unnecessary overhead
    and require locking to be used safely. They should be avoided unless
    documentation specifically states that they should be used.

    New applications should use the heap functions to allocate and manage
    memory unless the documentation specifically states that a global
    function should be used. For example, the global functions are still
    used with Dynamic Data Exchange (DDE), the clipboard functions, and OLE
    data objects.

    If the GlobalAlloc function succeeds, it allocates at least the amount
    of memory requested. If the actual amount allocated is greater than the
    amount requested, the process can use the entire amount. To determine
    the actual number of bytes allocated, use the GlobalSize function.

    If the heap does not contain sufficient free space to satisfy the
    request, GlobalAlloc returns NULL. Because NULL is used to indicate an
    error, virtual address zero is never allocated. It is, therefore, easy
    to detect the use of a NULL pointer.

    Memory allocated with this function is guaranteed to be aligned on an
    8-byte boundary. To execute dynamically generated code, use the
    VirtualAlloc function to allocate memory and the VirtualProtect function
    to grant PAGE_EXECUTE access.

    To free the memory, use the GlobalFree function. It is not safe to free
    memory allocated with GlobalAlloc using LocalFree.

    Examples
    ^^^^^^^^

    The following code shows a simple use of GlobalAlloc and GlobalFree.

    .. code:: cpp

       #include <windows.h>
       #include <stdio.h>
       #include <tchar.h>

       void _cdecl main()
       {
           PSECURITY_DESCRIPTOR pSD;

           pSD = (PSECURITY_DESCRIPTOR) GlobalAlloc(
                  GMEM_FIXED,
                  sizeof(PSECURITY_DESCRIPTOR));

           // Handle error condition
           if( pSD == NULL )
           {
              _tprintf(TEXT("GlobalAlloc failed (%d)\n"), GetLastError());
              return;
           }

           //see how much memory was allocated
           _tprintf(TEXT("GlobalAlloc allocated %d bytes\n"), GlobalSize(pSD));

           // Use the memory allocated

           // Free the memory when finished with it
           GlobalFree(pSD);
       }

    -see-also
    ---------

    Global and Local Functions

    GlobalDiscard

    GlobalFree

    GlobalLock

    GlobalSize

    Heap Functions

    Memory Management Functions
    """

    def __new__(cls, *args, **kwargs):
        """
        DECLSPEC_ALLOCATOR HGLOBAL GlobalAlloc(
            UINT   uFlags,
            SIZE_T dwBytes
        );
        https://docs.microsoft.com/en-gb/windows/win32/api/winbase/nf-winbase-globalalloc?redirectedfrom=MSDN
        """
        func = kernel32.GlobalAlloc
        func.argtypes = [
            UINT,
            SIZE_T
        ]
        func.restype = HGLOBAL
        return func(*args)


class GlobalLock(object):
    """
    GlobalLock function
    ===================

    -description
    ------------

    Locks a global memory object and returns a pointer to the first byte of
    the object’s memory block.

    .. container:: alert

       Note  The global functions have greater overhead and provide fewer
       features than other memory management functions. New applications
       should use the heap functions unless documentation states that a
       global function should be used. For more information, see Global and
       Local Functions.

    .. container::

        

    -parameters
    -----------

    -param hMem [in]
    ~~~~~~~~~~~~~~~~

    A handle to the global memory object. This handle is returned by either
    the GlobalAlloc or GlobalReAlloc function.

    -returns
    --------

    If the function succeeds, the return value is a pointer to the first
    byte of the memory block.

    If the function fails, the return value is NULL. To get extended error
    information, call GetLastError.

    -remarks
    --------

    The internal data structures for each memory object include a lock count
    that is initially zero. For movable memory objects, GlobalLock
    increments the count by one, and the GlobalUnlock function decrements
    the count by one. Each successful call that a process makes to
    GlobalLock for an object must be matched by a corresponding call to
    GlobalUnlock. Locked memory will not be moved or discarded, unless the
    memory object is reallocated by using the GlobalReAlloc function. The
    memory block of a locked memory object remains locked until its lock
    count is decremented to zero, at which time it can be moved or
    discarded.

    Memory objects allocated with GMEM_FIXED always have a lock count of
    zero. For these objects, the value of the returned pointer is equal to
    the value of the specified handle.

    If the specified memory block has been discarded or if the memory block
    has a zero-byte size, this function returns NULL.

    Discarded objects always have a lock count of zero.

    -see-also
    ---------

    Global and Local Functions

    GlobalAlloc

    GlobalReAlloc

    GlobalUnlock

    Memory Management Functions
    """

    def __new__(cls, *args, **kwargs):
        """
        LPVOID GlobalLock(
            HGLOBAL hMem
        );
        https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-globallock
        """
        func = kernel32.GlobalLock
        func.argtypes = [
            HGLOBAL
        ]
        func.restype = LPVOID
        return func(*args)


class GlobalUnlock(object):
    """
    GlobalUnlock function
    =====================

    -description
    ------------

    Decrements the lock count associated with a memory object that was
    allocated with GMEM_MOVEABLE. This function has no effect on memory
    objects allocated with GMEM_FIXED.

    .. container:: alert

       NoteThe global functions have greater overhead and provide fewer
       features than other memory management functions. New applications
       should use the heap functions unless documentation states that a
       global function should be used. For more information, see Global and
       Local Functions.

    .. container::



    -parameters
    -----------

    -param hMem [in]
    ~~~~~~~~~~~~~~~~

    A handle to the global memory object. This handle is returned by either
    the GlobalAlloc or GlobalReAlloc function.

    -returns
    --------

    If the memory object is still locked after decrementing the lock count,
    the return value is a nonzero value. If the memory object is unlocked
    after decrementing the lock count, the function returns zero and
    GetLastError returns NO_ERROR.

    If the function fails, the return value is zero and GetLastError returns
    a value other than NO_ERROR.

    -remarks
    --------

    The internal data structures for each memory object include a lock count
    that is initially zero. For movable memory objects, the GlobalLock
    function increments the count by one, and GlobalUnlock decrements the
    count by one. For each call that a process makes to GlobalLock for an
    object, it must eventually call GlobalUnlock. Locked memory will not be
    moved or discarded, unless the memory object is reallocated by using the
    GlobalReAlloc function. The memory block of a locked memory object
    remains locked until its lock count is decremented to zero, at which
    time it can be moved or discarded.

    Memory objects allocated with GMEM_FIXED always have a lock count of
    zero. If the specified memory block is fixed memory, this function
    returns TRUE.

    If the memory object is already unlocked, GlobalUnlock returns FALSE and
    GetLastError reports ERROR_NOT_LOCKED.

    A process should not rely on the return value to determine the number of
    times it must subsequently call GlobalUnlock for a memory object.

    -see-also
    ---------

    Global and Local Functions

    GlobalAlloc

    GlobalLock

    GlobalReAlloc

    Memory Management Functions
    """

    def __new__(cls, *args, **kwargs):
        """
        BOOL GlobalUnlock(
            HGLOBAL hMem
        );
        https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-globalunlock
        """
        func = kernel32.GlobalUnlock
        func.argtypes = [
            HGLOBAL
        ]
        func.restype = BOOL
        return func(*args)


class WideCharToMultiByte(object):
    """
    WideCharToMultiByte function
    ============================

    -description
    ------------

    Maps a UTF-16 (wide character) string to a new character string. The new
    character string is not necessarily from a multibyte character set.

    .. raw:: html

       <div class="alert">

    CautionUsing the WideCharToMultiByte function incorrectly can
    compromise the security of your application. Calling this function can
    easily cause a buffer overrun because the size of the input buffer
    indicated by lpWideCharStr equals the number of characters in the
    Unicode string, while the size of the output buffer indicated by
    lpMultiByteStr equals the number of bytes. To avoid a buffer overrun,
    your application must specify a buffer size appropriate for the data
    type the buffer receives.

    .. raw:: html

       <p class="note">

    Data converted from UTF-16 to non-Unicode encodings is subject to data
    loss, because a code page might not be able to represent every character
    used in the specific Unicode data. For more information, see Security
    Considerations: International Features.

    .. raw:: html

       </div>

    .. container::



    .. container:: alert

       NoteThe ANSI code pages can be different on different computers, or
       can be changed for a single computer, leading to data corruption. For
       the most consistent results, applications should use Unicode, such as
       UTF-8 or UTF-16, instead of a specific code page, unless legacy
       standards or data formats prevent the use of Unicode. If using
       Unicode is not possible, applications should tag the data stream with
       the appropriate encoding name when protocols allow it. HTML and XML
       files allow tagging, but text files do not.

    .. container::



    -parameters
    -----------

    -param CodePage [in]
    ~~~~~~~~~~~~~~~~~~~~

    Code page to use in performing the conversion. This parameter can be set
    to the value of any code page that is installed or available in the
    operating system. For a list of code pages, see Code Page Identifiers.
    Your application can also specify one of the values shown in the
    following table.

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

    CP_ACP

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The system default Windows ANSI code page.

    .. container:: alert

       NoteThis value can be different on different computers, even on the
       same network. It can be changed on the same computer, leading to
       stored data becoming irrecoverably corrupted. This value is only
       intended for temporary use and permanent storage should use UTF-16 or
       UTF-8 if possible.

    .. container::



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

    CP_MACCP

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The current system Macintosh code page.

    .. container:: alert

       NoteThis value can be different on different computers, even on the
       same network. It can be changed on the same computer, leading to
       stored data becoming irrecoverably corrupted. This value is only
       intended for temporary use and permanent storage should use UTF-16 or
       UTF-8 if possible.

    .. container::



    .. container:: alert

       Note This value is used primarily in legacy code and should not
       generally be needed since modern Macintosh computers use Unicode for
       encoding.

    .. container::



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

    CP_OEMCP

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The current system OEM code page.

    .. container:: alert

       NoteThis value can be different on different computers, even on the
       same network. It can be changed on the same computer, leading to
       stored data becoming irrecoverably corrupted. This value is only
       intended for temporary use and permanent storage should use UTF-16 or
       UTF-8 if possible.

    .. container::



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

    CP_SYMBOL

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Windows2000: Symbol code page (42).

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

    CP_THREAD_ACP

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Windows2000: The Windows ANSI code page for the current thread.

    .. container:: alert

       NoteThis value can be different on different computers, even on the
       same network. It can be changed on the same computer, leading to
       stored data becoming irrecoverably corrupted. This value is only
       intended for temporary use and permanent storage should use UTF-16 or
       UTF-8 if possible.

    .. container::



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

    CP_UTF7

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    UTF-7. Use this value only when forced by a 7-bit transport mechanism.
    Use of UTF-8 is preferred. With this value set, lpDefaultChar and
    lpUsedDefaultChar must be set to NULL.

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

    CP_UTF8

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    UTF-8. With this value set, lpDefaultChar and lpUsedDefaultChar must be
    set to NULL.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -param dwFlags [in]
    ~~~~~~~~~~~~~~~~~~~

    Flags indicating the conversion type. The application can specify a
    combination of the following values. The function performs more quickly
    when none of these flags is set. The application should specify
    WC_NO_BEST_FIT_CHARS and WC_COMPOSITECHECK with the specific value
    WC_DEFAULTCHAR to retrieve all possible conversion results. If all three
    values are not provided, some results will be missing.

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

    WC_COMPOSITECHECK

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Convert composite characters, consisting of a base character and a
    nonspacing character, each with different character values. Translate
    these characters to precomposed characters, which have a single
    character value for a base-nonspacing character combination. For
    example, in the character Ã¨, the e is the base character and the accent
    grave mark is the nonspacing character.

    .. container:: alert

       NoteWindows normally represents Unicode strings with precomposed
       data, making the use of the WC_COMPOSITECHECK flag unnecessary.

    .. container::



    Your application can combine WC_COMPOSITECHECK with any one of the
    following flags, with the default being WC_SEPCHARS. These flags
    determine the behavior of the function when no precomposed mapping for a
    base-nonspacing character combination in a Unicode string is available.
    If none of these flags is supplied, the function behaves as if the
    WC_SEPCHARS flag is set. For more information, see WC_COMPOSITECHECK and
    related flags in the Remarks section.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    WC_DEFAULTCHAR

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Replace exceptions with the default character during conversion.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    WC_DISCARDNS

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Discard nonspacing characters during conversion.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    WC_SEPCHARS

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Default. Generate separate characters during conversion.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>



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

    WC_ERR_INVALID_CHARS

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    WindowsVista and later: Fail (by returning 0 and setting the last-error
    code to ERROR_NO_UNICODE_TRANSLATION) if an invalid input character is
    encountered. You can retrieve the last-error code with a call to
    GetLastError. If this flag is not set, the function replaces illegal
    sequences with U+FFFD (encoded as appropriate for the specified
    codepage) and succeeds by returning the length of the converted string.
    Note that this flag only applies when CodePage is specified as CP_UTF8
    or 54936. It cannot be used with other code page values.

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

    WC_NO_BEST_FIT_CHARS

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    Translate any Unicode characters that do not translate directly to
    multibyte equivalents to the default character specified by
    lpDefaultChar. In other words, if translating from Unicode to multibyte
    and back to Unicode again does not yield the same Unicode character, the
    function uses the default character. This flag can be used by itself or
    in combination with the other defined flags.

    For strings that require validation, such as file, resource, and user
    names, the application should always use the WC_NO_BEST_FIT_CHARS flag.
    This flag prevents the function from mapping characters to characters
    that appear similar but have very different semantics. In some cases,
    the semantic change can be extreme. For example, the symbol for â€œâˆžâ€
    (infinity) maps to 8 (eight) in some code pages.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>



    For the code pages listed below, dwFlags must be 0. Otherwise, the
    function fails with ERROR_INVALID_FLAGS.

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    50220

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    50221

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    50222

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    50225

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    50227

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    50229

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    57002 through 57011

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    65000 (UTF-7)

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    42 (Symbol)

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    .. container:: alert

       NoteFor the code page 65001 (UTF-8) or the code page 54936
       (GB18030, WindowsVista and later), dwFlags must be set to either 0
       or WC_ERR_INVALID_CHARS. Otherwise, the function fails with
       ERROR_INVALID_FLAGS.

    .. container::



    -param lpWideCharStr [in]
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to the Unicode string to convert.

    -param cchWideChar [in]
    ~~~~~~~~~~~~~~~~~~~~~~~

    Size, in characters, of the string indicated by lpWideCharStr.
    Alternatively, this parameter can be set to -1 if the string is
    null-terminated. If cchWideChar is set to 0, the function fails.

    If this parameter is -1, the function processes the entire input string,
    including the terminating null character. Therefore, the resulting
    character string has a terminating null character, and the length
    returned by the function includes this character.

    If this parameter is set to a positive integer, the function processes
    exactly the specified number of characters. If the provided size does
    not include a terminating null character, the resulting character string
    is not null-terminated, and the returned length does not include this
    character.

    -param lpMultiByteStr [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a buffer that receives the converted string.

    -param cbMultiByte [in]
    ~~~~~~~~~~~~~~~~~~~~~~~

    Size, in bytes, of the buffer indicated by lpMultiByteStr. If this
    parameter is set to 0, the function returns the required buffer size for
    lpMultiByteStr and makes no use of the output parameter itself.

    -param lpDefaultChar [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to the character to use if a character cannot be represented in
    the specified code page. The application sets this parameter to NULL if
    the function is to use a system default value. To obtain the system
    default character, the application can call the GetCPInfo or GetCPInfoEx
    function.

    For the CP_UTF7 and CP_UTF8 settings for CodePage, this parameter must
    be set to NULL. Otherwise, the function fails with
    ERROR_INVALID_PARAMETER.

    -param lpUsedDefaultChar [out, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pointer to a flag that indicates if the function has used a default
    character in the conversion. The flag is set to TRUE if one or more
    characters in the source string cannot be represented in the specified
    code page. Otherwise, the flag is set to FALSE. This parameter can be
    set to NULL.

    For the CP_UTF7 and CP_UTF8 settings for CodePage, this parameter must
    be set to NULL. Otherwise, the function fails with
    ERROR_INVALID_PARAMETER.

    -returns
    --------

    If successful, returns the number of bytes written to the buffer pointed
    to by lpMultiByteStr. If the function succeeds and cbMultiByte is 0, the
    return value is the required size, in bytes, for the buffer indicated by
    lpMultiByteStr. Also see dwFlags for info about how the
    WC_ERR_INVALID_CHARS flag affects the return value when invalid
    sequences are input.

    The function returns 0 if it does not succeed. To get extended error
    information, the application can call GetLastError, which can return one
    of the following error codes:

    .. raw:: html

       <ul>

    .. raw:: html

       <li>

    ERROR_INSUFFICIENT_BUFFER. A supplied buffer size was not large enough,
    or it was incorrectly set to NULL.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    ERROR_INVALID_FLAGS. The values supplied for flags were not valid.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    ERROR_INVALID_PARAMETER. Any of the parameter values was invalid.

    .. raw:: html

       </li>

    .. raw:: html

       <li>

    ERROR_NO_UNICODE_TRANSLATION. Invalid Unicode was found in a string.

    .. raw:: html

       </li>

    .. raw:: html

       </ul>

    -remarks
    --------

    The lpMultiByteStr and lpWideCharStr pointers must not be the same. If
    they are the same, the function fails, and GetLastError returns
    ERROR_INVALID_PARAMETER.

    WideCharToMultiByte does not null-terminate an output string if the
    input string length is explicitly specified without a terminating null
    character. To null-terminate an output string for this function, the
    application should pass in -1 or explicitly count the terminating null
    character for the input string.

    If cbMultiByte is less than cchWideChar, this function writes the number
    of characters specified by cbMultiByte to the buffer indicated by
    lpMultiByteStr. However, if CodePage is set to CP_SYMBOL and cbMultiByte
    is less than cchWideChar, the function writes no characters to
    lpMultiByteStr.

    The WideCharToMultiByte function operates most efficiently when both
    lpDefaultChar and lpUsedDefaultChar are set to NULL. The following table
    shows the behavior of the function for the four possible combinations of
    these parameters.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    lpDefaultChar

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    lpUsedDefaultChar

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    Result

    .. raw:: html

       </th>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    NULL

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    NULL

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    No default checking. These parameter settings are the most efficient
    ones for use with this function.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    Non-null character

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    NULL

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Uses the specified default character, but does not set
    lpUsedDefaultChar.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    NULL

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Non-null character

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Uses the system default character and sets lpUsedDefaultChar if
    necessary.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    Non-null character

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Non-null character

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Uses the specified default character and sets lpUsedDefaultChar if
    necessary.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>



    Starting with WindowsVista, this function fully conforms with the
    Unicode 4.1 specification for UTF-8 and UTF-16. The function used on
    earlier operating systems encodes or decodes lone surrogate halves or
    mismatched surrogate pairs. Code written in earlier versions of Windows
    that rely on this behavior to encode random non-text binary data might
    run into problems. However, code that uses this function to produce
    valid UTF-8 strings will behave the same way as on earlier Windows
    operating systems.

    Starting with Windows: WideCharToMultiByte is declared in
    Stringapiset.h. Before Windows, it was declared in Winnls.h.

    .. raw:: html

       <h3>

    WC_COMPOSITECHECK and related flags

    .. raw:: html

       </h3>

    As discussed in Using Unicode Normalization to Represent Strings,
    Unicode allows multiple representations of the same string (interpreted
    linguistically). For example, Capital A with dieresis (umlaut) can be
    represented either precomposed as a single Unicode code point â€œÃ„â€
    (U+00C4) or decomposed as the combination of Capital A and the combining
    dieresis character (â€œAâ€ + â€œÂ¨â€, that is U+0041 U+0308). However, most
    code pages provide only composed characters.

    The WC_COMPOSITECHECK flag causes the WideCharToMultiByte function to
    test for decomposed Unicode characters and attempts to compose them
    before converting them to the requested code page. This flag is only
    available for conversion to single byte (SBCS) or double byte (DBCS)
    code pages (code pages < 50000, excluding code page 42). If your
    application needs to convert decomposed Unicode data to single byte or
    double byte code pages, this flag might be useful. However, not all
    characters can be converted this way and it is more reliable to save and
    store such data as Unicode.

    When an application is using WC_COMPOSITECHECK, some character
    combinations might remain incomplete or might have additional nonspacing
    characters left over. For example, A + Â¨ + Â¨ combines to Ã„ + Â¨. Using
    the WC_DISCARDNS flag causes the function to discard additional
    nonspacing characters. Using the WC_DEFAULTCHAR flag causes the function
    to use the default replacement character (typically â€œ?â€) instead. Using
    the WC_SEPCHARS flag causes the function to attempt to convert each
    additional nonspacing character to the target code page. Usually this
    flag also causes the use of the replacement character (â€œ?â€). However,
    for code page 1258 (Vietnamese) and 20269, nonspacing characters exist
    and can be used. The conversions for these code pages are not perfect.
    Some combinations do not convert correctly to code page 1258, and
    WC_COMPOSITECHECK corrupts data in code page 20269. As mentioned
    earlier, it is more reliable to design your application to save and
    store such data as Unicode.

    -see-also
    ---------

    MultiByteToWideChar

    Unicode and Character Set Functions

    Unicode and Character Sets
    """

    def __new__(cls, *args, **kwargs):
        """
        int WideCharToMultiByte(
            UINT                               CodePage,
            DWORD                              dwFlags,
            _In_NLS_string_(cchWideChar)LPCWCH lpWideCharStr,
            int                                cchWideChar,
            LPSTR                              lpMultiByteStr,
            int                                cbMultiByte,
            LPCCH                              lpDefaultChar,
            LPBOOL                             lpUsedDefaultChar
        );
        https://docs.microsoft.com/en-us/windows/win32/api/stringapiset/nf-stringapiset-widechartomultibyte
        """
        func = kernel32.WideCharToMultiByte
        func.argtypes = [
            UINT,
            DWORD,
            LPCWCH,
            INT,
            LPSTR,
            INT,
            LPCCH,
            LPBOOL
        ]
        func.restype = INT
        return func(*args)
