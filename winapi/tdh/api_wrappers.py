from ctypes import wstring_at, addressof
from .api import *
from winapi.common.winerror_h import ERROR_INSUFFICIENT_BUFFER, ERROR_SUCCESS


def tdh_enumerate_providers():
    buffer_size = ULONG()
    status = TdhEnumerateProviders(None, buffer_size)
    assert status == ERROR_INSUFFICIENT_BUFFER

    penum = PROVIDER_ENUMERATION_INFO(trace_provider_info_array_size=buffer_size.value)
    status = TdhEnumerateProviders(penum, buffer_size)
    assert status == ERROR_SUCCESS

    for i in range(0, penum.NumberOfProviders - 1):
        provider_guid = str(penum.TraceProviderInfoArray[i].ProviderGuid)
        provider_name = wstring_at(penum.TraceProviderInfoArray[i].ProviderNameOffset + addressof(penum))
        provider_schema = 'XML manifest' if penum.TraceProviderInfoArray[i].SchemaSource == 0 else 'WMI MOF Class'
        print(f"Provider name: {provider_name}")
        print(f"Provider GUID: {provider_guid}")
        print(f"Source: {provider_schema}")
        print("")

