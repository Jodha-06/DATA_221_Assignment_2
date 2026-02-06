import requests
from bs4 import BeautifulSoup

#Set a User-Agent so Wikipedia allows the request
headersInOrderToAccessWikipedia = {'User-Agent': 'Mozilla/5.0'}
#Download HTML content of the wikipedia page
retrieveHtmlPage = requests.get("https://en.wikipedia.org/wiki/Data_science",headers=headersInOrderToAccessWikipedia).text

soup = BeautifulSoup(retrieveHtmlPage, "html5lib")

#Find the main article content
contentDiv = soup.find("div", id="mw-content-text")

#list to store all valid section headings
listofHeadings = []

#Loop through every "h2" tag in the main content
for h2 in contentDiv.find_all("h2"):
    #Strip all whitespace from the text
    headingText = h2.get_text().strip()

    #Remove the "edit" text
    headingText = headingText.replace("[edit]","").strip()

    #list of headings that are not valid
    unwantedHeadings = ["References", "External links", "See also", "Notes"]
    skippedHeading = False

    for skip in unwantedHeadings:
        if skip in headingText:
            skippedHeading = True
            break
    if skippedHeading:
        continue

    listofHeadings.append(headingText)

#Save all valid headings to a new text file called "headings.txt"
with open("headings.txt","w",encoding="utf-8") as file:
    for heading in listofHeadings:
        file.write(heading+"\n")

for heading in listofHeadings:
    print(heading)

