import sys

input = sys.argv[1]

#Valid ASCII codes
spaceCode = 32
uppercaseCodes = range(65, 91)
lowercaseCodes = range(97, 123)

#Combine ASCII code into one list
codes = list()
codes.append(spaceCode)
codes.extend(uppercaseCodes)
codes.extend(lowercaseCodes)

#Parse input
for char in input:
    if ord(char) not in codes:
        print("Input can only contain letters and spaces. Please try again.")
        exit()

parsedInput = input.upper()

print(parsedInput)

#Print possible solutions
for i in range(1,26):
    output = ""
    for char in parsedInput:
        if ord(char) == 32:
            output += char
        else:
            newChrCode = ord(char) + i
            if newChrCode > 90:
                newChrCode -= 26
            output += chr(newChrCode)
    
    print(output)
