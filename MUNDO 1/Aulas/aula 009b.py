frase = 'Curso em Video Python'
f = 'Fatiamento'
a = 'Análise'
frase1 = '   Curso em Video Python   '

print(f'{f:=^50}')

print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[2::3])
print(frase[::2])

print(f'{a:=^50}')

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase1.strip)
print(frase.replace('Python', 'Android'))
print(frase)
frase2 = frase.replace('Python', 'Android')
print(frase2)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('curso'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])