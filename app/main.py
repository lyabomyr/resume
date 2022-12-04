import streamlit as st
from title import title
from skills import skills
from experience import experience
from education_and_cources import education

def main():
    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)
    title()
    skills()
    experience()
    education()

with st.sidebar:  
    with open("src/CV_QA_Kachko_Luibomyr.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label=" Download CV_QA_Kachko_Luibomyr.pdf",
                    data=PDFbyte,
                    file_name="CV_QA_Kachko_Luibomyr.pdf",
                    mime='application/octet-stream')
main()




