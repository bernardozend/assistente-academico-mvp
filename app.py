import streamlit as st
from datetime import datetime

from rag import responder
from privacidade import analisar_privacidade


# =========================================================
# CONFIGURAÇÃO GERAL
# =========================================================

st.set_page_config(
    page_title="Assistente Acadêmico IA",
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
    return NOMES_DOCUMENTOS.get(
        arquivo,
        arquivo
    )


# =========================================================
# EXIBIÇÃO DAS EVIDÊNCIAS
# =========================================================

def mostrar_evidencias(evidencias):

    if not evidencias:
        return

    with st.expander(
        "📚 Consultar fontes e evidências"
    ):

        for i, evidencia in enumerate(
            evidencias,
            start=1
        ):

            arquivo = evidencia.get(
                "arquivo",
                "Documento não identificado"
            )

            pagina = evidencia.get(
                "pagina",
                0
            )

            trecho = evidencia.get(
                "trecho",
                ""
            )

            st.markdown(
                f"### Evidência {i}"
            )

            st.markdown(
                f"**Fonte:** "
                f"{nome_documento(arquivo)}"
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
# STATUS DA RESPOSTA
# =========================================================

def mostrar_status(
    status,
    evidencias=None,
    data_consulta=None
):

    evidencias = evidencias or []

    if status == "privacidade":

        st.warning(
            "🛡️ **Proteção de dados ativada**  \n"
            "A solicitação foi interrompida antes "
            "de chegar à base documental."
        )

    elif status == "nao_encontrado":

        st.info(
            "ℹ️ **Informação não encontrada**  \n"
            "A base documental consultada não contém "
            "informação suficiente para responder."
        )

    elif status == "validada":

        st.success(
            "✓ **Informação fundamentada na "
            "base acadêmica simulada**  \n"
            f"Consulta: {data_consulta} · "
            f"Base: {VERSAO_BASE}"
        )

        mostrar_evidencias(
            evidencias
        )

    elif status == "erro":

        st.error(
            "Não foi possível concluir a consulta."
        )


# =========================================================
# CABEÇALHO
# =========================================================

st.title(
    "🎓 Assistente Acadêmico IA"
)

st.caption(
    "Prova de conceito para recuperação "
    "inteligente de informações acadêmicas"
)

st.warning(
    "⚠️ **Ambiente demonstrativo** — "
    "todos os documentos e informações "
    "utilizados neste protótipo são simulados."
)


# =========================================================
# ESTADO DO CHAT
# =========================================================

if "mensagens" not in st.session_state:

    st.session_state.mensagens = []


# =========================================================
# HISTÓRICO DO CHAT
# =========================================================

for mensagem in st.session_state.mensagens:

    with st.chat_message(
        mensagem["role"]
    ):

        st.markdown(
            mensagem["content"]
        )

        if mensagem["role"] == "assistant":

            mostrar_status(
                status=mensagem.get(
                    "status"
                ),
                evidencias=mensagem.get(
                    "evidencias",
                    []
                ),
                data_consulta=mensagem.get(
                    "data_consulta"
                )
            )


# =========================================================
# CAMPO DE PERGUNTA
# =========================================================

pergunta = st.chat_input(
    "Digite sua dúvida acadêmica..."
)


# =========================================================
# PROCESSAMENTO DA PERGUNTA
# =========================================================

if pergunta:

    # -----------------------------------------------------
    # Salva pergunta
    # -----------------------------------------------------

    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    with st.chat_message("user"):

        st.markdown(pergunta)


    # -----------------------------------------------------
    # Valores iniciais
    # -----------------------------------------------------

    data_consulta = datetime.now().strftime(
        "%d/%m/%Y"
    )

    resposta = ""
    evidencias = []
    status = None


    # -----------------------------------------------------
    # Processamento
    # -----------------------------------------------------

    with st.chat_message("assistant"):

        try:

            with st.spinner(
                "Analisando sua solicitação..."
            ):

                # =========================================
                # 1. PRIVACIDADE
                # =========================================

                analise = analisar_privacidade(
                    pergunta
                )

                if not analise["permitido"]:

                    resposta = analise[
                        "mensagem"
                    ]

                    status = "privacidade"

                    evidencias = []


                else:

                    # =====================================
                    # 2. RAG
                    # =====================================

                    resposta, evidencias = responder(
                        pergunta
                    )

                    # =====================================
                    # 3. VERIFICA SE ENCONTROU
                    # =====================================

                    if (
                        RESPOSTA_SEM_INFORMACAO.lower()
                        in resposta.lower()
                    ):

                        status = (
                            "nao_encontrado"
                        )

                        evidencias = []

                    else:

                        status = "validada"


            # -------------------------------------------------
            # Exibe resposta
            # -------------------------------------------------

            st.markdown(resposta)

            mostrar_status(
                status=status,
                evidencias=evidencias,
                data_consulta=data_consulta
            )


        except Exception as erro:

            resposta = (
                "Ocorreu um erro ao processar "
                "a solicitação."
            )

            status = "erro"
            evidencias = []

            st.error(resposta)

            # Durante desenvolvimento:
            st.caption(
                f"Detalhe técnico: {erro}"
            )


    # -----------------------------------------------------
    # Salva resposta no histórico
    # -----------------------------------------------------

    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta,
        "status": status,
        "evidencias": evidencias,
        "data_consulta": data_consulta
    })