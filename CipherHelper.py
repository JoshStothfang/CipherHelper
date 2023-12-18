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