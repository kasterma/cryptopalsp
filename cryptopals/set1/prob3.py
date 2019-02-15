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

from set1.utils import apply_key, printable, eng_freq, get_freqtable, dict_dist

cypher1 = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")


# First attempt: look for a message that has all its characters printable
def search(cypher_bytes):
    """Assume the message is of only printable characters"""
    possibles = {}
    for i in range(256):
        a = apply_key(cypher_bytes, i)
        p = [printable(i) for i in a]
        if all(p):
            possibles[str(i)] = a
    return possibles


possibles = search(cypher1)

# This gives 17 possibilities, of which only 1 reads like a sentence
print(json.dumps({k: v.decode('ascii') for k, v in possibles.items()}, indent=2))


# Second attempt; use the distribution of letters in English to find the message that is closest to it
target_freq = {c: v/100 * len(cypher1) for c, v in eng_freq.items()}

decodes = {i: apply_key(cypher1, i) for i in range(255)}

cts = {k: get_freqtable(v) for k, v in decodes.items()}

dists = {k: dict_dist(target_freq, dict(ct)) for k, ct in cts.items()}

best = {k: decodes[k].decode('utf-8') for k, ct in dists.items() if ct == min(dists.values())}

print(best)
