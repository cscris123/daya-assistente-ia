# 🌸 Daya — Assistente de Estudos em Ciência de Dados

A **Daya** é um assistente virtual com Inteligência Artificial criado para apoiar estudantes de Ciência de Dados.

Ela combina três papéis:

- 👩‍🏫 **Professora particular:** explica conceitos de forma didática.
- 🤝 **Colega de estudos:** ajuda o estudante a raciocinar e praticar.
- 🎓 **Mentora:** sugere próximos passos e identifica lacunas de conhecimento.

## Objetivo

A Daya atende principalmente estudantes iniciantes e intermediários, podendo complementar a conversa com conteúdos avançados quando forem relevantes.

A primeira versão trabalha com:

- Python;
- Estatística;
- SQL e Banco de Dados;
- Análise e Visualização de Dados;
- Machine Learning;
- Inteligência Artificial.

## Arquitetura

```text
Usuário
   ↓
Streamlit
   ↓
System Prompt + Base de Conhecimento
   ↓
OpenAI Responses API
   ↓
Daya
```

A aplicação carrega os arquivos Markdown da pasta `data/` e os utiliza como contexto para a resposta.

## Regra de confiabilidade

A Daya foi instruída a não inventar informações. Quando a base disponível não possui informação suficiente, o agente deve reconhecer a limitação.

## Estrutura

```text
daya-assistente-ia/
├── data/
├── docs/
│   └── avaliacao.md
├── prompts/
│   ├── system_prompt.md
│   └── exemplos_comportamento.md
├── src/
│   └── app.py
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Como executar localmente

### 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar o ambiente

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar a chave

Crie uma variável de ambiente chamada `OPENAI_API_KEY`.

Opcionalmente, defina:

```text
OPENAI_MODEL=gpt-5.6-luna
```

**Nunca publique a chave no GitHub.**

### 5. Executar

```bash
streamlit run src/app.py
```

## Avaliação

Os casos de teste estão documentados em `docs/avaliacao.md`. Eles verificam conhecimento, adaptação de profundidade, ensino ativo e reconhecimento de limitações.

Os resultados reais da avaliação serão registrados depois dos testes da aplicação.

## Evoluções possíveis

- busca semântica/RAG;
- embeddings e banco vetorial;
- memória de conversa mais estruturada;
- painel de métricas;
- testes automatizados de prompts;
- implantação pública.

## Projeto

Lab: **Construa Seu Assistente Virtual Com Inteligência Artificial — DIO**

Autora: Cristina Costa
