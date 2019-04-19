import re

#fh=open('testfile.txt')

#for line in fh:
#    y=re.findall('[aeiou]+',line)
#    print(y)

str='fanfan: 12.2312.46.1212.131  '

#y=re.findall('([^ ]*)@',str)
y=re.findall('[0-9.]+',str)
print(y)
#print(a)

#  ^X.*:
#fh=open('/Users/max/Develop/Coursera/py4egit/chapter7 - file/mbox-short.txt')

#for line in fh:
#    if re.search('^X.*:',line):
#        print(line)
#  ^X-\S+*:
#for line in fh:
#    if re.search('^X-\S+:',line):
#        print(line)
