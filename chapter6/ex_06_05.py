str = 'X-DSPAM-Confidence:0.8475'

pos= str.find(':')
leng = len(str)

charac= str[0:pos]
num =float(str[pos+1:leng])

print (charac,num)
