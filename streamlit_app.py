import streamlit as st

st.title("🧠 NLP Chatbot")
st.write("Welcome! This is your first deployed Streamlit app.")
import streamlit as st
import pandas as pd

st.set_page_config(page_title="NLP Chatbot", page_icon="🧠")
st.title("🧠 NLP Chatbot")

# Load dataset (assumes it's in the same repo)
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_chatbot_dataset.csv")

df = load_data()

# User input
user_question = st.text_input("Ask me something 👇")

if user_question:
    # Simple matching (case insensitive)
    matched = df[df['Question'].str.lower() == user_question.lower()]
    
    if not matched.empty:
        st.success(f"Answer: {matched.iloc[0]['Answer']}")
    else:
        st.warning("I couldn't find an answer to that question.")
