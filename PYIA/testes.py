from conta_bancaria.rules.cadastrar_conta import add_conta, contas
from conta_bancaria.rules.buscar_conta import get_contas
from conta_bancaria.rules.listar_contas import listar
from conta_bancaria.rules.deletar_comtas import delete_conta
from conta_bancaria.rules.editar_conta import edit_conta
from conta_bancaria.rules.saque import sacar

sacar(1, 1000)
sacar(1, 500)
sacar(1, 500)
sacar(-1, 500)


add_conta("Joana Marta")
print(contas)
# print(get_contas(1))
# print(get_contas(-1))
# listar()
# delete_conta(1)
# listar()
# edit_conta(1, "carlos felino")
# edit_conta(-1, "asasa")
# print(contas)










































