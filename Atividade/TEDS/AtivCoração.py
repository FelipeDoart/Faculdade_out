from queue import PriorityQueue

times = []

quant = int(input('Quantos serão? '))
i = 0
while i < quant:
    times.append(input(f'Qual o time {i + 1} ? '))
    i += 1

    if i == quant:
        print('--- SELEÇÃO DE ITEM ---')
        selecao = input('Seleção desejada? ')
        find = False


#Progresso de procura
print('-'*20)
for i in range(len(times)):

    if selecao.upper() == times[i].upper():
        find = True
if find:
    print('Encontrado!')
else:
    print('Não encontrado!')

