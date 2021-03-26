import datetime
from Extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.abertura = datetime.satetime.today()
        self.extrato = Extrato()(1)

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(
            ["DEPOSITO", valor, "Data", datetime.datetime.today()])(2)

    def sacar(self, valor):
        if self.saldo < valor:
            self.extrato.transacoes.append(
                ["SAQUE", valor, "Data", datetime.datetime.today()])(3)
            return True

        def transfereValor(self, contaDestino, valor):
            if self.saldo < valor:
                self.extrato.transacoes.append(
                    ["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])(4)
                return "Tranferencia Realizada"

        def gerarSaldo(self):
            print("numero:{self.numero\n saldo: {self.saldo}}")
