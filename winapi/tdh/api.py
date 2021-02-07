from .structs import *
from ctypes import windll
from .datatypes import TDHSTATUS


tdh = windll.tdh


class TdhEnumerateProviders(object):
    """
    TdhEnumerateProviders function
    ==============================

    -description
    ------------

    Retrieves a list of providers that have registered a MOF class or
    manifest file on the computer.

    -parameters
    -----------

    -param pBuffer [out]
    ~~~~~~~~~~~~~~~~~~~~

    Array of providers that publicly define their events on the computer.
    For details, see the PROVIDER_ENUMERATION_INFO structure.

    -param pBufferSize [in, out]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Size, in bytes, of the pBuffer buffer. If the function succeeds, this
    parameter receives the size of the buffer used. If the buffer is too
    small, the function returns ERROR_INSUFFICIENT_BUFFER and sets this
    parameter to the required buffer size. If the buffer size is zero on
    input, no data is returned in the buffer and this parameter receives the
    required buffer size.

    -returns
    --------

    Returns ERROR_SUCCESS if successful. Otherwise, this function returns
    one of the following return codes in addition to others.

    .. raw:: html

       <table>

    .. raw:: html

       <tr>

    .. raw:: html

       <th>

    Return code

    .. raw:: html

       </th>

    .. raw:: html

       <th>

    Description

    .. raw:: html

       </th>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INSUFFICIENT_BUFFER

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    The size of the pBuffer buffer is too small. Use the required buffer
    size set in pBufferSize to allocate a new buffer.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td width="40%">

    .. raw:: html

       <dl>

    .. raw:: html

       <dt>

    ERROR_INVALID_PARAMETER

    .. raw:: html

       </dt>

    .. raw:: html

       </dl>

    .. raw:: html

       </td>

    .. raw:: html

       <td width="60%">

    One or more of the parameters is not valid.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

    -remarks
    --------

    Because the number of registered event providers may fluctuate between
    calls to this function, you should place this function in a loop that
    loops until the returned value is no longer ERROR_INSUFFICIENT_BUFFER.

    Examples
    ^^^^^^^^

    For an example that shows how to enumerate providers, see Enumerating
    Providers.

    .. container:: code

    -see-also
    ---------

    TdhEnumerateProviderFieldInformation
    """
    def __new__(cls, *args, **kwargs):
        """
        TDHSTATUS TdhEnumerateProviders(
            PPROVIDER_ENUMERATION_INFO pBuffer,
            ULONG                      *pBufferSize
        );
        https://docs.microsoft.com/en-us/windows/win32/api/tdh/nf-tdh-tdhenumerateproviders
        """
        func = tdh.TdhEnumerateProviders
        func.argtypes = [
            POINTER(PROVIDER_ENUMERATION_INFO),
            POINTER(ULONG)
        ]
        func.restype = TDHSTATUS
        return func(*args)
