import numpy as np
from random import randrange
import matplotlib.pyplot as plt

# emberek száma
n = 100

# minden embernek 10 lej
kezdeti=np.ones([n])*10

# lefuttatjuk 1000-szer, 1000 szer üzletelnek
j = 0
while j < 1000:
      # egy random ember kiválasztása
      v = randrange(n)
      # a kiválasztott ember egy random összeget ad egy másik random embernek
      r = kezdeti[v]
      k = randrange(r)
      # de csak akkor adhat hogyha azzal nem kerül minuszba
      if kezdeti[v]-k>=0:
        # itt leveszi attól az összeget aki ad
        kezdeti[v]= kezdeti[v]-k
        # egy újabb random ember generálása aki megkapja a pénzt
        m = randrange(n)
        # hozza adja egy random emberhez azt az összeget amit levett a másiktól
        kezdeti[m]= kezdeti[m]+k
      j += 1    

print(kezdeti)

# végső pénzösszeg, ellenőrizzük, hogy ne változzon a pénzösszeg, 1000 lej kell legyen összesen
p=0
for b in kezdeti:
  p=p+b
print(p)

# histogramban való megjelenítés
plt.title("Tranzakciók")
plt.xlabel("emberek")
plt.ylabel("pénz")
plt.xticks(np.arange(0, 105, 5.0))
plt.plot(kezdeti)
plt.show()