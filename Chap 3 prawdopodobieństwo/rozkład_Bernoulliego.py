import numpy as np

t = np.random.binomial(1, 0.5, size=1000) # prawdopodieństwo tak czy nie aka flip coin
s = np.bincount(t)

print(s)