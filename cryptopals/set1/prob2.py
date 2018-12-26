# Fixed XOR
#
# Write a function that takes two equal-length buffers and produces their XOR combination.
#
# If your function works properly, then when you feed it the string:
#
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
#
# 686974207468652062756c6c277320657965
# ... should produce:
#
# 746865206b696420646f6e277420706c6179

import sys


def xor(s1, s2):
    i1 = int.from_bytes(bytes.fromhex(s1), byteorder=sys.byteorder)
    i2 = int.from_bytes(bytes.fromhex(s2), byteorder=sys.byteorder)
    iout = i1 ^ i2
    return iout.to_bytes(len(bytes.fromhex(s1)), byteorder=sys.byteorder).hex()
