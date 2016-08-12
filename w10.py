#purify ZWJ errors and write wt4.txt
import codecs
import sys

f = codecs.open("wt3.txt", 'r', encoding='utf-8')
doc = f.read()
f.close()

doc = doc.replace(u'\u0dca\u200d\u0dbb', u'\u0dcaA\u0dbb')
doc = doc.replace(u'\u0dca\u200d\u0dba', u'\u0dcaA\u0dba')
doc = doc.replace(u'\u0d9a\u0dca\u200d\u0dc2', u'\u0d9a\u0dcaA\u0dc2')
doc = doc.replace(u'\u200d', "")
doc = doc.replace(u'A', u'\u200d')

f = codecs.open("wt4.txt", 'w', encoding='utf-8')
f.write(doc)

print("Removing wrong occurences of ZWJ: DONE")
