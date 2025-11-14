class Cliente:
    def __init__(self, nome: str, cpf: str, endereco: str):
        """
        Inicializa um novo cliente.
        :param nome: Nome do cliente
        :param cpf: CPF do cliente
        :param endereco: Endereço do cliente
        """
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco


class ContaBancaria:
    def __init__(self, numero: str, titular: Cliente, saldo: float = 0):
        """
        Inicializa uma nova conta bancária.
        :param numero: Número da conta bancária
        :param titular: Objeto Cliente
        :param saldo: Saldo inicial da conta (padrão: 0)
        """
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor: float):
        """
        Adiciona um valor ao saldo da conta.
        :param valor: Valor a ser depositado
        """
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado!")

    def sacar(self, valor: float):
        """
        Remove um valor do saldo da conta, se houver saldo suficiente.
        :param valor: Valor a ser sacado
        """
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado!")
        else:
            print("Saldo insuficiente!")

    def exibir_extrato(self):
        """
        Exibe o extrato da conta com o saldo atual.
        """
        print(
            f"Extrato da conta {self.numero}: "
            f"Saldo atual R${self.saldo:.2f}"
        )
