class Tarefa:
    def __init__(self, titulo, descricao, data_vencimento, usuarios, status="pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.usuarios = usuarios
        self.status = status