import matplotlib.pyplot as plt
from matplotlib.pyplot import*
import numpy as np
from numpy import*


c1=plt.Circle((2.5,4),1,facecolor="none",edgecolor='r')
c2=plt.Circle((2.5,4),1.5,facecolor="none",edgecolor="orange")
c3=plt.Circle((2.5,4),2,facecolor="none",edgecolor="yellow")


c4=plt.Circle((7.5,4),1,facecolor="none",edgecolor='blue')
c5=plt.Circle((7.5,4),1.5,facecolor="none",edgecolor="aqua")
c6=plt.Circle((7.5,4),2,facecolor="none",edgecolor="skyblue")




fig, ax=plt.subplots()
ax.add_patch(c1)
ax.add_patch(c2)
ax.add_patch(c3)

ax.add_patch(c4)
ax.add_patch(c5)
ax.add_patch(c6)

ax.set(xlim=(0, 10), xticks=np.arange(0, 10),
       ylim=(0, 8), yticks=np.arange(0, 8))




plt.axvline (x=5, color='green')
plt.show()