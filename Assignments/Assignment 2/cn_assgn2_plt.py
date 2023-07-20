# -*- coding: utf-8 -*-
"""CN_Assgn2_plt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_8npZwVEjqo5GKDo6DEF7QKuVZ_iKj3c
"""

import matplotlib.pyplot as plt
from matplotlib import style
  
# x axis values
x = [1,2,4,8,16,32,64,128,256]
# corresponding y axis values
y1 = [423.1639699,
800.7879388,
923.2783939,
863.1627904,
849.3664326,
813.8852973,
704.6931621,
582.1458543,
523.7655298


]
y2=[214.685938,
518.2161268,
525.4527642,
579.5241005,
623.2959962,
486.8911729,
471.1996079,
461.3415744,
457.8666444

]
y3=[90.96765235,
161.6315979,
197.697147,
234.6459155,
250.6657704,
213.321212,
203.577612,
169.1411146,
141.9917673,

]
ticks=range(len(x))


# plotting the points 
plt.plot(ticks, y1, color='blue',marker='d', markerfacecolor='blue',label="Delay (5ms)")
plt.plot(ticks, y2, color='darkorange',marker='s', markerfacecolor='darkorange',label="Delay (25ms)")
plt.plot(ticks, y3, color='grey',marker='^', markerfacecolor='grey',label="Delay (100ms)")
ax = plt.axes()        
ax.yaxis.grid()
plt.ylim(0,1000)
plt.xticks(ticks,x)

plt.xlabel('Window Size',weight='bold')
plt.ylabel('Throughput (KBps)',weight='bold')
plt.legend(bbox_to_anchor=(1.4,0.5), loc='center right', borderaxespad=0,prop=dict(weight='bold'))
plt.show()