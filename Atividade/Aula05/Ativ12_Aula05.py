#Entrada de Dados
la = int(input('Digite seu lado'))
lb = int(input('Digite seu lado'))
lc = int(input('Digite seu lado'))

#Processamento e Saída
if la == lb == lc:
    print('Equilátero')
elif la == lb or lb == lc == la:
    print('Isóceles')
elif  la != lb != lc:
    print('Escaleno')
else:
    print('Não é triangulo')
