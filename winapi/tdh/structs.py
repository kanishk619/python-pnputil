from winapi.common.datatypes import ULONG, Structure
from winapi.guid import GUID


class TRACE_PROVIDER_INFO(Structure):
    """
    TRACE_PROVIDER_INFO structure
    =============================

    -description
    ------------

    Defines the GUID and name for a provider.

    -struct-fields
    --------------

    -field ProviderGuid
    ~~~~~~~~~~~~~~~~~~~

    GUID that uniquely identifies the provider.

    -field SchemaSource
    ~~~~~~~~~~~~~~~~~~~

    Is zero if the provider uses a XML manifest to provide a description of
    its events. Otherwise, the value is 1 if the provider uses a WMI MOF
    class to provide a description of its events.

    -field ProviderNameOffset
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Offset to a null-terminated Unicode string that contains the name of the
    provider. The offset is from the beginning of the
    PROVIDER_ENUMERATION_INFO buffer that TdhEnumerateProviders returns.

    -see-also
    ---------

    PROVIDER_ENUMERATION_INFO
    """
    _fields_ = [
        ("ProviderGuid", GUID),
        ("SchemaSource", ULONG),
        ("ProviderNameOffset", ULONG)
    ]


class PROVIDER_ENUMERATION_INFO(Structure):
    """
    PROVIDER_ENUMERATION_INFO structure
    ===================================

    -description
    ------------

    Defines the array of providers that have registered a MOF or manifest on
    the computer.

    -struct-fields
    --------------

    -field NumberOfProviders
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Number of elements in the TraceProviderInfoArray array.

    -field Reserved
    ~~~~~~~~~~~~~~~

    -field TraceProviderInfoArray
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Array of TRACE_PROVIDER_INFO structures that contain information about
    each provider such as its name and unique identifier.

    - Padding
    ^^^^^^^^^

    Reserved.

    -see-also
    ---------

    TdhEnumerateProviders

    https://docs.microsoft.com/en-us/windows/win32/api/tdh/ns-tdh-provider_enumeration_info
    """
    ANYSIZE_ARRAY = 1  # define ANYSIZE_ARRAY 1
    _fields_ = [
        ("NumberOfProviders", ULONG),
        ("Reserved", ULONG),
        ("TraceProviderInfoArray", (TRACE_PROVIDER_INFO * ANYSIZE_ARRAY))
    ]

    def __new__(cls, *args, trace_provider_info_array_size=None, **kwargs):
        """
        TODO: implement a better way to do dynamic buffer allocation
        :param args:
        :param trace_provider_info_array_size:
        :param kwargs:
        """
        if trace_provider_info_array_size:
            class tmp(cls):
                _fields_ = [("TraceProviderInfoArray", (TRACE_PROVIDER_INFO * trace_provider_info_array_size))]
            obj = tmp()
        else:
            obj = super().__new__(cls)
        return obj


