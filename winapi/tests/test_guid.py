from winapi.guid import GUID
from unittest import TestCase
from winapi.guid import DEFINE_GUID


class GuidTest(TestCase):
    guid_bytes = b'o\xe96M%\xe3\xce\x11\xbf\xc1\x08\x00+\xe1\x03\x18'
    guid_str = "{4d36e96f-e325-11ce-bfc1-08002be10318}"     # mouse
    intel_mei = "{e2d1ff34-3458-49a9-88da-8e6915ce9be5}"

    def test_from_bytes(self):
        self.assertEqual(str(GUID.from_bytes(self.guid_bytes)), self.guid_str)

    def test_unpack_bytes(self):
        self.assertEqual(str(GUID.unpack_bytes(self.guid_bytes)), self.guid_str)

    def test_check_unpack_bytes(self):
        self.assertEqual(str(GUID.check_unpack_bytes(self.guid_bytes)), self.guid_str)

    def test_cast_from_bytes(self):
        self.assertEqual(str(GUID.cast_from_bytes(self.guid_bytes)), self.guid_str)

    def test_clsid_from_string(self):
        self.assertEqual(str(GUID.clsid_from_string(self.guid_str)), self.guid_str)

    def test_from_buffer(self):
        g = GUID.from_bytes(self.guid_bytes)
        self.assertEqual(GUID.from_buffer(g), self.guid_str)

    def test_define_guid(self):
        DEFINE_GUID("GUID_DEVINTERFACE_HECI", 0xE2D1FF34, 0x3458, 0x49A9,
                    0x88, 0xDA, 0x8E, 0x69, 0x15, 0xCE, 0x9B, 0xE5)
        self.assertTrue("GUID_DEVINTERFACE_HECI" in globals())
        self.assertEqual(GUID_DEVINTERFACE_HECI, self.intel_mei)
