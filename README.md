---

```markdown
# 🏦 Sistema Bancário em Python

Este projeto é uma aplicação de terminal que simula um sistema bancário simples, utilizando os princípios da **programação orientada a objetos**. Ele permite o gerenciamento de clientes, contas bancárias, depósitos, saques e extratos.

## 📌 Funcionalidades

- Criar novos usuários (clientes)
- Criar contas bancárias associadas a usuários
- Realizar depósitos e saques
- Consultar extrato da conta
- Listar todas as contas registradas
- Interface de menu interativo via terminal

## 🧱 Estrutura de Classes

### `Cliente`
Representa um cliente do banco, contendo:
- `nome`
- `data_nascimento`
- `cpf`
- `endereco`

### `Conta`
Representa uma conta bancária, com:
- `numero`
- `agencia` (padrão: `"0001"`)
- `cliente` (associado à instância de `Cliente`)
- `saldo`
- `extrato`
- `limite` (padrão: R$500)
- `numero_saques` (máximo de 3 saques por conta)

### `Banco`
Gerencia os clientes e contas:
- Adiciona novos clientes
- Cria novas contas
- Busca clientes por CPF
- Lista todas as contas registradas

## 📋 Menu Interativo

Ao executar o programa, o usuário verá o seguinte menu:

```
================ MENU ================
[d]	Depositar
[s]	Sacar
[e]	Extrato
[nc]	Nova conta
[lc]	Listar contas
[nu]	Novo usuário
[q]	Sair
```

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Execute o script:
   ```bash
   python nome_do_arquivo.py
   ```

## 🛠 Requisitos

- Python 3.7 ou superior
- Terminal ou console interativo

## 📚 Conceitos aplicados

- Programação Orientada a Objetos (POO)
- Encapsulamento
- Composição de objetos
- Interação via terminal
- Validação de entrada

## 📦 Melhorias futuras

- Persistência de dados com arquivos ou banco de dados
- Interface gráfica com Tkinter ou PyQt
- Autenticação de usuários
- Exportação de extrato em PDF ou CSV

## 👨‍💻 Autor

**Walisson**  
Salvador, Bahia – Brasil  
Desenvolvedor em evolução 🚀

---

```
