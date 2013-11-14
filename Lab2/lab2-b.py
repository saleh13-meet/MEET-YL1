pa = raw_input("Please enter a word: ")

l = len(pa)

text = []
text2 = []

for i in range(0, l):
    text.append(pa[i])

for i in range(0, l):
    text2.append(pa[l-i-1])

if text == text2:
    print True
else:
    print False
