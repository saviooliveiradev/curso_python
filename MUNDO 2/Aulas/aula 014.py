'''for c in range(1, 10):
     print(c)
print('fim')'''

# while serve quando eu sei o limete e serve tbm quando eu não sei o limite 
'''c = 1
while c < 10:
    print(c)
    c += 1
print('fim')'''

# vai ler 4 valores
'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('fim')'''

# com while, parar o prog quando colocar (0)
'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('fim')'''

'''n = 1
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] '))
print('fim')'''

#informando quanto números foram digitados, pares e impares

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valot: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares')
