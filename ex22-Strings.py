a = input('Digite o seu nome completo: ').strip()
print('Analisando seu nome...')
'''a = a.strip()'''  # podemos usar o strip direto no input
print('Seu nome é {}'.format(a))
print('Seu nome em maiuscúlas é {}'.format(a.upper()))
print('Seu nome em mainuscúlas é {}'.format(a.lower()))
# outra forma de mostrar quantos caracteres
print('Outra forma de mostrar o total de caracteres do seu nome é {}.'
      .format(len(a) - a.count(' ')))
a1 = a.split()
a2 = ''.join(a1)
print('O total de caracteres do seu nome é {}.'.format(len(a2)))
print('O total de caracteres do seu primeiro nome é {}.'.format(len(a1[0])))
# outra forma de mostrar quantos caracteres no primeiro nome(gambiarra)
print('Outra forma de mostrar o total de caracteres do primeiro nome {}.'
      .format(a.find(' ')))

