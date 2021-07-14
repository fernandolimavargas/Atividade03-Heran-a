from Aluno import Aluno

class AlunoEnsinoMedio(Aluno): 
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula) 
        self.ano = ano 
        print(f'Ano: {self.ano}')