fname = "mbox-short.txt"
fh = open(fname)

lst = list()
lsttem = list()
hourcount=dict()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') :
        continue
    words=line.split()
    #print(words[5])
    pieces=words[5].split(':')
    # add all hours into one list
    lst.append(pieces[0])

#store the hour and count in a dictionary
for hr in lst:
    hourcount[hr] = hourcount.get(hr,0) + 1

#print(sorted(hourcount.items())
#t=sorted(hourcount.items())

for k,v in sorted(hourcount.items()) :
    print(k,v)
#print (sorted ([(v,k) for k,v in hourcount.items()]))
#print(hourcount)
    #pos=words[5].find(':')
    #word=words[5][0:pos]
    #lst.append(words[1])
    #print(words[1])
#print(lst)
#print("There were", len(lst), "lines in the file with From as the first word")
