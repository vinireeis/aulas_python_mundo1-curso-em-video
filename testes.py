a = 15 % 7
b = 10 % 2
c = 87 % 13
d = 127 % 35
e = 56 % 6

print(f'{a}, {b}, {c}, {d}, {e}')


valor = 45
for x in range(1, 4):
    if valor % 2 == 0:
        valor = valor/2
    else:
        valor -= 5
print(valor)


def fizzbuss(x):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")

    elif x % 3 == 0:
        print("Fizz")

    elif x % 5 == 0:
        print("Buzz")

    else:
        print("nothing")


print('-' * 30)
print(fizzbuss(18))
print('-' * 30)
print(fizzbuss(15))
print('-' * 30)
print(fizzbuss(10))
