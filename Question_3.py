import string

sampleTextFile = open("sample-file.txt", "r")
listofAllLinesinFile = sampleTextFile.readlines()
sampleTextFile.close()

dictionaryofNormalizedLines = {}

lineNumber = 1
for originalLine in listofAllLinesinFile:
    lowercaseLine = originalLine.lower()

    normalizedLine = ""
    for character in lowercaseLine:
        if character.isalpha():
            normalizedLine += character

    if normalizedLine == "":
        lineNumber += 1
        continue

    if normalizedLine in dictionaryofNormalizedLines:
        dictionaryofNormalizedLines[normalizedLine].append((lineNumber, originalLine.strip()))
    else:
        dictionaryofNormalizedLines[normalizedLine] = [(lineNumber, originalLine.strip())]

    lineNumber += 1

listofNearDuplicateSets = []

for normalizedLine in dictionaryofNormalizedLines:
    if len(dictionaryofNormalizedLines[normalizedLine]) > 1:
        listofNearDuplicateSets.append(dictionaryofNormalizedLines[normalizedLine])

print(f"Number of near-duplicate sets: {len(listofNearDuplicateSets)}")
print()

for duplicateSets in listofNearDuplicateSets[:2]:
    for InfoaboutLine in duplicateSets:
        print(f"Line {InfoaboutLine[0]} : {InfoaboutLine[1]}")
    print()
