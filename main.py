from Class_projeto import *
from Class_tarefa import *
from Class_usuario import *
import tkinter as tk
from tkinter import ttk
import pwinput
import os
import json


if __name__ == '__main__':


# criação do arquivo json
    contas = {}
    data_folder = 'data'

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    data_file = os.path.join(data_folder, 'contas.json')

    if os.path.exists(data_file) and os.path.getsize(data_file) > 0:
        with open(data_file, 'r') as f:
            data = json.load(f)
            if data:
                contas = {int(key): value for key,value in data.items()}
            else:
                contas = {}

# subsitituir o sistema de keys 1,2,3,4,5 para uma geração de numeros aleatórios com sla 10 casas
    count = max(contas.keys(), default=0) + 1

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
            break

        elif choice == 1:
            index = int(input("Número da conta: "))
            if not index in contas:
                input("Essa conta não existe...")
                continue
            else:
                senha = pwinput.pwinput("Digite sua senha: ")
                if contas[index]['senha'] != senha:
                    input("senha incorreta...")
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
                            "atividades": []
                            }
            with open(data_file, 'w') as f:
                json.dump(contas, f, indent=4)
            input("Conta cadastrada com sucesso!!")
            index = max(contas.keys())
            senha = contas[index]['senha']
            


        contaAtual = Usuario(
            contas[index]['nome'],
            contas[index]['email'],
            contas[index]['senha']
        )
        

        input('a')