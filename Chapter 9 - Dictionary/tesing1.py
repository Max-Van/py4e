
names = ['max','tom','max','jim','fan','tom','jackson','max','jack','fan']

namecount=dict()

for name in names:
    namecount[name] = namecount.get(name,0) + 1
print(namecount)

print(namecount.keys())
print(type(namecount.keys()))

print(namecount.values())
print(type(namecount.values()))

print(namecount.items())
print(type(namecount.items()))

#print(namecount.value())
#print(namecount.item())
