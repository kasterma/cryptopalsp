# Single-byte XOR cipher
#
# The hex encoded string:
#
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.
#
# You can do this by hand. But don't: write code to do it for you.
#
# How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
#
# Achievement Unlocked
# You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.

import sys
import json


cypher1 = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")


def attempt(cypher_bytes, key_int):
    return bytes(b ^ key_int for b in cypher_bytes)


def printable(i):
    """Is the integer i printable as ascii"""
    l = int.from_bytes(bytes.fromhex('20'), sys.byteorder)
    u = int.from_bytes(bytes.fromhex('7e'), sys.byteorder)
    return l <= i <= u


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
print(json.dumps({k:v.decode('ascii') for k, v in possibles.items()}, indent=2))