import mysql.connector as mc

mydb = mc.connect(
    host='localhost',
    user='max',
    password='Max13579',
    db='maxschema'
)
mycursor =mydb.cursor()
#print(mycursor)

mycursor.execute('select * from Course')

for i in mycursor:
    print(i)
