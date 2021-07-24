from math import sqrt
from math import hypot
# cateto oposto
co = float(input('Informe o comprimento do cateto oposto: '))
# cateto adjacente
ca = float(input('Informe o comprimento do cateto adjacente: '))
hip = sqrt(co ** 2 + ca ** 2)  # usando math.sqrt para raiz quadrada
# usando math.hypot ( calcular hipotenusa, poderia jogar direto no print)
hi = hypot(co, ca)
h = (co ** 2 + ca ** 2) ** (1 / 2)  # sem usar imports
print('O valor da hipotenusa é {:.2f}'.format(hip))
print('O valor da hipotenusa é {:.2f}'.format(hi))
print('O valor da hipotenusa é {:.2f}'.format(h))
