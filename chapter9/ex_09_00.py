fname = "mbox-short.txt"
fh = open(fname)

lst = list()
lsttem = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    words=line.split()
    lst.append(words[1])
    print(words[1])


print("There were", len(lst), "lines in the file with From as the first word")
print("print line 1")
print("print line 2")
