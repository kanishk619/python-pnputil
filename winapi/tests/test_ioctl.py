from unittest import TestCase

from winioctlcon import CTL_CODE

from winapi.ioctl import IOCTL, ACCESS, METHOD


class IoctlTest(TestCase):
    def test_create(self):
        ioctl = CTL_CODE(0x8000, 0x801, METHOD.NEITHER, ACCESS.FILE_READ_ACCESS | ACCESS.FILE_WRITE_ACCESS)
        self.assertEqual(ioctl, 0x8000E007)

    def test_decode(self):
        ioctl = IOCTL.decode(0x8000E007)
        self.assertEqual(ioctl.method, METHOD.NEITHER)
        self.assertEqual(ioctl.access, ACCESS.FILE_READ_ACCESS | ACCESS.FILE_WRITE_ACCESS)
        self.assertEqual(ioctl.device, 0x8000)
        self.assertEqual(ioctl, 0x8000E007)
