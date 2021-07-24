''' Leia o nome de uma pessoa e diga se ela tem "SILVA" no nome'''
p = input('Informe o seu nome completo: ').strip()
p = p.title()
print('Seu nome tem Silva? {}.'.format('Silva' in p))
