import base64


def count_nonzero_bits(b):
    ct = 0
    while b != 0:
        if b & 1 != 0:
            ct += 1
        b = b >> 1
    return ct

def test_cnb():
    assert count_nonzero_bits(1) == 1
    assert count_nonzero_bits(2) == 1
    assert count_nonzero_bits(3) == 2

def hamming(x1, x2):
    return sum(count_nonzero_bits(b1 ^ b2) for b1, b2 in zip(x1, x2))

def test_hamming():
    s1 = "this is a test"
    s2 = "wokka wokka!!!"

    i1 = s1.encode()
    i2 = s2.encode()

    assert hamming(i1, i2) == 37

with open("data/dat_set1_prob6.txt") as f:
    dat = f.readlines()
dat_bytes = b''.join([base64.b64decode(s) for s in dat])
