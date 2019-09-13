# reading and writing files

f = open("caractacus.txt","r")
text = f.read()
f.close()
#print(text)

text = "Hi guys" + text
print(text)

f1 = open("modified.txt","w")
f1.write(text)
f1.close()
