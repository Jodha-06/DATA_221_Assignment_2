import requests
from bs4 import BeautifulSoup

headersInOrderToAccessWikipedia = {'User-Agent': 'Mozilla/5.0'}
retrieveHtmlPage = requests.get("https://en.wikipedia.org/wiki/Data_science",headers=headersInOrderToAccessWikipedia).text
soup = BeautifulSoup(retrieveHtmlPage, "html5lib")

pageTitle = soup.title.text
print(pageTitle)

contentDiv = soup.find("div", id="mw-content-text")
paragraphs = contentDiv.find_all("p")

for paragraph in paragraphs:
    paragraphText = paragraph.text.strip()
    if len(paragraphText) >= 50:
        print(paragraphText)
        break
