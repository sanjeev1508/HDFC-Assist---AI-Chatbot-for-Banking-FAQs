import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process

# Load dataset
dataset_path = r"F:\AIVAR FINAL\Datasets\HDFC_Faq.csv"
df = pd.read_csv(dataset_path)

# Drop NaN values and duplicates
df = df.dropna(subset=["question", "answer"]).drop_duplicates(subset=["question"])

# Convert text to lowercase
df["question"] = df["question"].str.lower()

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["question"])

# Function to get the best match
def get_best_match(user_query):
    user_query = user_query.lower()
    
    # Use Fuzzy Matching
    fuzzy_result = process.extractOne(user_query, df["question"].tolist())
    
    if fuzzy_result is None:  # No match found
        return None

    best_match, score = fuzzy_result

    # If confidence is low, use TF-IDF similarity
    if score < 70:
        query_vector = vectorizer.transform([user_query])
        similarity_scores = cosine_similarity(query_vector, tfidf_matrix)
        best_index = similarity_scores.argmax()
        best_match = df.iloc[best_index]["question"]

    return best_match

# Streamlit UI
st.set_page_config(page_title="HDFC Chatbot", page_icon="💬", layout="wide")

st.markdown("""
    <style>
        .chat-container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border-radius: 10px;
            background-color: #F4F4F8;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }
        .chat-header {
            background-color: #5E35B1;
            padding: 10px;
            border-radius: 10px 10px 0px 0px;
            color: white;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }
        .chat-message {
            padding: 10px;
            margin: 5px 0;
            border-radius: 8px;
            max-width: 80%;
            display: inline-block;
        }
        .chat-user {
            background-color: #E3F2FD;
            align-self: flex-end;
        }
        .chat-bot {
            background-color: #EDE7F6;
            align-self: flex-start;
        }
    </style>
""", unsafe_allow_html=True)

# Chat title
st.markdown('<div class="chat-header">Hi, this is HDFC AI!</div>', unsafe_allow_html=True)
st.write("Welcome to HDFC Chatbot! How can I assist you today?")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input field
user_input = st.chat_input("Type your message here...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Find best response
    best_question = get_best_match(user_input)
    if best_question:
        answer = df[df["question"] == best_question]["answer"].values[0]
    else:
        answer = "I'm sorry, I couldn't find a relevant answer. Please try rephrasing your question."

    # Store bot response
    st.session_state.messages.append({"role": "assistant", "content": answer})

    # Display user and bot messages
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        st.markdown(answer)
