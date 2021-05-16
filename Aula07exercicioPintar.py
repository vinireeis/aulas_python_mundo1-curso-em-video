altura = float(input('Vamos calcular a área, digite em metros a altura da parede: '))
base = float(input('Agora, digite em metros o comprimento da parede: '))
area = base * altura
print('O tamanho da área é de {:.2f}m² e a quantidade de tinta necessária é {:.2f} litros.'.format(area, (area / 2)))

c = float(input('Informe a temperatura em Celsius: '))
f =  c * 9/5 + 32
print('A temperatura é {:.0f} fahrenheit.'.format(f))

p = float(input('Informe a quantidade de km percorrido: '))
d = float(input('informe por quantos dias ficou com o carro: '))
preco = (p * 0.15) + (d * 60)
print(' O valor total a se pagar é R${:.2f} pelo uso do automóvel.'.format(preco))
