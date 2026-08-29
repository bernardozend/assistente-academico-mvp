# 🎓 Assistente Acadêmico IA

Prova de conceito de um assistente acadêmico baseado em Inteligência Artificial para recuperação de informações acadêmicas e institucionais no Ensino Superior.

> ⚠️ **Projeto experimental:** atualmente, toda a documentação utilizada pelo sistema é simulada e criada exclusivamente para desenvolvimento, testes e demonstração.

---

## 📌 Sobre o projeto

O Assistente Acadêmico IA foi desenvolvido para investigar como a Inteligência Artificial pode facilitar o acesso de estudantes a informações que normalmente estão distribuídas entre diferentes documentos e serviços acadêmicos.

Em vez de o usuário precisar localizar manualmente uma informação em regulamentos, calendários, manuais ou outros documentos, a proposta é permitir que ele faça uma pergunta em linguagem natural.

Exemplo:

> Quando acontece a AV2?

O sistema pesquisa a documentação disponível, recupera os trechos considerados relevantes e utiliza essas informações para produzir uma resposta.

---

## 🎯 Objetivo

Desenvolver e avaliar uma prova de conceito capaz de:

- receber perguntas acadêmicas em linguagem natural;
- localizar informações em uma base documental;
- recuperar documentos e trechos relevantes;
- gerar respostas fundamentadas na documentação;
- apresentar fontes e evidências utilizadas;
- evitar respostas quando não houver informação suficiente;
- incorporar mecanismos básicos de privacidade e proteção de dados.

---

## 🧠 Como funciona

O projeto utiliza uma arquitetura baseada em **RAG (Retrieval-Augmented Generation)**.

Fluxo:

Usuário → Streamlit → Privacidade → Busca semântica → ChromaDB → Documentos → LLM local → Resposta + evidências

---

## 🛠️ Tecnologias utilizadas

- Python 3.12
- Streamlit
- Ollama
- Llama 3.2 3B
- ChromaDB
- Sentence Transformers
- PyMuPDF
- Git
- GitHub

Modelo de embeddings:

`paraphrase-multilingual-MiniLM-L12-v2`

---

## 📚 Base documental

Atualmente, o projeto utiliza uma base acadêmica totalmente simulada, dividida em seis documentos:

1. Regulamento Acadêmico Simulado
2. Calendário Acadêmico 2026 Simulado
3. Manual do Ambiente Virtual de Aprendizagem
4. Guia da Biblioteca
5. Guia de Estágio e Atividades Complementares
6. Guia de Atendimento e Tecnologia

A utilização de documentos simulados permite desenvolver e testar o sistema sem utilizar dados acadêmicos institucionais reais.

---

## 🔎 Fontes e evidências

Quando uma informação é encontrada, a interface pode apresentar:

- documento utilizado;
- página;
- trecho recuperado;
- data da consulta;
- versão da base utilizada.

---

## 🛡️ Privacidade

O projeto possui uma camada experimental de privacidade executada antes da consulta à base documental.

Ela está sendo desenvolvida para identificar situações envolvendo dados pessoais, credenciais e determinadas informações sensíveis.

A existência dessa camada não representa certificação ou garantia de conformidade com a LGPD.

---

## 🚦 Estados de resposta

### ✅ Informação encontrada
A documentação contém informação suficiente e o sistema apresenta a resposta e suas evidências.

### ℹ️ Informação não encontrada
Não existe informação suficiente na documentação para responder.

### 🛡️ Solicitação bloqueada
A camada de privacidade interrompe a consulta antes que ela chegue ao RAG.

---

## ⚠️ Limitações atuais

O protótipo:

- utiliza documentação simulada;
- não acessa sistemas acadêmicos reais;
- não utiliza dados reais de estudantes;
- não consulta notas ou históricos individuais;
- não possui autenticação institucional;
- não está integrado a um AVA real;
- não deve ser considerado um sistema institucional em produção.

---

## 🧪 Status do projeto

**Status atual: desenvolvimento e validação pré-MVP 1.0.**

A próxima etapa será a realização de testes controlados de precisão, recuperação de fontes, evidências, recusas, privacidade e possíveis alucinações.

---

## 📋 Histórico

O histórico detalhado das versões será mantido no arquivo:

`CHANGELOG.md`

---

## 👤 Autor

**Bernardo Augusto Gomes Zendersky**

Projeto acadêmico experimental — 2026.
