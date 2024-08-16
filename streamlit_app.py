import streamlit as st
import openai

# Set up the AIDELINE page configuration
st.set_page_config(page_title="AIDELINE - AI BDR Assistant", layout="wide", page_icon="🤖")

# AIDELINE Header
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>AIDELINE - AI-Powered BDR Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B8BBE;'>Manage Your BDR Tasks with AI-Powered Agents</h3>", unsafe_allow_html=True)

# OpenAI API Key input
st.markdown("### Enter your OpenAI API Key to Get Started:")
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please enter your OpenAI API key to continue.", icon="🔑")
else:
    # Set OpenAI API key
    openai.api_key = openai_api_key

    # Management Agent - Overseeing the operation
    st.markdown("## Management Agent")
    st.write("The Management Agent orchestrates tasks between different agents.")
    if st.button("Trigger Management Agent"):
        st.write("Management Agent triggered!")

    # Email Agent - Retrieve information and process prompts
    st.markdown("## Email Agent")
    st.write("The Email Agent retrieves information and processes email-related prompts.")
    email_prompt = st.text_area("Enter the email prompt or message you want the agent to process:")
    if st.button("Run Email Agent"):
        if email_prompt:
            st.write(f"Processing email prompt: {email_prompt}")
            # Simulate email agent action
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": email_prompt}
                ]
            )
            answer = response['choices'][0]['message']['content']
            st.markdown(f"**Agent Response:** {answer}")
        else:
            st.warning("Please enter a prompt for the Email Agent to process.")

    # Data Ingestion Agent - Trigger data collection, cleaning, and storage
    st.markdown("## Data Ingestion Agent")
    st.write("The Data Ingestion Agent collects, cleans, and stores data from various sources.")
    if st.button("Trigger Data Ingestion"):
        st.write("Data Ingestion Agent triggered!")
        # Simulate data ingestion actions
        st.write("Collecting data...")
        st.write("Cleaning data (removing HTML tags, etc.)...")
        st.write("Storing data...")
        st.success("Data has been successfully ingested and stored.")

    # Storage Visualization
    st.markdown("## Data Storage")
    st.write("Visualize the stored data (simulated).")
    stored_data = [
        {"Data Point": "Company Name", "Value": "Echomotion GmbH"},
        {"Data Point": "Contact Email", "Value": "info@echomotion.de"},
        {"Data Point": "Recent Activity", "Value": "Downloaded whitepaper"},
    ]
    st.table(stored_data)

# Footer Section
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### © 2024 Echomotion GmbH - All Rights Reserved")
st.markdown("For more information, visit our [website](https://yourwebsite.com) or contact us at info@echomotion.de")
