import streamlit as st
import pandas as pd
import joblib

model_load = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')  

st.title("Language Detection Panel")
st.subheader("Enter your sentence in your language")


ap = st.text_input("Enter the Sentence")
st.write("Your Text:", ap)


if st.button('Convert') and ap:
    
    X_input = vectorizer.transform([ap])
    
    result = model_load.predict(X_input)
    
    st.success(f"Your Language is: {result[0]}")


