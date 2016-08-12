# coding=UTF-8

#wrire wt9.txt form english letters replacing sinhala characters


import codecs
import more
import string


count = 0
length = 0
f = codecs.open("wt9.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()

siWords = doc
dummy = doc

#replacing ZWJ
doc = doc.replace(u'\u200d', "")
dummy = dummy.replace(u'\u200d', "")

length = len(more.vowels)
for key in more.vowels.keys():
	doc = doc.replace(key, more.vowels[key])
	dummy = dummy.replace(key,"")
	count += 1
	more.notify("replaceing vowels.{:>3}% done.".format(str(count*100/length)))

length = len(more.consonents)
count = 0
for key in more.consonents.keys():
	doc = doc.replace(key, more.consonents[key])
	dummy = dummy.replace(key,"")
	count += 1
	more.notify("replaceing consonents.{:>3}% done.".format(str(count*100/length)))

length = len(more.depVowels)
count = 0
for key in more.depVowels.keys():
	doc = doc.replace(key, more.depVowels[key])
	dummy = dummy.replace(key,"")
	count += 1
	more.notify("replaceing dependant vowels.{:>3}% done.".format(str(count*100/length)))

#check for character errors

dummy = dummy.replace("\n","")
dummy = dummy.replace("1","")
dummy = dummy.replace("2","")
dummy = dummy.replace("3","")
if dummy:
	errList = []
	for i in dummy:
		if i not in errList:
			errList.append(i)
			more.notify("{:>2} error characters found.".format(str(len(errList))))
	
	length = len(errList)
	count = 0
	for char in errList:
		doc = doc.replace(char, "")
		count += 1
		more.notify("Fixing character errors.{:>3}% done.".format(str(count*100/length)))
	while doc.count("\n\n"):
		doc = doc.replace("\n\n", "\n")

conCouples = [ x+y for x in more.enConsonents for y in more.enConsonents+"\n" ]
length = len(conCouples)
count = 0
for couple in conCouples:
	doc = doc.replace(couple, couple[0]+"a"+couple[1])
	count += 1
	more.notify("Modifying words. {:>3}% done.".format(str(count*100/length)))

doc = doc.replace("yi", "y.")
doc = doc.replace("vu", "v.")

vowCouples = [ x+y for x in more.enVowels+["1", "2", "3"] for y in more.enVowels +["1", "2", "3"] ]
length = len(vowCouples)
count = 0
errCount = 0
for couple in vowCouples:
	errCount += doc.count(couple)
	count += 1
	more.notify("Checking for errors. {:>3}% done.".format(str(count*100/length)))

count = 0
if errCount:
	more.notify("{:>7} errors found.....".format(errCount))
	f = codecs.open("errors_w22.txt", 'w', encoding='utf-8')
	siWords = siWords.split()
	words = doc.split()
	for i in range(len(words)):
		for couple in vowCouples:
			if couple in words[i]:
				f.write(siWords[i]+"\t\t\t\t"+words[i]+"\n")
				count += 1
				more.notify("Generating error report.{:>3}% done".format(count*100/errCount))
				break
	more.notify("Finished with{:>7} errors. See 'errors_w21.txt'.".format(errCount))
else:
	f = codecs.open("wt10.txt", 'w', encoding='utf-8')
	f.write(doc)
	more.notify("Done. wt10.txt has written.")


