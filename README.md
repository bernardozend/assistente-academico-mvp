# 🎓 Assistente Acadêmico IA

**Desenvolvimento de um Assistente Acadêmico com Inteligência Artificial e RAG como Prática Educativa no Ensino Superior.**

Protótipo acadêmico experimental desenvolvido para investigar a aplicação de Inteligência Artificial generativa e arquitetura **RAG (Retrieval-Augmented Generation)** na recuperação contextualizada de informações acadêmicas a partir de uma base documental controlada.

> ⚠️ **Projeto experimental:** a documentação utilizada pelo protótipo é sintética e foi criada exclusivamente para desenvolvimento, testes e demonstração. O sistema não utiliza dados acadêmicos institucionais reais.

---

## 📌 Sobre o projeto

O Assistente Acadêmico IA foi desenvolvido como uma **prática educativa** para explorar como técnicas de Inteligência Artificial, recuperação de informação e processamento documental podem ser aplicadas ao contexto do Ensino Superior.

A proposta parte de um problema comum: informações acadêmicas podem estar distribuídas entre regulamentos, calendários, manuais e diferentes documentos, tornando sua localização pouco intuitiva.

Em vez de realizar uma busca manual, o usuário pode formular uma pergunta em linguagem natural.

Exemplo:

> **Quando acontece a AV2?**

O sistema realiza uma busca semântica na base documental, recupera trechos considerados relevantes e utiliza essas informações como contexto para a geração da resposta.

Quando a documentação disponível não contém informação suficiente, o protótipo pode informar que não encontrou a informação, em vez de apresentar uma resposta sem fundamento documental.

---

## 🎯 Objetivo

Desenvolver um **MVP funcional** capaz de:

- receber perguntas em linguagem natural;
- recuperar informações em uma base documental controlada;
- realizar recuperação semântica de trechos relevantes;
- utilizar os trechos recuperados como contexto para um modelo de linguagem;
- gerar respostas em linguagem natural;
- apresentar fonte, página e evidências quando disponíveis;
- informar quando a documentação disponível não é suficiente;
- explorar mecanismos experimentais de privacidade e proteção de dados.

---

## 🧠 Arquitetura RAG

O projeto utiliza uma arquitetura baseada em **Retrieval-Augmented Generation (RAG)**.

Fluxo simplificado:

```text
Pergunta
   ↓
Embedding
   ↓
Recuperação semântica
   ↓
ChromaDB
   ↓
Trechos relevantes
   ↓
Contexto
   ↓
Llama 3.2
   ↓
Resposta + evidência
```

A ideia central é recuperar informações da documentação antes da geração da resposta.

O projeto **não realiza treinamento do LLM com os documentos**. São utilizados modelos previamente treinados; o desenvolvimento concentra-se na recuperação, integração, controle de contexto, interface e avaliação do protótipo.

---

## 🛠️ Tecnologias utilizadas

- **Python 3.12**
- **Streamlit**
- **Ollama**
- **Llama 3.2 3B**
- **ChromaDB**
- **Sentence Transformers**
- **PyMuPDF**
- **Git**
- **GitHub**

### Modelo de embeddings

```text
paraphrase-multilingual-MiniLM-L12-v2
```

---

## 📚 Base documental

O protótipo utiliza uma base acadêmica totalmente simulada composta por seis documentos:

1. Regulamento Acadêmico Simulado
2. Calendário Acadêmico 2026 Simulado
3. Manual do Ambiente Virtual de Aprendizagem
4. Guia da Biblioteca
5. Guia de Estágio e Atividades Complementares
6. Guia de Atendimento e Tecnologia

A utilização de documentação sintética permite testar o sistema sem utilizar dados acadêmicos institucionais ou informações pessoais reais.

---

## 🔎 Evidências e rastreabilidade

Quando uma informação é recuperada, o sistema pode apresentar elementos que permitem verificar sua origem, como:

- documento utilizado;
- página;
- trecho recuperado;
- evidência associada à resposta.

A presença de uma evidência **não garante que a resposta esteja correta**. Ela cria um caminho para que o usuário possa verificar de onde a informação foi obtida.

---

## 🛡️ Privacidade

O projeto possui uma camada **experimental** de privacidade executada antes da consulta à base documental.

