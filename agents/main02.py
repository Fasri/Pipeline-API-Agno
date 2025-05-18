import streamlit as st
from agno.agent import Agent 
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

# Título e layout
st.set_page_config(page_title="Nutrição Inteligente", layout="centered")
st.title("🥗 Assistente de Nutrição e Saúde")
st.markdown("Digite sua pergunta sobre nutrição e saúde abaixo e veja a resposta em tempo real.")

# Campo de entrada
pergunta = st.text_input("Qual a sua dúvida?", "")

# Inicializa o agente
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="Você é um especialista em nutrição e saúde. Você pode me ajudar a encontrar informações sobre nutrição e saúde?",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

# Resposta com streaming
if pergunta:
    st.subheader("🧠 Resposta do Assistente:")
    resposta_container = st.empty()
    resposta_completa = ""

    for chunk in agent.run(pergunta, stream=True):
        resposta_completa += chunk.content  # 🟢 AQUI! Pegamos o texto de cada parte
        resposta_container.markdown(resposta_completa + "▌")
