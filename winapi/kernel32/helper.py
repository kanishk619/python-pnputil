from .structs import SYSTEMTIME
from .api import GetLocalTime, GetSystemTime

__all__ = ['get_local_time', 'get_system_time']


def get_local_time() -> SYSTEMTIME:
    """
    Retrieves the current local date and time.
    :return: SYSTEMTIME Stucture
    """
    st = SYSTEMTIME()
    GetLocalTime(st)
    return st


def get_system_time() -> SYSTEMTIME:
    """
    Retrieves the current local date and time.
    :return: SYSTEMTIME Stucture
    """
    st = SYSTEMTIME()
    GetSystemTime(st)
    return st
