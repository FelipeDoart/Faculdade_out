from math import trunc


altura = []
altH = []
altM = []
genm = 0
genf = 0

# X = a quantidade de pessoas na lista
x = int(input("Insira a quantidade de participantes: "))


for i in range(int(x)):
    i = 1

    # ESTESTICO
    print("-" * 20)

    print("Participante: ", i)
    alt = (float(input("Indique a altura: ")))
    altura.append(alt)
    gen = input("Indique o gênero (m ou f): ")
    if gen == "m":
        altH.append(alt)
        genm += 1
    elif gen == "f":
        genf += 1
    else:
        print("Digite m ou f")

menor = min(altura)
maior = max(altura)
media = sum(altH)/x

print("-"*20)
print("São", genm, "participantes masculinos e",genf,"femininos")
print("Enquanto a média das alturas masculinas é de:",media)
print("A maior altura é de:", maior)
print("Enquanto a menor é:",menor)