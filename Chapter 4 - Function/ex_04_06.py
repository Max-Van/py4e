def computepay(h,r):
    if h <=40:
         sal = h * r
    elif h> 40:
        sal = 40 * r + ( h - 40 ) * r * 1.5
    return sal

hs=input('Enter Hours:')
h=float(hs)
rs=input('Enter Rates:')
r=float(rs)
mysal=computepay(h,r)
print('Pay:', mysal)
