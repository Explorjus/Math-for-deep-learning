import numpy as np
import matplotlib.pylab as plt

t = np.random.binomial(5, 0.3, size = 10) # 5 - liczba prób, 0.3 - prawdopodobieństwo sukcesu, 1000 - ile razy powtarzamy
s = np.bincount(t) # ile razy wypadło 0, 1, 2... sukcesów

prawd = s / s.sum() # zamiana na prawdopodobieństwa

i = []

for k in range(len(prawd)):
    print(k, prawd[k])
    i.append(k)
    

plt.bar(i, prawd, label="prawd")
plt.xlabel("liczba sukcesów")
plt.ylabel("prawdopodobieństwo")
plt.legend()
plt.show()