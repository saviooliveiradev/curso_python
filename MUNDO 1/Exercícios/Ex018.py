# aula 8

import math

num = float(input('Digite um ângulo: '))

randianos = math.radians(num)

seno = math.sin(randianos)
cos = math.cos(randianos)
tan = math.tan(randianos)

print(f'O ângulo que você digitou foi {num:.0f}° e seu seno é {seno:.2f}°\n seu cosseno é {cos:.2f}°\n seu tangente {tan:.2f}°')