import codecs
import more

#seperating consonents

f = codecs.open("wt10.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()

count = 0
length = doc.count("\n")

doc = doc.lower()

f = open("wt11.txt", 'w')

for word in doc.split():

	f.write("".join([ word[i] for i in range(0,len(word),2) ]+["\n"]))
	count += 1
	more.notify("{:>3}% done.".format(count*100/length))

more.notify("Consonent list created.")
