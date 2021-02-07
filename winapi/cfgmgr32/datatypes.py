from ctypes import POINTER
from winapi.guid import GUID
from winapi.setupapi.structs import DEVPROPKEY
from winapi.common.datatypes import ULONG, PCSTR, PCWSTR, DWORD, LPCSTR, LPCWSTR, \
    DEVINST, PWSTR, PULONG, LPWSTR, PBYTE, BYTE, WCHAR

DEVPROPKEY = POINTER(DEVPROPKEY)
DEVPROPTYPE = POINTER(ULONG)  # typedef ULONG DEVPROPTYPE, *PDEVPROPTYPE;
LPGUID = POINTER(GUID)  # typedef GUID* LPGUID;
DEVINSTID_A = PCSTR   # typedef _Null_terminated_ CHAR  *DEVNODEID_A, *DEVINSTID_A; // Device ID ANSI name.
DEVINSTID_W = PCWSTR
CONFIGRET = ULONG
DEVNODE = DWORD       # typedef DWORD       DEVNODE, DEVINST;
PDEVINST = POINTER(DEVNODE)     # typedef DEVNODE    *PDEVNODE, *PDEVINST;
PZZSTR = LPCSTR     # typedef _NullNull_terminated_ CHAR *PZZSTR;
PZZWSTR = LPCWSTR
LPCGUID = LPGUID    # typedef const GUID *LPCGUID;

