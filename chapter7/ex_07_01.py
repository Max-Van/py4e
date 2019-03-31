# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
accum=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos=line.find('.')
    num=float(line[pos-1:len(line)])
    accum=accum+num
    count=count+1
print("Average spam confidence:",accum/count)
