"""Escreva um programa que mostre as datas de criação e modificação de cada arquivo em um diretório."""

import os, time

dir_path = r"C:\\Users\\mariana.dsantos\\Documents\\Teste de performance 1_2\\Teste de performance 1_2 Python"
arquivos = os.listdir(dir_path)

for a in arquivos:
    arquivo_path = os.path.join(dir_path,a)
    status = os.stat(arquivo_path)
    print("Nome do Arquivo: ", arquivo_path, "Data de modificação: ", time.ctime(status.st_mtime))
