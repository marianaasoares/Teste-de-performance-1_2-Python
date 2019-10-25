""""Escreva um programa em Python, usando o módulo ‘psutil’, que imprima 20 vezes, de segundo a segundo, o percentual do uso de CPU do computador."""

import psutil, pid, subprocess, os 

p = psutil.Process(pid)
por_segundo = p.cpu_percent(interval=1.0)
print(por_segundo)