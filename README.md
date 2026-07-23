# Robô de Cadastro de Clientes – Portal Fake V1.0

## Sobre o Projeto

Este projeto foi desenvolvido como atividade da disciplina **Técnicas de Hyperautomation**, com o objetivo de criar um robô para automatizar o processo de cadastro de clientes utilizando Python e Playwright.

A solução acessa o Portal Fake, identifica e extrai automaticamente os dados do formulário de cadastro, gera uma ficha de cadastro em formato Word (.docx) e envia esse documento por e-mail ao cliente, solicitando o preenchimento e o envio da documentação necessária para continuidade do processo.

---

## Objetivo

Automatizar o processo de cadastro de clientes, reduzindo atividades manuais, aumentando a produtividade e padronizando o fluxo de geração e envio de documentos.

---

## Funcionalidades

- Acesso automático ao Portal Fake;
- Abertura da tela de Novo Cadastro;
- Identificação dos campos do formulário;
- Extração automática dos dados;
- Organização das informações coletadas;
- Geração da ficha de cadastro em formato Word (.docx);
- Envio automático da ficha por e-mail;
- Proteção das credenciais utilizando arquivo `.env`.

---

## Tecnologias Utilizadas

- Python 3.x
- Playwright
- python-docx
- python-dotenv
- SMTP Gmail
- Git
- GitHub
- GitFlow
- Draw.io

---

## Estrutura do Projeto

```
HyperAutomation/
│
├── source/
│   ├── extracao.py
│   ├── documento_email.py
│   └── main.py
│
├── resources/
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

---

## Estrutura das Branches (GitFlow)

O projeto foi organizado utilizando a estratégia GitFlow.

### Branches

- **main**
  - Contém apenas versões estáveis da aplicação.

- **develop (dev)**
  - Branch principal de desenvolvimento.

- **feature/extracao**
  - Desenvolvimento da funcionalidade responsável pela extração dos dados do Portal Fake.

- **feature/documento-email**
  - Desenvolvimento da geração da ficha de cadastro e envio automático de e-mail.

- **release/1.0**
  - Preparação da versão final do projeto.

---

## Fluxo de Desenvolvimento

```
feature
    ↓
develop
    ↓
release/1.0
    ↓
main
    ↓
tag v1.0
```

Durante o desenvolvimento:

1. Cada integrante desenvolveu sua funcionalidade em uma branch `feature`;
2. Após os testes, foi criado um Pull Request para a branch `develop`;
3. Todas as funcionalidades foram integradas;
4. Foi criada a branch `release/1.0`;
5. Após validação, a versão foi publicada na branch `main`;
6. Foi criada a tag `v1.0`.

---

## Instalação

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Entre na pasta:

```bash
cd HyperAutomation
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Configuração

Crie um arquivo `.env` contendo as credenciais utilizadas para envio de e-mails.

Exemplo:

```env
EMAIL=seu_email@gmail.com
SENHA=sua_senha_de_aplicativo
```

---

## Execução

Execute a aplicação:

```bash
python source/main.py
```

O robô irá:

1. Acessar o Portal Fake;
2. Abrir o formulário de cadastro;
3. Extrair as informações;
4. Gerar a ficha de cadastro;
5. Enviar automaticamente o documento por e-mail.

---

## Organização da Equipe

| Integrante | Responsabilidade |
|------------|------------------|
| Luan Pinhheiro | Modelagem BPMN |
| Éricle Costa | Extração dos Dados |
| Daniele Greice | Documento e E-mail |
| Luã Maquiné | GitFlow e GitHub |
| Integrante 5 | QA e Testes |

---

## Evidências Esperadas

- Execução do robô;
- Dados extraídos;
- Documento Word gerado;
- E-mail enviado;
- Projeto publicado no GitHub.

---

## Melhorias Futuras

- Interface gráfica para execução da automação;
- Integração com banco de dados;
- Validação automática dos documentos enviados;
- Geração de arquivos PDF;
- Integração com BotCity Maestro;
- Agendamento automático da execução.

---

## Versionamento

Versão atual:

```
v1.0
```

---

## Autor

Projeto desenvolvido para a disciplina **Técnicas de Hyperautomation**.

AX Academy • LG Inova • IFAM • FAEPI