Essa camada foi desenvolvida para explorar o bloqueio de determinadas entradas envolvendo dados pessoais, credenciais e outras informações consideradas sensíveis no contexto do protótipo.

A existência dessa camada não representa certificação, auditoria ou garantia de conformidade com a LGPD.

---

## 🚦 Estados de resposta

### ✅ Informação encontrada

Quando existe informação suficiente na documentação disponível, o sistema recupera os trechos relevantes e gera uma resposta acompanhada das evidências disponíveis.

### ℹ️ Informação não encontrada

Quando não há informação suficiente na documentação disponível, o sistema pode informar que a informação não foi encontrada.

Exemplo:

> **Não encontrei essa informação na documentação disponível.**

### 🛡️ Solicitação bloqueada

Quando uma entrada é identificada pela camada experimental de privacidade, a consulta pode ser interrompida antes da etapa de recuperação.

---

## 🧪 Demonstração

Exemplo de consulta com informação disponível:

> **Quando acontece a AV2?**

Resultado esperado:

> **16 a 20 de novembro de 2026.**

Fonte:

> **Calendário Acadêmico 2026 — página 1.**

Exemplo de consulta sem informação disponível:

> **Quanto custa o estacionamento?**

Resultado esperado:

> **Não encontrei essa informação na documentação disponível.**

---

## 🔬 Contribuição do trabalho

O RAG é uma arquitetura conhecida e já existem produtos e trabalhos acadêmicos que utilizam recuperação documental associada a modelos de linguagem.

A contribuição deste projeto não está na criação da arquitetura RAG, mas na **implementação e aplicação de um protótipo próprio no contexto do Ensino Superior**, explorando:

- base documental controlada;
- recuperação semântica;
- execução local do modelo de linguagem;
- apresentação de evidências documentais;
- comportamento controlado diante da ausência de informação;
- integração desses componentes como uma prática educativa.

---

## ⚠️ Limitações atuais

O protótipo:

- utiliza documentação sintética;
- não acessa sistemas acadêmicos reais;
- não utiliza dados reais de estudantes;
- não consulta notas ou históricos individuais;
- não possui autenticação institucional;
- não está integrado a um AVA real;
- não possui avaliação formal de precisão em escala;
- não deve ser considerado um sistema institucional em produção.

Uma implantação real exigiria, entre outros aspectos, autenticação, autorização, governança, atualização documental, segurança, monitoramento e avaliação formal do sistema.

---

## 🚀 Possibilidades futuras

Entre as possibilidades de evolução estão:

- avaliação formal da precisão da recuperação e das respostas;
- busca híbrida e reranking;
- integração com APIs e sistemas institucionais autorizados;
- atualização e versionamento da base documental;
- controle de vigência das fontes;
- evolução para integração com ferramentas por meio de MCP;
- utilização de agentes para tarefas de múltiplas etapas;
- interação por voz e recursos multimodais.

---

## 📋 Histórico

O histórico de desenvolvimento e evolução do projeto é mantido em:

```text
CHANGELOG.md
```

O histórico de commits do repositório também registra a evolução do desenvolvimento.

---

## 👤 Autor

**Bernardo Augusto Gomes Zendersky**

Projeto acadêmico desenvolvido em **2026** como prática educativa no Ensino Superior.

### Como citar

Caso este projeto seja utilizado, adaptado ou mencionado em trabalhos acadêmicos, recomenda-se citar o autor e o repositório conforme as informações disponíveis no arquivo [`CITATION.cff`](CITATION.cff).

Referência sugerida:

> **ZENDERSKY, Bernardo Augusto Gomes.** *Desenvolvimento de um Assistente Acadêmico com Inteligência Artificial e RAG*. 2026. GitHub: bernardozend/assistente-academico-mvp.

---

## © Direitos autorais

Copyright © 2026 **Bernardo Augusto Gomes Zendersky**.

Este repositório é disponibilizado publicamente para consulta e referência acadêmica. A disponibilização pública do código não constitui renúncia aos direitos autorais do autor.

Para informações sobre reutilização, distribuição ou criação de trabalhos derivados, consulte o autor antes de utilizar o código além das funcionalidades permitidas pelo próprio GitHub.

---

## 📫 Contato

**Bernardo Augusto Gomes Zendersky**

GitHub: `https://github.com/bernardozend`

Repositório: `https://github.com/bernardozend/assistente-academico-mvp`