import numpy as np

# poisson(λ, size): λ = 5 to średnia liczba zdarzeń w przedziale,
# size = 10 to liczba przedziałów (np. 10 godzin).
# Każda liczba w t to ile zdarzeń wystąpiło w danym przedziale.
# Brak górnej granicy, ale wyniki skupiają się wokół λ.
t = np.random.poisson(5, size=10)   # np. [11 4 6 6 7 5 7 4 2 5]
print(f"T: {t}")

# bincount: idzie po kolei przez t i WARTOŚĆ każdego wyniku traktuje jako NUMER PUDEŁKA.
#   wynik 11 -> +1 do s[11]
#   wynik 4  -> +1 do s[4]
#   wynik 6  -> +1 do s[6] ... itd.
# Pozycja wyniku w t nie ma znaczenia: [11, 4, 6] i [6, 11, 4] dadzą to samo s.
# Pudełka zawsze zaczynają się od 0, a te, które nie wypadły, mają wartość 0.
# Długość s = t.max() + 1 (pudełka od 0 do największego wyniku),
# więc przy każdym uruchomieniu może być inna.
s = np.bincount(t)                  # np. [0 0 1 0 2 2 2 2 0 0 0 1]

print(f"S: {s}")
print(f"T max: {t.max()}")          # największa wartość w t, wyznacza liczbę pudełek w s

# Dzielimy liczności przez liczbę przedziałów, dostajemy prawdopodobieństwa (suma = 1).
# Przy małym size wyniki mocno odbiegają od wzoru P(k) = λ^k · e^(-λ) / k!
# Większe size (np. 10000) da wyniki bliższe teorii.
s = s/s.sum()

print(s)