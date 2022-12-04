import streamlit as st
from app.title import title
from app.skills import skills
from app.experience import experience
from app.education_and_cources import education
from config import pdf_file_patch, file_name

def structure():
    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)
    title()
    skills()
    experience()
    education()

def main():
    structure()
    with st.sidebar:  
        with open(pdf_file_patch , "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label= f" Download {file_name}",
                        data=PDFbyte,
                        file_name= file_name,
                        mime='application/octet-stream')

if __name__ == "__main__":
    main()