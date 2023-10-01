import requests
from bs4 import BeautifulSoup
from helper.printer import print_text, print_html
url = 'https://en.wikipedia.org/wiki/Alexander_the_Great'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

first_p = soup.find('p')
parent = first_p.parent

# Remove siblings before first <p>
for element in parent.contents[:parent.contents.index(first_p)]:
    element.extract() 

print_html(str(soup),file='trash.html')