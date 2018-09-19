# Convert hex to base64
#
# The string:
#
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce:
#
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
# So go ahead and make that happen. You'll need to use this code for the rest of the exercises.
#
# Rule: alsway operate on raw bytes, never on encoded strings.  Only use hex and base64 for pretty-printing.

# Learn how to deal with different encodings in python

import unittest

def from_hex(s):
    return s

def to_base64(s):
    return s


class TestProblem1(unittest.TestCase):
    in_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d""
    out_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    def test_problem1(self):
        self.assertEqual(to_base64(from_hex(self.in_string)), self.out_string)