import datetime
from ctypes import byref, GetLastError

from winapi.common.datatypes import *

__all__ = ['BY_HANDLE_FILE_INFORMATION', 'FILETIME', 'OVERLAPPED', 'SECURITY_ATTRIBUTES', 'SYSTEMTIME',
           'TIME_DYNAMIC_ZONE_INFORMATION', 'TIME_ZONE_INFORMATION']


class SYSTEMTIME(Structure):
    """
    typedef struct _SYSTEMTIME {
        WORD wYear;
        WORD wMonth;
        WORD wDayOfWeek;
        WORD wDay;
        WORD wHour;
        WORD wMinute;
        WORD wSecond;
        WORD wMilliseconds;
    } SYSTEMTIME, *PSYSTEMTIME, *LPSYSTEMTIME;
    https://docs.microsoft.com/en-us/windows/win32/api/minwinbase/ns-minwinbase-systemtime
    """
    _fields_ = [
        ('wYear', WORD),
        ('wMonth', WORD),
        ('wDayOfWeek', WORD),
        ('wDay', WORD),
        ('wHour', WORD),
        ('wMinute', WORD),
        ('wSecond', WORD),
        ('wMilliseconds', WORD),
    ]

    def to_python(self):
        """
        :return: A python datetime object
        """
        return datetime.datetime(self.wYear, self.wMonth, self.wDay, self.wHour,
                                 self.wMinute, self.wSecond, self.wMilliseconds * 1000)

    def to_string(self):
        """
        :return: A string representation of Python datetime object as d/m/Y H:M:S:f"
        """
        return self.to_python().strftime("%d/%m/%Y %H:%M:%S:%f")[:-3]

    def __eq__(self, other):
        return str(self) == str(other)

    def __str__(self):
        return self.to_string()


class FILETIME(Structure):
    """
    typedef struct _FILETIME {
        DWORD dwLowDateTime;
        DWORD dwHighDateTime;
    } FILETIME, *PFILETIME, *LPFILETIME;
    https://docs.microsoft.com/en-us/windows/win32/api/minwinbase/ns-minwinbase-filetime
    """
    _fields_ = [
        ("dwLowDateTime", DWORD),
        ("dwHighDateTime", DWORD)
    ]

    def __str__(self):
        return hex(self.dwLowDateTime + self.dwHighDateTime)

    def to_system_time(self) -> SYSTEMTIME:
        """
        Converts file time to system time (UTC)
        :return: SYSTEMTIME struct
        """
        from winapi.kernel32.api import FileTimeToSystemTime
        st = SYSTEMTIME()
        r = FileTimeToSystemTime(byref(self), st)
        assert r != 0, GetLastError()
        return st

    def to_local_time(self) -> SYSTEMTIME:
        """
        Converts file time to local time based on currently active time zone
        :return: SYSTEMTIME struct
        """
        from winapi.kernel32.api import SystemTimeToTzSpecificLocalTime
        st = SYSTEMTIME()
        r = SystemTimeToTzSpecificLocalTime(
            None,
            byref(self.to_system_time()),
            byref(st)
        )
        assert r != 0, GetLastError()
        return st


class BY_HANDLE_FILE_INFORMATION(Structure):
    """
    typedef struct _BY_HANDLE_FILE_INFORMATION {
        DWORD    dwFileAttributes;
        FILETIME ftCreationTime;
        FILETIME ftLastAccessTime;
        FILETIME ftLastWriteTime;
        DWORD    dwVolumeSerialNumber;
        DWORD    nFileSizeHigh;
        DWORD    nFileSizeLow;
        DWORD    nNumberOfLinks;
        DWORD    nFileIndexHigh;
        DWORD    nFileIndexLow;
    } BY_HANDLE_FILE_INFORMATION, *PBY_HANDLE_FILE_INFORMATION, *LPBY_HANDLE_FILE_INFORMATION;
    https://docs.microsoft.com/en-us/windows/win32/api/fileapi/ns-fileapi-by_handle_file_information
    """
    _fields_ = [
        ('dwFileAttributes', DWORD),
        ('ftCreationTime', FILETIME),
        ('ftLastAccessTime', FILETIME),
        ('ftLastWriteTime', FILETIME),
        ('dwVolumeSerialNumber', DWORD),
        ('nFileSizeHigh', DWORD),
        ('nFileSizeLow', DWORD),
        ('nNumberOfLinks', DWORD),
        ('nFileIndexHigh', DWORD),
        ('nFileIndexLow', DWORD)
    ]


