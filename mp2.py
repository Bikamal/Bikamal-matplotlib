import matplotlib.pyplot as plt
from matplotlib.pyplot import*
import numpy as np
from numpy import*


c1=plt.Circle((0.5,0.5),0.3,facecolor="none",edgecolor='r')

c2=plt.Circle((0.5,0.4),0.2,facecolor="none",edgecolor='r')
c3=plt.Circle((0.5,0.3),0.1,facecolor="none",edgecolor='r')

fig, ax=plt.subplots()
ax.add_patch(c1)
ax.add_patch(c2)
ax.add_patch(c3)
#xpoints=np.array([])
#ypoints=np.array([])

#plt.plot(x,y)
plt.show()