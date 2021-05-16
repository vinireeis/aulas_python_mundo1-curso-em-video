''' leia qual a distancia de uma viagem em KM.
    calcule o preço da passagem, cobrando R$0,50 por KM para viagens até 200km
    calcule R$0,45 para viagens >200km'''

viagem = int(input('Informe qual a distância (em kilometros) da viagem que deseja fazer: '))
if viagem <= 200:
    custo = viagem * 0.50   # guardando o valor do custo em uma variável
    print('Sua passagem vai custar R${:.2f}.'.format(custo))
else:
    print('Sua passagem vai custar R${:.2f}.'.format(viagem * 0.45))  # fazendo o cálculo direto no format mas não guardando o valor da variável
