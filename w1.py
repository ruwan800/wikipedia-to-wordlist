import codecs
import string

f = codecs.open("wiki.xml", 'r', encoding='utf-8')
doc = f.read()
f.close()

count = 0
for char in string.ascii_letters:
	print("replacing "+str(char)+" "+str(doc.count(char))+" times")
	doc = doc.replace(char," ")
count = 0
for char in string.digits:
	print("replacing "+str(char)+" "+str(doc.count(char))+" times")
	doc = doc.replace(char," ")
count = 0
for char in string.punctuation:
	print("replacing '"+str(char)+"' "+str(doc.count(char))+" times")
	doc = doc.replace(char," ")


f = codecs.open("wt0.txt", 'w', encoding='utf-8')
f.write(doc)
