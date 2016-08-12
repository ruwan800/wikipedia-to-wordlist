#write wt2.txt from all words which cotains atleast one sinhala character
import codecs
import sys

count = 0
siCount = 0

f = codecs.open("wt1.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()

AllWords = doc.count("\n")

f = codecs.open("wt2.txt", 'w', encoding='utf-8')

for line in doc.split():
	count += 1
	for char in [unichr(i) for i in range(3456,3583)]:
		if char in line:
			siCount += 1
			f.write(line+"\n")
			break
	sys.stdout.write("::::|>>\r%d%%" %((count*100)/AllWords))
	sys.stdout.flush()

print("WWWWWWWWWWWWWWWWWWWWWWWWWW")
print(siCount)
print(count)
#
#
