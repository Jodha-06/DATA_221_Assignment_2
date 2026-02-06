import string

#Open the text file and read its contents
sampleTextFile = open("sample-file.txt", "r")
listofAllLinesinFile = sampleTextFile.readlines()
sampleTextFile.close()

#Dictionary to store normalized lines as keys
dictionaryofNormalizedLines = {}

# Go through each line in the file
lineNumber = 1
for originalLine in listofAllLinesinFile:
    #Convert the line into lowercase
    lowercaseLine = originalLine.lower()

    #Normalize the line
    normalizedLine = ""
    for character in lowercaseLine:
        if character.isalpha():
            normalizedLine += character

    #After Normalization, skip all lines that are empty
    if normalizedLine == "":
        lineNumber += 1
        continue

    #Add the line to the dictionary
    if normalizedLine in dictionaryofNormalizedLines:
        dictionaryofNormalizedLines[normalizedLine].append((lineNumber, originalLine.strip()))
    else:
        dictionaryofNormalizedLines[normalizedLine] = [(lineNumber, originalLine.strip())]

    lineNumber += 1

#List to store near-duplicate sets
listofNearDuplicateSets = []

#Find the normalized lines that appear more than once
for normalizedLine in dictionaryofNormalizedLines:
    if len(dictionaryofNormalizedLines[normalizedLine]) > 1:
        listofNearDuplicateSets.append(dictionaryofNormalizedLines[normalizedLine])

#Print the number of near duplicate sets in the file
print(f"Number of near-duplicate sets: {len(listofNearDuplicateSets)}\n")

#Print the first two near duplicate sets
for duplicateSets in listofNearDuplicateSets[:2]:
    for InfoaboutLine in duplicateSets:
        print(f"Line {InfoaboutLine[0]} : {InfoaboutLine[1]}\n")

