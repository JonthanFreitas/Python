# 🍧 Loja de Açaí da Debys

> ⚠️ **Projeto em desenvolvimento:** este sistema ainda **não está finalizado**. Novas funcionalidades, melhorias e correções serão adicionadas conforme o projeto evolui.

Sistema de pedidos desenvolvido em **Python** com integração ao **MySQL**, criado como projeto acadêmico para praticar programação, banco de dados e organização de código.

## 📌 Sobre o projeto

O sistema funciona via **CLI (terminal)** e permite:

- 👤 Cadastro de clientes
- 🔐 Login de clientes
- 🍧 Exibição do cardápio
- 🛒 Registro de pedidos
- 💰 Cálculo do total da compra
- 🗄️ Armazenamento dos dados no MySQL

O projeto começou como um exercício da faculdade e está sendo desenvolvido gradualmente para integrar os conhecimentos de **Python** e **Banco de Dados**.

## 🚧 Status do projeto

**Em desenvolvimento 🚧**

O projeto ainda não está terminado. Algumas funcionalidades estão sendo desenvolvidas, aprimoradas ou ainda precisam ser implementadas.

### Já desenvolvido

- [x] Estrutura inicial do projeto
- [x] Conexão com MySQL
- [x] Cadastro de clientes
- [x] Login de clientes
- [x] Consulta de produtos no banco de dados
- [x] Exibição do cardápio
- [x] Registro dos produtos escolhidos
- [x] Cálculo do total do pedido
- [x] Exibição do resumo da compra

### Próximas melhorias

- [ ] Melhorar a validação dos dados
- [ ] Utilizar hash para armazenamento de senhas
- [ ] Finalizar o relacionamento dos pedidos com os clientes
- [ ] Melhorar o gerenciamento dos pedidos
- [ ] Criar uma interface gráfica
- [ ] Transformar o sistema em uma aplicação web
- [ ] Criar uma API com Python
- [ ] Integrar um frontend ao sistema

## 🛠️ Tecnologias utilizadas

- Python
- MySQL
- MySQL Connector/Python
- Git
- GitHub

## 📚 Conceitos praticados

### Python

- Variáveis
- Condicionais (`if`, `elif`, `else`)
- Laços de repetição
- Funções
- Listas
- Dicionários
- `import`
- Organização em módulos
- Entrada e validação de dados
- Tratamento de fluxo do programa

### Banco de Dados

- MySQL
- Criação de bancos e tabelas
- `PRIMARY KEY`
- `FOREIGN KEY`
- `AUTO_INCREMENT`
- `UNIQUE`
- `CHECK`
- Relacionamentos entre tabelas
- Consultas SQL
- Inserção e alteração de dados

## 📁 Estrutura do projeto

```text
Loja açai/
│
├── banco/
│   └── banco.sql
│
├── src/
│   ├── main.py
│   ├── cadastro.py
│   ├── conexao.py
│   ├── cardapio.py
│   ├── pedidos.py
│   └── total.py
│
├── .gitignore
└── README.md
```

## 🗄️ Estrutura do Banco de Dados

O sistema utiliza as seguintes tabelas:

```text
CLIENTE
   │
   │ 1:N
   ▼
PEDIDO
   │
   │ 1:N
   ▼
ITENS_PEDIDO
   │
   │ N:1
   ▼
PRODUTOS
```

### Tabelas

- `cliente` — armazena os dados dos clientes.
- `produtos` — armazena os produtos, tamanhos e preços.
- `pedido` — registra os pedidos realizados pelos clientes.
- `itens_pedido` — relaciona os produtos aos pedidos.

## 🍧 Cardápio

### Cupuaçu

| Tamanho | Preço |
|---|---:|
| P | R$ 9,00 |
| M | R$ 14,00 |
| G | R$ 18,00 |

### Açaí

| Tamanho | Preço |
|---|---:|
| P | R$ 11,00 |
| M | R$ 14,00 |
| G | R$ 20,00 |

## ▶️ Como executar

### 1. Instale o Python

Tenha o Python instalado na sua máquina.

### 2. Instale as dependências

```bash
pip install mysql-connector-python
```

### 3. Configure o MySQL

Crie o banco de dados utilizando o arquivo:

```text
banco/banco.sql
```

### 4. Configure a conexão

Configure as informações de conexão com o MySQL de acordo com o seu ambiente.

> ⚠️ Não coloque senhas ou outras informações sensíveis diretamente no código ou no GitHub.

### 5. Execute o sistema

Dentro da pasta do projeto:

```bash
python src/main.py
```

## 🎯 Objetivo

O objetivo do projeto é colocar em prática os conhecimentos adquiridos durante o curso de **Análise e Desenvolvimento de Sistemas (ADS)**, principalmente nas áreas de:

- Programação em Python
- Lógica de programação
- Banco de Dados
- SQL
- Organização de código

## 👨‍💻 Autor

Projeto desenvolvido por **Jonathan Micael** como parte dos estudos em **Análise e Desenvolvimento de Sistemas (ADS)**.

---

🚧 **Projeto acadêmico em desenvolvimento. Novas funcionalidades e melhorias serão adicionadas futuramente.**