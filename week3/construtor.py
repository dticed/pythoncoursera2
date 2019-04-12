class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

carro_do_meu_pai = Carro("Del Rey", 1980, "Vermelho")

print(carro_do_meu_pai.ano)
print(carro_do_meu_pai.modelo)

print(carro_do_meu_pai.cor)

        