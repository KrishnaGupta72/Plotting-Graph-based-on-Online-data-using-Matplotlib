#Working with csv price data.
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
x= np.loadtxt('exampleFile.csv',unpack=True,delimiter = ',')
plt.plot(x)
plt.title('Epic Info')
plt.xlabel('X axis')
plt.show()
