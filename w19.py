#wrire wt8.txt form distinct words and their frequencies using wt6.txt and ucsc.txt

import codecs
import sys
import sqlite3

wcount = 0
frequency = 0
wordCount = 0
wordList = []

f = codecs.open("wt4.txt", 'r', encoding='utf-8')
doc1 = f.read()
f.close()

f = codecs.open("ucsc.txt", 'r', encoding='utf-8')
doc2 = f.read()
f.close()

doc = doc1+"\n"+doc2

words = doc.split()#[:1000000]
words.sort()

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("CREATE TABLE words (word text, freq int)")


while wcount < len(words):
	frequency = words[wcount:wcount+1000].count(words[wcount])
	if frequency == 1000:
		frequency = words[wcount:wcount+10000].count(words[wcount])
		if frequency == 10000:
			frequency = words[wcount:wcount+100000].count(words[wcount])
			if frequency == 100000:
				frequency = words[wcount:].count(words[wcount])

	wordList.append((words[wcount], frequency))
	if 1000 < len(wordList):
		c.executemany("INSERT INTO words (word,freq) values ( ?, ?)",wordList)
		wordList = []

	wcount = wcount + frequency
	wordCount += 1
	sys.stdout.write( \
		"\r{:>3}% ({:>7} words)completed.{:>7} distinct words found" \
		.format(str((wcount*100)/len(words)), str(wcount), str(wordCount)))
	sys.stdout.flush()


if wordList:
	c.executemany("INSERT INTO words (word,freq) values ( ?, ?)",wordList)

conn.commit()
c.execute("SELECT freq,word FROM words ORDER BY freq DESC")
results = c.fetchall()

f = codecs.open("wt7.txt", 'w', encoding='utf-8')

for result in results:
	f.write("{:<8}".format(str(result[0]))+result[1]+"\n")

print("\n\nWWWWWWWWWWWWWWWWWWWWWWWWWW")
print(str(wordCount)+" distinct words found from "+str(wcount)+" words")
