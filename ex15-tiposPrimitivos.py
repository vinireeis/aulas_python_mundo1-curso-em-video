n = input('Digite algo: ')
print(' O tipo primitivo desse valor é: ', type(n))
print(' Só tem espaços?', n.isspace())
print(' É um número?', n.isnumeric())
print(' É alfabético?', n.isalpha())          # trabalhando dados primitivos #
print(' É alphanumérico?', n.isalnum())
print(' É tudo maisculo?', n.isupper())
print(' É tudo minuscúla?', n.islower())
print(' Está Capitalizada?', n.istitle())
