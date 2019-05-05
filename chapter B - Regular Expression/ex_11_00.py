import re

string='max@fanfan'

a=re.search('fan',string)

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

#x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#y = re.findall('\S+?@\S+', x)
#print(y)


x = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
y = re.findall('http://.*', x)
print(y)
