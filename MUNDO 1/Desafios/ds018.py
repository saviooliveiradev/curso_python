# aula 8

import math 

num = int(input('Digite um número: '))

seno = math.sin(num)
cosseno = math.cos(num)
tangente = math.tan(num)

print(f'O angulo {num}, seno {math.trunc(seno)}, cosseno {cosseno} e tangente {tangente}')