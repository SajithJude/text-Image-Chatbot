import streamlit as st
import os
import openai


query = st.text_input("Input Query")

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

 