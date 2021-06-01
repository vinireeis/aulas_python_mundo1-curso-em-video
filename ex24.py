''' Leia um nome de uma cidade e diga se começa com a palavra Santo'''
c = input('Escreva o nome da sua cidade: ').strip()
c = c.title()
if 'Santo' in c:
    print('Sua cidade começa com a palavra Santo')
else:
    print('Não tem a palavra Santo')
# nesse caso melhor usar o print(c[:5] == Santo) para validar o começo
