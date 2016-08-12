#write wt3.txt from all words which does not cotains any invalid and error character
import codecs
import sys

count = 0
errCount = 0
errFlag = False

charList =	[u'\u0d82',u'\u0d83']+\
			[unichr(i) for i in range(3461,3479)]+\
			[unichr(i) for i in range(3492,3506)]+\
			[unichr(i) for i in range(3507,3516)]+\
			[u'\u0dbd']+\
			[unichr(i) for i in range(3520,3527)]+\
			[u'\u0dca']+\
			[unichr(i) for i in range(3535,3541)]+\
			[u'\u0dd6']+\
			[unichr(i) for i in range(3544,3552)]+\
			[unichr(i) for i in range(3570,3573)]+\
			[u'\u200d']



f = codecs.open("wt2.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()

f = codecs.open("wt3.txt", 'w', encoding='utf-8')

totalWords = doc.count('\n')

for word in doc.split():
	count += 1
	errFlag = False
	for char in word:
		if char not in charList:
			errFlag = True
			errCount += 1
			break
	if not errFlag:
		f.write(word+"\n")
	sys.stdout.write("::::|>>  \r%d%%" %((count*100)/totalWords))
	sys.stdout.flush()



print("WWWWWWWWWWWWWWWWWWWWWWWWWW")
print("Total No: of words: "+str(count))
print("Words with errors : "+str(errCount))
#
#
