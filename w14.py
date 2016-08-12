#wrire wt6.txt form distinct words and their frequencies

import codecs
import sys
import sqlite3

wordDict = {}
count = 0
wordCount = 0


f = codecs.open("wt4.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()
AllWords = doc.count("\n")

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("CREATE TABLE words (word text, freq int)")



for word in doc.split()[:10000]:
	count += 1
	c.execute("SELECT word FROM words WHERE word=?",[word])
	if c.fetchone():
		c.execute("UPDATE words SET freq = freq+1 WHERE word = ?",[word])
#		conn.commit()
	else:
		c.execute("INSERT INTO words (word,freq) values ( ?, ?)",[word,1])
#		conn.commit()
		wordCount += 1

	if not wordCount%1000:
		print(wordCount)
	sys.stdout.write(":::|>>\r%d%%" %((count*100)/AllWords))
	sys.stdout.flush()

f = codecs.open("wt5.txt", 'w', encoding='utf-8')

c.execute("SELECT * FROM words")
result = c.fetchall()
conn.close()

for item in result:
	text1 = "{:<8}".format(item[1])
	text2 = item[0]
	text = text1+text2
	f.write(text+"\n")

print("WWWWWWWWWWWWWWWWWWWWWWWWWW")
print(str(wordCount)+" distinct words found from "+str(count)+" words")
