import streamlit as st

def title():
    col1, col2 = st.columns([9,3])
    with col1:
        st.title('Luibomyr Kachko')
        st.markdown('''##### Role: *QA engineer*''')

        st.markdown('''
                    ##### CONTACTS:
                    - **Location**: Kyiv
                    - **Phone:** +38(066)621-95-72
                    - **Email:** <lyabomyr@gmail.com>
                    - **Skype:** lyabomyr
                    - **Linkedin:** <https://www.linkedin.com/in/luibomyrkachko2473611a5/>
                    ***''')
    with col2:
        st.image('src/lkphoto.jpg', width=200)
    st.markdown('''
    ##### SUMMARY
    Results-oriented quality assurance tester with 3+ years expertise in  application development life cycles. Independently set up testing in the company, which helped improve the product and helped reduce the burden on customer support. Get position of general QA  that can improve my knowledge and help make product better
    ***
    ''')