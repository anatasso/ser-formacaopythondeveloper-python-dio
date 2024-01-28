# Dicionário: {chave: valor}, sendo que a chave deve ser imutável
pessoa = {'nome': 'Ana', 'idade': 30}

pessoa1 = dict(nome='Ana', idade=30)
pessoa1['telefone'] = '9 9999-9999'

pessoa['nome']

# Dicionários aninhados
contatos = {'ana@gamil.com': {'nome': 'Ana', 'telefone': '9 9999-9999'}}

# Iterar
for chave in pessoa:
    print(chave, pessoa[chave])

for chave, valor in pessoa1.items(): # Melhor forma
    print(chave, valor)

# Métodos
pessoa.clear()
pessoa.copy()
pessoa.fromkeys(['nome','telefone']) # {'nome': None, 'telefone': None}
pessoa.fromkeys(['nome','telefone'], 'vazio') # {'nome': 'vazio', 'telefone': 'vazio'}
pessoa.get('chave') # None
pessoa.get('chave', {}) # {}
pessoa.items() # retorna lista de tuplas
pessoa.keys() # retorna as chaves do dicionário
pessoa.pop('chave', {}) # {}
pessoa.popitem() # retira os itens na sequência, não passamos parâmetro de chave
pessoa.setdefault('telefone', '9 9999-9999') # Se não existe, adc no dict. Sempre retorna o valor da chave.
pessoa.update()
pessoa.values()
'nome' in pessoa # True -> verifica se existe a chave no dict
del pessoa['idade']