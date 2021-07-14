class Aluno: 
    def __init__(self, codigo, nome, matricula):  
        self.codigo = codigo 
        self.nome = nome
        self.matricula = matricula
        self.imprimir()

    def imprimir(self):
        print(f'Codigo: {self.codigo}\nNome: {self.nome}\nMatricula: {self.matricula}')
    