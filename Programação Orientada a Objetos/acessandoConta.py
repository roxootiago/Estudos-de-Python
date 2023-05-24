from Conta import *

nomeTitular = input("Digite o nome completo do titular: ").title()

conta1 = Conta(222, nomeTitular, 212, 10)  # variável nomeia-se "referência"
conta2 = Conta(223, "Manoel Gomes", 213, 9000)
conta3 = Conta(224, "Jailson Mendes", 214, 100, 500)

deposito = int(input(f"Olá, {conta1.titular}!\nDigite o valor que deseja depositar: R$"))
conta1.Depositar(deposito)
conta1.Extrato()

valorRecebido = float(input("Digite o valor que deseja transferir: R$"))
conta2.Transferir(valorRecebido, conta1)  # origem.Transferir(<valor>,<destino>)

conta2.Extrato()
conta3.AumentoDeLimite(900)

conta1.Extrato()
conta1.Sacar(10)
conta1.Extrato()

print(f"Titular: {conta1.titular}\nCodigo do banco: {conta1.CodigoBanco()}")
