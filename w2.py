##make every errors into linefeeds and create proper wordlist

import codecs

f = codecs.open("wt0.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()

count = 0
for char in [ " "*(2**x) for x in range(10,0,-1)]:
	print("replacing "+str(len(char))+" spaces "+str(doc.count(char))+" times")
	doc = doc.replace(char," ")
doc = doc.replace("  "," ")
#while(True):
#	doc = doc.replace("  "," ")
#	count += 1
#	print(count)
#	if not doc.count("  "):
#		break
oddChars= [	" ",		#space
			"\n\t",		#line feed
			u'\u2191',	#UPWARDS ARROW
			u'\u2192',	#RIGHTWARDS ARROW
			u'\u2018',	#LEFT SINGLE QUOTATION MARK
			u'\u201c',	#LEFT DOUBLE QUOTATION MARK
			u'\u2019',	#RIGHT SINGLE QUOTATION MARK
			u'\u201d',	#RIGHT DOUBLE QUOTATION MARK
			u'\u2013',	#EN DASH
			u'\u2014',	#EM DASH
			u'\u02dd',	#DOUBLE ACUTE ACCENT
			u'\u2022',	#BULLET
			u'\u0ea9',	#SINGLE LOW-9 QUOTATION MARK
			u'\u0ef5',	#DOUBLE ACUTE ACCENT
		  ]


for strs in oddChars:
	doc = doc.replace(strs,"\n")

for char in [ "\n"*(2**x) for x in range(10,0,-1)]:
	print("replacing "+str(len(char))+" lineFeeds "+str(doc.count(char))+" times")
	doc = doc.replace(char,"\n")
doc = doc.replace("\n\n","\n")

f = codecs.open("wt1.txt", 'w', encoding='utf-8')
if doc[0] == "\n":
	doc = doc[1:]
f.write(doc)
