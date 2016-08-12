import codecs


count = 0
charDict = {}

f = codecs.open("wt2.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()

for char in doc:
	count += 1
	if char in charDict.keys():
		charDict[char] += 1
	else:
		charDict[char] = 1

	if not count%100000:
		print(count/1000000.0)

for char in [unichr(i) for i in range(3456,3583)]:
	if charDict[char]:
		del charDict[char]
	
print("WWWWWWWWWWWWWWWWWWWWWWWWWW")
print(count)
for i in range (len(charDict)):
	print(charDict.values()[i],charDict.keys()[i])

#f = codecs.open("wt2.txt", 'w', encoding='utf-8')
#f.write(line+"\n")
