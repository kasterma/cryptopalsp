## Detect single-character XOR
#
# One of the 60-character strings in the file dat_prob4.txt has been encrypted by single-character XOR.
#
# Find it.
#
# (Your code from #3 should help.)

from set1.utils import apply_key, get_freqtable, dict_dist, dict_dist2, eng_freq, printable

with open("data/dat_set1_prob4.txt") as f:
    dat = f.readlines()
dat_bytes = [bytes.fromhex(s) for s in dat]

plain1 = "Cooking MC's like a pound of bacon"
cypher1 = apply_key(plain1.encode('ascii'), 45)

dat_bytes.append(cypher1)

for idx, dat in enumerate(dat_bytes):
    target_freq = {k: v/100*len(dat) for k, v in eng_freq.items()}

    decodes = {k: apply_key(dat, k) for k in range(256)}

    cts = {k: get_freqtable(v) for k, v in decodes.items()}

    dists = {k: dict_dist(target_freq, dict(ct), miss_costs=20) for k, ct in cts.items()}

    best = {k: decodes[k].decode('utf-8', errors='ignore') for k, ct in dists.items() if ct < min(dists.values()) + 20}
    if len(best) < 100:
        print(f"idx {idx}, {best}")

# trying different distance (and filter out on nonprintables)
for idx, dat in enumerate(dat_bytes):
    target_freq = {k: v/100*len(dat) for k, v in eng_freq.items()}

    decodes = {k: apply_key(dat, k) for k in range(256)}
    decodes = {k: d for k,d in decodes.items() if all([printable(l) for l in list(d)])}

    cts = {k: get_freqtable(v) for k, v in decodes.items()}

    dists = {k: dict_dist2(target_freq, dict(ct), miss_costs=20) for k, ct in cts.items()}

    best = {k: decodes[k].decode('utf-8', errors='ignore') for k, ct in dists.items() if ct < min(dists.values()) + 20}
    if 0 < len(best) < 100:
        print(f"idx {idx}, {best}")
