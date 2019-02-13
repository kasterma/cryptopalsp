from set1.prob2 import xor


def test_problem2():
    in1 = "1c0111001f010100061a024b53535009181c"
    in2 = "686974207468652062756c6c277320657965"
    out = "746865206b696420646f6e277420706c6179"

    assert(xor(in1, in2) == out)
