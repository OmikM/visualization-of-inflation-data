from matplotlib import pyplot as plt
lata = [2014,2015,2016,2017,2018,2019,2020]
inflacjaPL = [0,-0.9,-0.7,2,1.8,2.2,3.4]
inflacjaUSA = [1.6,0.1,1.3,2.1,2.4,1.8,1.2] 
plt.plot(lata,inflacjaPL,label="inflacja w polsce")
plt.plot(lata,inflacjaUSA,label="inflacja w U.S",linestyle = 'dotted')
plt.legend()
plt.plot(marker='o')
plt.xlabel("rok")
plt.ylabel("inflacja")
plt.style.use('dark_background')
plt.show()
