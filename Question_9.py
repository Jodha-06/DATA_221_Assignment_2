import requests
from bs4 import BeautifulSoup
import csv
#Set a User-Agent so Wikipedia allows the request
headersInOrderToAccessWikipedia = {"User-Agent": "Mozilla/5.0"}
#Download HTML content of the wikipedia page
retrieveHtmlPage = requests.get("https://en.wikipedia.org/wiki/Machine_learning",headers=headersInOrderToAccessWikipedia).text
soup = BeautifulSoup(retrieveHtmlPage, "html5lib")

#Find the main article content
mainContentDiv = soup.find("div", id="mw-content-text")
#Find all tables in the main content
allTables = mainContentDiv.find_all("table")

selectedTable = None

#Choose first table with at least 3 data rows
for table in allTables:
    dataRows = table.find_all("tr")
    numberOfDataRows = 0

    for row in dataRows:
        if row.find_all("td"):
            numberOfDataRows += 1

    if numberOfDataRows >= 3:
        selectedTable = table
        break

#Stop if no table is found and output a message
if selectedTable is None:
    print("No suitable table found.")
    exit()

allRows = selectedTable.find_all("tr")

#list of table data
listofTableData = []

for row in allRows:
    cells = row.find_all(["th", "td"])
    rowValues = []

    for cell in cells:
        rowValues.append(cell.get_text().strip())

    if rowValues:
        listofTableData.append(rowValues)

#Decide table headers
headerRow = listofTableData[0]
dataRows = listofTableData[1:]

#Check if the headers exist
headersExist = True
for header in headerRow:
    if header == "":
        headersExist = False
        break

if headersExist:
    headers = headerRow
else:
    headers = []
    for i in range(len(headerRow)):
        headers.append(f"col{i + 1}")

#Make sure thta all rows have the same number of columns
maxNumberOfColumns = len(headers)

for row in dataRows:
    while len(row) < maxNumberOfColumns:
        row.append("")
    while len(row) > maxNumberOfColumns:
        row.pop()

#Save all data to a new file named "wiki_table.csv"
with open("wiki_table.csv", "w", newline="", encoding="utf-8") as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(headers)

    for row in dataRows:
        csvWriter.writerow(row)
