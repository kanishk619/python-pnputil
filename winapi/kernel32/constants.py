from enum import IntEnum

CREATE_ALWAYS = 0x00000002
LOCKFILE_EXCLUSIVE_LOCK = 0x00000002
LOCKFILE_FAIL_IMMEDIATELY = 0x00000001


class GENERIC(IntEnum):
    """
    https://docs.microsoft.com/en-us/windows/win32/secauthz/generic-access-rights
    https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/262970b7-cd4a-41f4-8c4d-5a27f0092aaa
    """
    ALL = 0x10000000
    EXECUTE = 0x20000000
    NONE = 0x00000000
    READ = 0x80000000
    WRITE = 0x40000000

