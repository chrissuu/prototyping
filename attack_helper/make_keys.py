validChars = ['A', 'B', 'C', 'D', 'E', 'F']
validNums = [str(i) for i in range(10)]

keyChars = validChars + validNums

import random

randomKey = ""
for i in range(144):
    randomKey += random.choice(keyChars)

print(randomKey)


