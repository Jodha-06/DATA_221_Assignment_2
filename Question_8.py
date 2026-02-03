import requests
from bs4 import BeautifulSoup

headersInOrderToAccessWikipedia = {'User-Agent': 'Mozilla/5.0'}
retrieveHtmlPage = requests.get("https://en.wikipedia.org/wiki/Data_science",headers=headersInOrderToAccessWikipedia).text

soup = BeautifulSoup(retrieveHtmlPage, "html5lib")

contentDiv = soup.find("div", id="mw-content-text")

listofHeadings = []

for h2 in contentDiv.find_all("h2"):
    headingText = h2.get_text().strip()

    headingText = headingText.replace("[edit]","").strip()

    unwantedHeadings = ["References", "External links", "See also", "Notes"]
    skippedHeading = False

    for skip in unwantedHeadings:
        if skip in headingText:
            skippedHeading = True
            break
    if skippedHeading:
        continue

    listofHeadings.append(headingText)

with open("headings.txt","w",encoding="utf-8") as file:
    for heading in listofHeadings:
        file.write(heading+"\n")

for heading in listofHeadings:
    print(heading)

