"""Escreva um programa que indique a extensão de um arquivo usando função do módulo os.path."""

import os

arquivo = ["'arq_texto.txt'"]

for nome_arquivo in arquivo:
    nome, extensao = os.path.splitext(nome_arquivo)
    print(extensao)

