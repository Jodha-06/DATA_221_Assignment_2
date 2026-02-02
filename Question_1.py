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

dictionaryOfFrequencies = {}

for currentToken in listOfValidTokens:
    if currentToken in dictionaryOfFrequencies:
        dictionaryOfFrequencies[currentToken] += 1
    else:
        dictionaryOfFrequencies[currentToken] = 1

sortedWordFrequencyList = sorted(dictionaryOfFrequencies.items(), key=lambda item: item[1], reverse=True)

for word,frequency in sortedWordFrequencyList[:10]:
    print(word, "-->", frequency)
