import streamlit as st

from src.main import (
    buscar_conhecimento,
    montar_contexto,
    gerar_resposta,
    carregar_prompt
)

st.set_page_config(page_title="Eva", page_icon="🎓")

st.title("🎓 Eva")
st.caption("Sua mentora de Java e Spring Boot")

if "historico" not in st.session_state:
    st.session_state.historico = []

if "mensagens_modelo" not in st.session_state:
    prompt_base = carregar_prompt()

    st.session_state.mensagens_modelo = [
        {
            "role": "system",
            "content": prompt_base
        }
    ]

for mensagem in st.session_state.historico:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

pergunta = st.chat_input("Digite sua dúvida sobre programação...")

if pergunta:
    st.session_state.historico.append({
        "role": "user",
        "content": pergunta
    })

    with st.chat_message("user"):
        st.markdown(pergunta)

        conteudo_relevante = buscar_conhecimento(pergunta, "data")
        conhecimento_relevante = montar_contexto(conteudo_relevante)
        resposta = gerar_resposta(pergunta, conhecimento_relevante, st.session_state.mensagens_modelo )
        
        st.session_state.historico.append({
        "role": "assistant",
        "content": resposta
    })

    with st.chat_message("assistant"):
        st.markdown(resposta)

