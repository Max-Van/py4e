a= [1,2,3,4,5]

b=[4,2,7,8]

c=a+b

newlist = list()

for i in c:
  if i not in newlist:
    newlist.append(i)

print(newlist)

string1 = 'Dr. Max FENG QI FAN'

words=string1.split()

fan=words[0] + words[len(words)-1]
fan1 = words[0] + words[-1]

fan2=string1[0:3] + string1[len(string1)-3: len(string1)]
fan3=string1[0:3] + string1[-3: -1]+string1[-1]



print(fan1)
