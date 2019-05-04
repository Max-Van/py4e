hs=input('Enter Hours:')
try:
    h=float(hs)
except Exception as e:
    print('Invalid Hour, Please input digits')
    quit()

rs=input('Enter Rates:')
try:
    r=float(rs)
except Exception as e:
    print('Invalid Rate, Please input digits')
    quit()

if h <=40:
    sal = h * r
elif h > 40:
    sal = 40 * r + ( h - 40 ) * r * 1.5
print('Pay:', sal)