class OVERLAPPED(Structure):
    """
    Overlapped is required and used in LockFileEx and UnlockFileEx.
    https://docs.microsoft.com/en-us/windows/win32/api/minwinbase/ns-minwinbase-overlapped
    """
    _fields_ = [
        ('Internal', LPVOID),
        ('InternalHigh', LPVOID),
        ('Offset', DWORD),
        ('OffsetHigh', DWORD),
        ('Pointer', LPVOID),
        ('hEvent', HANDLE)
    ]


class TIME_ZONE_INFORMATION(Structure):
    """
    typedef struct _TIME_ZONE_INFORMATION {
      LONG       Bias;
      WCHAR      StandardName[32];
      SYSTEMTIME StandardDate;
      LONG       StandardBias;
      WCHAR      DaylightName[32];
      SYSTEMTIME DaylightDate;
      LONG       DaylightBias;
    } TIME_ZONE_INFORMATION, *PTIME_ZONE_INFORMATION, *LPTIME_ZONE_INFORMATION;
    https://docs.microsoft.com/en-us/windows/win32/api/timezoneapi/ns-timezoneapi-time_zone_information
    """
    _fields_ = [
        ("Bias", LONG),
        ("StandardName", WCHAR),
        ("StandardDate", SYSTEMTIME),
        ("StandardBias", LONG),
        ("DaylightName", WCHAR),
        ("DaylightDate", SYSTEMTIME),
        ("DaylightBias", LONG),
    ]


class TIME_DYNAMIC_ZONE_INFORMATION(Structure):
    """
    typedef struct _TIME_DYNAMIC_ZONE_INFORMATION {
        LONG       Bias;
        WCHAR      StandardName[32];
        SYSTEMTIME StandardDate;
        LONG       StandardBias;
        WCHAR      DaylightName[32];
        SYSTEMTIME DaylightDate;
        LONG       DaylightBias;
        WCHAR      TimeZoneKeyName[128];
        BOOLEAN    DynamicDaylightTimeDisabled;
    } DYNAMIC_TIME_ZONE_INFORMATION, *PDYNAMIC_TIME_ZONE_INFORMATION;
    https://docs.microsoft.com/en-us/windows/win32/api/timezoneapi/ns-timezoneapi-dynamic_time_zone_information
    """
    _fields_ = [
        ("Bias", LONG),
        ("StandardName", WCHAR),
        ("StandardDate", SYSTEMTIME),
        ("StandardBias", LONG),
        ("DaylightName", WCHAR),
        ("DaylightDate", SYSTEMTIME),
        ("DaylightBias", LONG),
        ("TimeZoneKeyName", WCHAR),
        ("DynamicDaylightTimeDisabled", BOOLEAN),
    ]


class SECURITY_ATTRIBUTES(Structure):
    """
    typedef struct _SECURITY_ATTRIBUTES {
      DWORD nLength;
      LPVOID lpSecurityDescriptor;
      BOOL bInheritHandle;
    } SECURITY_ATTRIBUTES, *PSECURITY_ATTRIBUTES, *LPSECURITY_ATTRIBUTES;
    https://docs.microsoft.com/en-us/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)
    """
    _fields_ = [
        ("nLength", DWORD),
        ("lpSecurityDescriptor", LPVOID),
        ("bInheritHandle", BOOL)
    ]
