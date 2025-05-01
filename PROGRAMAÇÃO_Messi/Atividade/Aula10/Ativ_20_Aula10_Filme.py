# Menu

banco_filme = []


def cadastra_filmes(lista, titulo, ano):
    filme = [titulo, ano]
    lista.append(filme)
    return lista

def lista_filme(bd):
    for i in range(len(bd)):
        print(f'{i+1} | {bd[i][1]} {bd[i][0]}')

def altera_filme (bd, indice, titulo, ano):
    bd[indice][0] = titulo
    bd[indice][1] = ano
    return bd

while True:
    print('1 - Cadastrar Filmes')
    print('2 - Listar Filmes')
    print('3 - Alterar Filmes')
    op = int(input('Digite sua opção: '))
    # Configurando as opções

    if op == 1:
        filme = input('Insira seu filme: ')
        ano = int(input('Insira o Ano de lançamento: '))
        banco_filme = cadastra_filmes(
            lista=banco_filme,
            titulo=filme,
            ano=ano
        )
        print('Filme cadastrado')
    elif op == 2:
        lista_filme(banco_filme)
    elif op == 3:
        lista_filme(banco_filme)
        i = int(input('Qual o filme deseja alterar? '))
        titulo = input('Digite o novo título: ')
        ano = int(input('Digite o novo ano: '))
        banco_filme = altera_filme(
            bd=banco_filme,
            indice=(i-1),
            titulo=titulo,
            ano=ano
        )