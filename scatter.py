import matplotlib.pyplot as plt
import numpy as np


np.random.seed(5)
x = 3 +  np.random.normal(0,5.8,24)
y = 3 + np.random.normal(0,5.8, len(x))

sizes   = np.random.uniform(4,20,len(x))
colors = np.random.uniform(15, 80,len(x))

fig, ax = plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=10)

ax.set(xlim=(-0.2, 1.2), xticks=np.arange(-0.2, 1.2),
       ylim=(-0.2, 1.2), yticks=np.arange(-0.2, 1.2))

plt.show()