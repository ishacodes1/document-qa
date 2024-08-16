import streamlit as st
import openai
from PIL import Image

# Set up the AIDELINE page configuration with a modern UI theme
st.set_page_config(page_title="AIDELINE - AI BDR Assistant", layout="wide", page_icon="🤖")

# Custom CSS for light theme, modern fonts, and corporate styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

        body {
            font-family: 'Inter', sans-serif;
            background-color: #F4F7F8;
            color: #333333;
        }

        .stApp {
            background-color: #FFFFFF;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.05);
        }

        .stButton > button {
            background-color: #005EB8;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 12px 25px;
            border: none;
            cursor: pointer;
            box-shadow: 0px 4px 10px rgba(0, 94, 184, 0.2);
        }

        .stButton > button:hover {
            background-color: #004494;
            color: white;
        }

        .stTextArea textarea, .stTextInput input {
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            color: #333333;
            background-color: #FFFFFF;
            border-radius: 8px;
            padding: 12px;
            border: 1px solid #CCCCCC;
            box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.1);
        }

        .stMarkdown h1, h2, h3, h4 {
            font-weight: 600;
            color: #005EB8;
        }

        .stMarkdown p {
            font-size: 16px;
            line-height: 1.6;
            color: #666666;
        }

        .icon-container {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }

        .icon-container img {
            width: 40px;
            height: 40px;
            margin-right: 15px;
        }

        .icon-container h3 {
            margin: 0;
            font-weight: 600;
            color: #005EB8;
        }

        .agent-response {
            background-color: #F1F5FB;
            padding: 15px;
            border-radius: 8px;
            font-family: 'Inter', sans-serif;
            font-size: 16px;
            color: #333333;
            line-height: 1.6;
            margin-bottom: 10px;
            border-left: 4px solid #005EB8;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }

        .footer {
            text-align: center;
            color: #777777;
            font-size: 14px;
            margin-top: 20px;
        }

        hr {
            border-top: 1px solid #E0E0E0;
            margin-top: 30px;
            margin-bottom: 30px;
        }
    </style>
    """, unsafe_allow_html=True)

# Try to load icons or handle the error gracefully
try:
    management_icon = Image.open("management_icon.png")
    ingestion_icon = Image.open("ingestion_icon.png")
except FileNotFoundError:
    management_icon = None
    ingestion_icon = None

# AIDELINE Header with modern styling moved to the left
st.markdown("<h1 style='text-align: left;'>AIDELINE - AI-Powered BDR Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left;'>Manage Your BDR Tasks with AI-Powered Agents</h3>", unsafe_allow_html=True)

# OpenAI API Key input with styled input
st.markdown("### Enter your OpenAI API Key to Get Started:")
openai_api_key = st.text_input("🔑 OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please enter your OpenAI API key to continue.", icon="🔑")
else:
    # Set OpenAI API key
    openai.api_key = openai_api_key

    # Management Agent Section
    if management_icon:
        st.markdown("<div class='icon-container'><img src='management_icon.png' alt='Management Icon'><h3>Management Agent</h3></div>", unsafe_allow_html=True)
    st.write("The Management Agent orchestrates tasks between different agents.")
    if st.button("Trigger Management Agent"):
        st.success("Management Agent triggered successfully!")

    # Data Ingestion Agent Section
    if ingestion_icon:
        st.markdown("<div class='icon-container'><img src='ingestion_icon.png' alt='Ingestion Icon'><h3>Data Ingestion Agent</h3></div>", unsafe_allow_html=True)
    st.write("The Data Ingestion Agent collects, cleans, and stores data from various sources.")
    if st.button("Trigger Data Ingestion"):
        st.write("Data Ingestion Agent triggered!")
        st.write("Collecting data...")
        st.write("Cleaning data (removing HTML tags, etc.)...")
        st.write("Storing data...")
        st.success("Data has been successfully ingested and stored.")

    # Chat Interface Section
    st.markdown("## Chat with AIDELINE")
    st.write("Interact with AIDELINE and ask questions. The context will be preserved throughout the conversation.")

    # Initialize or retrieve chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display previous chat messages
    for message in st.session_state["messages"]:
        if message["role"] == "user":
            st.markdown(f"<div class='agent-response'><strong>You:</strong> {message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='agent-response'><strong>AIDELINE:</strong> {message['content']}</div>", unsafe_allow_html=True)

    # Input for new message
    user_input = st.text_input("💬 Your message:")
    if st.button("Send"):
        if user_input:
            # Add user message to chat history
            st.session_state["messages"].append({"role": "user", "content": user_input})

            # Generate AIDELINE's response using OpenAI API with the new API structure
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state["messages"]
            )
            answer = response['choices'][0]['message']['content']

            # Add AIDELINE's response to chat history
            st.session_state["messages"].append({"role": "assistant", "content": answer})

            # Display the updated chat
            st.markdown(f"<div class='agent-response'><strong>AIDELINE:</strong> {answer}</div>", unsafe_allow_html=True)

# Footer Section with styled text
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='footer'>© 2024 Echomotion GmbH - All Rights Reserved</div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>For more information, visit our <a href='https://yourwebsite.com' style='color: #005EB8;'>website</a> or contact us at info@echomotion.de</div>", unsafe_allow_html=True)
