import streamlit as st
from rag import responder

st.set_page_config(
    page_title="Assistente Acadêmico IA",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Assistente Acadêmico IA")

st.caption(
    "Prova de conceito para recuperação inteligente "
    "de informações acadêmicas"
)

st.warning(
    "Protótipo experimental. As informações utilizadas "
    "nesta demonstração são simuladas."
)


if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


# Histórico
for mensagem in st.session_state.mensagens:

    with st.chat_message(mensagem["role"]):

        st.markdown(mensagem["content"])

        if (
            mensagem["role"] == "assistant"
            and mensagem.get("evidencias")
        ):

            with st.expander("📚 Evidências consultadas"):

                for i, evidencia in enumerate(
                    mensagem["evidencias"],
                    start=1
                ):

                    st.markdown(
                        f"**Evidência {i}**"
                    )

                    st.write(
                        f"📄 Documento: "
                        f"{evidencia['arquivo']}"
                    )

                    if evidencia["pagina"] > 0:
                        st.write(
                            f"📖 Página: "
                            f"{evidencia['pagina']}"
                        )

                    st.info(
                        evidencia["trecho"]
                    )

                    st.divider()


pergunta = st.chat_input(
    "Digite sua dúvida acadêmica..."
)


if pergunta:

    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    with st.chat_message("user"):
        st.markdown(pergunta)


    with st.chat_message("assistant"):

        with st.spinner(
            "Consultando a documentação..."
        ):

            resposta, evidencias = responder(
                pergunta
            )

        st.markdown(resposta)


        with st.expander(
            "📚 Evidências consultadas"
        ):

            for i, evidencia in enumerate(
                evidencias,
                start=1
            ):

                st.markdown(
                    f"**Evidência {i}**"
                )

                st.write(
                    f"📄 Documento: "
                    f"{evidencia['arquivo']}"
                )

                if evidencia["pagina"] > 0:
                    st.write(
                        f"📖 Página: "
                        f"{evidencia['pagina']}"
                    )

                st.info(
                    evidencia["trecho"]
                )

                st.divider()


    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta,
        "evidencias": evidencias
    })