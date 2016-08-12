

import codecs
import sys

count = 0
totalErrCount = 0
errWord = False
errorList = []

f = codecs.open("wt2.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()

f = codecs.open("wt3.txt", 'w', encoding='utf-8')

for word in doc.split()[:10000]:
	count += 1
	errCount = 0
	errWord = False
	for char in word:
		if char not in [unichr(i) for i in range(3456,3583)]:
			errCount += 1
			if 1 < errCount:
				errWord = True
				totalErrCount += 1
				break
		else:
			errCount = 0
	if errWord:
		errorList.append(word)
	else:
		pass
#		f.write(word+"\n")
	print("  "+str(count)+" words done. "+str(totalErrCount)+" errors found\n")
for item in errorList:
	print(item)
