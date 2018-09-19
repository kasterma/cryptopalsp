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

import unittest


def xor(s1, s2):
    return s1


class TestProblem2(unittest.TestCase):
    in1 = "1c0111001f010100061a024b53535009181c"
    in2 = "686974207468652062756c6c277320657965"
    out = "746865206b696420646f6e277420706c6179"

    def test_problem2(self):
        self.assertEqual(xor(self.in1, self.in2), self.out)