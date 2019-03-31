fname = "romeo.txt"
fh = open(fname)
lst = list()
lsttem = list()
for line in fh:
    lsttemp = line.split()
    for lsttempitem in lsttemp :
        if lsttempitem not in lst :
            lst.append(lsttempitem)
lst.sort()
print(lst)
