for pov in range(1000, 2001):
    rest = pov % 11
    if rest == 5:
        print(F'Seu número de resto "5" são: ')
        print(pov)