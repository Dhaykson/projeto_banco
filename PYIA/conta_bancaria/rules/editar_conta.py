from conta_bancaria.repositorio.conta_repositorio import contas
from conta_bancaria.rules.buscar_conta import get_contas

def edit_conta(numero: int, novo_nome: str) -> None:
    conta = get_contas(numero)
    if conta:
      conta['nome'] = novo_nome
      