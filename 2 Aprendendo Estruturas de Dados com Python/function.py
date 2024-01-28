def exibir_mensagem(parametro='Não foi passado parâmetro'):
    print(f'{parametro}')
    return None # default

exibir_mensagem()
exibir_mensagem('Ana')
exibir_mensagem(parametro='Ana')

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(retorna_antecessor_e_sucessor(1))

# *args (tupla [valores separados por vírgula, independente de parênteses])
# **kwargs (dicionário [estrutura chave e valor])