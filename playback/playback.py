#This program prompts the user to enter a string
#The program then replaces all the spaces in the string with three dots eg ...

def main():
    #spaces = "Enter a string of text: "
    spaces = input("Enter a string of text: ")
    print("Replacing spaces \" \" with ... yeilds: ", end= "\n" )
    print(spaces.replace(" ", "..."))


main()    