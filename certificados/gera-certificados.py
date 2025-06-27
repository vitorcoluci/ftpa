## -*- coding: utf-8 -*-
# coding: utf8
import pandas as pd
import math
import numpy as np
import subprocess, os

# carrega nomes
alunos = pd.read_csv("participantes-FTPA-2025.csv", encoding='utf-8') #encoding='latin-1')
num_alunos=alunos.shape[0]
print(num_alunos)
# gera certificado
for i in range(num_alunos):
    aluno = str(alunos.at[i,"Nome"])
    aluno_junto = "".join(aluno.split())
    ra = str(alunos.at[i,"RA"])
    texto=r"\documentclass[12pt,landscape]{{article}} \input{{sctruct.tex}} \begin{{document}} \pagestyle{{empty}} \para{{{0}}}{{{1}}} \end{{document}} ".format(aluno,ra)

    #print(texto)
    file = open("main.tex", "w") 
    file.write(texto)
    file.close()

    a = subprocess.run('pdflatex --enable-write18 --shell-escape main.tex > log.latex',shell=True)
    b = subprocess.run('mv main.pdf ' + str(aluno_junto) + '.pdf',shell=True)
    c = subprocess.run('rm main.* log.latex',shell=True)