f = open("iofile.txt","r")

f.seek(3)
print(f.tell())
content = f.read()
print(content)
f.close()