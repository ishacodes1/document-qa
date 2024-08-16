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

        .stMarkdown h1 {
            text-align: center;
            font-size: 36px;
            margin-bottom: 10px;
        }

        .stMarkdown h3 {
            text-align: center;
            font-size: 22px;
            margin-bottom: 20px;
            color: #666666;
        }

        .stMarkdown p {
            font-size: 16px;
            line-height: 1.6;
            color: #666666;
            text-align: center;
            margin-bottom: 40px;
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

# AIDELINE Header and Introduction with modern styling
st.markdown("<h1>AIDELINE</h1>", unsafe_allow_html=True)
st.markdown("<h3>Your AI-Powered Business Development Representative</h3>", unsafe_allow_html=True)
st.markdown("""
    <p>Welcome to AIDELINE, where cutting-edge AI technology meets the art of business development. Our AI-powered BDR assistant
    is designed to streamline your sales process, from lead research to personalized outreach. Enhance your team's productivity and
    watch your conversions soar with AIDELINE's intelligent tools.</p>
    """, unsafe_allow_html=True)

# Add a visual guide to the user journey
st.markdown("<h2 style='text-align: center;'>User Journey</h2>", unsafe_allow_html=True)
st.image("path_to_your_image/user_journey.png", use_column_width=True)  # Replace with actual path to your image

# Optional: Textual representation of steps
st.markdown("""
    <h3 style='text-align: center;'>Start</h3>
    <p style='text-align: center;'>User messages the name of target company or person to AIDELINE.</p>
    <p style='text-align: center;'>AIDELINE collects data for profiling.</p>
    
    <h3 style='text-align: center;'>Analyze</h3>
    <p style='text-align: center;'>AIDELINE creates the profile and provides insights.</p>
    
    <h3 style='text-align: center;'>Reach Out</h3>
    <p style='text-align: center;'>The user gets recommendations and starts interaction with the prospect.</p>
    
    <h3 style='text-align: center;'>Optimize</h3>
    <p style='text-align: center;'>AIDELINE helps to optimize the follow-up and provides LOI scores.</p>
""", unsafe_allow_html=True)

# OpenAI API Key input with styled input
st.markdown("### Enter your OpenAI API Key to Get Started:")
openai_api_key = st.text_input("🔑 OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please enter your OpenAI API key to continue.", icon="🔑")
else:
    # Set OpenAI API key
    openai.api_key = openai_api_key

    # Left-aligned sections starting from "Management Agent"
    st.markdown("<h2 style='text-align: left;'>Management Agent</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;'>The Management Agent orchestrates tasks between different agents.</p>", unsafe_allow_html=True)
    if st.button("Trigger Management Agent"):
        st.success("Management Agent triggered successfully!")

    st.markdown("<h2 style='text-align: left;'>Data Ingestion Agent</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;'>The Data Ingestion Agent collects, cleans, and stores data from various sources.</p>", unsafe_allow_html=True)
    if st.button("Trigger Data Ingestion"):
        st.write("Data Ingestion Agent triggered!")
        st.write("Collecting data...")
        st.write("Cleaning data (removing HTML tags, etc.)...")
        st.write("Storing data...")
        st.success("Data has been successfully ingested and stored.")

    # Chat Interface Section
    st.markdown("<h2 style='text-align: left;'>Chat with AIDELINE</h2>", unsafe_allow_html=True)
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

        # Generate AIDELINE's response using OpenAI API with the updated API structure
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state["messages"]
        )
        answer = response['choices'][0]['message']['content']

        # Add AIDELINE's response to chat history
        st.session_state["messages"].append({"role": "assistant", "content": answer})

        # Display the updated chat
        st.markdown(f"<div class='agent-response'><strong>AIDELINE:</strong> {answer}</div>", unsafe_allow_html=True)
