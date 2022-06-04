# This program will read in a text string
# Any :) text in the string will be converted to the Smiling Face Emoji
# Any :( text in the string will be converted to the Frowning Face Emoji
# use a funtion to convert the string

def main():
    inputString = getInput()
    newString = convert(inputString)
    printOutput(newString)

def getInput():
    inputString = input("Enter a string of characters: ")
    return inputString

def convert(string):
    newString = string.replace(":)", "🙂")
    newString = newString.replace(":(","🙁")
    return newString

def printOutput(printString):
    print(printString)

main()                
