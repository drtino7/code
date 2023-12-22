import sqlite3
import pandas

conn = sqlite3.connect("database.db")

square = lambda x: x * x

conn.create_function("square", 1, square)

cursor = conn.cursor()

execution = cursor.execute("SELECT * FROM user")

data = pandas.DataFrame(execution)

cursor.close()
conn.close()

#with sqlite3.connect("database.db") as conn:
#    cursor = conn.cursor()
#    execution = cursor.execute("SELECT * FROM user")
#    data = pandas.DataFrame(execution)

#pd.read_sql_query(query, conn)