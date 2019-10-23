"""Escreva um programa que indique se um arquivo existe ou não. Caso exista, indique se é realmente um arquivo ou não."""

import os
p = 'diretorio_exemplo'
if os.path.exists(p):
    print(p, 'existe!')
else:
    print(p, 'não existe!')
