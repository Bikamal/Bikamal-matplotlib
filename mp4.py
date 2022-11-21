#histogram


import matplotlib.pyplot as plt
from matplotlib.pyplot import*
import numpy as np
from numpy import*

plt.title("Weekday Data")


marks=[25,48,75,5,20,65,30]
bars=('Mon','Tue','Wed','Thu','Fri', 'Sat', 'Sun')
y=np.arange(len(bars))
#plt.bar(y,marks,color=’g’)
plt.bar(y,marks,color=['cyan','skyblue','lightpink','purple','lime','aqua','gold'])
plt.xticks(y,bars)



plt.show()

# mon 25, tue 48, wed 75, thu 5 , fri 20 , sat 65, sun 30