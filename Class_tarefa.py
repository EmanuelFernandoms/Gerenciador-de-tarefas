from datetime import datetime, date
import os
import json

tarefas_dict = {}
projetos_dict = {}

data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

data_file_tarefas = os.path.join(data_folder, 'tarefas.json')
data_file_projetos = os.path.join(data_folder, 'projetos.json')

if os.path.exists(data_file_tarefas) and os.path.getsize(data_file_tarefas) > 0:
        with open(data_file_tarefas, 'r') as f:
            data = json.load(f)
            if data:
                tarefas_dict = {int(key): value for key,value in data.items()}
            else:
                tarefas_dict = {}

if os.path.exists(data_file_projetos) and os.path.getsize(data_file_projetos) > 0:
    with open(data_file_projetos, 'r') as f:
        data = json.load(f)
        if data:
            projetos_dict = {int(key): value for key,value in data.items()}
        else:
            projetos_dict = {}

class Atividade:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao



class Tarefa(Atividade):
    def __init__(self, nome, descricao, data_vencimento, status="pendente"):
        self.nome = nome
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.status = status

    def __str__(self):
        return f"Nome: {self.nome}\nDescrição: {self.descricao}\ndata_vencimento: {self.data_vencimento}\nstatus: {self.status}"



class Projeto(Atividade):
    def __init__(self, nome, descricao):
        super().__init__(nome, descricao)
        self.tarefas = []

    def __str__(self):
        return f"{super().__str__()}\nTarefas: {', '.join(tarefa.nome for tarefa in self.tarefas)}"
