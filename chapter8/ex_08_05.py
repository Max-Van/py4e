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

#print(lst)
print("There were", len(lst), "lines in the file with From as the first word")
