import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

def print_db_contents(cursor):
    result = cursor.execute ( ''' SELECT * FROM person''')
    print("---------------")
    for row in result:
        print(row)
    print("--------------------\n")

c.execute('''
    INSERT INTO person (name, town) VALUES ('Annie', 'Rathmines');
''')
print_db_contents(c)
conn.commit()
conn.close()