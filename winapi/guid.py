import inspect
import re
from ctypes import (
    byref, sizeof, memmove, cast, POINTER, Structure,
    WinDLL, create_unicode_buffer, FormatError, GetLastError
)
from struct import unpack
from textwrap import wrap

from winapi.common.datatypes import UINT_32, UINT_16, UBYTE
from winapi.utils import hex_to_int

__all__ = ['InvalidGUID', 'GUID', 'DEFINE_GUID']


GUID_PATTERN = re.compile(r'{[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}}')


class InvalidGUID(ValueError):
    pass


class GUID(Structure):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/guiddef/ns-guiddef-guid
    Example: GUID(0xE2D1FF34, 0x3458, 0x49A9, (0x88, 0xDA, 0x8E, 0x69, 0x15, 0xCE, 0x9B, 0xE5))
             GUID(0xE2D1FF34, 0x3458, 0x49A9, (ctypes.c_ubyte*8)(0x88, 0xDA, 0x8E, 0x69, 0x15, 0xCE, 0x9B, 0xE5))
    """
    _fields_ = [
        ('Data1', UINT_32),
        ('Data2', UINT_16),
        ('Data3', UINT_16),
        ('Data4', UBYTE * 8),
    ]

    def __str__(self):
        return "{%08x-%04x-%04x-%s-%s}" % (
            self.Data1,
            self.Data2,
            self.Data3,
            ''.join(["%02x" % d for d in self.Data4[:2]]),
            ''.join(["%02x" % d for d in self.Data4[2:]]),
        )

    @staticmethod
    def is_valid(guid: str) -> bool:
        res = GUID_PATTERN.match(guid.lower())
        return True if res else False

    @staticmethod
    def _guid_blobs(guid: str) -> list:
        res = re.findall(r'[^\W-]+', guid)
        data1 = hex_to_int(res[0])
        data2 = hex_to_int(res[1])
        data3 = hex_to_int(res[2])
        data4 = tuple(
            hex_to_int(hex_str)
            for hex_str in wrap(res[3] + res[4], 2)
        )
        return data1, data2, data3, data4

    @staticmethod
    def from_guid_string(guid: str) -> Structure:
        if GUID.is_valid(guid):
            d1, d2, d3, d4 = GUID._guid_blobs(guid)
            return GUID(d1, d2, d3, d4)
        else:
            raise InvalidGUID("Supplied value is not a valid GUID string")

    @staticmethod
    def from_bytes(buffer: bytes):
        guid = GUID()
        memmove(byref(guid), bytes(buffer), sizeof(guid))
        return guid

    @staticmethod
    def unpack_bytes(buffer: bytes):
        buf = unpack('<IHHBBBBBBBB', bytes(buffer)[:16])
        return GUID(buf[0], buf[1], buf[2], (buf[3:]))

    @staticmethod
    def check_unpack_bytes(buffer: bytes):
        buf = unpack('<IHHBBBBBBBB', bytes(buffer)[:16])
        guid_str = '{%08x-%04x-%04x-%02x%02x-%02x%02x%02x%02x%02x%02x}' % buf  # a bit slow due to extra checks
        return GUID.from_guid_string(guid_str)

    @staticmethod
    def cast_from_bytes(buffer: bytes):
        return cast(buffer, POINTER(GUID)).contents

    @staticmethod
    def clsid_from_string(guid_str: str):
        """Similar to from_string except it uses CLSIDFromString"""
        guid = GUID()
        ret = WinDLL('ole32').CLSIDFromString(create_unicode_buffer(str(guid_str)), byref(guid))
        assert ret == 0, WindowsError(GetLastError(), FormatError(GetLastError()), guid_str)
        return guid

    def __eq__(self, other):
        return True if str(self).lower() == str(other).lower() else False


def DEFINE_GUID(name, l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
    """
    Replica of native macro DEFINE_GUID 
    This should be considered insecure as it modifies global scope with user values without any checks
    """
    guid = GUID(l, w1, w2, (b1, b2, b3, b4, b5, b6, b7, b8))
    caller_scope = inspect.stack()[1][0].f_globals  # get caller global scope
    caller_scope[name] = guid  # register the new GUID name and value in the caller global scope
