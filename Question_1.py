import string

#Open the text file and read its contents
sampleTextFile = open("sample-file.txt", "r")
fullTextFromFile = sampleTextFile.read()
sampleTextFile.close()

#Split the text into individual words
listOfAllTokens = fullTextFromFile.split()
# Store the tokens that are valid
listOfValidTokens = []

# Go through each word
for currentToken in listOfAllTokens:
    #Convert the word into lowercase
    lowercaseToken = currentToken.lower()
    #Remove any punctuation from the token
    tokenWithoutPunctuation = lowercaseToken.strip(string.punctuation)

    #Count how many letters each word has
    numberOfAlphabeticCharacters = 0
    for currentCharacter in tokenWithoutPunctuation:
        if currentCharacter.isalpha():
            numberOfAlphabeticCharacters += 1

    # Only keep the words that have more than 1 character
    if numberOfAlphabeticCharacters > 1:
        listOfValidTokens.append(tokenWithoutPunctuation)

dictionaryOfFrequencies = {}

for currentToken in listOfValidTokens:
    if currentToken in dictionaryOfFrequencies:
        dictionaryOfFrequencies[currentToken] += 1
    else:
        dictionaryOfFrequencies[currentToken] = 1

#Sort the frequencies in descending order
sortedWordFrequencyList = sorted(dictionaryOfFrequencies.items(), key=lambda item: item[1], reverse=True)

#Print the top 10 most frequent words in the file
for word,frequency in sortedWordFrequencyList[:10]:
    print(word, "-->", frequency)
