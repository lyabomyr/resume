
from config import pdf_file_patch, PdfStructure

import re
from PyPDF2 import PdfReader

def remove_whitespace_in_word(text, word):
    return text.replace(word, ''.join(word.split()))
    
class PdfParser:
    def __init__(self) -> None:
        self.title = {}
        self.experience = []
        self.education = []
        self.courses= [] 
        self.text= ''
        self.skills = []

    def read_pdf(self):
        reader = PdfReader(pdf_file_patch)
        for page in reader.pages:
            self.text += page.extract_text()
        return(self.text.replace("\n", " "))

    def title_from_pdf(self):
        title_start = PdfStructure.start_lastname
        title_end = 'SKILLS:'
        result = re.search('%s(.*)%s' % (title_start, title_end), self.read_pdf()).group(1)
        self.title['role'] = re.search('((.*)Engineer)', result).group(1).replace('(','')
        self.title['location'] = re.search('Location:(.*)Phone', result).group(1)
        self.title['phone'] = re.search('Phone:(.*) Email', result).group(1)
        self.title['email'] = re.search('Email:(.*) Skype', result).group(1)
        self.title['skype'] = re.search('Skype:(.*) Linkedin', result).group(1)
        self.title['linkedin'] = re.search('Linkedin:(.*) SUMMAR Y:', result).group(1).replace(' ','')
        self.title['summary'] = re.search('SUMMAR Y:(.*)', result).group(1)
        return(self.title)

    def skills_from_pdf(self):
        title_start = PdfStructure.skills
        title_end = PdfStructure.experience
        self.skills = re.search('%s(.*)%s' % (title_start, title_end), self.read_pdf()).group(1).split('●')
        return self.skills

    def experience_from_pdf(self):
        title_start = PdfStructure.experience
        title_end = PdfStructure.education
        experience_row_list = list(filter(None,re.search('%s(.*)%s' % (title_start, title_end), self.read_pdf()).group(1).split(';')))
        for i in experience_row_list:
            dcexperience= {}
            dcexperience['time_range']= i.split('●')[0]
            dcexperience['company'] = re.search('Company:(.*)', i.split('●')[1]).group(1)
            dcexperience['position'] = re.search('Position:(.*)', i.split('●')[2]).group(1)
            dcexperience['responsibilities'] = re.search('Responsibilities:(.*)', i.split('●')[3]).group(1)
            self.experience.append(dcexperience)
        return(self.experience)


    def education_from_pdf(self):
        title_start = PdfStructure.education
        title_end = PdfStructure.courses
        education_row_list = list(filter(None,re.search('%s(.*)%s' % (title_start, title_end), self.read_pdf()).group(1).split('●')))
        for univer in education_row_list:
            if univer != ' ':
                educt_dict = {}
                educt_dict['time_range_title'] = re.search('((.*)degree.)', univer).group(1)
                educt_dict['univer_description'] = re.search('degree.(.*)', univer).group(1)
                self.education.append(educt_dict)
        return(self.education)

    def courses_from_pdf(self):
        title_start = 'COURSES :'
        self.courses = re.search('%s(.*)' % (title_start), self.read_pdf()).group(1).split('●')
        return(self.courses)