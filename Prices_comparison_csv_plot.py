from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
x= np.loadtxt('Prices.csv',unpack=True,delimiter = ',')
# can plot specifically, after just showing the defaults:
plt.plot(x[0],'ob',label='First Price', linewidth=5)#info about lines
plt.plot(x[1],'c',label='Second Price',linewidth=5)
plt.title('Price Comparision')
plt.ylabel('Prices')
plt.xlabel('X-axis Base')
print("Krishna Gupta")
plt.legend()
plt.grid(True,color='k')#Enable grid view
plt.show()
