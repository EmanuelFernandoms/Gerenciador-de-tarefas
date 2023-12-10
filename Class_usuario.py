# class Usuario:
#     def __init__(self, nome, email, senha):
#         self.nome = nome
#         self.email = email
#         self.senha = senha

#     def criar_tarefa (self):
#         pass

#     def criar_projeto (self):
#         pass

#     def excluir_tarefa (self):
#         pass

#     def mudar_data_tarefa (self):
#         pass

from Class_tarefa import Tarefa
from Class_projeto import Projeto

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.projetos = []

    def criar_tarefa(self, projeto, titulo, descricao, data_vencimento, status="pendente"):
        tarefa = Tarefa(titulo, descricao, data_vencimento, [self], status)
        projeto.tarefas.append(tarefa)
        return tarefa

    def criar_projeto(self, nome, descricao):
        projeto = Projeto(nome, descricao)
        self.projetos.append(projeto)
        return projeto

    def excluir_tarefa(self, projeto, tarefa):
        if tarefa in projeto.tarefas:
            projeto.tarefas.remove(tarefa)
            return True
        else:
            return False

    def mudar_data_tarefa(self, tarefa, nova_data):
        tarefa.data_vencimento = nova_data
        return tarefa