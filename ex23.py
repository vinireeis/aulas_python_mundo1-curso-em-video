n = int(input('Informe um número de 0 a 9999: '))
if n >= 0 and n <= 9999:
    n1 = str(n)
    # n2 = n1.split() não é necessário
    print(n1)
    print('A casa do milhar é {}\nda centena {}\nda dezena {}\nda unidade {}'.format(n1[0], n1[1], n1[2], n1[3]))
else:
    print('Você digitou um número incorreto, tente novamente.')


''' forma do guanabara'''
num = int(input('Informe um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O milhar é {}\nA centena é {}\nA dezena é {}\nA unidade é {}.'.format(m, c, d, u))