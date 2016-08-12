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
words = doc.split()[:200000]
allWords = len(words)

f = codecs.open("wt5.txt", 'w', encoding='utf-8')

for i in range(allWords):
	count += 1
	if words[i]:
		wordCount += 1
		childCount = 0
		frequency = 1
		for j in range(i+1,allWords):
			childCount += 1
			if words[j]:
				if words[i] == words[j]:
					frequency += 1
					words[j] = None
		
					sys.stdout.write("\r{:>3}% ({:>7} words)completed. Child process{:>3}% completed.{:>7} distinct words found".format(str((count*100)/allWords), str(count), str((childCount*100)/allWords), str(wordCount)))
					sys.stdout.flush()
		
		f.write("{:<8}".format(str(frequency))+words[i]+"\n")

#	if not wordCount%1000:
#		print(wordCount)


#	sys.stdout.write(str(((count*100)/allWords))+"% complete. "+str(((childCount*100)/allWords)) + '\n')
#	sys.stdout.write(":::|>>\r%d%%" %((count*100)/allWords))


print("\n\nWWWWWWWWWWWWWWWWWWWWWWWWWW")
print(str(wordCount)+" distinct words found from "+str(count)+" words")
