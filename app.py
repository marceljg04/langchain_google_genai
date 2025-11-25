import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Chatbot")
st.title("Marcel Chatbot")
st.markdown("Este es un Chatbot construido con LangChain + Streamlit.")

st.sidebar.header("Configuración")

temperatura = st.sidebar.slider(
    "Temperatura del modelo", 
    min_value=0.0, 
    max_value=1.0, 
    value=0.5, 
    step=0.05
)

modelo = st.sidebar.selectbox(
    "Modelo a usar",
    [
        "gemini-2.5-flash",
        "gemini-2.0-pro",
    ]
)

borrar = st.sidebar.button("Borrar conversación")

if borrar:
    st.session_state.mensajes = []

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

chat_model = ChatGoogleGenerativeAI(
    model=modelo,
    temperature=temperatura,
    api_key=GOOGLE_API_KEY
)

for msg in st.session_state.mensajes:
    role = "assistant" if isinstance(msg, AIMessage) else "user"
    with st.chat_message(role):
        st.markdown(msg.content)

pregunta = st.chat_input("Escribe tu mensaje:")

if pregunta:
    with st.chat_message("user"):
        st.markdown(pregunta)

    st.session_state.mensajes.append(HumanMessage(content=pregunta))

    respuesta = chat_model.invoke(st.session_state.mensajes)

    with st.chat_message("assistant"):
        st.markdown(respuesta.content)

    st.session_state.mensajes.append(respuesta)
