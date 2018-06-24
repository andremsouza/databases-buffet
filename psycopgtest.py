# -*- coding: utf-8 -*-
import psycopg2
import getpass
from dbCommands import *

# Tests connection and SQL command execution.

passwd = getpass.getpass() # Get a password ('buffet01')

# Connecting to database
try:
	conn = psycopg2.connect("dbname = 'buffet' user = 'buffet' host = 'localhost' password = '"+passwd+"'")
except Exception as e:
	print("I am unable to connect to the database. Exception: " + str(e))
	exit(1)

stri = searchPessoa(conn, True)
print(stri[0])
for row in stri[1]:
	print(row)
# Creating cursor and executing commands
#cur = conn.cursor()
#cur.execute("SELECT datname FROM pg_database")

# Printing query result
#rows = cur.fetchall()
#print("\nShow me the databases:\n")
#for row in rows:
#	print("\t"+row[0])

# Another SQL test
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
#cur.execute("INSERT INTO test (num, data) VALUES (%s, %s);", (100, "abc'def"))
#cur.execute("INSERT INTO test (num, data) VALUES (%s, %s);", (200, "abc'def"))

#cur.execute("SELECT * FROM test;")
#rows = cur.fetchall()
#for row in rows:
#	print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[2]))





#Closing cursor and connection
#cur.close()
conn.close()
