from conta_bancaria.repositorio.conta_repositorio import contas


def get_contas(numero: int) -> dict | None:
  for cliente in contas:
    if cliente["numero"] == numero:
      return cliente
  print("Conta não encontrada")  