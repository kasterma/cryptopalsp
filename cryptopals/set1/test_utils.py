from .utils import apply_key
import random


def test_idempotent():
    for _ in range(100):
        key = random.randint(0, 255)
        bs = bytes(random.sample(range(0, 256), 100))
        assert(apply_key(apply_key(bs, key), key) == bs)
