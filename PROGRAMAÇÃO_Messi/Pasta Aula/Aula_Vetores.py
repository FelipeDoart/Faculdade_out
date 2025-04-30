# Teste de Matrizes e Vetores

film = [
    'Up',
    'Vingadores',
    'Barbie',
    'Sonic'
]

print('---Imprimindo a lista completa---')
# Imprimindo a lista completa
print(film)
print('-'*100)

print('---Imprimindo um filmes---')
# Imprimindo um filmes
print(film[1].upper())

print('----- Pecorrendo uma Lista (fácil)-----')
# Percorrer a Lista de filme
for nomes in film:
    print(nomes.upper())

print('---Percorrer a lista - Vetores---')
#Percorrer a lista - Vetores
for i in range(len(film)):
    print(film[i].upper())

