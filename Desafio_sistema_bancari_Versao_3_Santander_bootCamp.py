from abc import ABC, abstractmethod
import textwrap

class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    LIMITE_SAQUES = 3

    def __init__(self, numero, cliente, agencia="0001"):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0
        self.extrato = ""
        self.limite = 500
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > self.limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif self.numero_saques >= Conta.LIMITE_SAQUES:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def mostrar_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def adicionar_cliente(self):
        cpf = input("Informe o CPF (somente número): ")
        if self.buscar_cliente(cpf):
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        cliente = Cliente(nome, data_nascimento, cpf, endereco)
        self.clientes.append(cliente)
        print("=== Usuário criado com sucesso! ===")

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        cliente = self.buscar_cliente(cpf)
        if cliente:
            numero_conta = len(self.contas) + 1
            conta = Conta(numero_conta, cliente)
            self.contas.append(conta)
            print("\n=== Conta criada com sucesso! ===")
        else:
            print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

    def listar_contas(self):
        for conta in self.contas:
            linha = f"""\  
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero}
                Titular:\t{conta.cliente.nome}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():
    banco = Banco()

    while True:
        opcao = menu()

        if opcao == "d":
            numero = int(input("Informe o número da conta: "))
            conta = next((c for c in banco.contas if c.numero == numero), None)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
            else:
                print("\n@@@ Conta não encontrada. @@@")

        elif opcao == "s":
            numero = int(input("Informe o número da conta: "))
            conta = next((c for c in banco.contas if c.numero == numero), None)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)
            else:
                print("\n@@@ Conta não encontrada. @@@")

        elif opcao == "e":
            numero = int(input("Informe o número da conta: "))
            conta = next((c for c in banco.contas if c.numero == numero), None)
            if conta:
                conta.mostrar_extrato()
            else:
                print("\n@@@ Conta não encontrada. @@@")

        elif opcao == "nu":
            banco.adicionar_cliente()

        elif opcao == "nc":
            banco.criar_conta()

        elif opcao == "lc":
            banco.listar_contas()

        elif opcao == "q":
            print("\nSaindo do sistema bancário... Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()