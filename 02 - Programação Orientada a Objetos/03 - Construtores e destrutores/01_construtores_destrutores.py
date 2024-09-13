# Definindo a classe Cachorro
class Cachorro:
    # O método __init__ é o construtor da classe
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome         # Atributo nome do cachorro
        self.cor = cor           # Atributo cor do cachorro
        self.acordado = acordado # Atributo para verificar se o cachorro está acordado

    # O método __del__ é o destruidor da classe
    def __del__(self):
        print("Removendo a instância da classe.")

    # Método que simula o som que o cachorro faz
    def falar(self):
        print("auau")


# Função que cria um cachorro e imprime seu nome
def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


# Criando um objeto Cachorro e chamando seus métodos
c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

# Explicitamente deletando o objeto
del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# Criando um cachorro dentro de uma função
# criar_cachorro()
