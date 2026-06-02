class Funcionario: # classe mãe 
    def __init__(self, nome, matricula, salario_fixo):
        self.nome = nome
        self.matricula = matricula
        self.salario_fixo = salario_fixo

    # encapsulamento 
    # @property
    # def matricula(self):
    #    return self.__matricula
    @property
    def salario_fixo(self):
        return self.__salario_fixo
    
    @salario_fixo.setter
    def salario_fixo(self, new_salario):
        if new_salario <= 0:
            raise ValueError("O salário não pode ser negativo.")
        self.__salario_fixo = new_salario

    # polimorfismo
    def calcular_salario():
        return print('Tipo de usuário não específicado.')
    def exibir():
        return print('Tipo de usuário não específicado.')
    
# Classe-filha CLT (apenas o salário fixo)
class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        # iniciando os campos da classe-mãe
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return f'R$ {self.salario_fixo:.2f}'
    
    def exibir(self):
        return f'[CLT #{self.matricula}] {self.nome} - {self.calcular_salario()}'
    
# Classe-filha Vendedor (salário fixo + comissão)
class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_fixo, total_vendas):
        self.total_vendas = total_vendas

        # iniciando os campos da classe-mãe
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        salario_final = self.salario_fixo + (self.total_vendas * 0.1)
        return f'R$ {salario_final:.2f}'
    
    def exibir(self):
        return f'[VENDEDOR #{self.matricula}] {self.nome} - {self.calcular_salario()}'
    
# Classe-filha Gerente (Salário fixo + bônus)
class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        # iniciando os campos da classe-mãe
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        salario_final = self.salario_fixo + 1500.0
        return f'R$ {salario_final:.2f}'
    
    def exibir(self):
        return f'[GERENTE #{self.matricula}] {self.nome} - {self.calcular_salario()}'
    

gerente = Gerente(nome='Emanuel', matricula='456789', salario_fixo=3000)
clt = CLT(nome='Mariah', matricula='096789', salario_fixo=2000)
vendedor = Vendedor(nome='Nicholas', matricula='028642', salario_fixo=2500, total_vendas=1500)

for funcionario in Funcionario.objects():
    