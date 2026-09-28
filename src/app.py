import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
PROMPT_PATH = BASE_DIR / "prompts" / "system_prompt.md"

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")


@st.cache_data
def load_knowledge():
    files = sorted(DATA_DIR.glob("*.md"))
    parts = []
    for file in files:
        if file.name.lower() == "readme.md":
            continue
        parts.append(f"# {file.stem.replace('_', ' ').title()}\n\n{file.read_text(encoding='utf-8')}")
    return "\n\n---\n\n".join(parts)


@st.cache_data
def load_system_prompt():
    return PROMPT_PATH.read_text(encoding="utf-8")


def get_api_key():
    # Streamlit Cloud: st.secrets["OPENAI_API_KEY"]
    try:
        key = st.secrets.get("OPENAI_API_KEY")
        if key:
            return key
    except Exception:
        pass
    return os.getenv("OPENAI_API_KEY")


def build_instructions():
    system_prompt = load_system_prompt()
    knowledge = load_knowledge()
    return f"""{system_prompt}

## BASE DE CONHECIMENTO DISPONÍVEL

Use a base abaixo como referência principal para responder.
Não invente informações que não estejam sustentadas pela base.
Se a base não tiver informação suficiente, diga explicitamente que não possui informação suficiente.

{knowledge}
"""


def answer(messages):
    api_key = get_api_key()
    if not api_key:
        return (
            "Ainda não consigo conversar porque a chave da API não foi configurada. "
            "Configure `OPENAI_API_KEY` nas variáveis de ambiente ou nos Secrets do Streamlit."
        )

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=MODEL,
        instructions=build_instructions(),
        input=messages,
    )
    return response.output_text


st.set_page_config(
    page_title="Daya — Assistente de Ciência de Dados",
    page_icon="🌸",
    layout="centered",
)

st.title("🌸 Daya")
st.caption("Assistente de Estudos em Ciência de Dados")

with st.sidebar:
    st.subheader("Sobre a Daya")
    st.write(
        "Professora, colega de estudos e mentora para estudantes "
        "de Ciência de Dados."
    )
    st.divider()
    st.write(f"Modelo: `{MODEL}`")
    st.write("Base: Python, Estatística, SQL, Análise de Dados, Machine Learning e IA.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Pergunte algo sobre Ciência de Dados...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("A Daya está pensando..."):
            response = answer(st.session_state.messages)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
