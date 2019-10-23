"""Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo, usando o módulo ‘os’, de bloco de notas (notepad) para abri-lo"""


import os

arquivo = r'C:\\Users\\mariana.dsantos\\Documents\\Teste de performance 1_2\\Teste de performance 1_2 Python\\exemplo.txt'

if os.path.exists(arquivo):
    open(arquivo)
else:
    print(arquivo, 'não existe!')
