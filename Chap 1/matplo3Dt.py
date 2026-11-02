from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pylab as plt
import numpy as np

x = np.random.random(20)
y = np.random.random(20)
z = np.random.random(20)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)
plt.show()