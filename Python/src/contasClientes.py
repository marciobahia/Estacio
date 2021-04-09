from contas import Conta
from clientes import Cliente
cliente1 = Cliente(123, "joao", "Rua 1")
cliente2 = Cliente(345, "marcio", "Rua 2")
cliente1 = Conta([cliente1, cliente2], 1, 0)(1)
conta.gerarSaldo()
conta.depositar(1500)
conta.sacar(500)
conta.gerarSaldo()
