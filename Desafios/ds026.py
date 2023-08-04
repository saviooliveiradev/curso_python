# aula 9

frase = str(input('Digite uma frase: ')).upper()

print(f'A letrra A aparece {frase.count("A")} vezes na frase')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')
print(f'A ultima letra A apareceu {frase.rfind("A")+1}')