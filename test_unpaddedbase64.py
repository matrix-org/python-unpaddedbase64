# Copyright 2015 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unpaddedbase64 import encode_base64, decode_base64
import unittest


class TestUnpaddedBase64(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode_base64(b""), "")
        self.assertEqual(encode_base64(b"\x00"), "AA")
        self.assertEqual(encode_base64(b"\x00\x00"), "AAA")
        self.assertEqual(encode_base64(b"\x00\x00\x00"), "AAAA")

    def test_decode(self):
        self.assertEqual(decode_base64(""), b"")
        self.assertEqual(decode_base64("AA"), b"\x00")
        self.assertEqual(decode_base64("AAA"), b"\x00\x00")
        self.assertEqual(decode_base64("AAAA"), b"\x00\x00\x00")
        with self.assertRaises(Exception):
            decode_base64("A")

    def test_encode_urlunsafe_chars(self):
        self.assertEqual(encode_base64(b"\xff\xe6\x9a"), "/+aa")
        self.assertEqual(encode_base64(b"\xff\xe6\x9a", True), "_-aa")

    def test_decode_urlunsafe_chars(self):
        self.assertEqual(decode_base64("/+aa"), b"\xff\xe6\x9a")
        self.assertEqual(decode_base64("_-aa"), b"\xff\xe6\x9a")
