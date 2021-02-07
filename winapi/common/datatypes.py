"""
https://docs.microsoft.com/en-us/windows/win32/winprog/windows-data-types
"""
from ctypes import Structure, c_ubyte, c_char_p, POINTER
from ctypes.wintypes import (
    HANDLE, HWND,
    DWORD, WORD,
    LONG, ULONG,
    BYTE, BOOL,
    SHORT, USHORT,
    INT, UINT,
    CHAR, WCHAR,
    LPCWSTR, LPCSTR, LPVOID, LPWSTR, LPSTR, LPBOOL,
    PBYTE, PDWORD, PULONG, ULARGE_INTEGER
)


NULL = None
INT_32 = INT
UINT_32 = UINT
INT_16 = SHORT
UINT_16 = USHORT
ULONG_PTR = POINTER(ULONG)
PCWSTR = LPCWSTR
INTPTR = HWND
HDEVINFO = INTPTR
UBYTE = c_ubyte     # unsigned char
PCHAR = c_char_p

DEVINST = DWORD
PWSTR = LPWSTR
BOOLEAN = BOOL
PCSTR = LPCSTR      # typedef CONST CHAR *PCSTR;
ULONGULONG = ULARGE_INTEGER

