import os
import streamlit as st
from openai import OpenAI

# --- SETUP ---
API_KEY="OPENAI_API_KEY"

# API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key="OPENAI_API_KEY")

# --- UI ---

st.set_page_config(page_title="AI Q&A Bot", page_icon="🤖", layout="centered")

# --- Custom CSS ---
st.markdown(
    """
    <style>
        body {
            background-color: #c7dde4;
        }
        .title {
            font-size: 42px;
            font-weight: 800;
            text-align: center;
            margin-top: 50px;
            margin-bottom: 10px;
            color: #ddcbcb;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            margin-bottom: 40px;
            color: #555;
        }
        .stTextInput label {
            font-size: 18px !important;
            font-weight: 600 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header ---
st.markdown("<div class='title'>🤖 Welcome to AI Q&A Bot</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Let's get started</div>", unsafe_allow_html=True)

# --- User Input ---
user_input = st.text_input("💬 Ask me anything:",placeholder="type here..")

if user_input:
    with st.spinner("Thinking... 🤔"):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response.choices[0].message["content"]
        st.markdown(f"**🤖 AI:** {answer}")

# --- Footer ---
st.markdown(
    """
    <div style='position: fixed; left: 0; bottom: 15px; width: 100%; text-align: center; color: gray; font-size: 14px;'>
        Made by <b>Parjinder Singh</b><br>
        <div style="margin-top: 10px;">
            <a href='https://www.linkedin.com/in/parjinder-singh' target='_blank' 
               style='background-color:#0A66C2;color:white;padding:8px 16px;border-radius:8px;
                      text-decoration:none;font-weight:bold;display:inline-block;'>
                🔗 Connect on LinkedIn
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

