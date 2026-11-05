import numpy as np

n = np.random.randint(0, 10, 10000)
h = np.bincount(n)

print(h/h.sum())