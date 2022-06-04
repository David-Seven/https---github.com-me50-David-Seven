# einstein.py

# This program will prompt the user to enter the mass as an integer in kilograms
# The program then prints out the Energy E in joules as an integer.
#
# Assume the user will input integer values

def main():
    kgs = getInput()
    printOutput(kgs)

def getInput():
    print("Enter an integer value for the mass")
    mass = int(input("Mass in kg: "))
    return mass

def printOutput(m):
    c = 3 * 10**8       #The speed of light is 3x10^8 m/s
    Energy = m * c ** 2
    print("The Energy is ", Energy, " joules.")

main()