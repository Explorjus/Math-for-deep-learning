import random

sukces = 0
nie_sukces = 0
j = 0
N = 1 * 10**6

while j < N:
	kule = ["red"] * 8 + ["blue"] * 2

	wybor = random.choice(kule)
	kule.remove(wybor)
	wybor_2 = random.choice(kule)
	kule.remove(wybor_2)
 
	if wybor == "red" and wybor_2 == "red":
		sukces += 1

	else:
		nie_sukces += 1

	j += 1
 
print(f"Sukces: {sukces/N:.3f} nie sukces: {nie_sukces/N:.3f}")