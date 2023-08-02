# frase = Curso em Video Python, 20 caracteres.

'''Fatiamento = é pegar algumas partes da string. 
exemplo = frase[9], ele consegue só printar o indeci daquela string 9 da frase, no python também ele diferenciar
letras minúsculas e maiúsculas, essa é a forma mais simples.'''

'''Termos também, frase[9:13], significa que vai printar até o indeci 12, sempre menos 1
obs: o indeci das string sempre começa a contar com o num 0.
então voltando ao assunto para pegar a palavra certo seria [9:14]'''

# frase[9:21] ele vai printar (Video Python), essa não é a melhor forma de se fazer esse tipo de comando
# frase[9:21:2] o ultimo número vai fazer a função de pular em 2 em 2, então ficaria (Vdo Pto)
# frase[:5] só não estou indico qual número de carecter começar, nisso ele começará no carecter (0).
# frase [15:] não estou indicando o final, só trocaria a ordem
# frase[9::3] vai começar no caracter 9 e vai pular em 3 em 3 até o final da frase

'''Análise = É saber informação da str, por exemplo qual o tamanho dela, qual letra ela começa ou termina, 
qual palavra inteira ela começa, por issso o nome, análizar.'''

'''Vamoss utilizar o método da função len(frase), que é ler o comprimento da frase, então vai ser 20 caracteres 
ou contagem normal seria 21'''

# frase.count('o') aqui vamos mandar que o programa conte quantas letras 'o' minúsculo aparece no programa
'''termos esse frase.count('o', 0, 13) essa função vai obrigar a contagem começar no 0 e terminar no 13 que no
caso seria o 12, analizando com fatiamento já'''
# frase.find('deo') essa função vai dizer quantas vezes encontrou palavra 'deo' 
# frase.find('Android') quando colocamos uma string que não termos na frase, ele nos retorna -1
# 'Curso' in frase = vai informar se dentro da varialvel frase existe a string cursom, True ou False

'''Transformação = uma lista de string ela é imutável, mais conseguimos mundar nela através de métodos,
mais não conseguimos mexer direto nos elementos'''

# frase.replace('Python', 'Android') Vai procurar a string ('Python') e substituir pela string ('Android')
# frase.upper() vai ficar em maiúscula, todas as letras que não forem maiúsculas
# frase.lower() vai ficar em minúscula, acontrario da funcionalidade anterior
# frase.capitalize() vai jogar todos os caracteres em minúscula e só o primeiro em maiúsculo
# frase.title() ele vai analizar quantas palavras tem a frase, através da quebra do espaço do teclado e vai colocar em maiúsculo  

# frase = ---Aprenda Python-- (- = espaço)
# frase.strip() vai remover todos o epaços inúties do inicio e final, apenas
# frase.rstrip() de direita e frae.lstrip de essquerda, vai remover todos os espaços ao lado direito ou esquerdo

'''Divisão = Vamos dividir strings'''
# frase = Curso em Video Python

'''frase.split() ele tem algumas funcionalidades a mais, basicamente ele vai dividir a frase através do espaço, 
então na divisão cada palavra vai começar com 0 e terminar conforme quantos caracter a palavra tem e gera uma lista
conforme a palavra por exemplo (Curso = 0), (Em = 1), (Video = 2), (Python = 3)'''

'''Junção = Juntar as strings'''
''' '-'.join(frase) vai juntar todos elementos da variavel frase com o separador indicado (-), exemplo: 
 Curso-em-Video-Pytohn'''

