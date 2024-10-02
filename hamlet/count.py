hamlet = open('hamlet.txt', 'r')

num_spaces = 0
num_chars = 0
word_set = set()
for line in hamlet:
    words = line.split()
    num_spaces += len(words)
    for word in words:
        word_set.add(word)
        num_chars += len(word)

print(num_chars + num_spaces)
print(len(word_set))