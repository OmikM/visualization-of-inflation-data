from ast import While
import pandas as pd
from matplotlib import pyplot as plt
df = pd.DataFrame({"inflacjaPL": [0,-0.9,-0.7,2,1.8,2.2,3.4],
                   "inflacjaUSA": [1.6,0.1,1.3,2.1,2.4,1.8,1.2],
                 "lata":[2014,2015,2016,2017,2018,2019,2020]})
fig, ax = plt.subplots()
lata = [2014,2015,2016,2017,2018,2019,2020]
plt.subplot(2, 1, 1)
pl = plt.plot(lata,df.inflacjaPL,label="inflacja w polsce",marker='o')
us = plt.plot(lata,df.inflacjaUSA,label="inflacja w U.S",linestyle = 'dotted',marker='o')
plt.legend()
plt.xlabel("rok")
plt.ylabel("inflacja")
plt.style.use("dark_background")
plt.grid(axis = 'y')

for i in range(5):
    plt.plot(lata,
            df.inflacjaPL,
            marker='o',
            linewidth=2+(5*i),
            alpha=0.03,
            color='#00ff41')
ax = plt.subplot(2, 1, 2)
while plt.get_fignums():
    i+=1
    bars = plt.bar([0,1],[df.inflacjaPL[i%6],df.inflacjaUSA[i%6]], label=lata[i%6])
    plt.legend()
    plt.pause(1)
    ax.clear()

plt.show()
