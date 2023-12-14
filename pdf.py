#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:35:19 2021

@author: meryemecedal
"""

import re
import fitz
import nltk
import PyPDF2
import linecache
from nltk.tokenize import word_tokenize
from nameparser.parser import HumanName

#PDF READING PART
fname = 'CV-eng.pdf'
doc = fitz.open(fname)
resume1 = ""
for page in doc:
    resume1 = resume1 + str(page.getText())
#print(resume1)
    

#GETTING EMAIL PART
def get_email(resume1):
    email = ''
    pattern = re.search(r'[\w\.-]+@[\w\.-]+', resume1)
    if pattern is None:
        print('Email address cannot be found.')
    else:
        email = pattern.group(0)
        print(email)
print('\nEmail:')
get_email(resume1)          
    

#GETTING PHONE NUMBER PART
def get_phone(resume1):
    phone = ''
    pattern = re.search(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', resume1)
    if pattern is None:
        print('Phone info cannot be found.')
    else:
        phone = pattern.group(0)
        print(phone)
print('\nPhone:')
get_phone(resume1)          
    

#GETTING LINKEDIN LINK PART
def get_linkedin(resume1):
    linkedin = ''
    pattern = re.search('(?:(?:www?|ftp):\/\/)?[\w/\-?=%.]+linkedin+\.[\w/\-&?=%.]+', resume1)
    if pattern is None:
        print('LinkedIn link cannot be found.')
    else:
        linkedin = pattern.group(0)
        print(linkedin)
print('\nLinkedIn:')
get_linkedin(resume1) 


#GETTING EDUCATION INFO
def get_edu(resume1):
    edu = ''
    pattern = re.search('university', resume1, re.IGNORECASE)
    if pattern is None:
        print('Education info cannot be found.')
    else:
        edu = pattern.group(0)
        print(edu)
print('\nEducation:')
get_edu(resume1)

print(len(resume1))

for i in range():
    a = ''
    a = a + str(linecache.getline(resume1, i))
    print(a)





