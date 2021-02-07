from ctypes import windll
from winapi.common.datatypes import *


__all__ = [
    'CloseClipboard', 'EmptyClipboard', 'GetClipboardData', 'OpenClipboard', 'SetClipboardData'
]


user32 = windll.user32


class OpenClipboard(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-openclipboard

    OpenClipboard function
    ======================

    -description
    ------------

    Opens the clipboard for examination and prevents other applications from
    modifying the clipboard content.

    -parameters
    -----------

    -param hWndNewOwner [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Type: HWND

    A handle to the window to be associated with the open clipboard. If this
    parameter is NULL, the open clipboard is associated with the current
    task.

    -returns
    --------

    Type: BOOL

    If the function succeeds, the return value is nonzero.

    If the function fails, the return value is zero. To get extended error
    information, call GetLastError.

    -remarks
    --------

    OpenClipboard fails if another window has the clipboard open.

    An application should call the CloseClipboard function after every
    successful call to OpenClipboard.

    The window identified by the hWndNewOwner parameter does not become the
    clipboard owner unless the EmptyClipboard function is called.

    If an application calls OpenClipboard with hwnd set to NULL,
    EmptyClipboard sets the clipboard owner to NULL; this causes
    SetClipboardData to fail.

    Examples
    ^^^^^^^^

    For an example, see Copying Information to the Clipboard.

    .. container:: code

    -see-also
    ---------

    Clipboard

    CloseClipboard

    Conceptual

    EmptyClipboard

    Reference
    """

    def __new__(cls,
                hWndNewOwner: HWND = None
                ) -> BOOL:
        """

        :param hWndNewOwner: HWND [in, optional]
        :return: BOOL
        """

        func = user32.OpenClipboard
        func.argtypes = [
            HWND
        ]
        func.restype = BOOL
        return func(hWndNewOwner)


class SetClipboardData(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setclipboarddata

    SetClipboardData function
    =========================

    -description
    ------------

    Places data on the clipboard in a specified clipboard format. The window
    must be the current clipboard owner, and the application must have
    called the `OpenClipboard <nf-winuser-openclipboard.md>`__ function.
    (When responding to the
    `WM_RENDERFORMAT </windows/win32/dataxchg/wm-renderformat>`__ message,
    the clipboard owner must not call **OpenClipboard** before calling
    **SetClipboardData**.)

    -parameters
    -----------

    -param uFormat [in]
    ~~~~~~~~~~~~~~~~~~~

    Type: UINT

    The clipboard format. This parameter can be a registered format or any
    of the standard clipboard formats. For more information, see Standard
    Clipboard Formats and Registered Clipboard Formats.

    -param hMem [in, optional]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Type: HANDLE

    A handle to the data in the specified format. This parameter can be
    NULL, indicating that the window provides data in the specified
    clipboard format (renders the format) upon request; this is known as
    `delayed
    rendering </windows/win32/dataxchg/clipboard-operations#delayed-rendering>`__.
    If a window delays rendering, it must process the
    `WM_RENDERFORMAT </windows/win32/dataxchg/wm-renderformat>`__ and
    `WM_RENDERALLFORMATS </windows/win32/dataxchg/wm-renderallformats>`__
    messages.

    If SetClipboardData succeeds, the system owns the object identified by
    the hMem parameter. The application may not write to or free the data
    once ownership has been transferred to the system, but it can lock and
    read from the data until the CloseClipboard function is called. (The
    memory must be unlocked before the Clipboard is closed.) If the hMem
    parameter identifies a memory object, the object must have been
    allocated using the function with the GMEM_MOVEABLE flag.

    -returns
    --------

    Type: HANDLE

    If the function succeeds, the return value is the handle to the data.

    If the function fails, the return value is NULL. To get extended error
    information, call GetLastError.

    -remarks
    --------

    Windows : Bitmaps to be shared with Windows Store app apps must be in
    the CF_BITMAP format (device-dependent bitmap).

    If an application calls SetClipboardData in response to WM_RENDERFORMAT
    or WM_RENDERALLFORMATS, the application should not use the handle after
    SetClipboardData has been called.

    If an application calls OpenClipboard with hwnd set to NULL,
    EmptyClipboard sets the clipboard owner to NULL; this causes
    SetClipboardData to fail.

    The system performs implicit data format conversions between certain
    clipboard formats when an application calls the GetClipboardData
    function. For example, if the CF_OEMTEXT format is on the clipboard, a
    window can retrieve data in the CF_TEXT format. The format on the
    clipboard is converted to the requested format on demand. For more
    information, see Synthesized Clipboard Formats.

    Examples
    ^^^^^^^^

    For an example, see Copying Information to the Clipboard.

    .. container:: code

    -see-also
    ---------

    Clipboard

    CloseClipboard

    Conceptual

    GetClipboardData

    OpenClipboard

    Reference

    RegisterClipboardFormat

    WM_RENDERALLFORMATS

    WM_RENDERFORMAT
    """

    def __new__(cls,
                uFormat: UINT = None,
                hMem: HANDLE = None
                ) -> HANDLE:
        """

        :param uFormat: UINT [in]
        :param hMem: HANDLE [in, optional]
        :return: HANDLE
        """

        func = user32.SetClipboardData
        func.argtypes = [
            UINT,
            HANDLE
        ]
        func.restype = HANDLE
        return func(uFormat, hMem)


class CloseClipboard(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-closeclipboard

    CloseClipboard function
    =======================

    -description
    ------------

    Closes the clipboard.

    -parameters
    -----------

    -returns
    --------

    Type: BOOL

    If the function succeeds, the return value is nonzero.

    If the function fails, the return value is zero. To get extended error
    information, call GetLastError.

    -remarks
    --------

    When the window has finished examining or changing the clipboard, close
    the clipboard by calling CloseClipboard. This enables other windows to
    access the clipboard.

    Do not place an object on the clipboard after calling CloseClipboard.

    Examples
    ^^^^^^^^

    For an example, see Example of a Clipboard Viewer.

    .. container:: code

    -see-also
    ---------

    Clipboard

    Conceptual

    GetOpenClipboardWindow

    OpenClipboard

    Reference
    """

    def __new__(cls) -> BOOL:
        """

        :return: BOOL
        """

        func = user32.CloseClipboard
        func.argtypes = [

        ]
        func.restype = BOOL
        return func()


class EmptyClipboard(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-emptyclipboard

    EmptyClipboard function
    =======================

    -description
    ------------

    Empties the clipboard and frees handles to data in the clipboard. The
    function then assigns ownership of the clipboard to the window that
    currently has the clipboard open.

    -parameters
    -----------

    -returns
    --------

    Type: BOOL

    If the function succeeds, the return value is nonzero.

    If the function fails, the return value is zero. To get extended error
    information, call GetLastError.

    -remarks
    --------

    Before calling EmptyClipboard, an application must open the clipboard by
    using the OpenClipboard function. If the application specifies a NULL
    window handle when opening the clipboard, EmptyClipboard succeeds but
    sets the clipboard owner to NULL. Note that this causes SetClipboardData
    to fail.

    Examples
    ^^^^^^^^

    For an example, see Copying Information to the Clipboard.

    .. container:: code

    -see-also
    ---------

    Clipboard

    Conceptual

    OpenClipboard

    Reference

    SetClipboardData

    WM_DESTROYCLIPBOARD
    """

    def __new__(cls) -> BOOL:
        """

        :return: BOOL
        """

        func = user32.EmptyClipboard
        func.argtypes = [

        ]
        func.restype = BOOL
        return func()


class GetClipboardData(object):
    """
    https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getclipboarddata

    GetClipboardData function
    =========================

    -description
    ------------

    Retrieves data from the clipboard in a specified format. The clipboard
    must have been opened previously.

    -parameters
    -----------

    -param uFormat [in]
    ~~~~~~~~~~~~~~~~~~~

    Type: UINT

    A clipboard format. For a description of the standard clipboard formats,
    see Standard Clipboard Formats.

    -returns
    --------

    Type: HANDLE

    If the function succeeds, the return value is the handle to a clipboard
    object in the specified format.

    If the function fails, the return value is NULL. To get extended error
    information, call GetLastError.

    -remarks
    --------

    .. container:: alert

       Caution Clipboard data is not trusted. Parse the data carefully
       before using it in your application.

    .. container::



    An application can enumerate the available formats in advance by using
    the EnumClipboardFormats function.

    The clipboard controls the handle that the GetClipboardData function
    returns, not the application. The application should copy the data
    immediately. The application must not free the handle nor leave it
    locked. The application must not use the handle after the EmptyClipboard
    or CloseClipboard function is called, or after the SetClipboardData
    function is called with the same clipboard format.

    The system performs implicit data format conversions between certain
    clipboard formats when an application calls the GetClipboardData
    function. For example, if the CF_OEMTEXT format is on the clipboard, a
    window can retrieve data in the CF_TEXT format. The format on the
    clipboard is converted to the requested format on demand. For more
    information, see Synthesized Clipboard Formats.

    Examples
    ^^^^^^^^

    For an example, see Copying Information to the Clipboard.

    .. container:: code

    -see-also
    ---------

    Clipboard

    CloseClipboard

    Conceptual

    EmptyClipboard

    EnumClipboardFormats

    Reference

    SetClipboardData
    """

    def __new__(cls,
                uFormat: UINT = None
                ) -> HANDLE:
        """

        :param uFormat: UINT [in]
        :return: HANDLE
        """

        func = user32.GetClipboardData
        func.argtypes = [
            UINT
        ]
        func.restype = HANDLE
        return func(uFormat)
