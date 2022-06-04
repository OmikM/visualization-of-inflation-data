from matplotlib import pyplot as plt
import pandas as pd
df = pd.DataFrame({"inflacjaPL": [0,-0.9,-0.7,2,1.8,2.2,3.4],
                   "inflacjaUSA": [1.6,0.1,1.3,2.1,2.4,1.8,1.2],
                 "lata":[2014,2015,2016,2017,2018,2019,2020]})
fig, ax = plt.subplots()
lata = [2014,2015,2016,2017,2018,2019,2020]
pl = plt.plot(lata,inflacjaPL,label="inflacja w polsce",marker='o')
us = plt.plot(lata,inflacjaUSA,label="inflacja w U.S",linestyle = 'dotted',marker='o')
plt.legend()
plt.xlabel("rok")
plt.ylabel("inflacja")
plt.style.use("dark_background")
plt.grid(axis = 'y')

for i in range(5):
    plt.plot(lata,
            inflacjaPL,
            marker='o',
            linewidth=2+(5*i),
            alpha=0.03,
            color='#00ff41')
plt.show()
