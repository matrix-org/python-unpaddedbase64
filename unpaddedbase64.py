# Copyright 2014, 2015 OpenMarket Ltd
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

import base64

__version__ = "1.1.0"


def encode_base64(input_bytes, urlsafe=False):
    """Encode bytes as a base64 string without any padding."""

    encode = base64.urlsafe_b64encode if urlsafe else base64.b64encode
    output_bytes = encode(input_bytes)
    output_string = output_bytes.decode("ascii")
    return output_string.rstrip(u"=")


def decode_base64(input_string):
    """Decode a base64 string to bytes inferring padding from the length of the
    string."""

    input_bytes = input_string.encode("ascii")
    input_len = len(input_bytes)
    padding = b"=" * (3 - ((input_len + 3) % 4))
    decode = base64.b64decode
    if u'-' in input_string or u'_' in input_string:
        decode = base64.urlsafe_b64decode
    output_bytes = decode(input_bytes + padding)
    return output_bytes
