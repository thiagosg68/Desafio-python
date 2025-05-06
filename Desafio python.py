class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado!")
        else:
            print("Saldo insuficiente!")

    def exibir_extrato(self):
        print(f"Extrato da conta {self.numero}: Saldo atual R${self.saldo:.2f}")