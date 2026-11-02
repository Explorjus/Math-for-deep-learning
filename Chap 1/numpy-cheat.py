import numpy as np 

print(np.__version__)

#b = np.array([[1,2,3,4],[5,6,7,8]]) #zmiana z listy na tblice

#print(b)

################################################################################################
# Typy dancyh

#c = np.array([[1,2,3,4],[5,6,7,8]], dtype="uint64")

#print(c.shape)
#print(c)

################################################################################################
# Dwuwyiaore

#d = np.array([[1,2,3],[4,5,6],[7,8,9]])

#print(d.shape)
#print(d.size)
#print(d)

################################################################################################
# np.zeros i np.ones

#a = np.zeros((3,4), dtype="uint32")
#a[0,2] = 42
#a[1,1] = 66
#print(a)

################################################################################################
# ZAAWANSOWANE INDEKSOWANNIE

#a = np.arange(12).reshape((4,3))
#print(a)
#print(f"czwary rząd -> {a[3]}")

#print(a[2:,0])

################################################################################################
# ODCZYT I ZAPIS

#a = np.random.randint(0,99,(4,4))

#print(a)

#np.save("random.npy", a)

#b = np.load("random.npy")
#b[0:,0:] = 67
#print(b)