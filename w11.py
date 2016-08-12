#check for vowel doubles

import codecs
import sys

Xvowels = 	{	u'\u0d85' : ".a",
				u'\u0d86' : ".a",
				u'\u0d87' : ".a",#ah",
				u'\u0d88' : ".a",#Ah",
				u'\u0d89' : ".i",
				u'\u0d8a' : ".i",
				u'\u0d8b' : ".u",
				u'\u0d8c' : ".u",
				u'\u0d91' : ".e",
				u'\u0d92' : ".e",
				u'\u0d93' : ".x",
				u'\u0d94' : ".o",
				u'\u0d95' : ".o",
				u'\u0d96' : ".x",
				u'\u0d8d' : "s.ru",	#sru
				u'\u0d8e' : "s.ru",}

vowels = Xvowels.keys()

count = 0
errCount = 0
errorDict = {}
prevChar = ""

f = codecs.open("wt4.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()
AllWords = doc.count("\n")

f = codecs.open("vowel_doubles.txt", 'w', encoding='utf-8')

for word in doc.split():
	count += 1
	prevChar = ""
	for char in word:
		if char in vowels and prevChar in vowels :
			if char+prevChar in errorDict.keys():
				errorDict[char+prevChar] += 1
			else:
				errorDict[char+prevChar] = 1
			f.write(word+"\n")
			errCount += 1
		prevChar = char

	sys.stdout.write("<::>\r%d%%" %((count*100)/AllWords))
	sys.stdout.flush()

print("WWWWWWWWWWWWWWWWWWWWWWWWWW")
print(str(errCount)+" Errors")
for i in range (len(errorDict)):
	text = errorDict.values()[i],errorDict.keys()[i]
	print(text)
	f.write(str(text)+"\n")
