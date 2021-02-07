from ctypes import sizeof, GetLastError
from sys import maxsize

from winapi.common.winerror_h import ERROR_INSUFFICIENT_BUFFER
from winapi.common.winnls_h import WC_NO_BEST_FIT_CHARS, WC_DEFAULTCHAR, WC_COMPOSITECHECK, CP_UTF8
from winapi.common.datatypes import CHAR
from winapi.kernel32.api import WideCharToMultiByte


IS_PYTHON_32 = maxsize <= 0x7fffffff
IS_PYTHON_64 = not IS_PYTHON_32


def str_to_hex(string: str) -> str:
    return hex(hex_to_int(string))


def hex_to_int(string: str) -> int:
    return int(string, base=16)


def unicode_buffer_to_string_array(buffer) -> list:
    """
    `Converts a buffer having unicode strings array to python string list`

    :param buffer: ctype buffer
    :return: A generator object of strings
    """
    flags = WC_NO_BEST_FIT_CHARS | WC_COMPOSITECHECK | WC_DEFAULTCHAR
    multibyte_buffer = (CHAR * int(sizeof(buffer)/2))()   # the size required to store result byte would be half of unicode buffer
    r = WideCharToMultiByte(
        CP_UTF8,
        flags,
        buffer,
        sizeof(buffer),
        multibyte_buffer,
        sizeof(multibyte_buffer),
        None,
        None
    )
    # the above call will always return 0 because the unicode buffer will be double the size of ANSI, however the target
    # buffer is always updated
    assert all([r == 0, GetLastError() == ERROR_INSUFFICIENT_BUFFER]), "unicode_buffer_to_string_array failed"
    return filter(None, bytes(multibyte_buffer).decode("utf-8").split("\x00"))
