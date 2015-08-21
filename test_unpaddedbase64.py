from unpaddedbase64 import encode_base64, decode_base64
import unittest


class TestStringMethods(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(encode_base64(b''), u'')
        self.assertEqual(encode_base64(b'\x00'), u'AA')
        self.assertEqual(encode_base64(b'\x00\x00'), u'AAA')
        self.assertEqual(encode_base64(b'\x00\x00\x00'), u'AAAA')

    def test_decode(self):
        self.assertEqual(decode_base64(u''), b'')
        self.assertEqual(decode_base64(u'AA'), b'\x00')
        self.assertEqual(decode_base64(u'AAA'), b'\x00\x00')
        self.assertEqual(decode_base64(u'AAAA'), b'\x00\x00\x00')
        with self.assertRaises(Exception):
            decode_base64(u'A')
