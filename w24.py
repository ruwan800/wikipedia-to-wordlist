import codecs
import more

#seperating vowels

f = codecs.open("wt10.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()

count = 0
length = doc.count("\n")

doc = doc.lower()
doc = doc.replace("1","a")
doc = doc.replace("2","a")
doc = doc.replace("3","a")


f = open("wt12.txt", 'w')

for word in doc.split():

	f.write("".join([ word[i] for i in range(1,len(word),2) ]+["\n"]))
	count += 1
	more.notify("{:>3}% done.".format(count*100/length))

more.notify("vowel list created.")

