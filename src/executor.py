
file = open("function.stupid", 'r')

string = file.read().replace('\n', '')
point = 0
char = ''
lastChar = ''
numChar = 0
interpreted = ''
while point < len(string):
    char = string[point]
    if char != lastChar:
        interpreted = interpreted + chr(numChar+1)
        lastChar = char
        numChar = 0
    else:
        numChar = numChar + 1
    point = point + 1
interpreted = interpreted.replace(interpreted[0], '')

file.close()

print(interpreted)

exec(interpreted)
