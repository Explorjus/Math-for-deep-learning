import numpy as np
import random

nb = 0
N = 1000000

for i in range(N):
    s = np.random.randint(0,50,3)
    fail = False
    for t in range(3):
        if (s[t] < 4):
            fail = True
    
    if (not fail):
        nb += 1
        
print(f"Prawdopodobieństwo niebycia w Bostonie jesienią = {nb/N:.3f}")