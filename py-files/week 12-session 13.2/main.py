import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor.()

c.execute('''CREATE TABLE "person" (
    "id"  INTEGER NOT NULL UNIQUE,
    "name" TEXT,
    "town" TEXT,
    PRIMARY KEY ("id" AUTOINCREMENT)

          )
);''')

