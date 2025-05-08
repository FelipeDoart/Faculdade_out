import time
from loguru import logger

bd_filmes = [
    ['Matrix', 1997],
    ['Vingadores', 2015]
]

def cadastra_filmes(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd

def lista_filmes(bd):
    for i in range(len(bd)):
        print(f'{i+1} | {bd[i][1]} | {bd[i][0]}')

def altera_filme(bd, indice, titulo, ano):
    bd[indice][0] = titulo
    bd[indice][1] = ano
    return bd

def salvar_filmes(bd):
    with open ('bd_filmes.txt','w', encoding='utf-8') as arquivo:
        for i in range(len(bd)):
            logger.info (f'Salvando o filme {bd[i][0]}')
            arquivo.write(f'{bd [i][1]},{bd[i][0]}\n')
while True:
    print('1 - Cadastrar Filme')
    print('2 - Listar Filmes')
    print('3 - Alterar Filme')
    print('4 - Salvar Itens')
    try:
        op = int(input('Digite sua opção: '))
    except Exception as e:
        logger.error(f'Error:{e}')
        logger.info('Digite um valor númerico!')
        op = -1

    #Primeira opção "Listar"

    if op == 1:
        logger.info('Iniciando o cadastro de filme')
        titulo = input('Digite o título do filme: ')
        ano = int(input('Digite o ano do filme: '))

        bd_filmes = cadastra_filmes(
            bd=bd_filmes,
            titulo=titulo,
            ano=ano
        )

        logger.info('Filme Cadastrado com sucesso!')
        print('Filme cadastrado!')

    # Segunda Opção "Listar"

    elif op == 2:
        logger.info('Iniciando o listamento de filmes')

        lista_filmes(bd_filmes)

        logger.info('Filmes Listados com sucesso')

    #Terceira opção "Editar"

    elif op == 3:
        logger.info('Iniciando a edição de filme')

        lista_filmes(bd_filmes)
        i = int(input('Qual filme deseja alterar? '))
        titulo = input('Digite o novo título: ')
        ano = int(input('Digite o novo ano: '))

        bd_filmes = altera_filme(
            bd=bd_filmes,
            indice=(i-1),
            titulo=titulo,
            ano=ano
        )
        logger.warning('O Seu filme foi alterado!')

    #Quarta opção "Salvar"

    elif op == 4:
        logger.info('Iniciando salvamento dos filmes')

        salvar_filmes(bd_filmes)

        logger.info('Filmes salvos com sucesso!')

    else:
        print(f'Opção {op} inválida!')

    time.sleep(3)