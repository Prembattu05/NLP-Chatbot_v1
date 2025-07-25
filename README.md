# NLP-Chatbot
This is a chatbot that will answer the questions you will ask.
# 💬 Smart NLP Chatbot with Fuzzy Matching

A simple and intelligent chatbot built using **Python**, **Streamlit**, and **fuzzy matching**. It responds to user queries based on a custom Q&A dataset using natural language similarity.

> 🔗 **Live Demo**: *[Deploy on Streamlit Cloud to get a public link]*  
> *(You can add the link here once deployed)*

---

## 🚀 Features

- 💬 Conversational UI using Streamlit
- 🔍 Fuzzy string matching with `difflib`
- 📄 Customizable Q&A dataset (CSV-based)
- ⚡ Lightweight, fast, and fully local
- 🛠 Easy to extend with new questions and answers

---

## 🗂️ Project Structure

NLP-Chatbot_v1/
├── chatbot_dataset_augmented.csv # Dataset (user_utterance, bot_response)
├── streamlit_app.py # Main Streamlit chatbot app
├── app.py # (Optional) older version of the app
├── requirements.txt # Python dependencies
├── README.md # Project overview and instructions
└── .streamlit/ # Streamlit config folder (optional)

---

## 📄 Dataset Format

The chatbot uses a CSV file with the following columns:

| user_utterance         | bot_response                              |
|------------------------|--------------------------------------------|
| hello                  | hi! how can i help you today?              |
| who are you?           | i'm a chatbot built using NLP.             |
| how do i reset password?| click 'forgot password' and follow steps. |

You can expand or modify this dataset to train your chatbot with more responses.

---

## 🧪 How to Run the App Locally

### 1. Clone this repository

```bash
git clone https://github.com/Prembattu05/NLP-Chatbot_v1.git
cd NLP-Chatbot_v1
pip install -r requirements.txt
streamlit run streamlit_app.py
