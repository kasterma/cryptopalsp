import sys
from collections import Counter


def apply_key(bs: bytes, key: int) -> bytes:
    """Apply the key to every byte in bs.

    @:param bs the bytes to be encoded or decoded
    @:param key key to use
    """
    return bytes(b ^ key for b in bs)


def printable(i):
    """Is the integer i printable as ascii"""
    lower = int.from_bytes(bytes.fromhex('20'), sys.byteorder)
    upper = int.from_bytes(bytes.fromhex('7e'), sys.byteorder)
    return lower <= i <= upper or i == 10


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


def get_freqtable(bs: bytes):
    """Get a frequency table assuming the bytes are utf-8 encoded.

    If the utf-8 decode fails, return empty table.
    We decided on this implementation to be easily able to compare with the frequency table of English.
    """
    # noinspection PyBroadException
    try:
        return Counter(bs.decode('utf-8'))
    except:
        return Counter()


def dict_dist(d1: dict, d2: dict, miss_costs: int = 20) -> int:
    """Distance between two dictionaries.

    The distance is the sum of absulte values of differences, but miss_costs * number of keys not in both.
    """
    keys = set(d1.keys()).union(set(d2.keys()))
    d = 0
    for key in keys:
        d += abs(d1.get(key, miss_costs) - d2.get(key, miss_costs))
    return d


def dict_dist2(eng_freq: dict, d2: dict, miss_costs: int = 20) -> int:
    missing = set(d2.keys()).difference(set(eng_freq.keys()))
    found = set(d2.keys()).intersection(set(eng_freq.keys()))
    d = len(missing) * miss_costs
    for key in found:
        d += abs(eng_freq.get(key) - d2.get(key))
    return d
