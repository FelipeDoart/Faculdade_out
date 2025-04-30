Mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# Imprimir a matriz
print(Mat)

#Imprimir a segunda linha da matriz
print(Mat[1])
print(Mat[1][2])

#Desafil
print('----Solução desafio----')
for linha in Mat:
    for numero in linha:
        print(numero)
#Outro método
print('----Outra maneira----')
for i in range(len(Mat)):
    for y in range(len(Mat[i])):
        print(Mat[i][y])
