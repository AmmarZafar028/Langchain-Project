import streamlit as st
from langchain.llms import OpenAI
st.title("Language Chain")
st.write("This is a demo of the Language Chain. It is a tool that allows you to generate text in a variety of styles. It is powered by OpenAI's GPT-3.")
OpenAI_api_key = st.sidebar.text_input("OpenAI API Key")
def generate_response(input_text):
    llm = OpenAI(temperature = 0.7, OpenAI_api_key = OpenAI_api_key)
    st.info(llm(input_text))
    with st.form(key='my_form'):
        text = st.text_area("Enter text:","What are the three pieces od advice for learning how to code?")
        submitted = st.form_submit_button('Submit')
        if not OpenAI_api_key.startswith("sk-"):
            st.warning("Please enter your OpenAI API Key",icon="A")
            if submitted and OpenAI_api_key.startswith("sk-"):
                generate_response(text)
            