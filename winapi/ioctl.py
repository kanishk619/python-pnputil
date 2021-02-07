from enum import IntEnum

__all__ = ['IOCTL', 'CTL_CODE']


class ACCESS(IntEnum):
    """
    https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/d4drvif/nf-d4drvif-ctl_code
    """
    FILE_ANY_ACCESS = 0x0000
    FILE_READ_ACCESS = 0x0001
    FILE_WRITE_ACCESS = 0x0002
    FILE_READ_WRITE_ACCESS = 0x0003

    def __str__(self):
        return self.name


class METHOD(IntEnum):
    """
    https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/d4drvif/nf-d4drvif-ctl_code
    """
    BUFFERED = 0
    IN_DIRECT = 1
    OUT_DIRECT = 2
    NEITHER = 3

    def __str__(self):
        return self.name


class DEVICE(IntEnum):
    FILE_DEVICE_BEEP = 1
    FILE_DEVICE_CD_ROM = 2
    FILE_DEVICE_CD_ROM_FILE_SYSTEM = 3
    FILE_DEVICE_CONTROLLER = 4
    FILE_DEVICE_DATALINK = 5
    FILE_DEVICE_DFS = 6
    FILE_DEVICE_DISK = 7
    FILE_DEVICE_DISK_FILE_SYSTEM = 8
    FILE_DEVICE_FILE_SYSTEM = 9
    FILE_DEVICE_INPORT_PORT = 10
    FILE_DEVICE_KEYBOARD = 11
    FILE_DEVICE_MAILSLOT = 12
    FILE_DEVICE_MIDI_IN = 13
    FILE_DEVICE_MIDI_OUT = 14
    FILE_DEVICE_MOUSE = 15
    FILE_DEVICE_MULTI_UNC_PROVIDER = 16
    FILE_DEVICE_NAMED_PIPE = 17
    FILE_DEVICE_NETWORK = 18
    FILE_DEVICE_NETWORK_BROWSER = 19
    FILE_DEVICE_NETWORK_FILE_SYSTEM = 20
    FILE_DEVICE_NULL = 21
    FILE_DEVICE_PARALLEL_PORT = 22
    FILE_DEVICE_PHYSICAL_NETCARD = 23
    FILE_DEVICE_PRINTER = 24
    FILE_DEVICE_SCANNER = 25
    FILE_DEVICE_SERIAL_MOUSE_PORT = 26
    FILE_DEVICE_SERIAL_PORT = 27
    FILE_DEVICE_SCREEN = 28
    FILE_DEVICE_SOUND = 29
    FILE_DEVICE_STREAMS = 30
    FILE_DEVICE_TAPE = 31
    FILE_DEVICE_TAPE_FILE_SYSTEM = 32
    FILE_DEVICE_TRANSPORT = 33
    FILE_DEVICE_UNKNOWN = 34
    FILE_DEVICE_VIDEO = 35
    FILE_DEVICE_VIRTUAL_DISK = 36
    FILE_DEVICE_WAVE_IN = 37
    FILE_DEVICE_WAVE_OUT = 38
    FILE_DEVICE_8042_PORT = 39
    FILE_DEVICE_NETWORK_REDIRECTOR = 40
    FILE_DEVICE_BATTERY = 41
    FILE_DEVICE_BUS_EXTENDER = 42
    FILE_DEVICE_MODEM = 43
    FILE_DEVICE_VDM = 44
    FILE_DEVICE_MASS_STORAGE = 45
    FILE_DEVICE_SMB = 46
    FILE_DEVICE_KS = 47
    FILE_DEVICE_CHANGER = 48
    FILE_DEVICE_SMARTCARD = 49
    FILE_DEVICE_ACPI = 50
    FILE_DEVICE_DVD = 51
    FILE_DEVICE_FULLSCREEN_VIDEO = 52
    FILE_DEVICE_DFS_FILE_SYSTEM = 53
    FILE_DEVICE_DFS_VOLUME = 54
    FILE_DEVICE_SERENUM = 55
    FILE_DEVICE_TERMSRV = 56
    FILE_DEVICE_KSEC = 57
    FILE_DEVICE_FIPS = 58
    FILE_DEVICE_INFINIBAND = 59
    FILE_DEVICE_VMBUS = 62
    FILE_DEVICE_CRYPT_PROVIDER = 63
    FILE_DEVICE_WPD = 64
    FILE_DEVICE_BLUETOOTH = 65
    FILE_DEVICE_MT_COMPOSITE = 66
    FILE_DEVICE_MT_TRANSPORT = 67
    FILE_DEVICE_BIOMETRIC = 68
    FILE_DEVICE_PMI = 69
    UNKNOWN = 0xFFFFFFF

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


class IOCTL(int):
    def __init__(self, device_type, function, method, access):
        self.device = int(device_type)
        self.function = int(function)
        self.method = int(method)
        self.access = int(access)
        self.device_name = DEVICE(self.device).name
        super().__init__()

    def __new__(cls, device_type, function, method, access):
        ioctl = (int(device_type) << 16) | (int(access) << 14) | (int(function) << 2) | int(method)
        return int.__new__(cls, ioctl)

    def __repr__(self):
        """Return hex representation for general view/usage"""
        return hex(self)

    @property
    def info(self):
        return self.device, self.function, self.method, self.access

    def __str__(self):
        info = '''
            code     : 0x%08X
            device   : %s (0x%X)
            function : 0x%X
            method   : %s (%d)
            access   : %s (%d)
        ''' % (self, self.device_name, self.device, self.function, METHOD(self.method), self.method,
               ACCESS(self.access), self.access)
        return "\n".join([l.strip() for l in info.strip().splitlines()])

    @staticmethod
    def decode(ioctl_code):
        try:
            ioctl_code = int(ioctl_code, 16)
        except TypeError:  # handle if ioctl is an int
            ioctl_code = int(ioctl_code)
        device = (ioctl_code >> 16) & 0xffff
        access = (ioctl_code >> 14) & 3
        function = (ioctl_code >> 2) & 0xfff
        method = ioctl_code & 3
        return IOCTL(device, function, method, access)


def CTL_CODE(device_type, function, method, access):
    """replica of native macro CTL_CODE"""
    return IOCTL(device_type, function, method, access)
