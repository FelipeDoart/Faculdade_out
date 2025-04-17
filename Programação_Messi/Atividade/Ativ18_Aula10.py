#Lista de notas
list = []
#Loop infinito
while True:
    nota = float(input('Digite sua nota: '))
    #Caso queira finalizar, digite "-1"
    if nota == -1:
        break
    elif 0 <= nota <= 10:
        list.append(nota)
    else:
        print(f'Caractere {nota} Invalido')
soma = 0
for i in range(len(list)):
    soma = soma + list[i]
media = soma / len(list)

print(f'A sua média é -> {media}')
print(f'As suas notas são: {list}')