import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

df_mestrado = pd.read_csv('../data/mestrado-2012-2023.csv')
df_doutorado = pd.read_csv('../data/doutorado-2012-2023.csv')

# conteudo
# Ano,Alunos ao final do ano base anterior,Alunos novos matriculados,Titulado,Desligado,Abandonou,MUDANCA DE NÍVEL SEM DEFESA,MUDANCA DE NÍVEL COM DEFESA,Total de Entradas,Total de Saídas,Alunos ao final do ano base corrente

# O total de entradas é a soma entre os alunos ao final do ano base anterior + alunos novos matriculados.

# total de saída é o somatório entre Titulado, Desligado, Abandonou, MUDANCA DE NÍVEL SEM DEFESA, MUDANCA DE NÍVEL COM DEFESA.

ms_ano = df_mestrado["Ano"]
ms_ano_anterior = df_mestrado["Alunos ao final do ano base anterior"]
ms_ano_corrente = df_mestrado["Alunos ao final do ano base corrente"]
ms_matriculados = df_mestrado["Alunos novos matriculados"]
ms_titulados = df_mestrado["Titulado"]
ms_desligados = df_mestrado["Desligado"]
ms_abandonos = df_mestrado["Abandonou"]
ms_entradas = df_mestrado["Total de Entradas"]
ms_saidas = df_mestrado["Total de Saídas"]

plt.plot(ms_ano, ms_entradas, color='r', label='Cursando', marker='o') 
plt.plot(ms_ano, ms_matriculados, color='g', label='Matriculados',marker='o')
plt.plot(ms_ano, ms_titulados, color='b', label='Titulados', marker='o')
plt.gca().add_patch(Rectangle((2021, -5), 3, 175,fill=True,facecolor = 'blue',alpha=0.2))

plt.xlabel("Ano")
plt.ylabel("Alunos")
plt.title("Mestrado")
plt.xlim(2008, 2025)
plt.ylim(-5, 170)
plt.legend()
#plt.show()
plt.savefig("../analise/evolucao-alunos-MESTRADO.png",dpi=200)

'''
plt.plot(ms_ano, ms_entradas, color='black', label='Cursando', marker='o')
plt.plot(ms_ano, ms_saidas, color='b', label='Saídas', marker='o')
plt.plot(ms_ano, ms_desligados, color='r', label='Desligados') 
plt.plot(ms_ano, ms_abandonos, color='g', label='Abandonos')
plt.xlabel("Ano")
plt.ylabel("Alunos")
plt.title("Mestrado")
plt.xlim(2008, 2024)
plt.ylim(-5, 170)
plt.legend()
plt.show()
'''
# limpa o plot
plt.clf()

dt_ano = df_doutorado["Ano"]
dt_ano_anterior = df_doutorado["Alunos ao final do ano base anterior"]
dt_ano_corrente = df_doutorado["Alunos ao final do ano base corrente"]
dt_matriculados = df_doutorado["Alunos novos matriculados"]
dt_titulados = df_doutorado["Titulado"]
dt_desligados = df_doutorado["Desligado"]
dt_abandonos = df_doutorado["Abandonou"]
dt_entradas = df_doutorado["Total de Entradas"]
dt_saidas = df_doutorado["Total de Saídas"]

plt.plot(dt_ano, dt_entradas, color='r', label='Cursando', marker='o') 
plt.plot(dt_ano, dt_matriculados, color='g', label='Matriculados',marker='o')
plt.plot(dt_ano, dt_titulados, color='b', label='Titulados', marker='o')
plt.gca().add_patch(Rectangle((2021, -5), 3, 175,fill=True,facecolor = 'blue',alpha=0.2))

plt.xlabel("Ano")
plt.ylabel("Alunos")
plt.title("Doutorado")
plt.xlim(2008, 2025)
plt.ylim(-5, 170)
plt.legend()
#plt.show()
plt.savefig("../analise/evolucao-alunos-DOUTORADO.png",dpi=200)

#plt.plot(dt_ano, dt_entradas, color='black', label='Cursando', marker='o')
#plt.plot(dt_ano, dt_saidas, color='b', label='Saídas', marker='o')
#plt.plot(dt_ano, dt_desligados, color='r', label='Desligados') 
#plt.plot(dt_ano, dt_abandonos, color='g', label='Abandonos')
#plt.xlabel("Ano")
#plt.ylabel("Alunos")
#plt.title("Doutorado")
#plt.xlim(2008, 2024)
#plt.ylim(-5, 170)
#plt.legend()
#plt.show()

