import psycopg2
import getpass

# Basic search
# Searches a table 'tName' from connection 'coon' with given constraint(string).
# The constraint must be given as in the SQL language.
# 	(e.g.: NAME = 'Zé')
def searchTable(conn, tName, constraint):
	#Checking datatypes
	if(!isinstance(tName, str) or !isinstance(constraint, str)):
		raise TypeError("The function parameters have invalid types.")

	strout = []
	# Executing command
	try:
		cur = conn.cursor()
		cur.execute("""SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s';""", (tName.upper()))
		strout[1] = cur.fetchall()
		cur.execute("""SELECT * FROM %s WHERE %s;""", (tName.upper(), constraint.upper()))
		strout[2] = cur.fetchall()
		return strout
	except Exception as e:
		print("Unable to execute table search. Exception: " + str(e))
		return None


# Insert 'values' into a table 'tName' 'columns' from connection 'conn'
def insertTable(conn, tName, columns, values):
	# Checking datatypes
	if(!isinstance(tName, str) or !isinstance(columns, str) or !isinstance(values, list)):
		raise TypeError("The function parameters have invalid types.")
	for a in values:
		if(!isinstance(a, str)):
			raise TypeError("The function parameters have invalid types.")
	# Executing command
	try:
		cur = conn.cursor()
		for a in values:
			cur.execute("""INSERT INTO %s (%s) VALUES (%s);""", (tName, columns, a))
	except Exception as e:
		print("Unable to execute table insertion. Exception: " + str(e))

# Delete rows from table 'tName' from connection 'conn' using a 'constraint'
# The constraint must be given as in the SQL language.
# 	(e.g.: NAME = 'Zé')
def deleteTable(conn, tName, constraint):
	# Checking datatypes
	if(!isinstance(tName, str) or !isinstance(constraint, str)):
		raise TypeError("The function parameters have invalid types")
	try:
		cur = conn.cursor()
		cur.execute("""DELETE FROM $s WHERE %s;""", (tName, constraint))
	except Exception as e:
		print("Unable to execute table deletion. Exception: " + str(e))

# Update 'sets' from table 'tName' from connection 'conn' using a 'constraint'
# The constraint and sets must be given as in the SQL language.
# 	(constraint example: NAME = 'Zé' AND CPF = '001.112.223-45')
#	(sets example: NAME = 'Zé', CPF = '001.112.223-45')
def updateTable(conn, tName, sets, constraint):
	# Checking datatypes
	if(!isinstance(tName, str) or !isinstance(constraint, str) or !isinstance(set, str)):
		raise TypeError("The function parameters have invalid types")
	# Executing command
	try:
		cur = conn.cursor()
		cur.execute("""UPDATE $s SET $s WHERE $s;""", (tName, sets, constraint))
	except Exception as e:
		print("Unable to execute table update. Exception: " + str(e))

# Principais operações: Consultar quantas pessoas estão envolvidas em determinado evento;
# "Pessoas", neste contexto, são quaisquer tuplas da relação "Pessoa", conectadas de alguma maneira a um determinado evento (Cliente, Funcionário, ou especialista)