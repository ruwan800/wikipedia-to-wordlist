#wrire wt6.txt form distinct words and their frequencies

import codecs
import sys

wcount = 0
frequency = 0
wordCount = 0

f = codecs.open("wt4.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()
words = doc.split()#[:1000000]
words.sort()


f = codecs.open("wt5.txt", 'w', encoding='utf-8')


while wcount < len(words):
	frequency = words[wcount:wcount+1000].count(words[wcount])
	if frequency == 1000:
		frequency = words[wcount:wcount+10000].count(words[wcount])
		if frequency == 10000:
			frequency = words[wcount:wcount+100000].count(words[wcount])
			if frequency == 100000:
				frequency = words[wcount:].count(words[wcount])
	f.write("{:<8}".format(str(frequency))+words[wcount]+"\n")
	wcount = wcount + frequency
	wordCount += 1
	sys.stdout.write( \
		"\r{:>3}% ({:>7} words)completed.{:>7} distinct words found" \
		.format(str((wcount*100)/len(words)), str(wcount), str(wordCount)))
	sys.stdout.flush()


print("\n\nWWWWWWWWWWWWWWWWWWWWWWWWWW")
print(str(wordCount)+" distinct words found from "+str(wcount)+" words")
