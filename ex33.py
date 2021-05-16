'''Faça um programa que leia 3 números, qual é o maior, qual é o menor'''
numeros = []
numeros.append(int(input('Digite um número: ')))
numeros.append(int(input('Digite o segundo número: ')))
numeros.append(int(input('Digite o último número: ')))
numeros = sorted(numeros)
print('O menor valor é: {} e o maior {}.'.format(numeros[0], numeros[-1]))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o último número'))
if n1 > n2 and n1 > n3 and n2 > n3:
    print('O maior número é {} e o menor é {}'. format(n1, n3))
elif n1 > n2 and n1 > n3 and n3 > n2:
    print('O maior número é {} e o menor é {}'. format(n1, n2))
elif n2 > n1 and n2 > n3 and n3 > n1:
    print('O maior número é {} e o menor é {}'. format(n2, n1))
elif n2 > n1 and n2 > n3 and n1 > n3:
    print('O maior número é {} e o menor é {}'. format(n2, n3))
elif n3 > n1 and n3 > n2 and n2 > n1:
    print('O maior número é {} e o menor é {}'. format(n3, n1))
else:
    print('O maior número é {} e o menor é {}'. format(n3, n2))
    # guanabara utilizou variáveis menor e maior para guardar os valores.