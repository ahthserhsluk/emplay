from bs4 import BeautifulSoup
def preprocess(soup):
    

    #Extracting the main div with class 'mw-parser-output' 
    main_content_div = soup.findAll(class_="mw-parser-output")[2]

    # Removing the right table of content - no need for summarization
    for table in main_content_div.find_all('table', class_=['infobox vcard','sidebar']):
        table.extract()

    # Removing all the Image and their caption
    for figImg in main_content_div.find_all('figure', attrs={'typeof':'mw:File/Thumb'}):
        figImg.extract()

    #Removing the tail content {see also, references, external links, etc.}

    pBeforeTail = main_content_div.find_all('p')[-2]

    for sibling in pBeforeTail.find_next_siblings():
        sibling.extract()

    # Removing all the superscripts 
    for sup in main_content_div.findAll('sup'):
        sup.extract()

    #Removing all the links
    for link in main_content_div.findAll('a'):
        link.replaceWithChildren()


    return main_content_div

