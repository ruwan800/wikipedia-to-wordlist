import codecs

f = codecs.open("wt2.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()

count = 0
errorWords = []

ignoreChars	= [ 
						]


replaceChars= [	" ",		#space
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
				u'\u2022',	##BULLET
				
						]
				
#replaceChars= {	u'\u02db' : u'\u0dd4',	#OGONEK by SINHALA VOWEL SIGN KETTI PAA-PILLA
#				u'\u0ee7' : ""
#						}

#errorChars = [	u'\u0e83',	#invalid
#				u'\u0e8b',	#invalid
#				u'\x8f',	#unknown
#				u'\u20ac',	#EURO SIGN
#				u'\uf020',	#invalid
#				u'\u0224',	#LATIN CAPITAL LETTER Z WITH HOOK
#				u'\uf0a7',	#invalid
#				u'\u03a9',	#GREEK CAPITAL LETTER OMEGA
#				u'\xab',	#unknown
#				u'\u200c'	#ZERO WIDTH NON-JOINER
#				#Han Character 'very, too, much; big; extreme'				
#						]



errChar = u'\u02dd'


for word in doc.split():
	count += 1
	if errChar in word:
		print(":: "+str(count)+" ::")
		errorWords.append(word)
		print(word)

print("EEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")


#f = codecs.open("wt1.txt", 'w', encoding='utf-8')
#f.write(doc[1:])
