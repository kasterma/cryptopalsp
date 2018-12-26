def apply_key(bs: bytes, key: int) -> bytes:
    """Apply the key to every byte in bs.

    @:param bs the bytes to be encoded or decoded
    @:param key key to use
    """
    return bytes(b ^ key for b in bs)
