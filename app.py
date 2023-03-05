import streamlit as st
import os
import urllib.request
import openai

openai.api_key =  os.getenv("APIKEY")

query = st.text_input("Input Query")

if st.button("Generate Diagram"):
    response = openai.Image.create(
    prompt=query,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    urllib.request.urlretrieve(image_url, 'img.png')
    img = Image.open("img.png")
    st.image(img)