import streamlit as st

st.set_page_config(page_title="Eva", page_icon="🎓")

st.title("🎓 Eva")
st.caption("Sua mentora de Java e Spring Boot")

if "historico" not in st.session_state:
    st.session_state.historico = []

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