# Implement repeating-key XOR
#
# Here is the opening stanza of an important work of the English language:
#
# Burning 'em, if you ain't quick and nimble
# I go crazy when I hear a cymbal
#
# Encrypt it, under the key "ICE", using repeating-key XOR.
#
# In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.
#
# It should come out to:
#
# 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
# a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
#
# Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.
from set1.utils import apply_key

plaintext = ["Burning 'em, if you ain't quick and nimble", "I go crazy when I hear a cymbal"]
cyphertext = ["0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272",
              "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"]
key = "ICE"


class RepeatingKeyXor:
    def __init__(self, key):
        if isinstance(key, bytes):
            self.kb = key
        else:
            self.kb = key.encode('ascii')
        self.idx = 0

    def reset(self):
        self.idx = 0

    def getk(self):
        rv = self.kb[self.idx % len(self.kb)]
        self.idx += 1
        return rv

    def encode(self, plain):
        if isinstance(plain, bytes):
            bs = plain
        else:
            bs = plain.encode('ascii')
        return bytes(b ^ self.getk() for b in bs)

    @staticmethod
    def chunk(xs, chunk_size: int = 75):
        return [xs[i:i+chunk_size] for i in range(0, len(xs), chunk_size)]


rkx = RepeatingKeyXor(key)

rkx.reset()
c = rkx.encode("\n".join(plaintext)).hex()
l = 75
c_out = rkx.chunk(c)

assert cyphertext[0] == c_out[0]
assert cyphertext[1] == c_out[1]

