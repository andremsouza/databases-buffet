import psycopg2
import getpass

# Tests connection and SQL command execution.


try:
	conn = psycopg2.connect("dbname = 'buffet' user = 'buffet' host = 'localhost' password = 'buffet01'")
except:
	print("I am unable to connect to the database.")
	exit(1)
cur = conn.cursor()
cur.execute("SELECT datname FROM pg_database")
rows = cur.fetchall()
print("\nShow me the databases:\n")
for row in rows:
	print("\t"+row[0])
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

cur.execute("INSERT INTO test (num, data) VALUES (%s, %s);", (100, "abc'def"))
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s);", (200, "abc'def"))

cur.execute("SELECT * FROM test;")
rows = cur.fetchall()
for row in rows:
	print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[2]))
cur.close()
conn.close()