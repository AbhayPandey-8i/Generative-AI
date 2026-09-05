import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

st.set_page_config(page_title="Mood ChatBot", page_icon="💬", layout="centered")

# ---------- Styling ----------
st.markdown(
    """
    <style>
    .stChatMessage { border-radius: 12px; }
    div[data-testid="stSidebar"] { background-color: #f5f5f7; }
    .mode-badge {
        display: inline-block;
        padding: 4px 14px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

MODES = {
    "Normal": {
        "prompt": "You are a normal AI agent and answers normally as you usually do",
        "emoji": "🙂",
        "color": "#4CAF50",
    },
    "Angry": {
        "prompt": "You are angry AI agent and answers in angry way",
        "emoji": "😠",
        "color": "#E53935",
    },
    "Sad": {
        "prompt": "You are sad AI agent and answers in sad way",
        "emoji": "😢",
        "color": "#5C6BC0",
    },
}


@st.cache_resource
def get_model():
    llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-V4-Flash-0731"
    )
    return ChatHuggingFace(llm=llm)


model = get_model()

# ---------- Sidebar: mode selection ----------
with st.sidebar:
    st.header("Choose Your AI Mode")
    selected_mode = st.radio(
        "Enter your mode no.",
        options=list(MODES.keys()),
        format_func=lambda m: f"{MODES[m]['emoji']}  {m} mode",
    )
    st.divider()
    if st.button("Reset Chat", use_container_width=True):
        st.session_state.history = [SystemMessage(content=MODES[selected_mode]["prompt"])]
        st.session_state.active_mode = selected_mode
        st.rerun()

# ---------- Initialize / switch mode ----------
if "history" not in st.session_state or st.session_state.get("active_mode") != selected_mode:
    st.session_state.history = [SystemMessage(content=MODES[selected_mode]["prompt"])]
    st.session_state.active_mode = selected_mode

mode_info = MODES[selected_mode]

st.title("💬 ChatBot")
st.markdown(
    f'<span class="mode-badge" style="background-color:{mode_info["color"]}22; '
    f'color:{mode_info["color"]};">{mode_info["emoji"]} {selected_mode} mode</span>',
    unsafe_allow_html=True,
)

# ---------- Render past conversation (skip SystemMessage) ----------
for message in st.session_state.history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar=mode_info["emoji"]):
            st.markdown(message.content)

prompt = st.chat_input("You: ")

if prompt:
    st.session_state.history.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=mode_info["emoji"]):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.history)
            st.markdown(response.content)

    st.session_state.history.append(AIMessage(content=response.content))