import streamlit as st
from pdfparser.pdf_parser  import PdfParser


def create_skill_print():
    skills_text = ''
    for i in PdfParser().skills_from_pdf():
        if i != ' ':
            skills_text += f'\n - {i}'
    return skills_text

def skills():
    st.markdown(f'''
        ##### **SKILLS**:
        {create_skill_print()}
         \n ***''')

        # '''
        # ##### **SKILLS**:
        # - Good knowledge of software testing theory;
        # - Creating test documentation;
        # - Bug tracking systems tools : Jira; TestRail;
        # - Software development methodologies: Agile(Scrum, Kanban);
        # - Tools for performance and load testing: JMeter, locust;
        # - CI/CD: Docker, GitHubActions, Jenkins(user experience), Kubernetes, AWS(basic, user experience);
        # - API testing tools (Postman, Jmetr, Charles proxy, Swagger, Python request, Cypress API );
        # - Programing languages: Python, JS, SQL
        # - DataBase: Redshift, S3(minio), MySql
        # - OS: work with Linux, Windows 
        # - Automation tools: Python Selenium, Macrodroid(android), JS Cypress
        # - Web technologies: HTML, CSS, JS, Devtool;
        # - Version control system: github, gitlab
        # - Soft skills: communication, problem-solving creativity, adaptability;
        # - English **Intermediate**.
        # ***''')