#!/usr/bin/env python
# coding: utf-8

import os
import glob
import pandas as pd
import csv
from bs4 import BeautifulSoup as bs

# input the email list that the contacts will be imported into
email_list = input('Email list name: ')

# create a dataframe for the contacts
contact_df = pd.DataFrame(columns = ['Email List', 'Email Address', 'Name','Company', 'Job Title', 'Phone','Address', 'City', 'State'])
                          
# function for extracting text from <td>
def get_text(data):
    """Extract the text from the <td>"""
    try:
        result = data.text
        if result == '-':
            return chr(32)
        else:
            return result
    except:
        return chr(32)
    
# function for extracting 'input' class in <td>
# else pass to 'extract_text' function
def get_input(data):
    """Extract the text from the 'input' class"""
    try:
        result = data['title']
        if result == '-':
            return chr(32)
    except:
        result = get_text(data)
    return result

# a counter that will increment for each row
row_ct = 0

# Read HTML from file
for file_name in glob.glob(os.path.join('html_files', '*.html')):
    with open(file_name, encoding='utf-8') as file:
        html = file.read()

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(html, 'html.parser')
    
    texts = soup.find_all(text=True)
    for t in texts:
        newtext = t.replace(u'\xa0', '-')
        t.replace_with(newtext)

    # parse out two main sections
    contact_records = soup.find('div', id='htmlFixedColumns').find_all('tr', class_='GridCursorHand')
    address_records = soup.find('table', id='tblMainGrid').find_all('tr', class_='GridCursorHand')

    for i in range(len(contact_records)):
        
        contact_fields = contact_records[i].find_all('td')
        address_fields = address_records[i].find_all('td')
        recd = contact_fields + address_fields
        
        # get email address
        try:
            email = recd[1].a['onclick']
            email = email[4 : email.find(",") - 1]
        except:
            email = chr(32)
        
        # get other contact fields
        name = get_text(recd[2])
        company = get_input(recd[3])
        job_title = get_input(recd[4])
        phone = get_text(recd[5])
        address = get_text(recd[6])
        city = get_input(recd[7])
        state = get_text(recd[8])
        row_ct = row_ct + 1
        contact_df.loc[row_ct] = [email_list, email, name, company, job_title, phone, address, city, state]   

# export to csv
contact_df.to_csv('export.csv', encoding='utf-8', index=False)




