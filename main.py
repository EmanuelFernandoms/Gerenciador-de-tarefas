from Class_tarefa import *
from Class_usuario import *
import tkinter as tk
from tkinter import ttk
import pwinput

import sys
import os
import json
from datetime import datetime, date


if __name__ == '__main__':


# criação do arquivo json
    # contas = {}
    # tarefas_dict = {}
    # projetos_dict = {}


    # data_folder = 'data'

    # if not os.path.exists(data_folder):
    #     os.makedirs(data_folder)

    # data_file_tarefas = os.path.join(data_folder, 'tarefas.json')
    # data_file_projetos = os.path.join(data_folder, 'projetos.json')
    # data_file_contas = os.path.join(data_folder, 'contas.json')

    # if os.path.exists(data_file_tarefas) and os.path.getsize(data_file_tarefas) > 0:
    #     with open(data_file_tarefas, 'r') as f:
    #         data = json.load(f)
    #         if data:
    #             tarefas_dict = {int(key): value for key,value in data.items()}
    #         else:
    #             tarefas_dict = {}

    # if os.path.exists(data_file_projetos) and os.path.getsize(data_file_projetos) > 0:
    #     with open(data_file_projetos, 'r') as f:
    #         data = json.load(f)
    #         if data:
    #             projetos_dict = {int(key): value for key,value in data.items()}
    #         else:
    #             projetos_dict = {}

    # if os.path.exists(data_file_contas) and os.path.getsize(data_file_contas) > 0:
    #     with open(data_file_contas, 'r') as f:
    #         data = json.load(f)
    #         if data:
    #             contas = {int(key): value for key,value in data.items()}
    #         else:
    #             contas = {}

# subsitituir o sistema de keys 1,2,3,4,5 para uma geração de numeros aleatórios com sla 10 casas
    # count = max(contas.keys(), default=0) + 1
    # count_tarefas = max(tarefas_dict.keys(), default=0) + 1
    # count_projetos = max(projetos_dict.keys(), default=0) + 1


    count_tarefas = 0
    count_projetos = 0
    count = 0

    while True:
        print("""
1- Login
2- Cadastro
0- Sair
""")

        try:
            choice = int(input("Escolha uma opção: "))
        except:
            input("Opção inválida...")
            continue

        if choice == 0:
            sys.exit()

        elif choice == 1:
            email = input("E-mail: ")
            index = Usuario.buscar_por_email(email)

            if index is None:
                input("Essa conta não existe...")
                continue

            senha = pwinput.pwinput("Digite sua senha: ")
            if contas[index]['senha'] != senha:
                input("Senha incorreta...")
                continue
                

        elif choice == 2:
            nome = input("Digite seu nome completo: ")
            while True:
                email = input("Digite seu email: ")
                if any(conta['email'] == email for conta in contas.values()):
                    input("Email já cadastrado, forneça outro email")
                else:
                    break

            while True:
                senha = pwinput.pwinput("Digite sua senha: ")
                confirmacao = pwinput.pwinput("Repita a senha: ")
                if senha != confirmacao:
                    input("A confirmação está diferente da senha...")
                    continue
                else:
                    break
            contas[count] = {"nome": nome,
                            "email": email,
                            "senha": senha,
                            "tarefas": [],
                            "projetos": []
                            }
            with open(data_file_contas, 'w') as f:
                json.dump(contas, f, indent=4)
            input("Conta cadastrada com sucesso!!")
            index = max(contas.keys())
            senha = contas[index]['senha']
            


        contaAtual = Usuario(
            contas[index]['nome'],
            contas[index]['email'],
            contas[index]['senha']
        )
        break

    while True:

        choice = int(input("""
0 - Sair
1 - Criar tarefa
2 - Criar Projeto
3 - ver minhas tarefas
4 - ver meus projetos
5 - Adicionar pessoa em atividade
6 - Adicionar pessoa em projeto
choice: 
"""))
        
        if choice == 0:
            sys.exit()
    
        elif choice == 1:
            nome = input("Digite o nome da atividade: ")
            descricao = input("Descrição: ")
            data_vencimento_str = input("Digite a data de vencimento (formato YYYY-MM-DD): ")
            try:
                data_vencimento = datetime.strptime(data_vencimento_str, "%Y-%m-%d")
                # Verifica se a data é no futuro
                if data_vencimento.date() < date.today():
                    print("A data de vencimento não pode ser no passado. Digite uma data válida.")
                    continue
            except ValueError:
                print("Formato de data inválido. Use o formato YYYY-MM-DD.")

            contaAtual.criar_tarefa(nome,descricao,data_vencimento_str, index)


            # tarefas_dict[count_tarefas] = {
            #     "nome": nome,
            #     "descricao": descricao,
            #     "data_vencimento": data_vencimento_str,
            #     "status": "pendente"
            # }

            # with open(data_file_tarefas, 'w') as f:
            #     json.dump(tarefas_dict, f, indent=4)
            

            # contas[index]['tarefas'].append(count_tarefas)
            # with open(data_file_contas, 'w') as f:
            #     json.dump(contas, f, indent=4)
            # count_tarefas = max(tarefas_dict.keys(), default=0) + 1

        
        elif choice == 2:
            nome = input("Digite o nome do projeto: ")
            descricao = input("descrição: ")
            contaAtual.criar_projeto(nome, descricao, index)

            


        elif choice == 3:
            tarefas_usuario = contas[index]['tarefas']
            for i in tarefas_usuario:
                tarefa = tarefas_dict.get(i)
                print(f"tarefa: {tarefa['nome']}, termino: {tarefa['data_vencimento']}, status: {tarefa['status']}")
            input()


        elif choice == 4:
            projetos_usuario = contas[index]['projetos']
            for i in projetos_usuario:
                projeto = projetos_dict.get(i)
                print(f"tarefa: {projeto['nome']}, descrição: {projeto['descricao']}")
            input()

        elif choice == 5:
            pass