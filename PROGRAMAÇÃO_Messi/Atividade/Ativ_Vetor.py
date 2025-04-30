from random import randint


q = []


for n in range (20):
    numero = randint(0, 1000)
    q.append(numero)

maior = -1
menor = 1000
indice_M = -1
indice_m = -1

for i in range(len(q)):
    #Teste de maior
    if q[i] > maior:
        maior = q[i]
        indice_M = i

    #Teste de menor

    if q[i] < menor:
        menor = q[i]
        indice_m = i

print(q)
print(maior)
print(indice_M)
print(menor)
print(indice_m)

