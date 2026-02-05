import requests
from bs4 import BeautifulSoup
import csv

headersInOrderToAccessWikipedia = {"User-Agent": "Mozilla/5.0"}
retrieveHtmlPage = requests.get("https://en.wikipedia.org/wiki/Machine_learning",headers=headersInOrderToAccessWikipedia).text
soup = BeautifulSoup(retrieveHtmlPage, "html5lib")

mainContentDiv = soup.find("div", id="mw-content-text")
allTables = mainContentDiv.find_all("table")

selectedTable = None

for table in allTables:
    tableRows = table.find_all("tr")
    if len(tableRows) >= 4:
        selectedTable = table
        break

if selectedTable is None:
    print("No suitable table found.")
    exit()

allRows = selectedTable.find_all("tr")

listofTableData = []

for row in allRows:
    cells = row.find_all(["th", "td"])
    rowValues = []

    for cell in cells:
        rowValues.append(cell.get_text().strip())

    if rowValues:
        listofTableData.append(rowValues)

headerRow = listofTableData[0]
dataRows = listofTableData[1:]

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

maxNumberOfColumns = len(headers)

for row in dataRows:
    while len(row) < maxNumberOfColumns:
        row.append("")
    while len(row) > maxNumberOfColumns:
        row.pop()

with open("wiki_table.csv", "w", newline="", encoding="utf-8") as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(headers)

    for row in dataRows:
        csvWriter.writerow(row)
