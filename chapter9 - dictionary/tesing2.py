
nameemail=dict()

nameemail['maxfan']='maxffq@max.com'
nameemail['jimli']='jimli@jim.com'
nameemail['tomzhang']='tomzhang@tom.com'
nameemail['candyliu']='candykiu@candy.com'

print("******Access with default(key)******")
for name in nameemail:
    print(name,nameemail[name])
print("******Access with default(key)******")

print("")

print("******Access with keys******")
for name2 in nameemail.keys():
    print(name2,nameemail[name2])
print("******Access with keys******")

print("")

print("******Access with values******")
for name3 in nameemail.values():
    print(name3)
print("******Access with values******")

print("")
print("******Access with key-values******")
for name4,email in nameemail.items():
    print(name4,email)
print("******Access with key-values******")
