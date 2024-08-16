import streamlit as st
import openai

# Set up the AIDELINE page configuration with a modern UI theme
st.set_page_config(page_title="AIDELINE - AI BDR Assistant", layout="wide", page_icon="🤖")

# Custom CSS for light theme, modern fonts, and corporate styling
st.markdown("""
    <style>
        /* Your existing CSS */
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
    st.write("Engage in a conversation with AIDELINE, your AI-powered assistant. You can ask questions, provide prompts, and receive intelligent responses. AIDELINE remembers the context of your previous conversations, allowing for a seamless and continuous dialogue as you interact.")

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

            try:
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

            except Exception as e:  # Catching a broader range of exceptions
                st.error(f"An error occurred: {e}")

# Footer
st.markdown("<div class='footer'>Powered by OpenAI and Streamlit</div>", unsafe_allow_html=True)
