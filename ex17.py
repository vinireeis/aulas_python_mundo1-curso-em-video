from math import sqrt
from math import hypot

co = float(input('Informe o comprimento do cateto oposto: '))     # cateto oposto
ca = float(input('Informe o comprimento do cateto adjacente: '))      # cateto adjacente
hip = sqrt(co ** 2 + ca ** 2)  # usando math.sqrt para raiz quadrada
hi = hypot(co, ca)  # usando math.hypot ( calcular hipotenusa, poderia jogar direto no print)
h = (co ** 2 + ca ** 2) ** (1 / 2)  # sem usar imports
print('O valor da hipotenusa é {:.2f}'.format(hip))
print('O valor da hipotenusa é {:.2f}'.format(hi))
print('O valor da hipotenusa é {:.2f}'.format(h))
