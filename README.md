![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-success)
![ML](https://img.shields.io/badge/Machine%20Learning-NLP-orange)
# Fake News Detection Web Application

A Machine Learning based web application that classifies news articles as **Real** or **Fake** using Natural Language Processing (NLP) techniques.

**Live Demo:**  
https://arshav-fake-news-detector.streamlit.app/


## Project Overview

This project uses TF-IDF vectorization and Logistic Regression to detect fake news from textual input.  
The trained model is deployed as an interactive web application using Streamlit.

The system preprocesses text using:
- Lowercasing
- Regex-based cleaning
- Stopword removal
- Stemming (Porter Stemmer)

The final model achieves:

- **97.9% Test Accuracy**
- Fast real-time predictions
- Publicly deployed web interface


## Machine Learning Pipeline

1. Data Cleaning
2. Text Preprocessing
3. TF-IDF Feature Extraction
4. Train-Test Split
5. Logistic Regression Model Training
6. Model Evaluation
7. Deployment using Streamlit


## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit


## Model Details

- Algorithm: Logistic Regression
- Feature Extraction: TF-IDF Vectorizer
- Text Processing: Porter Stemming + Stopword Removal
- Accuracy: 97.9% on test dataset


## Project Structure
fake-news-detection/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md


## How to Run Locally

1. Clone the repository:
    git clone https://github.com/arshavsuman20/Fake-News-Detection-main.git

2. Install dependencies:
    pip install -r requirements.txt

3. Run the app:
    streamlit run app.py

## Features

- Real-time fake news classification
- Clean and interactive UI
- Fast prediction response
- Deployable ML model


## Future Improvements

- Add probability confidence score
- Improve UI styling
- Add more advanced models (SVM, BERT)
- Deploy on custom domain


## Author

**Arshav Suman**  
Machine Learning & Software Development Enthusiast