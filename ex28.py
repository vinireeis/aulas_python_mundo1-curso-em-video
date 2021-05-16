''' escreva um programa que faça o computador "pensar" em um número inteiro
    entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
    escolhido pelo computador'''
import random

from time import sleep

n = [0, 1, 2, 3, 4, 5]
sort = random.choice(n)
n1 = int(input('O computador está pensando em um número de 0 a 5, digite um número para saber se acertou o mesmo valor: '))
if sort == n1:
    print('Parabéns o computador pensou no {} e você digitou {}.'.format(sort, n1))
else:
    print('Você errou, o computador pensou em outro número')
    print('eu pensei no {} e você digitou {}.'.format(sort, n1))

''' forma de resolução do guanabara'''
from random import randint

comp = randint(0, 5)
print('-=-' *20)
print('Estou pensando em um número de 0 a 5. Tente adivinhar')
print('-=-' *20)
n = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)
if n ==  comp:
    print('Parabéns eu pensei no número {} e você digitou o mesmo {}'.format(comp, n))
else:
    print('Ganhei! eu pensei no número {} e você digitou {}.'.format(comp, n))
