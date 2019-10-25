"""Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de memória principal e quanto de memória de paginação (swap) existem no computador."""

import psutil

print(psutil.virtual_memory()) 
print(psutil.swap_memory())