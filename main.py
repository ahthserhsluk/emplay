import requests
from bs4 import BeautifulSoup
from helper.printer import print_text, print_html
from helper.preprocess import preprocess

url = 'https://en.wikipedia.org/wiki/Alexander_the_Great'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title=soup.find(id="firstHeading").text



# Extracting the main content after preprocessing
main_content_div = preprocess(soup)


#summarizing 
l=''
for p in main_content_div.find_all('p'):
    l+=p.text
print_text(l)

# Print the HTML after making changes
# print_html(str(main_content_div),title=title)