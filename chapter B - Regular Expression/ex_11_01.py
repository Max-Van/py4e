import re
#fh=open('regex_sum_42.txt')
fh=open('regex_sum_202314.txt')

sum=0

for line in fh:
    fl=re.findall('[0-9]+',line)
    if len(fl) != 0 :
        for item in fl :
            sum += int(item)

print(sum)
