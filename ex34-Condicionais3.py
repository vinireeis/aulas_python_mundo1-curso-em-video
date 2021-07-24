'''Escreva um programa que pergunte o salário de um funcionário e calcule
    o valor do seu aumento
    se salario >1250,00 então calcule um aumento de 10%
    se <= aumento = 15%'''

sal = float(input('Informe o seu salário para receber aumento: '))
if sal > 1250:
    sal = sal * 1.10
    print('Seu novo salário é {}'.format(sal))
else:
    sal = sal * 1.15
    print('Seu novo salário é {}'.format(sal))
