from hashlib import sha256
from random import choices
from time import monotonic


def encipher(plain_str, key):
    assert len(plain_str) == len(key)
    return sha256(bytes(k ^ ord(b) for b, k in zip(plain_str, key))).digest().hex()


key = choices(range(256), k=3)
cipher = encipher("tes", key)

before = monotonic()
for i in range(256):
    print(i)
    for j in range(256):
        for k in range(256):
            if cipher == encipher("tes", [i, j, k]):
                print("done")

after = monotonic()

print("duration" + str(after - before))
