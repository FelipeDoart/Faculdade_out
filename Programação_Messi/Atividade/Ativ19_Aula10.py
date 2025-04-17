#Jogo Aleatorio

from random import randint


numero = randit (a:1, b:10)
tentativas = int(input('Quantas tentativas: '))

for i in range(tentativas):
    palpite = int(input('Qual o seu palpite: '))

    if numero == palpite:
        print('Correto!')
        break
    elif palpite < numero:
        print('O seu número foi abaixo!')
    elif palpite > numero:
        print('O numero é maior!')


