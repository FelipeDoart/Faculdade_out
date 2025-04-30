#SUBPROGRAMAS:
#FUNCTIONS  &  PROCEDURES
#-----------------------------------------------------------------------------------------------------#
#Podem ser definidos por:
#Blocos separados contendo instruições que podem ser "Chamados" pelo nome
#Tipos:
#Funções: Retornam um valor;
#Procedimentos: Realizam uma ação, não retoma valor.

#Ex.:
def somar (a, b):
    return  a + b

def minha_funcao():
    variavel_local = "Sou local"
    print(variavel_local)
#Variaveis criadas dentro da função não poderão ser citadas fora.
#Ex.: "variavel_local"
minha_funcao() #Será imprimido "Sou local"