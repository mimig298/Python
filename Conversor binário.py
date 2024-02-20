from random import randint
from math import log2, floor, ceil

decDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
binDigits = ["0", "1"]

# Function that creates a random binary number with maxLen digits
def createBin(maxLen):
    bin = ""
    for x in range(randint(1, maxLen)):
        bin += binDigits[randint(0, len(binDigits)-1)]
    bin = "0"*(maxLen-len(bin)) + bin
    return bin

# Function that creates all decimal numbers from 0 to maxNum
def createDecs(maxNum):
    decs = []
    for x in range(maxNum):
        decs.append(x)
    return decs

# Function that converts a binary number to decimal
def convertToDec(number):
    number = str(number)
    decNumber = 0
    for x in range(len(number)):
        decNumber += int(number[len(number)-1-x])*(2**x)
    return decNumber

# Function that converts a decimal number to binary
def convertToBin(number):
    number = int(number)
    binNumber = []
    if number == 0:
        return "0"
    for x in range(floor(log2(number))+1):
        binNumber.append("0")
    while number > 0:
        pow2 = floor(log2(number))
        binNumber[len(binNumber)-1-pow2] = "1"
        number -= 2**pow2
    binFinal = ""
    for x in binNumber:
        binFinal = binFinal + x
    return binFinal

# Debug function
def debugCode(maxVal):
    print("\nPreparing to debug...")
    decs = createDecs(maxVal)
    # Convert the decimal numbers to binary
    print("\nConverting to binary...")
    bins = []
    progress = 0
    progressMarks = 1
    for number in decs:
        bins.append(convertToBin(number))
        progress += 1
        if progress / len(decs) * 100 >= progressMarks:
            print("(" + str(progressMarks*1) + "% done)")
            progressMarks += 1
    # Say the conversions it did (uncomment the lines to activate; it slows the program down A LOT)
    #for x in range(len(bins)):
        #print(decs[x], "is", bins[x], "in binary!")
    # Convert the binary numbers back to decimal
    print("\nConverting to decimal...")
    decs2 = []
    progress = 0
    progressMarks = 1
    for number in bins:
        decs2.append(convertToDec(number))
        progress += 1
        if progress / len(decs) * 100 >= progressMarks:
            print("(" + str(progressMarks*1) + "% done)")
            progressMarks += 1
    # Say the conversions it did (uncomment the lines to activate; it slows the program down A LOT)
    #for x in range(len(decs)):
        #print(bins[x], "is", decs2[x], "in decimal!")
    # Auto-debug by checking for discrepancies in the conversions
    errors = 0
    for x in range(len(decs2)):
        if decs2[x] != decs[x]:
            errors += 1
            print("There was an error in the conversion!\n" + str(decs[x]) + " was converted to " + str(bins[x]) + ", but when converted back, resulted in " + str(decs2[x]) + "!")
    if errors == 0:
        print("\nNo errors were found!")
    else:
        print("\nA total of", errors, "were found!")

while True:
    print("Insert a number followed by the letter 'b' or 'd' to specify if it is decimal or binary.\nExamples: 1000101b   420d")
    answr = input("\n>>> ")
    if answr[0:5] == "debug":
        debugCode(int(answr[5:]))
    elif answr[len(answr)-1] == "b":
        print(convertToDec(answr[:len(answr)-1]))
    elif answr[len(answr)-1] == "d":
        print(convertToBin(int(answr[:len(answr)-1])))
    input()
