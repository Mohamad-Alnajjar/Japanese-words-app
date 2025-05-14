# from google import genai
# import streamlit as st
# import pandas as pd
# import numpy as np

# client = genai.Client(api_key="AIzaSyDIaOVvqvaYvh_MIFRhfi-eK13Vjw_8s6E")

# def generate_respone(w1, w2):
#     response = client.models.generate_content(
#     model="gemini-2.0-flash", 
#     contents=f"""for the two Japanese words i am going to provide you, return the differneces between them using a 
#     table containing the words, meaning in english, nuances, and 2 exammples for each one.
#     1st word: {w1}
#     2nd word: {w2}
    
#     output rules:
#     1. dont output anything other than the table.
#     2. follow the instructions strictly
#     """
    
#     )
#     return st.write(response.text)

# w1 = st.text_area(
#         "Enter w1:",
#     )

# w2 = st.text_area(
#         "Enter w2:",
#     )
# button = st.button("Enter", type="primary")

# if w1 and w2 and button:
#     generate_respone(w1, w2)

# #tests


import os
import streamlit as st
from google import genai

# Load API key securely
# api_key = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key="AIzaSyDIaOVvqvaYvh_MIFRhfi-eK13Vjw_8s6E")

def generate_response(w1, w2):
    prompt = f"""
    For the two Japanese words below, return the differences between them using a table with the following columns:
    - Word
    - Meaning in English
    - Nuances
    - 2 Examples for each word

    Words:
    1st word: {w1}
    2nd word: {w2}

    Output rules:
    1. Only output the table, nothing else.
    2. Follow the format strictly.
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

# Streamlit UI
st.title("Japanese Word Comparison")

w1 = st.text_area("Enter 1st Japanese word:")
w2 = st.text_area("Enter 2nd Japanese word:")
button = st.button("Compare Words", type="primary")

if w1 and w2 and button:
    result = generate_response(w1, w2)
    st.write(result)
