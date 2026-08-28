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

# Exibe histórico
for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

pergunta = st.chat_input("Digite sua dúvida acadêmica...")

if pergunta:

    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):

        with st.spinner("Consultando a documentação..."):

            resposta, fontes = responder(pergunta)

        st.markdown(resposta)

        if fontes:
            with st.expander("📄 Fontes consultadas"):
                for fonte in fontes:
                    st.write(f"• {fonte}")

    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta
    })