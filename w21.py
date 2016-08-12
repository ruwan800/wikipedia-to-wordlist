#wrire wt9.txt by removing vowel doubles


import codecs
import more

vowels1 =	[unichr(i) for i in range(3461,3479)]

vowels2 =	[u'\u0d82',u'\u0d83']

vowels3 =	[u'\u0dca']+\
			[unichr(i) for i in range(3535,3541)]+\
			[u'\u0dd6']+\
			[unichr(i) for i in range(3544,3552)]+\
			[unichr(i) for i in range(3570,3573)]

vowels = vowels1 + vowels2 +vowels3

vowelDoubles = [ x+y for x in vowels1+vowels2+vowels3 for y in vowels3 ]

count = 0
errCount = 0
errorDict = {}
prevChar = ""
errFlag = False

f = codecs.open("wt8.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()
AllWords = doc.count("\n")

f = codecs.open("wt9.txt", 'w', encoding='utf-8')
g = codecs.open("errors_w21.txt", 'w', encoding='utf-8')

for word in doc.split():
	count += 1
	errFlag = False
	for double in vowelDoubles:
		if double in word:
			errFlag = True
			break
	
	if word[0] in vowels2+vowels3:
		errFlag = True
	
	if not errFlag :
		f.write(word+"\n")
	else:
		g.write(word+"\n")
		errCount += 1

	more.notify("{:>3}% done".format((count*100)/AllWords))

print("\nWWWWWWWWWWWWWWWWWWWWWWWWWW")
print(str(errCount)+" Errors")
