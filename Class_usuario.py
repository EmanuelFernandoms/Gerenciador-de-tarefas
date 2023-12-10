from datetime import datetime, date
from Class_tarefa import *
import json
import os


contas = {}

data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

data_file_contas = os.path.join(data_folder, 'contas.json')

if os.path.exists(data_file_contas) and os.path.getsize(data_file_contas) > 0:
        with open(data_file_contas, 'r') as f:
            data = json.load(f)
            if data:
                contas = {int(key): value for key,value in data.items()}
            else:
                contas = {}

count = max(contas.keys(), default=0) + 1
count_tarefas = max(tarefas_dict.keys(), default=0) + 1
count_projetos = max(projetos_dict.keys(), default=0) + 1





class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha
        self.projetos = []

    def __str__(self):
        return f"Nome: {self.nome}\nEmail: {self.email}\nSenha: {self.senha}\nProjetos: {self.projetos}"

    @classmethod
    def buscar_por_email(cls, email):
        for index, conta in contas.items():
            if conta['email'] == email:
                return index
        return None

    def criar_tarefa(self,nome, descricao, data_vencimento_str, index):
        global count_tarefas  # Adicione esta linha para indicar que a variável está no escopo global

        tarefas_dict[count_tarefas] = {
            "nome": nome,
            "descricao": descricao,
            "data_vencimento": data_vencimento_str,
            "status": "pendente"
        }

        with open(data_file_tarefas, 'w') as f:
            json.dump(tarefas_dict, f, indent=4)

        contas[index]['tarefas'].append(count_tarefas)
        with open(data_file_contas, 'w') as f:
            json.dump(contas, f, indent=4)
        count_tarefas += 1





    def criar_projeto(self, nome, descricao, index):
        global count_projetos
    
        projetos_dict[count_projetos] = {
            "nome": nome,
            "descricao": descricao,
            "tarefas": []
        }
        with open(data_file_projetos, 'w') as f:
            json.dump(projetos_dict, f, indent=4)

        contas[index]['projetos'].append(count_projetos)
        with open(data_file_contas, 'w') as f:
            json.dump(contas, f, indent=4)
        count_projetos = max(tarefas_dict.keys(), default=0) + 1


    def adicionar_pessoa(self, id_tarefa, index):

        id_tarefa = int(id_tarefa)
        if id_tarefa not in tarefas_dict:
            print("ID da tarefa não encontrado.")
            return
        
        contas[index]['tarefas'].append(id_tarefa)

        with open(data_file_contas, 'w') as f:
            json.dump(contas, f, indent=4)

