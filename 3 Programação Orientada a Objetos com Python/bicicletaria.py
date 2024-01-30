class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print('Plim plim')
    
    def parar(self):
        print('Bicicleta parada')

    def correr(self):
        print('Vrummmmm')

    def __str__(self):
        # return f'Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}'
        return f'{self.__class__.__name__}: {", ".join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}'
        
caloi = Bicicleta('vermelha', 'caloi', 2022, 600)
caloi.buzinar()
caloi.correr()
caloi.parar()
print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)
Bicicleta.parar(caloi)
print(caloi) # tá acessando def __str__