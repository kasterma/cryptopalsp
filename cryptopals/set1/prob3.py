# Single-byte XOR cipher
#
# The hex encoded string:
#
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.
#
# You can do this by hand. But don't: write code to do it for you.
#
# How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate
# each output and choose the one with the best score.
#
# Achievement Unlocked
# You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.

import json
import sys

cypher1 = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")


def attempt(cypher_bytes, key_int):
    return bytes(b ^ key_int for b in cypher_bytes)


def printable(i):
    """Is the integer i printable as ascii"""
    lower = int.from_bytes(bytes.fromhex('20'), sys.byteorder)
    upper = int.from_bytes(bytes.fromhex('7e'), sys.byteorder)
    return lower <= i <= upper


def search(cypher_bytes):
    """Assume the message is of only printable characters"""
    possibles = {}
    for i in range(256):
        a = attempt(cypher_bytes, i)
        p = [printable(i) for i in a]
        if all(p):
            possibles[str(i)] = a
    return possibles


possibles = search(cypher1)

# This gives 17 possibilities, of which only 1 reads like a sentence
print(json.dumps({k: v.decode('ascii') for k, v in possibles.items()}, indent=2))


def dict_dist(d1: dict, d2: dict) -> int:
    """Distance between two dictionaries"""
    keys = set(d1.keys()).union(set(d2.keys()))
    d = 0
    for key in keys:
        d += abs(d1.get(key, 20) - d2.get(key, 20))  # 20 is penalty for difference in keys
        # this penalty makes sense since 20 is a large number compared to the length of the strings
    return d


eng_freq = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.360,
    "x": 0.150,
    "y": 1.974,
    "z": 0.074}

target_freq = {c: v/100 * len(cypher1) for c, v in eng_freq.items()}

decodes = {i: attempt(cypher1, i) for i in range(255)}

import pandas as pd
pd.Series(list(decodes[0].decode('utf-8'))).value_counts()

from collections import Counter

cts = {k: Counter(v.decode('utf-8', errors='ignore'))
       for k, v in decodes.items()
       if len(v) == len(v.decode('utf-8', errors='ignore'))}

dists = {k: dict_dist(target_freq, dict(ct)) for k, ct in cts.items()}

best = {k: decodes[k].decode('utf-8') for k, ct in dists.items() if ct == min(dists.values())}
