####this create complexity factor for words
# coding=UTF-8

import codecs
import more



f = codecs.open("wt10.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()


words = doc.split()
count = 0
length = len(words)

CF1chars = ["K", "G", "C", "J", "T", "D", "N", "P", "B", "L", "S", "1", "I", "U", "E", "O", "X" ]
CF2chars = ["2" ]
CF3chars = ["3" ]

f = codecs.open("wt13.txt", 'w', encoding='utf-8')

for word in words:
	complexityFactor = 0
	for char in word[:8]:
		if char in CF1chars:
			complexity = 1
		elif char in CF2chars:
			complexity = 2
		elif char in CF3chars:
			complexity = 3
		else:
			complexity = 0
		if complexityFactor == 0:
			complexityFactor = complexity
		else:
			complexityFactor = (complexityFactor*4)+complexity

	f.write(str(complexityFactor)+"\n")

	count += 1
	more.notify("{:>3}% done.".format(count*100/length))


more.notify("Complexity factor list created.")

