import math
angulo = float(input('Informe o ângulo para calcular seno, cosseno'
                     ' e tangente: '))
seno = math.sin(math.radians(angulo))
conseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo de {:.0f}º tem o seno de {:.2f}, o coseno de {:.2f} e '
      'a tangente de {:.2f}.'.format(angulo, seno, conseno, tangente))
