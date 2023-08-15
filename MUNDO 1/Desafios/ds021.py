# aula 8

import pygame #biblioteca utilizada para jogos

# primeira regra da bib, termos que iniciar ele
pygame.mixer.init()
pygame.init()

# nome do arquivo
pygame.mixer.music.load('Desafios\musica.mp3')

# play na música
pygame.mixer.music.play()

# encerrar quando parar de tocar a música
pygame.event.wait()
