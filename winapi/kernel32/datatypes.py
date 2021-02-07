from ctypes import POINTER
from ctypes.wintypes import HGLOBAL
from winapi.common.datatypes import WCHAR, CHAR


LPCWCH = POINTER(WCHAR)   # type LPCWCH = *const WCHAR;
LPCCH = POINTER(CHAR)     # type LPCCH = *const CHAR;
