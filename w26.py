#####this will insert data into mysql-db

#orig:m25.py

import codecs
import sqlite3
import more

conn = sqlite3.connect("vadan.sqlite")
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS vadan")
c.execute("CREATE TABLE vadan (word TEXT, con TEXT, vow TEXT, CF INT, frequency INT)")


# coding: utf-8
newLine = []
SQL = "INSERT INTO vadan (word,con,vow,CF,frequency) VALUES (?,?,?,?,?) "
count = 0
ourDict = {}

f = codecs.open("wt9.txt", 'r', encoding='utf-8')
wordLine = f.read()
f.close()

f = open("wt11.txt", 'r')
conLine = f.read()
f.close()

f = open("wt12.txt", 'r')
vowLine = f.read()
f.close()

f = open("wt13.txt", 'r')
CFLine = f.read()
f.close()

words = wordLine.split()
cons = conLine.split()
vows = vowLine.split()
CFs = CFLine.split()

length = len(words)
for i in range(len(words)):
	word = words[i]
	con = cons[i]
	vow = vows[i]
	CF = CFs[i]
	newLine.append( (word, con, vow, CF, 0 ) )
	
	if 1000 < len(newLine):
		c.executemany(SQL,newLine)
		newLine = []
	
	count += 1
	more.notify("{:>3}% done.".format(count*100/length))

if len(newLine):
	c.executemany(SQL,newLine)

conn.commit()
c.close()

more.notify("Inserting data into 'vadan.sqlite' finished.")

