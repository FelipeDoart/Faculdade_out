
def contagem_vogais(string):
    result = {}
    vogais = 'aeiouAEIOU'
    for i in vogais:
        if i in string:
            result[i] = string.count(i)
    return result
print('Irei contar as vogais de sua palavra')
print('-'*50)
print(contagem_vogais(input('Digite a palavra que será lida: ')))
