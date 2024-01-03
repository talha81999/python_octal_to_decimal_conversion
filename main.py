# Octal number
octalNumber = input("Enter Octal Value: ")
octalNumber = octalNumber.replace('0o', '')

power = 0
newList = []
for i in range(len(octalNumber) - 1, -1, -1):
    temp = 8 ** power
    newTemp = int(octalNumber[i]) * temp
    newList.insert(0,  newTemp)
    power += 1

decimalValue = sum(newList)
print("Octal value: ", octalNumber, "\n", "Decimal value: ", decimalValue)
