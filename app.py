import streamlit as st
import os
import urllib.request
import openai


query = st.text_input("Input Query")

response = openai.Image.create(
  prompt=query,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
urllib.request.urlretrieve(img_url, 'img.png')
img = Image.open("img.png")
st.image(img)