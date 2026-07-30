import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('inscritos.dat')

ano = data["ano"]
inscritos = data["inscritos"]

plt.plot(ano, inscritos, color='g', marker='o') 
plt.xticks(np.arange(2017, 2027, step=1))
plt.xlabel("Ano")
plt.ylabel("Inscritos no Vestibular")
plt.ylim(1000,2000)
#plt.legend()
plt.savefig("inscritos.png",dpi=200)

