from math import trunc

n = float(input('Informe um número real, para transformar em um valor'
                'truncado: '))
# usando import math.trunc
print('O número real é {} e seu valor truncado é {}.'.format(n, trunc(n)))
# usando conversão em int (três formas de fazer)
print('O número real é {} e seu valor truncado é {}.'.format(n, int(n)))
# usando format
print('O número real é {} e seu valor truncado é {:.0f}.'.format(n, n))
