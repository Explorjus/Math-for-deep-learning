import numpy as np                      # wczytuje bibliotekę numpy pod skróconą nazwą np

for m in range(2,31):                   # m = wielkość grupy, kolejno od 2 do 30 osób
    matches = 0                         # licznik eksperymentów, w których ktoś miał te same urodziny

    for n in range(100000):             # powtarza eksperyment 100 000 razy dla tej samej grupy
        match = 0                       # licznik par z tymi samymi urodzinami w jednym eksperymencie
        b = np.random.randint(0,364,m)  # losuje m dni urodzin (liczby od 0 do 363)
        for i in range(m):              # i = numer pierwszej osoby (od 0 do m-1)
            for j in range(m):          # j = numer drugiej osoby (od 0 do m-1)
                if (i != j) and (b[i] == b[j]):  # różne osoby, a ten sam dzień urodzin?
                    match += 1          # jeśli tak, zwiększ licznik par o 1
        if (match != 0):                # czy w tym eksperymencie była choć jedna para?
            matches += 1                # jeśli tak, zalicz eksperyment jako trafienie

    print("%2d %0.6f" % (m, matches/100000))  # wypisz wielkość grupy i prawdopodobieństwo