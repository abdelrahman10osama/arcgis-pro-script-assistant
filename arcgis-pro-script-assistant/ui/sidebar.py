import streamlit as st
from core.memory_manager import clear_chat

def render_sidebar():

    st.sidebar.title("⚙️ Settings")

    api_key = st.sidebar.text_input(
        "Gemini API Key",
        type="password"
    )

    model = st.sidebar.selectbox(
    "Select Model",
    [
        "llama3-8b-8192",
        "llama3-70b-8192",
        "mixtral-8x7b-32768"
    ]
)

    temperature = st.sidebar.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.3
    )

    if st.sidebar.button("🗑️ Clear Chat"):
        clear_chat()

    return {
        "api_key": api_key,
        "model": model,
        "temperature": temperature
    }