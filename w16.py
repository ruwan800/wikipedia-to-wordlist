#wrire wt6.txt form distinct words and their frequencies

import codecs
import sys

wordDict = {}
count = 0
frequency = 0
wordCount = 0
childCount = 0

f = codecs.open("wt4.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()
words = doc.split()[:10000]
allWords = len(words)

f = codecs.open("wt5.txt", 'w', encoding='utf-8')

i = 0
while len(words):
	
	count += 1
	wordCount += 1
	childCount = 0
	frequency = 1
	j = 1
	while j < len(words):
		childCount += 1
		if words[0] == words[j]:
			frequency += 1
			count += 1
			del words[j]
		else:
			j += 1
			
		sys.stdout.write("\r{:>3}% ({:>7} words)completed. Child process{:>3}% completed".format( \
					str((count*100)/allWords), str(count), str((childCount*100)/allWords)))
		sys.stdout.flush()
			
	f.write("{:<8}".format(str(frequency))+words[0]+"\n")
	del words[0]



print("\n\nWWWWWWWWWWWWWWWWWWWWWWWWWW")
print(str(wordCount)+" distinct words found from "+str(count)+" words")
