import streamlit as st
from chatbot import graph, HumanMessage, AIMessage

# Streamlit app
st.markdown("""
    <style>
    /* Set the background to a watercolor-like gradient with a subtle animation */
    .stApp {
        background: linear-gradient(135deg, #a1c4fd, #c2e9fb, #f4f4d6, #ffd1dc, #d4a5f5);
        background-size: 200% 200%;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        animation: backgroundShift 15s ease infinite;
    }
    /* Background animation */
    @keyframes backgroundShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    /* Center the header content */
    .header {
        text-align: center;
        margin-top: 20px;
    }
    /* Style the title with fade-in animation */
    h1 {
        font-family: 'Arial', sans-serif;
        color: #1a2b4c;
        font-size: 2.5em;
        margin: 0;
        animation: fadeIn 1.5s ease-in-out;
    }
    /* Style the subtitle with fade-in animation */
    .subtitle {
        font-family: 'Arial', sans-serif;
        color: #4a5e7b;
        font-size: 1.2em;
        margin-top: 5px;
        margin-bottom: 20px;
        animation: fadeIn 2s ease-in-out;
    }
    /* Fade-in animation */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    /* Style the chat messages with slide-in animations */
    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
        max-width: 80%;
        opacity: 1;
        display: block;
    }
    .stChatMessage.user {
        background-color: #DCF8C6;
        text-align: right;
        margin-left: auto;
        animation: slideInRight 0.5s ease forwards;
    }
    .stChatMessage.assistant {
        background-color: #ECECEC;
        margin-right: auto;
        animation: slideInLeft 0.5s ease forwards;
    }
    /* Slide-in animations for messages */
    @keyframes slideInRight {
        0% { opacity: 0; transform: translateX(50px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    @keyframes slideInLeft {
        0% { opacity: 0; transform: translateX(-50px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    /* Style the chat input area with a pulse animation */
    .stTextInput > div > div > input {
        border-radius: 20px;
        padding: 10px;
        border: 1px solid #ccc;
        animation: pulse 2s infinite;
    }
    /* Pulse animation for chat input */
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(74, 94, 123, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(74, 94, 123, 0); }
        100% { box-shadow: 0 0 0 0 rgba(74, 94, 123, 0); }
    }
    /* Ensure chat area takes remaining space and is scrollable */
    .chat-container {
        width: 100%;
        max-width: 800px;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
    }
    .chat-messages {
        flex-grow: 1;
        overflow-y: auto;
        padding: 20px;
        min-height: 200px;
    }
    </style>
""", unsafe_allow_html=True)

# Header with title and subtitle
st.markdown("""
    <div class="header">
        <h1>Agentic AI Chatbot</h1>
        <div class="subtitle">A Chatbot powered by large language models and tools like arxiv, wiki, and tavily.</div>
    </div>
""", unsafe_allow_html=True)

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Chat messages
st.markdown('<div class="chat-messages">', unsafe_allow_html=True)
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
st.markdown('</div>', unsafe_allow_html=True)

# User input with error handling
if prompt := st.chat_input("Type your message (e.g., 'My name is Alice, tell me about AI')"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        state = {"messages": [HumanMessage(content=msg["content"]) for msg in st.session_state.messages]}
        result = graph.invoke(state)
        response = result["messages"][-1].content
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
    except Exception as e:
        st.error(f"Error: {str(e)}")

st.markdown('</div>', unsafe_allow_html=True)