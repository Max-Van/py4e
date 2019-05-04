smallest_so_far = None
largest_so_far = None
while True:
    num =  input("Enter a number: ")
    if num == 'done':
        break
    try:
        numn=int(num)
    except Exception as e:
        print('Invalid input')
        continue
    if smallest_so_far == None :
        smallest_so_far = numn
    if largest_so_far == None :
        largest_so_far = numn
    if numn < smallest_so_far :
        smallest_so_far = numn
    if numn > largest_so_far :
        largest_so_far = numn

print('Maximum is' , largest_so_far)
print('Minimum is' , smallest_so_far)
