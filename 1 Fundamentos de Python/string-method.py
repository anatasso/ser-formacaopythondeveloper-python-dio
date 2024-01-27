# Métodos úteis genéricos
curso = ' pYtHon '
print('.' + curso.title() + '.')
print('.' + curso.strip() + '.')
print('.' + curso.lstrip() + '.')
print('.' + curso.rstrip() + '.')
print('.'.join(curso.strip().title()))
for _ in range(1):
    A, B = input().split(' ')
    print('encaixa' if A.endswith(B) else 'nao encaixa')
print()

# Interpolação
PI = 3.14159265358979323846
print(f'Olá, este é o método f-string para concatenação de strings em {curso.strip().title()}.')
print(f'Valor de PI: {PI:10.2f}') # 10 é width que é um valor opcional
print()

# Fatiamento -> variável[start:stop:step]. Tudo(:) e espelhamento(::-1)
nome = 'Totó Tasso'
print(nome[:4])
print()

# Strings triplas
print(f"""Olá, meu nome é {nome[:4]}
Sou fera em {curso.strip().title()}.""")