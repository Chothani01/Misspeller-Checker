# 📝 Misspelled Word Detector Web App

## For try this application, [click here](https://misspeller-checker-byprincechothani.streamlit.app/)

This is a simple **Streamlit web application** that detects and corrects misspelled words in user-provided text using the `TextBlob` library.

---

## 🚀 Features

- ✅ Detects and lists misspelled words
- ✅ Provides corrected sentence
- ✅ Clean and simple web UI with Streamlit
- ✅ Word-by-word correction and counting of errors

---

## 🧠 How It Works

The logic is implemented in [`model.py`](model.py):

- It splits the input text into individual words
- Uses `TextBlob` to correct each word
- Compares original and corrected words to find spelling errors
- Returns both the corrected sentence and the list of incorrect words