tabuada = int(input('Informe um número inteiro para apresentar sua tabuada: '))

for x in range(1, 10 + 1):
    tab = tabuada * x       # print('{} x {} = {}'. format(tabuada, count, (tabuada * count)))  # OUTRA FORMA DE FAZER A TABUADA, count é a mesma coisa que X ou a mesma coisa que um contador no WHILE
    print('{} x {} = {}'.format(tabuada, x, tab))

valor = float(input('Digite quantos reais quer converter em dólares: '))
dolar = valor / 3.27
print('Você tem {:.2f} reais e pode trocar em {:.2f} dólares.'.format(valor, dolar))
