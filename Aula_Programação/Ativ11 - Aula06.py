esAt = int(input('Insira a quantidade atual do estoque: '))
esMx = int(input('Insira a quantidade máxima do estoque: '))
esMi = int(input('Insira a quantidade mínima do estoque: '))

esmed = (esMx + esMi)/2

if esmed >= esAt:
    print('Não Efetue a compra.')
else:
    print('Efetuar a compra.')