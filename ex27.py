''' faça um programa que leia o nome de uma pessoa
    mostrando o primeiro e último nome separadamente'''
nome = input(' Digite seu nome completo: ').strip().title()
n = nome.split()
print('O seu primeiro nome é {}\nO seu último nome é {}.'
      .format(n[0], n[-1]))
