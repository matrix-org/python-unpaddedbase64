Unpadded Base64
===============

Encode and decode Base64 without "=" padding.

`RFC 4648`_ specifies that Base64 should be padded to a multiple of 4 bytes
using "=" characters. However this conveys no benefit so many protocols choose
to use Base64 without the "=" padding.

.. _`RFC 4648`: https://tools.ietf.org/html/rfc4648

Installing
----------

.. code:: bash

   pip install unpaddedbase64

Using
-----

.. code:: python

    import unpaddedbase64
    assert (unpaddedbase64.encode_base64(b'\x00')) == u'AA'
    assert (unpaddedbase64.decode_base64(u'AA')) == b'\x00'
