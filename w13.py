#wrire wt6.txt form distinct words and their frequencies

import codecs
import sys

wordDict = {}
count = 0
wordCount = 0

f = codecs.open("wt4.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()
AllWords = doc.count("\n")


for word in doc.split()[:100000]:
	count += 1
	if word in wordDict.keys():
		wordDict[word] += 1
	else:
		wordDict[word] = 1
		wordCount += 1

	if not wordCount%1000:
		print(wordCount)
	sys.stdout.write(":::|>>\r%d%%" %((count*100)/AllWords))
	sys.stdout.flush()

f = codecs.open("wt5.txt", 'w', encoding='utf-8')

for i in range(len(wordDict)):
	text1 = "{:<12}".format(wordDict.values()[i])
	text2 = wordDict.keys()[i]
	text = text1+text2
	f.write(text+"\n")

print("WWWWWWWWWWWWWWWWWWWWWWWWWW")
