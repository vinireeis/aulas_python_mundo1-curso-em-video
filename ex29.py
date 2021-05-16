''' escreva um programa que leia a velocidade de um carro
    se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
    a multa vai custar 7,00 por cada km acima do limite.
    '''

velc = float(input('Informe a velocidade do carro em KM/H: '))
if velc >= 80:
    multa = (velc - 80) * 7
    print('Você ultrapassou a velocidade e será multado em {:.2f} reais.'.format(multa))
else:
    ('Você está dentro da velocidade correta, obrigado por dirigir com segurança!')
