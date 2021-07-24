n1 = int(input('Digite um valor:'))  # trabalhando aritiméticos
n2 = int(input('Digite outro valor:'))
soma = n1 + n2
subtrai = n1 - n2
multiplica = n1 * n2
divisao = n1 / n2  # divisão normal, divide em float, ou seja 3/2 é 1.5.
divisao_inteira = n1 // n2  # divisão inteira não considera o resto para antes de colocar virgula na divisão
exponenciacao = n1 ** n2  # exponente 4² = 16
resto = n1 % n2   # resto da divisão
print('O total da soma é {}, a subtração é {}, o produto é {}, a divisão é {}, a divisão inteira é {}, a exponenciacao é {}, o resto é {}.'.format(soma, subtrai, multiplica, divisao, divisao_inteira, exponenciacao, resto))
print(' Mostrando a divisão com formatação, a divisão é {:.3f}'.format(divisao))    # dentro da chaves podemos formatar o texto ou valor apresentado como {:.3f} dizendo que quero 3 casas depois da "virgula"
print(' Queabrando linha com "BARRAn" \n linha foi quebrada e juntando com o próximo print usando a tag "end"', end=' ')
print(' Este print é separado mas foi juntado pela tag end')
