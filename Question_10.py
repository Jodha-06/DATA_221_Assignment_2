#Function to find lines containing a specific keyword
def find_lines_containing(filename,keyword):
    #List that stores matching lines
    listofMatchingLines = []

    #Open the file and read its contents
    with open(filename,"r",encoding="utf-8") as file:
        lineNumber = 1
        for line in file:
            #Check if keyword is in the line
            if keyword.lower() in line.lower():
                #Add line number and cleaned line text to the list
                listofMatchingLines.append((lineNumber,line.strip()))
            lineNumber += 1
    #Return list of matching lines
    return listofMatchingLines

# Test Case

results = find_lines_containing("sample-file.txt", "lorem")

print(f"Number of matching lines found: {len(results)}")

print("\nFirst 3 matching lines:")
for lineNumber, lineText in results[:3]:
    print(f"Line {lineNumber}: {lineText}")
