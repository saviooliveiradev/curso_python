# aula 12

print('-=-'* 20)
print('Analisador de Triângulos')
print('-=-'* 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceito segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end='') # não vai ter fim da linha
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES')
           
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
