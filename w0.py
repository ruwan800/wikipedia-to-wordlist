import codecs

f = codecs.open("wiki.xml", 'r', encoding='utf-8')
doc = f.read()
f.close()
ourList = []
newLine = ""
count = 0
newCount = 0
lineCount = 0
for line in doc.split()[:100]:
	print(line)#################################
	lineCount += 1
	for word in line.split():
		print(word)#################################
		count+= 1
		if not count %100000:
			print(count)
		if word not in ourList:
			print(word)#################################
			ourList.append(word)
			newCount += 1
			
		
print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")########################
print(count)
print("WWWWW")########################
print(newCount)
print("WWWWW")########################
print(lineCount)

#f = open("src/temp4.txt", 'w')
#f.write(newLine)
