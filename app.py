import streamlit as st
from PIL import Image
from emoji import emojize
import clf

dc = {0: f"person name {emojize(':person:')}", 1: f"company name {emojize(':bank:')}"}
favicon = Image.open('favicon.ico')
st.set_page_config(page_title='Brazilian Person/Company name classifier', page_icon=favicon, layout='wide')
name = st.text_input("Please type a name:")
if name:
    st.info(f"{name} is a {dc[clf.clfpfpj.predict([name])[0]]}")
