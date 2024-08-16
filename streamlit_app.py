import streamlit as st
import openai

# Set up the AIDELINE page configuration with a modern UI theme
st.set_page_config(page_title="AIDELINE - AI BDR Assistant", layout="centered", page_icon="🤖")

# Custom CSS for modern fonts and clean layout
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
        
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #F4F7F8;
            color: #333333;
        }

        .stButton > button {
            background-color: #007ACC;
            color: white;
            border-radius: 5px;
            font-size: 16px;
            padding: 10px 20px;
        }

        .stButton > button:hover {
            background-color: #005F9E;
            color: white;
        }

        .stTextArea textarea {
            font-family: 'Roboto', sans-serif;
            font-size: 14px;
            color: #333333;
            border-radius: 5px;
            padding: 10px;
            border: 1px solid #CCCCCC;
        }

        .stTextInput input {
            font-family: 'Roboto', sans-serif;
            font-size: 14px;
            color: #333333;
            border-radius: 5px;
            padding: 10px;
            border: 1px solid #CCCCCC;
        }

        .stMarkdown h1, h2, h3, h4 {
            font-weight: 500;
            color: #007ACC;
        }

        .stMarkdown p {
            font-size: 16px;
            line-height: 1.6;
            color: #555555;
        }

        .agent-response {
            background-color: #E8F0FE;
            padding: 15px;
            border-radius: 8px;
            font-family: 'Roboto', sans-serif;
            font-size: 16px;
            color: #333333;
            line-height: 1.6;
        }

        .footer {
            text-align: center;
            color: #777777;
            font-size: 14px;
            margin-top: 20px;
        }

        hr {
            border-top: 1px solid #CCCCCC;
            margin-top: 30px;
            margin-bottom: 30px;
        }
    </style>
    """, unsafe_allow_html=True)

# AIDELINE Header with modern styling
st.markdown("<h1 style='text-align: center;'>AIDELINE - AI-Powered BDR Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Manage Your BDR Tasks with AI-Powered Agents</h3>", unsafe_allow_html=True)

# OpenAI API Key input with styled input
st.markdown("### Enter your OpenAI API Key to Get Started:")
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please enter your OpenAI API key to continue.", icon="🔑")
else:
    # Set OpenAI API key
    openai.api_key = openai_api_key

    # Management Agent Section
    st.markdown("## Management Agent")
    st.write("The Management Agent orchestrates tasks between different agents.")
    if st.button("Trigger Management Agent"):
        st.success("Management Agent triggered successfully!")

    # Email Agent Section
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
            st.markdown(f"<div class='agent-response'><strong>Agent Response:</strong> {answer}</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter a prompt for the Email Agent to process.")

    # Data Ingestion Agent Section
    st.markdown("## Data Ingestion Agent")
    st.write("The Data Ingestion Agent collects, cleans, and stores data from various sources.")
    if st.button("Trigger Data Ingestion"):
        st.write("Data Ingestion Agent triggered!")
        st.write("Collecting data...")
        st.write("Cleaning data (removing HTML tags, etc.)...")
        st.write("Storing data...")
        st.success("Data has been successfully ingested and stored.")

    # New Section: Lead Qualification and Action Triggering
    st.markdown("## Lead Qualification")
    st.write("Review and qualify leads. Once satisfied, you can trigger actions like sending emails or connecting to a CRM.")

    # Input for qualifying leads
    lead_qualification_prompt = st.text_area("Enter details or criteria to qualify leads:")
    if st.button("Review and Qualify Leads"):
        if lead_qualification_prompt:
            st.write(f"Qualifying leads based on: {lead_qualification_prompt}")
            # Simulate lead qualification
            qualified_leads = ["Lead 1: High Potential", "Lead 2: Medium Potential", "Lead 3: Low Potential"]
            st.markdown(f"<div class='agent-response'><strong>Qualified Leads:</strong><br>{'<br>'.join(qualified_leads)}</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter lead qualification criteria.")

    # Trigger Email and CRM Actions
    st.markdown("### Trigger Actions for Qualified Leads")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Send Email via Outlook"):
            st.write("Connecting to Outlook...")
            st.success("Emails sent successfully!")

    with col2:
        if st.button("Connect to CRM (HubSpot)"):
            st.write("Connecting to HubSpot...")
            st.success("Data ingested into CRM successfully!")

    # Data Storage Visualization
    st.markdown("## Data Storage")
    st.write("Visualize the stored data (simulated).")
    stored_data = [
        {"Data Point": "Company Name", "Value": "Echomotion GmbH"},
        {"Data Point": "Contact Email", "Value": "info@echomotion.de"},
        {"Data Point": "Recent Activity", "Value": "Downloaded whitepaper"},
    ]
    st.table(stored_data)

# Footer Section with styled text
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='footer'>© 2024 Echomotion GmbH - All Rights Reserved</div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>For more information, visit our <a href='https://yourwebsite.com'>website</a> or contact us at info@echomotion.de</div>", unsafe_allow_html=True)
