import streamlit as st
import openai

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
            font-size: 48px;
            margin-bottom: 5px;
            letter-spacing: -0.5px;
        }

        .stMarkdown h2 {
            text-align: center;
            font-size: 28px;
            color: #333333;
            margin-top: -5px;
            margin-bottom: 15px;
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

        .tab-content {
            padding: 20px;
            background-color: #FFFFFF;
            border-radius: 8px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
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

        .sidebar-section {
            padding: 10px;
            border-radius: 8px;
            background-color: #FFFFFF;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for navigation or additional information
st.sidebar.markdown("<h3>Navigation</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-section'>Option 1</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-section'>Option 2</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-section'>Option 3</div>", unsafe_allow_html=True)

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
    # Placeholder for OpenAI API interaction
    st.markdown("<h2 style='text-align: left;'>Personalized Outreach</h2>", unsafe_allow_html=True)

    # Create tabs for Email, Call Script, and Social Media
    tabs = st.tabs(["Email", "Call Script", "Social Media"])

    with tabs[0]:
        st.markdown("<div class='tab-content'>Compose your email script here.</div>", unsafe_allow_html=True)
        email_input = st.text_area("✉️ Draft your email:")
        if st.button("Generate Email", key="email_script"):
            # Placeholder for backend integration
            st.success("Email script generated successfully!")

    with tabs[1]:
        st.markdown("<div class='tab-content'>Draft your call script here.</div>", unsafe_allow_html=True)
        call_input = st.text_area("📞 Draft your call script:")
        if st.button("Generate Call Script", key="call_script"):
            # Placeholder for backend integration
            st.success("Call script generated successfully!")

    with tabs[2]:
        st.markdown("<div class='tab-content'>Create your social media outreach here.</div>", unsafe_allow_html=True)
        social_input = st.text_area("📱 Draft your social media message:")
        if st.button("Generate Social Media Message", key="social_media"):
            # Placeholder for backend integration
            st.success("Social media message generated successfully!")

# Footer
st.markdown("<div class='footer'>Powered by OpenAI and Streamlit</div>", unsafe_allow_html=True)
