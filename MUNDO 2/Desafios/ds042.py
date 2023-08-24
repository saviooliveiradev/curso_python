# aula 12

print('-=-'* 20)
print('Analisador de Triângulos')
print('-=-'* 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceito segmento: '))

if r1 == r2 or r1 == r3 or r2 == r1 or r2 == r3 or r3 == r1 or r3 == r2:
    print('\033[34mEQUILÁTERO\033[m')
elif r1 == r2:
    print('\033[34mISÓSCELES\033[m')
else:
    print('\033[34mESCALENO\033[m')