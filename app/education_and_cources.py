import streamlit as st
from pdfparser.pdf_parser import PdfParser


print(PdfParser().courses_from_pdf())
def education_list():
    education_list = ''
    for i in PdfParser().education_from_pdf():
        if i != ' ':
            education_list += f'\n - ' + i['time_range_title'] + '\n' + i['univer_description'] 
    return education_list

def courses_list():
    courses_list = ''
    for i in PdfParser().courses_from_pdf():
        if i != ' ':
            courses_list += f'\n - {i}'
    return courses_list

def education():
    st.markdown(f'''
        ##### EDUCATION:
        {education_list()} 

        \n##### COURSES:
        {courses_list()} 
          \n ***''')

#         ##### EDUCATION:
#         - November 2022, Master's degree.
#         National University of Life and Environmental Sciences of Ukraine, Automation and Computer-Integrated Technologies;

#         - June 2020, Bachelor’s degree.
#         Separated subdivision National University of Life and Environmental Sciences of Ukraine, Engineer Electricity;

#         ##### COURSES:

#         - Projector Institute, Machine learning in production 
#         - Applitools, Advanced Cypress
#         - Applitools, API Test Automation with Postman
#         - Stepik JavaScript
#         - Automation testing Python Selenium
#         - Stepik Python Programming
#         - SKILLUP (Ukraine), Software testing
#         - SKILLUP (Ukraine), Basic Web and SQL for software testing
#         - LG Internal practice