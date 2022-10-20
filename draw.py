from numpy import genfromtxt
my_data = genfromtxt('foo.csv', delimiter=',')

import matplotlib as mpl
import matplotlib.pyplot as plt

plt.imshow(my_data, cmap=mpl.cm.binary)
plt.axis("off")

plt.show()