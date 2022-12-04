import streamlit as st
from pdfparser.pdf_parser import PdfParser, remove_whitespace_in_word

def experience_list_from_pdf():
    experience_list = ''
    for i in PdfParser().experience_from_pdf():
        if 'pr esent' in i['time_range']:
            present = remove_whitespace_in_word(i['time_range'], 'pr esent')
            experience_list += '###### '+ present  + '\n' +  ' - **Company:**' + i['company'] + '\n' + ' - **Position:**' + i['position'] + '\n' + ' - **Responsibilities:**' + i['responsibilities'] + '\n'
        else:
            experience_list += '###### '+  i['time_range'] + '\n' + ' - **Company:**' + i['company'] + '\n' + ' - **Position:**' + i['position'] + '\n' + ' - **Responsibilities:**' + i['responsibilities'] + '\n'

    return experience_list

def experience():
    st.markdown(f'''##### Experience: \n {experience_list_from_pdf()} \n ***''')

        # ##### Experience:
        # ###### August 2021 - present day
        # - **Company:** Suntech Innovation
        # - **Position:** QA Engineer
        # - **Responsibilities:** Testing web application, BI system(PowerBI); Big Data testing; Integration testing (3th party); Work with testrail, confluence, figma, Jira, Jenkins, Docker, database(redshift, MySQL); Create and support automation tests for three projects (python selenium, js cypress); Administration redshift(setting DMS and prepare data)

        # ###### February 2021 - October 2021
        # - **Company:** UTOR(Smoozly)
        # - **Position:** QA Engineer
        # - **Responsibilities:** Testing iOS mobile applications. Creating test documentations and setting up the testing process in a team. Communication (description of problems, questions) with tech support apphud, apple.  I had experience with testing purchases and testing with charles proxy.

        # ###### September 2020 – August 2021
        # - **Company:** Binotel
        # - **Position:** QA Engineer
        # - **Responsibilities:** Testing web-service and Android application. Creation tests and scripts. Work with Python selenium (e2e test). Setting up and working with TestRail. Created product test plans that were put in use by the QA team. Collaborated with  software development engineers to build a deep understanding of features and architecture prior to testing. Helping out with the training of new employees. Had experience work with AndroidStudio. Drafted testing reports, reducing data to key insights that helped increase team efficiency. 
        
        # ###### December 2020 – September 2020
        # - **Company:** Utest.com
        # - **Position:** QC Engineer.
        # - **Responsibilities:** Tested web services, single-page sites and mobile applications. I had experience with simple automation web test, API-test, Ad-hoc testing, localization testing, usability testing, UI testing, compatibility testing, system / end-to-end testing. 

        # ###### July 2018 – April 2020      
        # - **Company**: IE Ivashchuk                                                                                                            
        # - **Position**: Verifier Metrologist                                                                                          
        # - **Responsibilities**: Worked as an inspector for testing water meters, recording inspection results into software and also on to paper records, ensuring that all items dispatched conform to the company’s procedures and customer specifications;

        # ###### January 2018 – May 2018 
        # - **Company:** LG
        # - **Position:** QC Engineer.
        # - **Responsibilities:** International practice in company LG Electronics Mlawa. I did quality control in the production of TVs. Worked with technical documentation (formal testing), functional testing, UI testing, localization testing. Found defects and reported them.
        # ***