# aula 8

from math import sqrt

cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = sqrt(pow(cat_oposto, 2) + pow(cat_adjacente, 2)) 
              
print(f'Sua hiponetusa é {hipotenusa}')