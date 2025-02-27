from conta_bancaria.rules.buscar_conta import get_contas
from conta_bancaria.rules.extrato import criar_extrato

def sacar(numero: int, valor: float) -> None:
    conta = get_contas(numero)
    if not conta:
        return None
    
    if valor > conta['saldo']:
        print('Saldo Insuficiente!')
        return
    conta['saldo'] -= valor
    transacao = criar_extrato("saque", valor)
    conta['extrato'].append(transacao)
    print('Saque realizado com sucesso!')
