filehandle=open("mbox-short.txt")
wordslist = list()
count = 0
for line in filehandle :
    if line.startswith('From: ') :
        words = line.split()
        print(words[1])
        count += 1
print(count)
