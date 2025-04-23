#Entrada de sálario

sala = float(input('Insira seu sálario: '))

if 0 < sala <= 2000:
    print('Seu sálario está isento')
elif 2000.1 < sala < 3500:
    imposto = sala * 0.1
    print(f'Seu sálario será de {imposto}')
elif sala > 3500:
    imposto1 = sala * 0.15
    print(f'Seu sálario será de {imposto1}')
else:
    print('Sálario invalido')