####disctinct char combinations of words different lengths



f = open("wt12.txt", 'r')
doc = f.read()
f.close()

f = open("r1.txt", 'w')
f.write("{:<10}{:<10}{:<10}{:<10}\n".format("Length","Count","Disctincts","Possibilities"))


words = doc.split()
count = 0
wordList   = []



for i in range(1,11):
	for word in words:
		if len(word)==i :
			count += 1
			if word not in wordList :
				wordList.append(word)

	f.write("{:<10}{:<10}{:<10}{:<10}\n".format(str(i),str(count),str(len(wordList)),str(6**i)))
	
	count    = 0
	wordList = []

f.close()

