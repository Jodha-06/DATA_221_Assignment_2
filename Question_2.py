import string

sampleTextFile = open("sample-file.txt", "r")
fullTextFromFile = sampleTextFile.read()
sampleTextFile.close()

listOfAllTokens = fullTextFromFile.split()
listOfValidTokens = []

for currentToken in listOfAllTokens:
    lowercaseToken = currentToken.lower()
    tokenWithoutPunctuation = lowercaseToken.strip(string.punctuation)

    numberOfAlphabeticCharacters = 0
    for currentCharacter in tokenWithoutPunctuation:
        if currentCharacter.isalpha():
            numberOfAlphabeticCharacters += 1

    if numberOfAlphabeticCharacters > 1:
        listOfValidTokens.append(tokenWithoutPunctuation)

listofBigrams = []

for index in range(len(listOfValidTokens)-1):
    firstWord = listOfValidTokens[index]
    secondWord = listOfValidTokens[index+1]
    bigram = firstWord.lower() +" "+ secondWord.lower()
    listofBigrams.append(bigram)

dictionaryofBigramFrequencies = {}
for bigram in listofBigrams:
    if bigram in dictionaryofBigramFrequencies:
        dictionaryofBigramFrequencies[bigram] += 1
    else:
        dictionaryofBigramFrequencies[bigram] = 1

sortedBigramFrequency = sorted(dictionaryofBigramFrequencies.items(), key=lambda x: x[1], reverse=True)

for bigram, frequency in sortedBigramFrequency[:5]:
    print(bigram,"->",frequency)

