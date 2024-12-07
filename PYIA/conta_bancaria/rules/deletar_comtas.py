from conta_bancaria.repositorio.conta_repositorio import contas
from conta_bancaria.rules.buscar_conta import get_contas

def delete_conta(numero: int) -> None:
    conta_old = get_contas(numero)
    if conta_old:
        contas.remove(conta_old)
        return None
    print("Conta não encontrada!")
    return None
