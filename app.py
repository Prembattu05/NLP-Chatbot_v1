import pandas as pd
import streamlit as st

# Load dataset
df = pd.read_csv("chatbot_dataset.csv")
df = df[['User Utterance', 'Bot Response']].dropna()
df.columns = ['input', 'response']

# Simple logic: Match exact question
def get_response(user_input):
    for i in range(len(df)):
        if user_input.lower() == df['input'][i].lower():
            return df['response'][i]
    return "Sorry, I don't understand that yet."

# Streamlit interface
st.title("💬 Simple NLP Chatbot")
user_input = st.text_input("You:", "")

if st.button("Get Response"):
    response = get_response(user_input)
    st.text_area("Bot:", response, height=100)
