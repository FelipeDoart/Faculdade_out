from random import randint

matriz = [

]

for i in range(10):
    lista_temporaria = []
    for l in range(10):
        lista_temporaria.append(randint(0, 1000))

    matriz.append(lista_temporaria)
maior = -1
#Percorrer a matriz ultilizando o conceito de vetores e matrizes
for li in range(len(matriz)):
        print(matriz[li])
        for co in range(len(matriz[li])):
            print(matriz[li][co])
            if matriz[li][co] > maior:
                maior = matriz[li][co]

print(f'Sendo o maior valor é: {maior}')