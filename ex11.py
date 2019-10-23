"""Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo, usando o módulo ‘os’, de bloco de notas (notepad) para abri-lo"""


import os

arquivo = 'exemplo.txt'

if os.path.exists(arquivo):
    os.system(arquivo)
else:
    print(arquivo, 'não existe!')
