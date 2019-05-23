import sqlite3

conn = sqlite3.connect('/Users/max/Develop/Coursera/maxdatabase.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = '/Users/max/Develop/Coursera/py4egit/Chapter F - Using Database with Python/mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    orgn2 = pieces[1].split('@')
    orgn=orgn2[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (orgn,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (orgn,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (orgn,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
