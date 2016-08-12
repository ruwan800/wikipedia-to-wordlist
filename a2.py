####8 char strings availability



f = open("wt12.txt", 'r')
doc = f.read()
f.close()

#f = open("r2.txt", 'w')
#f.write("{:<10}{:<10}{:<10}{:<10}\n".format("Length","Count","Disctincts","Possibilities"))


words = doc.split()
count = 0
wordList1   = []
wordList2   = []


for word in words:
	if len(word)==8:
		count += 1
		if word[:4] not in wordList1 :
			wordList1.append(word)
		if word[4:] not in wordList2 :
			wordList2.append(word)

print("{:<10}{:<10}{:<10}{:<10}\n".format(str(count),str(len(wordList1)),str(len(wordList2)),str(6**8)))

#	f.write("{:<10}{:<10}{:<10}{:<10}\n".format(str(i),str(count),str(len(wordList)),str(6**i)))
	
#	count    = 0
#	wordList = []

#f.close()

