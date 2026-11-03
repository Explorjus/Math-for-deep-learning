import matplotlib.pylab as plt
import random

zakres = [1,2,3] # zakres losowanych drzwi
i = 0 # licznik gier
wins = 0
wins_2 = 0
x = []
y = []
y_2 = []

while i < 1000:
    wygrana = random.choice(zakres) # losowanie drzwi z nagroda
    drzwi_wybor = random.choice(zakres) # wybor drzwi przez gracza
    zakres_2 = zakres.copy() # kopia na kazda kolejną gre
    
    if drzwi_wybor == wygrana:
        wins += 1
        
    else:
        zakres_2.remove(drzwi_wybor) # usuwanie drzwi gracza aby uniemozliwic dalszy wybor
       
        for d in zakres_2: # petla ma za zadanie znalezc drzwi ktore nie sa wygrna ani te ktore sa obecnie wybrane
            if d != wygrana:
                puste = d
                
        zakres_2.remove(puste) # usuniecie pustych drzwi
        nowe_drzwi = zakres_2[0] # wybor pozostalych jedynych drzwi
        nowe_drzwi == wygrana
        wins_2 += 1
            
    i += 1
    x.append(i)
    y.append(wins)
    y_2.append(wins_2)
        
plt.plot(x,y, label="bez zmiany drzwi")
plt.plot(x,y_2, label="zmiana drzwi")
plt.xlabel("liczba losowań")
plt.ylabel("wygrane")
plt.legend()
plt.show()

            

