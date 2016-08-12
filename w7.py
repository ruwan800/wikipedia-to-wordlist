#give odd characters when they occure twice or more times concecatively

import codecs
import sys

count = 0
totalErrCount = 0
errChar = ""
errorDict = {}

f = codecs.open("wt2.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()


for word in doc.split():
	count += 1
	errChar = ""
	errWord = False
	for char in word:
		if char not in [unichr(i) for i in range(3456,3583)]:
			errChar = char
			if errChar:
				if errChar+char in errorDict.keys():
					errorDict[errChar+char] += 1
				else:
					errorDict[errChar+char] = 1
				errChar = ""
				errWord = False
	sys.stdout.write("\r%d%%" %count)
	sys.stdout.flush()

print("WWWWWWWWWWWWWWWWWWWWWWWWWW")
print(str(len(errorDict))+" Error couples")
for i in range (len(errorDict)):
	print(errorDict.values()[i],errorDict.keys()[i])
