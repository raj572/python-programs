import random

# Set base pattern.
n, r = 4, 1 # To change: see above!
base_patterns = [(n-i)*'0' + i*'1' for i in range(1, n - r)]
patterns = ("".join(random.sample(s, len(s))) for s in base_patterns)
base_code = ord("0"), ord("1")

# Set ascii codes for colored squares.
color_rng = range(128997, 129004)
sq_colors = (chr(i) for i in random.sample(color_rng, 2))
trsl = dict(zip(base_code, sq_colors))

# Build pattern block; shuffle every other row.
block = (b.translate(trsl) for b in
(g[1:] + g[:1] if j else g for g in patterns for j in range(2)))

# Expand pattern block and mirror image.
h = l = 2 # Affects image size.
s = "".join(l*p + l*p[::-1]+ "\n" for p in block)
res1 = (h*s)[:-1] + (h*s)[::-1]
res2 = (h*s)[::-1] + '\n' + (h*s)[:-1]

# Print image.
print(random.choice((res1, res2)))