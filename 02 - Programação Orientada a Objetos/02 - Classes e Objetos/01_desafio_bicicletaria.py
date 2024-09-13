# Definindo a classe Bicicleta
class Bicicleta:
    # O método __init__ é o construtor da classe
    # É chamado quando um novo objeto da classe é criado
    def __init__(self, cor, modelo, ano, valor):
        # Inicializando os atributos da bicicleta
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Método para simular o som da buzina
    def buzinar(self):
        print("Plim plim...")

    # Método para simular a parada da bicicleta
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    # Método para simular a ação de correr
    def correr(self):
        print("Vrummmmm...")

    # Método especial __str__ para fornecer uma representação em string do objeto
    def __str__(self):
        # Retorna uma string formatada com o nome da classe e os atributos do objeto
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Criando um objeto da classe Bicicleta
b1 = Bicicleta("vermelha", "caloi", 2022, 600)

# Chamando métodos do objeto
b1.buzinar()   # Simula o som da buzina
b1.correr()    # Simula a ação de correr
b1.parar()     # Simula a parada da bicicleta

# Imprimindo os atributos do objeto diretamente
print(b1.cor, b1.modelo, b1.ano, b1.valor)

# Criando outro objeto da classe Bicicleta
b2 = Bicicleta("verde", "monark", 2000, 189)

# Imprimindo a representação em string do objeto
print(b2)

# Chamando o método correr do segundo objeto
b2.correr()



#################################


# Classe base que representa um veículo genérico
class Veiculo:
    # O método __init__ é o construtor da classe base
    def __init__(self, marca, modelo, ano):
        self.marca = marca  # Marca do veículo
        self.modelo = modelo  # Modelo do veículo
        self.ano = ano  # Ano de fabricação

    # Método para exibir informações do veículo
    def exibir_info(self):
        print(f"{self.__class__.__name__}: {self.marca} {self.modelo} ({self.ano})")

    # Método que pode ser sobrescrito pelas subclasses
    def ligar(self):
        print("Veículo ligado!")

    # Método para fornecer uma representação em string do objeto
    def __str__(self):
        return f"{self.__class__.__name__} - Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

# Classe derivada que representa um carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)  # Chama o construtor da classe base
        self.portas = portas  # Número de portas do carro

    # Sobrescreve o método ligar da classe base
    def ligar(self):
        print("Carro ligado!")

    # Método para exibir informações do carro
    def exibir_info(self):
        super().exibir_info()  # Chama o método da classe base
        print(f"Portas: {self.portas}")

    # Método específico da classe Carro
    def buzinar(self):
        print("Beep beep!")

# Classe derivada que representa uma moto
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)  # Chama o construtor da classe base
        self.tipo = tipo  # Tipo da moto (esportiva, touring, etc.)

    # Sobrescreve o método ligar da classe base
    def ligar(self):
        print("Moto ligada!")

    # Método para exibir informações da moto
    def exibir_info(self):
        super().exibir_info()  # Chama o método da classe base
        print(f"Tipo: {self.tipo}")

    # Método específico da classe Moto
    def fazer_wheelie(self):
        print("Fazendo um wheelie!")

# Criando instâncias das classes derivadas
carro1 = Carro("Toyota", "Corolla", 2024, 4)
moto1 = Moto("Harley-Davidson", "Street 750", 2021, "Cruiser")

# Chamando métodos das instâncias
carro1.exibir_info()
carro1.ligar()
carro1.buzinar()
print(carro1)

print()  # Linha em branco para separação

moto1.exibir_info()
moto1.ligar()
moto1.fazer_wheelie()
print(moto1)
