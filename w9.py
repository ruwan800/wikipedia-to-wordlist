#give naiboring character values to ZWJ and write them in errors_zwj.txt

import codecs
import sys

count = 0
errorDict = {}
prevChar = ""
veryPrevChar = ""

f = codecs.open("wt4.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()
AllWords = doc.count("\n")

f = codecs.open("errors_zwj.txt", 'w', encoding='utf-8')

for word in doc.split():
	count += 1
	prevChar = ""
	veryPrevChar = ""
	for char in word:
		if char == u'\u200d' and prevChar != u'\u0dca':
			if char+prevChar in errorDict.keys():
				errorDict[char+prevChar] += 1
			else:
				errorDict[char+prevChar] = 1
		elif prevChar == u'\u200d' and veryPrevChar != u'\u0dca':
			if prevChar+char in errorDict.keys():
				errorDict[prevChar+char] += 1
			else:
				errorDict[prevChar+char] = 1
		veryPrevChar = prevChar
		prevChar = char

	sys.stdout.write("<::>\r%d%%" %((count*100)/AllWords))
	sys.stdout.flush()

print("WWWWWWWWWWWWWWWWWWWWWWWWWW")
print(str(len(errorDict))+" Error couples")
for i in range (len(errorDict)):
	text = errorDict.values()[i],errorDict.keys()[i]
	print(text)
	f.write(str(text)+"\n")

for i in range (len(errorDict)):
	wordCount = 0
	print("                       ")
	f.write("\n")
	errVal = errorDict.keys()[i]
	print(errVal+str([errVal])+str(errorDict.values()[i]))
	f.write(errVal+str([errVal])+str(errorDict.values()[i])+"\n")
	f.write("~~~~~~~~~~~~~~~~~~~~~~~\n")
	for word in doc.split():
		if errVal in word:
			print(word)
			f.write(word+str([word])+"\n")
			wordCount += 1
			if 5 < wordCount:
				break
