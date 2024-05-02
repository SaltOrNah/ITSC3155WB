import pandas as pd
from repositories import builds_repo
import requests 
from bs4 import BeautifulSoup 

  
# for holding the resultant list 
element_list = [] 
from lxml import html 
import requests 

case_db = pd.read_csv("parts\Case.csv")

#'motherboard', 'cpu', 'storage', 'power', 'graphics', 'cooling', 'memory', 'casing'
from lxml import html 
import requests 
  
# Parse the HTML content using lxml 

  
# Extract specific elements from the HTML tree using XPath 
# For example, let's extract the titles of all the links on the page 

  
# Print the extracted link titles 


for pc_case in case_db.itertuples():
    for item in pc_case:
        print(item)

    # Making a GET request 
    r = requests.get(f'{pc_case[4]}') 
    tree = html.fromstring(r.content) 
    link_titles = tree.xpath('finalPrice/') 
    for title in link_titles: 
        print(type(title)) 


    soup = BeautifulSoup(r.content, 'html.parser') 
    #print(soup.prettify()) 
    s = soup.find('div', class_='finalPrice') 
    print(type(s))
    #content = s.find_all('p')
    #builds_repo.create_part(pc_case[2], 'casing', pc_case[3], pc_case[4], 'N/A', ,4.7)
    break