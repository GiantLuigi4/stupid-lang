
file = open("function.py", 'r')

string = file.read()
point = 0
charNum = ord('A')
lastCharNum = ord('A')
unInterpreted = ''
charAmt = 0
while point < len(string):
    char = string[point]
    point = point + 1
    charAmt = ord(char)
    num = 0
    while num < charAmt:
        unInterpreted = unInterpreted + chr(charNum)
        num = num + 1
    lastCharNum = charNum
    charNum = charNum + 1
    if lastCharNum != charNum:
        unInterpreted = unInterpreted + '\n'
    if charNum > ord('z'):
        charNum = ord('A')

print(unInterpreted)

file2 = open("function.stupid", 'w')
file2.write(unInterpreted)
file2.close()
file.close()
