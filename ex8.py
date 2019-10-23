"""Escreva um programa que mostre a quantidade de bytes (em KB) de cada arquivo em um diretório."""

import os

dir_path = r"C:\\Users\\mariana.dsantos\\Documents\\Teste de performance 1_2\\Teste de performance 1_2 Python"
arquivos = os.listdir(dir_path)
for a in arquivos:
    arquivo_path = os.path.join(dir_path,a)
    tamanho_arquivo = os.path.getsize(arquivo_path)
    tamanho_arquivo_kb = tamanho_arquivo/1024 
    print("Nome do arquivo: {} - Tamanho do arquivo em KB: {}".format(arquivo_path, tamanho_arquivo_kb))