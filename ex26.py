''' Programa que leia uma frase qualquer e diga:
    Quantas vezes aparece a letra A
    Em que posição ela aparece a primeira vez
    Em que posição ela aparece a última vez
'''
frase = input('Escreva sua frase: ').strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('Ela aparece primeiro na posição {}'.format(frase.find('a')))
print('A última posição é {}'.format(frase.rfind('a')))
# rfind para procurar da direita para a esquerda.
