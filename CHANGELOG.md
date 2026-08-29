# 📋 Histórico de Desenvolvimento

Este documento registra a evolução do projeto **Assistente Acadêmico IA**, incluindo versões, funcionalidades implementadas, testes e alterações relevantes realizadas durante o desenvolvimento.

O projeto consiste em uma prova de conceito de um assistente acadêmico baseado em Inteligência Artificial e RAG para recuperação de informações acadêmicas e institucionais no Ensino Superior.

---

## 27/08/2026 — Início do desenvolvimento

### Preparação do ambiente

Foi preparado o ambiente local necessário para o desenvolvimento do protótipo.

Principais componentes configurados:

- Python 3.12
- Visual Studio Code
- Git
- Ollama
- modelo Llama 3.2 3B
- ambiente virtual Python `.venv`

Também foram instaladas as principais bibliotecas utilizadas pelo projeto:

- Streamlit
- ChromaDB
- PyMuPDF
- Sentence Transformers
- Ollama para Python

---

## 27/08/2026 — MVP v0.1

### Primeiro protótipo funcional

Foi desenvolvida a primeira versão funcional do assistente acadêmico.

### Implementado

- interface de chat utilizando Streamlit;
- execução local do modelo Llama 3.2 3B através do Ollama;
- criação de uma base acadêmica simulada inicial;
- geração de embeddings;
- armazenamento vetorial utilizando ChromaDB;
- busca semântica;
- primeira implementação da arquitetura RAG;
- recuperação de contexto antes da geração da resposta;
- respostas baseadas na documentação recuperada;
- regra para evitar respostas quando não houver informação suficiente na base.

### Testes iniciais

Foram realizadas perguntas cuja resposta estava presente na documentação simulada.

Exemplo:

> Perdi minha prova. Quanto tempo tenho para solicitar segunda chamada?

O sistema conseguiu recuperar a informação correspondente ao prazo de **5 dias úteis**.

Também foi realizada uma pergunta cuja resposta não estava presente na documentação:

> Quanto custa o estacionamento?

O assistente respondeu:

> Não encontrei essa informação na documentação disponível.

O teste demonstrou o funcionamento inicial do mecanismo de recusa para informações ausentes.

### Versionamento

Primeiro marco registrado no Git:

`MVP v0.1 - chat local com RAG e fonte`

Commit:

`48b788f`

---

## 28/08/2026 — MVP v0.2

### Suporte a documentos PDF e evidências

A estrutura documental do protótipo foi ampliada para permitir processamento de arquivos PDF.

### Implementado

- leitura de documentos PDF com PyMuPDF;
- processamento do conteúdo por página;
- divisão dos textos em trechos;
- armazenamento dos trechos no banco vetorial;
- armazenamento de metadados;
- identificação do arquivo de origem;
- identificação da página;
- recuperação dos trechos utilizados pela busca semântica;
- apresentação das fontes na interface;
- apresentação das páginas;
- apresentação das evidências recuperadas.

Essa versão aumentou a rastreabilidade das respostas geradas pelo assistente.

---

## 28/08/2026 — MVP v0.3

### Base acadêmica com múltiplos documentos

A base simulada foi dividida em seis documentos independentes para permitir testes de recuperação entre diferentes fontes acadêmicas.

### Documentos simulados

1. Regulamento Acadêmico
2. Calendário Acadêmico 2026
3. Manual do Ambiente Virtual de Aprendizagem
4. Guia da Biblioteca
5. Guia de Estágio e Atividades Complementares
6. Guia de Atendimento e Tecnologia

### Implementado

- indexação de múltiplos documentos;
- recuperação semântica entre diferentes fontes;
- identificação automática do documento utilizado;
- identificação da página;
- apresentação dos trechos recuperados;
- nomes amigáveis para as fontes na interface;
- separação entre resposta gerada e evidências documentais;
- indicação da versão da base;
- registro da data da consulta.

### Objetivo desta evolução

Permitir avaliar se o sistema consegue localizar a informação correta quando existem diferentes documentos disponíveis simultaneamente.

---

## 29/08/2026 — Camada experimental de privacidade

### Status: EM TESTE

Foi iniciado o desenvolvimento de uma camada de privacidade anterior ao mecanismo RAG.

Foi criado o módulo:

`privacidade.py`

### Objetivo

Evitar que determinadas informações pessoais, credenciais ou solicitações inadequadas sejam encaminhadas desnecessariamente para o mecanismo de recuperação e para o modelo de linguagem.

### Primeiras verificações implementadas

- CPF;
- e-mail;
- telefone;
- possíveis números de cartão;
- senhas e credenciais;
- determinados termos relacionados a informações sensíveis;
- determinadas solicitações envolvendo dados pessoais de terceiros.

### Novo fluxo

Perguntas permitidas seguem para o mecanismo RAG.

Perguntas identificadas pela camada de proteção podem ser interrompidas antes da consulta documental.

### Estados definidos para a interface

O protótipo passa a trabalhar com três comportamentos principais:

**1. Informação encontrada**

A documentação possui informação suficiente para responder e as evidências podem ser apresentadas.

**2. Informação não encontrada**

A base não possui informação suficiente e o assistente deve informar essa limitação.

**3. Solicitação bloqueada**

A camada de privacidade interrompe o processamento antes da consulta ao RAG.

### Observação

Esta funcionalidade encontra-se em desenvolvimento e validação.

A camada experimental de privacidade não representa certificação ou garantia de conformidade com a LGPD.

---

## Situação atual — Pré-MVP 1.0

O núcleo funcional do protótipo encontra-se desenvolvido.

Atualmente estão disponíveis:

- interface conversacional;
- modelo de linguagem executado localmente;
- arquitetura RAG;
- busca semântica;
- banco vetorial;
- múltiplos documentos simulados;
- recuperação de fontes;
- recuperação de páginas;
- apresentação de evidências;
- mecanismo para informações ausentes;
- camada experimental de privacidade.

A etapa seguinte será dedicada principalmente à **validação experimental do protótipo**.

---

## Próxima etapa — Validação do MVP 1.0

### Status: PLANEJADO

Antes de estabelecer a versão **MVP 1.0**, será realizada uma bateria controlada de testes.

Serão avaliados:

- respostas para perguntas diretas;
- perguntas formuladas de maneiras diferentes;
- recuperação entre múltiplos documentos;
- seleção da fonte correta;
- seleção da página correta;
- qualidade das evidências recuperadas;
- perguntas com premissas incorretas;
- informações inexistentes na documentação;
- recusas corretas;
- comportamento da camada de privacidade;
- possíveis alucinações;
- estabilidade da aplicação;
- tempo de resposta.

Os resultados serão registrados para permitir análise quantitativa e qualitativa do comportamento do protótipo.

---

## MVP 1.0

### Status: AINDA NÃO LIBERADO

O MVP 1.0 somente será registrado após a execução da etapa de validação e análise dos resultados.

O objetivo é que a definição da primeira versão estável seja baseada em evidências obtidas durante os testes, e não apenas no funcionamento aparente da aplicação.
