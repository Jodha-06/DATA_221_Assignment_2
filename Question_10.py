def find_lines_containing(filename,keyword):
    listofMatchingLines = []

    with open(filename,"r",encoding="utf-8") as file:
        lineNumber = 1
        for line in file:
            if keyword.lower() in line.lower():
                listofMatchingLines.append((lineNumber,line.strip()))
            lineNumber += 1
    return listofMatchingLines

# Test Case

results = find_lines_containing("sample-file.txt", "lorem")

print(f"Number of matching lines found: {len(results)}")

print("\nFirst 3 matching lines:")
for lineNumber, lineText in results[:3]:
    print(f"Line {lineNumber}: {lineText}")
