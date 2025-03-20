# HDFC Assist - AI Chatbot  

HDFC Assist is an AI-powered chatbot designed to answer frequently asked questions about HDFC banking services. It uses Natural Language Processing (NLP) and Fuzzy Matching techniques to provide accurate responses based on a predefined dataset.

## 🚀 Features  
- 💡 NLP-based question matching  
- 📖 Preloaded with HDFC FAQ dataset  
- 🌐 Streamlit-powered user interface  
- 🔍 Fuzzy matching & TF-IDF for better accuracy  
- ☁️ Easy deployment on Streamlit Cloud  

## 📂 Dataset Description  

The chatbot uses an FAQ dataset stored in **HDFC_Faq.csv**, which contains the following attributes:  

| Column Name        | Description |
|--------------------|-------------|
| **question**       | The user query or frequently asked question |
| **answer**         | The corresponding response to the question |
| **found_duplicate** | Indicates if the question is a duplicate (1 = Yes, 0 = No) |

- **Purpose:** To provide accurate responses to HDFC-related queries  

## 🛠 Installation  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/sanjeev1508/HDFC-Assist---AI-Chatbot-for-Banking-FAQs.git
cd hdfc-assist
