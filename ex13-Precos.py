produto = float(input('Informe o valor do produto para receber o desconto: '))
desc = produto * 0.95
print(' O novo valor do produto com desconto é R${:.2f}.'.format(desc))


salario = float(input('Para calcular o seu aumento, informe o seu salário atual: '))
print('O seu novo salário é de R${:.2f}'.format(salario * 1.15))
