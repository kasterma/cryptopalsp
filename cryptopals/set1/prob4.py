import unittest
from collections import Counter
from typing import List

from set1.utils import apply_key

with open("dat_prob4.txt") as f:
    dat = [s.strip() for s in f.readlines()]

ETAOIN = " etaoinshrdlu"
dat.append(apply_key(bytes("hello hello hello hello hello".encode("ascii")), 12).hex())


def try_candidate(e: int, top: List[chr], *, etaoin_k):
    key_candidate = ord('e') ^ e
    for l in top:  # note: the candidate for e is also in here, but that passed this test
        if not chr(l ^ key_candidate).lower() in ETAOIN[:etaoin_k]:
            return
    return key_candidate


def find_possible_keys(s, *, top_k=3, etaoin_k=6):
    # get the counts of the letters in the string
    cts = Counter(bytes.fromhex(s))
    # try to the top top_k occurrences as encodings of e
    # we believe we have found a valid encoding if the other two most common decode to letters also
    # in etaoinshrdlu[:etaoin_k]
    top = [l for l, _ in cts.most_common(top_k)]
    possible_keys = []
    for e_candidate in top:
        key = try_candidate(e_candidate, top, etaoin_k=etaoin_k)
        if key:
            possible_keys.append(key)
    return possible_keys


def decode(s: str, key: int) -> str:
    """Decode the string with the given key

    @:param s string containing the ciphertext in hex encoding
    @:param key the integer key (or proposed key)
    """
    return bytes(key ^ b for b in bytes.fromhex(s)).decode('ascii')


def decode2ascii(s: str, key: int) -> str:
    """Decode the string with the given key

    @:param s string containing the ciphertext in hex encoding
    @:param key the integer key (or proposed key)
    """
    return "".join([chr(x) for x in bytes(key ^ b for b in bytes.fromhex(s))])


def encode_from_ascii(s: str, k: int) -> str:
    """Encode an ascii string.

    @:param s the asci string to encode
    @:param k the key
    @:return hex encoded cipher string
    """
    s_nos = [ord(c) for c in s]
    s_cipher = [k ^ n for n in s_nos]
    cipher = bytes(s_cipher)
    return cipher.hex()


class TestDecode(unittest.TestCase):
    def test(self):
        self.assertEqual(decode2ascii(encode_from_ascii("hello", 88), 88), "hello")
        self.assertEqual(encode_from_ascii(decode2ascii("112233", 88), 88), "112233")


xx = {idx: find_possible_keys(l, top_k=3, etaoin_k=13) for idx, l in enumerate(dat)}

xx = {k: v for k, v in xx.items() if len(v) > 0}

find_possible_keys(dat[179])
decode2ascii(dat[179], 88)

print(xx)
for idx, keys in xx.items():
    for key in keys:
        try:
            print(decode(dat[idx], key))
        except:  # noqa: E722
            print("eror")
