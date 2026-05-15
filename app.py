import streamlit as st
from groq import Groq

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="ArcGIS Pro Script Assistant",
    page_icon="🗺️",
    layout="wide"
)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("⚙️ Settings")

api_key = st.sidebar.text_input(
    "Groq API Key",
    type="password"
)

model = st.sidebar.selectbox(
    "Select Model",
    [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile"
    ]
)

temperature = st.sidebar.slider(
    "Temperature",
    0.0,
    1.0,
    0.3
)

# =========================
# CHAT MEMORY
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# TITLE
# =========================
st.title("🗺️ ArcGIS Pro Script Assistant")

st.markdown(
    "AI assistant for ArcGIS Pro workflows, troubleshooting, and GIS guidance."
)

# =========================
# DISPLAY CHAT
# =========================
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =========================
# USER INPUT
# =========================
prompt = st.chat_input("Ask a GIS question...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            client = Groq(api_key=api_key)

            system_prompt = """
            You are a professional GIS Assistant specialized in ArcGIS Pro.

            Always:
            - Explain GIS workflows clearly
            - Warn about CRS issues
            - Suggest ArcGIS Pro tools
            - Explain best practices
            - Avoid hallucinations
            """

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=model,
                temperature=float(temperature)
            )

            response = chat_completion.choices[0].message.content

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )