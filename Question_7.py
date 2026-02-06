import requests
from bs4 import BeautifulSoup

#Set a User-Agent so Wikipedia allows the request
headersInOrderToAccessWikipedia = {'User-Agent': 'Mozilla/5.0'}
#Download HTML content of the wikipedia page
retrieveHtmlPage = requests.get("https://en.wikipedia.org/wiki/Data_science",headers=headersInOrderToAccessWikipedia).text
soup = BeautifulSoup(retrieveHtmlPage, "html5lib")

#Extract and print the page title
pageTitle = soup.title.text
print(pageTitle)

#Find main content area of the article
contentDiv = soup.find("div", id="mw-content-text")
#Find all paragraph tags inside the main content area
paragraphs = contentDiv.find_all("p")

#Loop through each paragraph
for paragraph in paragraphs:
    #Remove all whitespace from paragraph text
    paragraphText = paragraph.text.strip()
    #Check if paragraph has at least 50 characters
    if len(paragraphText) >= 50:
        #Print the first paragraph that has at least 50 characters
        print(paragraphText)
        break
