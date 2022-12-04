import streamlit as st
from config import photo_patch
from pdfparser.pdf_parser import PdfParser

def title():
    col1, col2 = st.columns([9,3])
    with col1:
        st.title('Luibomyr Kachko')
        st.markdown(f'''##### Role: *{PdfParser().title_from_pdf()['role'].strip()}*''')
        st.markdown(f'''
                    ##### CONTACTS:
                    - **Location**: {PdfParser().title_from_pdf()['location']}
                    - **Phone:** {PdfParser().title_from_pdf()['phone']}
                    - **Email:** <{PdfParser().title_from_pdf()['email']}>
                    - **Skype:** {PdfParser().title_from_pdf()['skype']}
                    - **Linkedin:** <{PdfParser().title_from_pdf()['linkedin']}>
                    ***''')
            
            # '''
            #         ##### CONTACTS:
            #         - **Location**: Kyiv
            #         - **Phone:** +38(066)621-95-72
            #         - **Email:** <lyabomyr@gmail.com>
            #         - **Skype:** lyabomyr
            #         - **Linkedin:** <https://www.linkedin.com/in/luibomyrkachko2473611a5/>
            #         ***'''

    with col2:
        st.image(photo_patch, width=200)
    st.markdown(f'''
    ##### SUMMARY:
    {PdfParser().title_from_pdf()['summary']}
    ***
    ''')