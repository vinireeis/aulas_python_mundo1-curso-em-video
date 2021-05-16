'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
    se ele pode ou não formar um triangulo/ estudar regra de poder montar triangulo'''
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
t1 = float(input('Informe o tamanho do primeiro seguimento: '))
t2 = float(input('Informe o segundo seguimento: '))
t3 = float(input('Informe o terceiro seguimento: '))
if t1  < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os seguimentos digitados, podem formar um triângulo!')
else:
    print('Os seguimentos não podem formar um triângulo!')
