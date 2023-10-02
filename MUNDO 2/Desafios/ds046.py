import emoji
from time import sleep

print('\033[1;31mCONTAGEM REGRESSIVA\033[m')

for c in range(10, 0, -1):
     sleep (1)
     print(c)

print(emoji.emojize(':fireworks:', language='alias'))
