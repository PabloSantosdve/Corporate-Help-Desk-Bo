# 🤖 Corporate Help Desk Bot

Chatbot corporativo desenvolvido em **Python puro**, sem uso de APIs de Inteligência Artificial, simulando um sistema de atendimento interno de uma empresa. O projeto foi criado como exercício prático de programação, com foco em **Programação Orientada a Objetos**, **modularização de código**, **persistência em banco de dados** e **boas práticas de desenvolvimento**.

Este é um projeto de **aprendizado e portfólio**: toda a lógica é implementada manualmente, com regras de negócio, busca por palavras-chave e uma base de conhecimento própria — sem depender de serviços externos de IA.

---

## 📋 Funcionalidades

- **Base de Conhecimento**: responde dúvidas frequentes de TI, RH, Financeiro, Facilities e outras áreas (senha, VPN, benefícios, férias, impressora, home office, compliance, entre mais de 50 categorias) buscando por palavras-chave.
- **Abertura de Chamados**: registra nome, departamento, categoria e descrição do problema, gerando um número de protocolo único automaticamente.
- **Consulta de Chamados**: permite consultar um chamado já aberto pelo número ou protocolo completo (ex: `8` ou `TICKET-0008`), exibindo status, categoria, descrição e data de abertura.
- **Histórico de Interações**: toda pergunta feita ao chatbot é registrada automaticamente, com data e horário.

Disponível em **três interfaces diferentes**, todas reutilizando a mesma lógica de negócio: terminal, aplicação desktop (Tkinter) e aplicação web (Flask).

---

## 🖥️ Versões do projeto

| Versão | Descrição | Status |
|---|---|---|
| 1 | Terminal | ✅ Concluída |
| 2 | Interface gráfica (Tkinter) | ✅ Concluída |
| 3 | Web (Flask) | ✅ Concluída |
| 4 | Banco de dados (SQLite) | ✅ Concluída |

---

## 🏗️ Arquitetura do projeto

```text
corporate-helpdesk-bot/
│
├── main.py                 # Ponto de entrada - versão terminal
├── interface.py             # Ponto de entrada - versão com interface gráfica (Tkinter)
├── app.py                   # Ponto de entrada - versão web (Flask)
│
├── chatbot/
│   ├── chatbot.py            # Classe ChatBot (orquestradora - une todos os módulos)
│   ├── knowledge.py           # Busca e formatação de respostas da base de conhecimento (SQLite)
│   ├── tickets.py             # Classe Chamado + abertura/consulta de chamados (SQLite)
│   └── history.py             # Registro de interações do usuário (SQLite)
│
├── data/
│   ├── database.db            # Banco de dados SQLite (tickets, history, categorias, palavras_chave)
│   └── database.py            # Scripts de criação de tabelas e migração inicial de dados
│
├── templates/
│   ├── index.html              # Página inicial da versão web (formulários)
│   └── resultado.html          # Página de resultado reutilizável (sucesso/erro)
│
└── utils/
    └── file_manager.py         # Funções genéricas de leitura/escrita em JSON (uso auxiliar)
```

### Modelo de dados (SQLite)

O banco é composto por 4 tabelas:

- **`tickets`**: um registro por chamado aberto (`protocolo`, `nome`, `departamento`, `categoria`, `descricao`, `status`, `data_abertura`).
- **`history`**: um registro por interação com o chatbot (`id` autoincrementável, `data_hora`, `mensagem`, `resposta`).
- **`categorias`**: uma linha por tópico da base de conhecimento (`id`, `nome`, `resposta`).
- **`palavras_chave`**: uma linha por palavra-chave, relacionada a uma categoria via chave estrangeira (`id`, `palavra`, `categoria_id`), permitindo que cada categoria tenha múltiplas palavras-chave associadas.

### Principais decisões de design

- **Separação de responsabilidades**: cada módulo cuida de uma única parte do sistema (conhecimento, chamados, histórico), seguindo o princípio de responsabilidade única.
- **Classe orquestradora (`ChatBot`)**: centraliza o acesso aos módulos, permitindo que as três interfaces (terminal, Tkinter e web) reutilizem exatamente a mesma lógica de negócio, sem duplicação de código.
- **Persistência em banco de dados relacional**: os dados são armazenados em SQLite, com uso de `PRIMARY KEY`, `FOREIGN KEY` e `AUTOINCREMENT` para garantir integridade e evitar duplicidade — substituindo a abordagem inicial baseada em arquivos JSON.
- **Consultas parametrizadas**: todas as operações de banco usam placeholders (`?`) em vez de concatenação de strings, prevenindo vulnerabilidades de SQL Injection.
- **Template de resultado reutilizável**: a versão web usa uma única página (`resultado.html`) para exibir qualquer resposta (pergunta, abertura ou consulta de chamado), alternando entre estado de sucesso e erro.

---

## 🚀 Como executar

### Pré-requisitos

- Python 3.12 ou superior
- Flask (apenas para a versão web)

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/PabloSantosdve/Corporate-Help-Desk-Bo.git
cd Corporate-Help-Desk-Bo
```

2. Execute a versão desejada:

**Versão terminal:**
```bash
python main.py
```

**Versão com interface gráfica (Tkinter):**
```bash
python interface.py
```

**Versão web (Flask):**
```bash
pip install flask
python app.py
```
Depois, acesse `http://127.0.0.1:5000` no navegador.

> O banco de dados SQLite (`data/database.db`) já vem com a base de conhecimento populada. As versões de terminal e Tkinter não exigem dependências externas além do Python padrão. Apenas a versão web depende do Flask.

---

## 🧠 Aprendizados aplicados neste projeto

- Estruturas de decisão e repetição (`if`/`elif`/`else`, `while`, `for`)
- Tratamento de exceções (`try`/`except`)
- Programação Orientada a Objetos (classes, `__init__`, `self`)
- Modularização e organização de código em múltiplos arquivos
- Interfaces gráficas com Tkinter (widgets, eventos, layout com `Frame`)
- Desenvolvimento web com Flask (rotas, métodos HTTP, formulários, templates Jinja2)
- HTML e CSS aplicados a uma interface moderna (glassmorphism, responsividade)
- Banco de dados relacional com SQLite (`CREATE TABLE`, `INSERT`, `SELECT`, `JOIN`, `PRIMARY KEY`, `FOREIGN KEY`)
- Prevenção de SQL Injection com consultas parametrizadas
- Versionamento de código com Git e GitHub

---

## 📄 Licença

Este projeto está sob a licença especificada no arquivo [LICENSE](LICENSE).