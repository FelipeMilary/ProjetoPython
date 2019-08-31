class Cliente:
    def __init__(self, nome="", email="", tel="", tipo=""):
        self.nome = nome
        self.email = email
        self.telefone = tel
        self.tipo = tipo
    
if __name__ == "__main__":
    joao = Cliente("Joao da Silva", "joaodasilva@gmail.com", "3541-1230", "Aluno")
    print(joao.nome, ",", joao.email, ",", joao.telefone, ",", joao.tipo)