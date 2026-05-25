# Exercício 1 – ex01_oo.py
class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
obj1 = Product('Pão', 5)
obj2 = Product('Banana', 15)

print(f'1° Produto: {obj1.nome} R$ {obj1.preco}')
print(f'2° Produto: {obj2.nome} R$ {obj2.preco}')

# Exercício 2 – ex02_oo.py
class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percent):
        self.preco = self.preco - (self.preco * (percent / 100))

obj1 = Product('Pão', 5)
obj2 = Product('Banana', 15)

print(f'Preco do {obj1.nome} antes do desconto: R$ {obj1.preco}')
obj1.desconto(percent=10)
print(f'Preco do {obj1.nome} depois do desconto: R$ {obj1.preco}')

# Exercício 3 – ex03_oo.py
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
    def freiar(self):
        self.velocidade -= 10
    def acelerar(self):
        self.velocidade += 10
    def __str__(self):
        return f'{self.modelo} [{self.marca}]'
        
carro = Carro('Volkswagen', 'Fusca')
carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.freiar()
print(f'Velocidade do {carro}: {carro.velocidade}')

# Desafio – ex04_oo.py
class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if self.saldo < valor:
            return print(f"Saldo insuficiente [Atual: R$ {self.saldo}].")
        else:
            self.saldo -= valor
            return print(f'Valor sacado [Saldo atual: R$ {self.saldo}].')
    def extrato(self):
        return f"{self.titular} [Saldo atual: R$ {self.saldo}]"