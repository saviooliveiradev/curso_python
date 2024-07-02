# aula 8
import math 

cat_aposto = float(input('Informe o comprimento do cateto aposto: '))
cat_adjacente = float(input('Informe o comprimento do cateto adjacente: '))

hipotenusa = math.hypot(cat_aposto, cat_adjacente)

print(math.ceil(hipotenusa))