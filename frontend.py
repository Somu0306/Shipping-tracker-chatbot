import streamlit as st
from app.data_loader import load_shipments
from app.chatbot import chatbot_response

# Page configuration
st.set_page_config(
    page_title="Shipping Tracker Chatbot",
    page_icon="🚚",
    layout="centered"
)

# Title
st.title("🚚 Shipping Tracker Chatbot")
st.write("Track your shipments quickly using natural language.")

# Load shipment data
shipments = load_shipments()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot response
    response = chatbot_response(user_input, shipments)

    # Show bot message
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    with st.chat_message("assistant"):
        st.markdown(response)
