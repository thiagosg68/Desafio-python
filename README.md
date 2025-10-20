# 🏦 Sistema Bancário Simples

Um sistema bancário básico implementado em Python utilizando programação orientada a objetos.

## 📋 Descrição

Este projeto implementa uma classe `ContaBancaria` que simula as operações básicas de uma conta bancária, incluindo depósitos, saques e consulta de extrato.

## ⚙️ Funcionalidades

- ✅ **Criação de Conta**: Criar uma nova conta bancária com número, titular e saldo inicial
- ✅ **Depósito**: Adicionar valores ao saldo da conta
- ✅ **Saque**: Retirar valores do saldo (com validação de saldo suficiente)
- ✅ **Extrato**: Visualizar o saldo atual da conta

## 🚀 Como Usar

### Pré-requisitos
- Python 3.x instalado

### Executando o código

1. Clone o repositório:
```bash
git clone https://github.com/thiagosg68/Desafio-python.git
cd Desafio-python
```

2. Execute o arquivo Python:
```bash
python "Desafio python.py"
```

### Exemplo de Uso

```python
# Importar ou executar o arquivo
from desafio_python import ContaBancaria

# Criar uma nova conta
conta = ContaBancaria("12345", "João Silva", 1000)

# Realizar operações
conta.depositar(500)        # Deposita R$ 500
conta.sacar(200)           # Saca R$ 200
conta.exibir_extrato()     # Mostra o saldo atual
```

## 📖 Documentação da Classe

### `ContaBancaria`

#### Construtor
```python
ContaBancaria(numero, titular, saldo=0)
```

**Parâmetros:**
- `numero` (str): Número da conta bancária
- `titular` (str): Nome do titular da conta
- `saldo` (float, opcional): Saldo inicial da conta (padrão: 0)

#### Métodos

##### `depositar(valor)`
Adiciona um valor ao saldo da conta.

**Parâmetros:**
- `valor` (float): Valor a ser depositado

**Exemplo:**
```python
conta.depositar(500.00)  # Deposita R$ 500,00
```

##### `sacar(valor)`
Remove um valor do saldo da conta, se houver saldo suficiente.

**Parâmetros:**
- `valor` (float): Valor a ser sacado

**Comportamento:**
- Se o saldo for suficiente: realiza o saque
- Se o saldo for insuficiente: exibe mensagem de erro

**Exemplo:**
```python
conta.sacar(200.00)  # Saca R$ 200,00 se houver saldo
```

##### `exibir_extrato()`
Exibe o extrato da conta com o saldo atual.

**Exemplo:**
```python
conta.exibir_extrato()  # Mostra: "Extrato da conta 12345: Saldo atual R$1000.00"
```

## 🧪 Testes

O código foi testado com os seguintes cenários:

1. ✅ Criação de conta com saldo inicial
2. ✅ Criação de conta sem saldo inicial (saldo = 0)
3. ✅ Depósito de valores
4. ✅ Saque com saldo suficiente
5. ✅ Tentativa de saque com saldo insuficiente
6. ✅ Exibição de extrato

### Executar Testes

Para executar os testes automatizados:

```bash
python -c "
exec(open('Desafio python.py').read())

# Teste básico
conta = ContaBancaria('12345', 'Teste', 1000)
conta.depositar(500)
conta.sacar(300)
conta.exibir_extrato()
"
```

## 📁 Estrutura do Projeto

```
Desafio-python/
├── Desafio python.py    # Código principal da classe ContaBancaria
└── README.md           # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação
- **POO (Programação Orientada a Objetos)**: Paradigma de programação utilizado

## 👨‍💻 Autor

**thiagosg68**
- GitHub: [@thiagosg68](https://github.com/thiagosg68)

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 🔄 Melhorias Futuras

- [ ] Implementar histórico de transações
- [ ] Adicionar validação de entrada
- [ ] Implementar diferentes tipos de conta
- [ ] Adicionar sistema de transferência entre contas
- [ ] Interface gráfica ou web
- [ ] Persistência de dados (banco de dados/arquivo)
