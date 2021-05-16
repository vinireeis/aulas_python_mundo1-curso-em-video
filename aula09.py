frase = 'Curso em Video Python'
print(frase[5:20:])  # fatiamento começando no 5 caractere e indo até o 20 sem pulo
print(frase[5:20:2])  # fatiamento pulando de 2 em 2.
print(len(frase))   # quantidade de caracteres da frase
print(frase.count('o'))  # contando quanos caracteres tem especifico
print(frase.count('o', 2, 15))  # contando com fatiamento
print(frase.find('deo'))  # vai indicar a posição que começa
print(frase.find('android'))  # -1 siginifica que não foi encontrado
print('Curso' in frase)  # se existe "curso" dentro da frase, retorna true ou false.
frase.replace('Python', 'Android')  # não consegui fazer o replace/substituir
print(frase.upper())     # deixa tudo maiusculo
print(frase.lower())    # deixa tudo minusculo
print(frase.capitalize())  # Somente a primeira letra da frase fica maíuscula
print(frase.title())    # todas as iniciais ficam maiúsculas
frase = ('   Aprenda Python  ')
print(frase)
print(frase.rstrip())   # remove somente os últimos caracteres em branco >> o que está a direita
print(frase.lstrip())   # remove somente os caracteres em branco a esquerda <<
print(frase.strip())    # remove em ambos espaços em branco no ínicio e fim
print(frase.split())    # separa a cadeia de caracteres em palavras dentro de uma lista
frase = 'Curso em Video Python'
print(frase.split())
novafrase = (frase.split())    # guardar as palavras separadas em uma nova variavel
print(frase)
print(novafrase[3])   # visualizar as palavras separadas na lista
print('-'.join(novafrase))   # colocar um tracinho nas palavras que foram separadas em lista
