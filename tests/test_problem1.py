from set1.prob1 import to_base64, from_hex
import base64


def test_problem1():
    """Test as stated in the problem; passing this test passes the problem"""

    in_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    out_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    assert(to_base64(from_hex(in_string)) == out_string)


def test_problem1_extra():
    """Do some extra work with the functions used in problem 1"""

    in_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    out_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    assert(bytes.fromhex(in_string) == base64.b64decode(out_string))
    assert(base64.b64encode(bytes.fromhex(in_string)).decode('utf-8') == out_string)
