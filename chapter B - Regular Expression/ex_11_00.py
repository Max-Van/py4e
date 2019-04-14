import re

string='max@fanfan'

a=re.search('fan',string)

#print(a)

#  ^X.*:
fh=open('/Users/max/Develop/Coursera/py4egit/chapter7 - file/mbox-short.txt')

#for line in fh:
#    if re.search('^X.*:',line):
#        print(line)
#  ^X-\S+*:
for line in fh:
    if re.search('^X-\S+:',line):
        print(line)

str='max12 fan3 hello548'

fl=re.findall('[0-9]+',str)
print(fl)
