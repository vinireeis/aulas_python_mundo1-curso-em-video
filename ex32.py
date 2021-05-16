'''Faça um programa que leia um ano e mostre se ele é bissexto.'''
ano = int(input('Informe um ano para saber se ele é Bissexto: '))  # poderia usar elif como na linha comentada ou OR como utilizado
if ano % 4 == 0 and ano % 100 != 0 or ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print("O ano de {} é bissexto!".format(ano))
#  elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:  print("O ano de {} é bissexto!".format(ano))
else:
    print ("O ano de {} não é bissexto!".format(ano))
