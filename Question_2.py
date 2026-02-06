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
    # Convert token to lowercase
    lowercaseToken = currentToken.lower()
    #Remove punctuation
    tokenWithoutPunctuation = lowercaseToken.strip(string.punctuation)

    # Count how many letters each word has
    numberOfAlphabeticCharacters = 0
    for currentCharacter in tokenWithoutPunctuation:
        if currentCharacter.isalpha():
            numberOfAlphabeticCharacters += 1

    # Only keep the words that have more than 1 character
    if numberOfAlphabeticCharacters > 1:
        listOfValidTokens.append(tokenWithoutPunctuation)

# Create a list to store bigrams
listofBigrams = []

#Build bigrams using consecutive words
for index in range(len(listOfValidTokens)-1):
    firstWord = listOfValidTokens[index]
    secondWord = listOfValidTokens[index+1]
    bigram = firstWord.lower() +" "+ secondWord.lower()
    listofBigrams.append(bigram)

#Dictionary containing bigram frequencies
dictionaryofBigramFrequencies = {}
#Count how often each bigram appears
for bigram in listofBigrams:
    if bigram in dictionaryofBigramFrequencies:
        dictionaryofBigramFrequencies[bigram] += 1
    else:
        dictionaryofBigramFrequencies[bigram] = 1

#Sort frequency from highest to lowest
sortedBigramFrequency = sorted(dictionaryofBigramFrequencies.items(), key=lambda x: x[1], reverse=True)

# Print the top 5 most frequent bigrams
for bigram, frequency in sortedBigramFrequency[:5]:
    print(bigram,"->",frequency)

