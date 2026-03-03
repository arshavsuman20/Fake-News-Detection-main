import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

stop_words = set(stopwords.words('english'))
port_stem = PorterStemmer()

def preprocess_text(content):
    content = re.sub('[^a-zA-Z]', ' ', content)
    content = content.lower()
    content = content.split()
    content = [port_stem.stem(word) for word in content if word not in stop_words]
    return ' '.join(content)

st.title("📰 Fake News Detection System")

user_input = st.text_area("Enter News Text Here")

if st.button("Predict"):
    if user_input.strip() != "":
        processed_text = preprocess_text(user_input)
        vectorized_text = vectorizer.transform([processed_text])
        prediction = model.predict(vectorized_text)

        if prediction[0] == 1:
            st.success("This is Real News ✅")
        else:
            st.error("This is Fake News ❌")
    else:
        st.warning("Please enter some text.")