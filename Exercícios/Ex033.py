# aula 10

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

menor = a

# Verificando quem é menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é o maior
maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')