import streamlit as st
from datetime import datetime

from rag import responder


# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title=" COMO EU POSSO TE AJUDAR HOJE, ALUNO?",
    page_icon="🎓",
    layout="centered"
)

VERSAO_BASE = "Demo 1.0"

RESPOSTA_SEM_INFORMACAO = (
    "Não encontrei essa informação na documentação disponível."
)


# =========================================================
# NOMES AMIGÁVEIS DOS DOCUMENTOS
# =========================================================

NOMES_DOCUMENTOS = {
    "01_regulamento_academico_simulado.pdf":
        "Regulamento Acadêmico",

    "02_calendario_academico_2026_simulado.pdf":
        "Calendário Acadêmico 2026",

    "03_manual_ava_simulado.pdf":
        "Manual do Ambiente Virtual de Aprendizagem",

    "04_biblioteca_simulada.pdf":
        "Guia da Biblioteca",

    "05_estagio_simulado.pdf":
        "Guia de Estágio e Atividades Complementares",

    "06_atendimento_tecnologia_simulado.pdf":
        "Guia de Atendimento e Tecnologia",
}


def nome_documento(arquivo):
    return NOMES_DOCUMENTOS.get(arquivo, arquivo)


# =========================================================
# FUNÇÃO PARA EXIBIR EVIDÊNCIAS
# =========================================================

def mostrar_evidencias(evidencias):

    if not evidencias:
        return

    with st.expander("📚 Consultar fontes e evidências"):

        for i, evidencia in enumerate(evidencias, start=1):

            arquivo = evidencia["arquivo"]
            pagina = evidencia.get("pagina", 0)
            trecho = evidencia["trecho"]

            st.markdown(f"### Evidência {i}")

            st.markdown(
                f"**Fonte:** {nome_documento(arquivo)}"
            )

            if pagina > 0:
                st.markdown(
                    f"**Página:** {pagina}"
                )

            st.caption(
                "Trecho recuperado automaticamente "
                "pela busca semântica:"
            )

            st.info(trecho)

            if i < len(evidencias):
                st.divider()


# =========================================================
# CABEÇALHO
# =========================================================

st.title("🎓 Assistente Acadêmico IA")

st.caption(
    "Prova de conceito para recuperação inteligente "
    "de informações acadêmicas"
)

st.warning(
    "⚠️ Ambiente demonstrativo — todos os documentos e "
    "informações utilizados neste protótipo são simulados."
)


# =========================================================
# ESTADO DO CHAT
# =========================================================

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


# =========================================================
# HISTÓRICO
# =========================================================

for mensagem in st.session_state.mensagens:

    with st.chat_message(mensagem["role"]):

        st.markdown(mensagem["content"])

        if mensagem["role"] == "assistant":

            validada = mensagem.get("validada", False)

            if validada:

                data_consulta = mensagem.get(
                    "data_consulta",
                    ""
                )

                st.success(
                    "✓ Informação fundamentada na "
                    f"base acadêmica simulada · "
                    f"Consulta: {data_consulta} · "
                    f"Base: {VERSAO_BASE}"
                )

                mostrar_evidencias(
                    mensagem.get("evidencias", [])
                )

            else:

                st.caption(
                    "ℹ️ A base documental consultada não "
                    "contém informação suficiente para "
                    "responder a esta pergunta."
                )


# =========================================================
# ENTRADA DO USUÁRIO
# =========================================================

pergunta = st.chat_input(
    "Digite sua dúvida acadêmica..."
)


# =========================================================
# PROCESSAMENTO
# =========================================================

if pergunta:

    # Salva pergunta
    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    # Mostra pergunta
    with st.chat_message("user"):
        st.markdown(pergunta)

    # Gera resposta
    with st.chat_message("assistant"):

        with st.spinner(
            "Consultando a base acadêmica..."
        ):

            resposta, evidencias = responder(pergunta)

        st.markdown(resposta)

        # Verifica se a IA encontrou informação válida
        validada = (
            RESPOSTA_SEM_INFORMACAO.lower()
            not in resposta.lower()
        )

        data_consulta = datetime.now().strftime(
            "%d/%m/%Y"
        )

        if validada:

            st.success(
                "✓ Informação fundamentada na "
                f"base acadêmica simulada · "
                f"Consulta: {data_consulta} · "
                f"Base: {VERSAO_BASE}"
            )

            mostrar_evidencias(evidencias)

        else:

            st.caption(
                "ℹ️ A base documental consultada não "
                "contém informação suficiente para "
                "responder a esta pergunta."
            )

    # Salva resposta no histórico
    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta,
        "evidencias": evidencias,
        "validada": validada,
        "data_consulta": data_consulta
    })