# coding=UTF-8

import string

consonents = {	u'\u0d85' : ".",		#අ 
				u'\u0d9a' : "k",		#ක 
				u'\u0d9b' : "K",		#ඛ 
				u'\u0d9c' : "g",		#ග 
				u'\u0d9d' : "G",		#ඝ 
				u'\u0d9f' : "G",#00g,	#ඟ 
				u'\u0da0' : "c",		#ච 
				u'\u0da1' : "C",		#ඡ 
				u'\u0da2' : "j",		#ජ 
				u'\u0da3' : "J",		#ඣ 
				u'\u0da4' : "N",#g0n",	#ඤ 
				u'\u0da5' : "N",#g0n",	#ඥ  
				u'\u0da6' : "J",#00j",	#ඦ 
				u'\u0da7' : "T",		#ට 
				u'\u0da8' : "T",		#ඨ 
				u'\u0da9' : "d",		#ඩ 
				u'\u0daa' : "D",		#ඪ 
				u'\u0dab' : "N",		#ණ 
				u'\u0dac' : "D",#00D",	#ඬ 
				u'\u0dad' : "t",#th",	#ත 
				u'\u0dae' : "T",#Th",	#ථ 
				u'\u0daf' : "d",#da",	#ද 
				u'\u0db0' : "D",#Da",	#ධ 
				u'\u0db1' : "n",		#න 
				u'\u0db3' : "D",#00da",	#ඳ 
				u'\u0db4' : "p",		#ප 
				u'\u0db5' : "P",		#ඵ 
				u'\u0db6' : "b",		#බ
				u'\u0db7' : "B",		#භ 
				u'\u0db8' : "m",		#ම 
				u'\u0db9' : "B",#00b",	#ඹ 
				u'\u0dba' : "y",		#ය 
				u'\u0dbb' : "r",		#ර 
				u'\u0dc5' : "L",		#ළ 
				u'\u0dc0' : "v",		#ව 
				u'\u0dc3' : "s",		#ස 
				u'\u0dc1' : "S",#sh",	#ශ 
				u'\u0dc2' : "S",#SH",	#ෂ 
				u'\u0dc4' : "h",		#හ 
				u'\u0dbd' : "l",		#ල 
				u'\u0dc6' : "P"	}		#ෆ 

vowels 	= 	{	u'\u0d85' : ".a",		#අ 
				u'\u0d86' : ".1",		#ආ 
				u'\u0d87' : ".2",#ah",	#ඇ 
				u'\u0d88' : ".3",#Ah",	#ඈ 
				u'\u0d89' : ".i",		#ඉ 
				u'\u0d8a' : ".I",		#ඊ 
				u'\u0d8b' : ".u",		#උ 
				u'\u0d8c' : ".U",		#ඌ 
				u'\u0d8f' : ".ilu",		#ඏ
				u'\u0d90' : ".ilU",		#ඐ
				u'\u0d91' : ".e",		#එ 
				u'\u0d92' : ".E",		#ඒ 
				u'\u0d93' : ".ay.",		#ඓ 
				u'\u0d94' : ".o",		#ඔ 
				u'\u0d95' : ".O",		#ඕ 
				u'\u0d96' : ".av.",		#ඖ 
				u'\u0d8d' : "s.ru",	#sru#ඍ 
				u'\u0d8e' : "s.rU",}	#ඎ 

depVowels = {	u'\u0dca' : ".",		#ක් 
				u'\u0dcf' : "1",		#කා
				u'\u0dd0' : "2",#ah",	#කැ 
				u'\u0dd1' : "3",#Ah",	#කෑ 
				u'\u0dd2' : "i",		#කි
				u'\u0dd3' : "I",		#කී 
				u'\u0dd4' : "u",		#කු 
				u'\u0dd6' : "U",		#කූ 
				u'\u0dd9' : "e",		#කෙ 
				u'\u0dda' : "E",		#කේ 
				u'\u0ddb' : "ay.",		#කෛ 
				u'\u0ddc' : "o",		#කො 
				u'\u0ddd' : "O",		#කෝ 
				u'\u0dde' : "av.",		#කෞ 
				u'\u0dd8' : ".ru",		#කෘ 
				u'\u0df2' : ".rU",		#කෲ
				u'\u0d82' : "n.",		#කං
				u'\u0d83' : "h."}		#කඃ

enVowels = [ "a", "e", "i", "o", "u", "A", "E", "I", "O", "U" ]


enConsonentsTmp = string.ascii_letters
for char in enVowels:
	enConsonentsTmp = enConsonentsTmp.replace(char,"")

enConsonents = enConsonentsTmp
