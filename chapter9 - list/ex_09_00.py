
#dictionary practice

#dictionary : count name

names = ['max','tom','max','jim','fan','tom','jackson','max','jack','fan']

counts = dict()
counts2 = dict()

#method 1
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] += 1
#method 2
for name2 in names :
    counts2[name2] = counts2.get(name2,0) +1

#access the item in the dictionary with key
for count in counts2 :
    print(count,counts2[count])



#get which name appears most
