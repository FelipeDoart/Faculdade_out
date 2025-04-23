list = []
nub = int(input('Quantos amigos: '))
n = 1
while n <= nub:
    list.append(input('Insira seu amigo: '))
    n += 1
for nome in list:
    print(f'olá {nome}')