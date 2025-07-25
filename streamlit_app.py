import streamlit as st
import pandas as pd
import difflib
import os

st.set_page_config(page_title="Smart NLP Chatbot", page_icon="💬")
st.title("💬 Smart NLP Chatbot with Fuzzy Matching")

# ✅ Debug (temporarily)
st.write("📂 Working directory:", os.getcwd())
st.write("📄 Files:", os.listdir())

# ✅ Load CSV
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("chatbot_dataset_augmented.csv")
        df = df.dropna()
        return df
    except Exception as e:
        st.error(f"❌ Failed to load dataset: {e}")
        return pd.DataFrame(columns=["Question", "Answer"])

df = load_data()

def get_response(user_input):
    questions = df['Question'].str.lower().tolist()
    matches = difflib.get_close_matches(user_input.lower(), questions, n=1, cutoff=0.5)
    if matches:
        matched_row = df[df['Question'].str.lower() == matches[0]]
        return matched_row['Answer'].values[0]
    else:
        return "Sorry, I don't understand that yet."

user_input = st.text_input("You:", placeholder="Type your question here...")

if user_input:
    answer = get_response(user_input)
    st.text_area("Bot:", answer, height=100)
