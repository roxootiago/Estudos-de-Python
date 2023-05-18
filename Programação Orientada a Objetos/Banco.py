def criarConta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite":
        limite}
    return conta


def depositar(conta, valor):
    conta["saldo"] += valor


def sacar(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print(f"Saldo atual: {conta['saldo']}")


conta = criarConta(212, "Tiago", 400, 5000)
print(conta)

depositar(conta, 200)
extrato(conta)

sacar(conta, 150)
extrato(conta)
