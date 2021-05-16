import math

n = int(input('Informe um valor inteiro: '))
print('Esté é o número digitado {}, este é seu antecessor {}, este é seu sucessor {}.'.format(n, n - 1, n + 1))

n1 = int(input('Informe um valor inteiro: '))
raiz = math.sqrt(n1)  # também pode ser feito como raiz = n1 ** (1/2)   
print('O dobro é {}, o triplo é {}, a raiz quadrada é {}.'.format(n1 * 2, n1 * 3, raiz))

n2 = float(input('Informe uma nota de 0 a 10: '))
n3 = float(input('Informe uma segunda nota de 0 a 10: '))
media = ((n2 + n3) / 2)
print('A sua média é {:.2f}'.format(media))

metro = float(input('Digite um valor em metros para ser convertido: '))
centimetro = metro * 100
milimetro = metro * 1000
print('Este valor de {} metros, é igual a {:.0f} centimetros e {:.0f} milimetros.'.format(metro, centimetro, milimetro))

tabuada = int(input('Informe um número para apresentar sua tabuada'))
contador = 0
for count in range(1, 10 + 1):
    print('{} x {} = {}'. format(tabuada, count, (tabuada * count)))  # OUTRA FORMA DE FAZER A TABUADA, count é a mesma coisa que X ou a mesma coisa que um contador no WHILE
