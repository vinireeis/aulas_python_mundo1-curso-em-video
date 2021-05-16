''' crie um programa que leia um número inteiro qualquer e mostre
    se ele é par ou ímpar'''

n = int(input('Informe um número para saber se ele é par ou ímpar: '))
if n % 2 == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é ÍMPAR.'.format(n))
