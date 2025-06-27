import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('../dados/candidato-vaga.csv')

# conteudo
# ANO,TADS,EAMB,ETEL,ETRANS,BSI,TSA

ano = dados["ANO"]
tads = dados["TADS"]
eamb = dados["EAMB"]
etel = dados["ETEL"]
etrans = dados["ETRANS"]
bsi = dados["BSI"]
tsa = dados["TSA"]

plt.plot(ano, bsi, color='b', label='Sistemas de Informação', marker='o')

plt.xlabel("Ano")
plt.ylabel("Candidato-vaga")
plt.title("Bacharelado")
plt.xlim(2017, 2025)
plt.ylim(0, 25)
plt.legend()
#plt.show()
plt.savefig("../dados/grafico-candidato-vaga-bacharelado.png",dpi=200)

plt.clf()

plt.plot(ano, eamb, color='g', label='Ambiental',marker='o')
plt.plot(ano, etel, color='gray', label='Telecomunicações', marker='o')
plt.plot(ano, etrans, color='black', label='Transporte', marker='o')

plt.xlabel("Ano")
plt.ylabel("Candidato-vaga")
plt.title("Engenharias")
plt.xlim(2017, 2025)
plt.ylim(0, 25)
plt.legend()
plt.savefig("../dados/grafico-candidato-vaga-engenharias.png",dpi=200)

plt.clf()

plt.plot(ano, tads, color='b', label='Análise de Sistemas', marker='o') 
plt.plot(ano, tsa, color='g', label='Saneamento ambiental', marker='o')

plt.xlabel("Ano")
plt.ylabel("Candidato-vaga")
plt.title("Tecnologias")
plt.xlim(2017, 2025)
plt.ylim(0, 25)
plt.legend()
plt.savefig("../dados/grafico-candidato-vaga-tecnologia.png",dpi=200)
