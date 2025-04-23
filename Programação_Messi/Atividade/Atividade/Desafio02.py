arq = 'arquivo.txt'
numero = int(input())
with open (arq, 'w', encoding='utf-8') as Tabuda:
    for m in range(1, 11):
        res = numero * m
        Tabuda.write(f'{numero} x {m} = {res}\n')