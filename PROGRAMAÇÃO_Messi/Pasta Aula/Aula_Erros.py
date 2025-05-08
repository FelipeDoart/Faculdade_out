#TRATAMENTO DE ERROS E EXCEÇÃO

# Exceções: Objetos especiais chamados para administrar erros que surgirem durante a execução.
# Sempre que ocorrer um erro, uma exceção será criada.

try:
    print(50/0)

except ZeroDivisionError as e:
    print(f'Error: {e}')