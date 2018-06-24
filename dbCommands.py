import psycopg2
import getpass

# Basic search in table "Pessoa"
# Returns column names in strout[0], and query results in strout[1]
# Similar structure for each function
def searchPessoa(conn):
	try:
		strout = [] # Output
		cur = conn.cursor() # Connection cursor. For sgbd command execution
		cur.execute("""SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE UPPER(TABLE_NAME) = 'PESSOA';""") # SGBD command
		strout.append(cur.fetchall()) # Output column names
		cur.execute("""SELECT * FROM PESSOA ORDER BY NOME;""")
		strout.append(cur.fetchall()) # Output rows
		return strout
	except Exception as e:
		#print("Unable to execute table search. Exception: " + str(e))
		raise e

# All informations of all persons in the system, except for phone numbers
def searchPessoaAll(conn):
	try:
		strout = []
		cur = conn.cursor()
		strout.append([('CPF', ), ('NOME', ), ('ENDERECO', ), ('SALARIO', ), ('FUNCAO', ), ('ESPECIALIDADE', ), ('TAXA_HORA', )])
		cur.execute("""
			SELECT P.CPF, P.NOME, P.EMAIL, P.ENDERECO, F.SALARIO, F.FUNCAO, E.ESPECIALIDADE, E.TAXA_HORA FROM PESSOA P
				LEFT JOIN FUNCIONARIO F ON P.CPF = F.CPF
				LEFT JOIN ESPECIALISTA E ON P.CPF = E.CPF
				ORDER BY P.NOME;
				""")
		strout.append(cur.fetchall())
		return strout
	except Exception as e:
		#print("Unable to execute table search. Exception: " + str(e))
		raise e

# Basic search for phone numbers
def searchPhone(conn):
	try:
		strout = []
		cur.conn.cursor()
		strout.append([('CPF', ), ('NOME', ), ('TELEFONE', )])
		cur.execute("""
			SELECT P.CPF, P.NOME, T.TELEFONE FROM TELEFONES T
				INNER JOIN PESSOA P ON T.PESSOA = P.CPF
				ORDER BY P.NOME;
			""")
		strout.append(cur.fetchall())
		return strout
	except Exception as e:
		#print("Unable to execute table search. Exception: " + str(e))
		raise e

def insertCliente(conn, client):
	try:
		cur = conn.cursor()
		cur.execute("""
			INSERT INTO PESSOA (CPF, NOME, EMAIL, ENDERECO) VALUES (%s, %s, %s, %s);
			""", (client['cpf'], client['name'], cliente['email'], cliente['address']))
		cur.execute("""
			INSERT INTO CLIENTE (CPF) VALUES (%s);
			""", (client['cpf'], ))
		conn.commit()
	except Exception as e:
		#print("Unable to execute table insertion. Exception: " + str(e))
		raise e

def insertFuncionario(conn, employee):
	try:
		cur = conn.cursor()

		# Checando consistência
		cur.execute("""SELECT * FROM ESPECIALISTA WHERE CPF = %s;""", (employee['cpf'], ))
		if(len(cur.fetchall()) != 0):
			raise ValueError("O funcionário não pode ser um especialista.")

		# Inserindo tupla
		cur.execute("""
			INSERT INTO PESSOA (CPF, NOME, EMAIL, ENDERECO) VALUES (%s, %s, %s, %s);
			""", (employee['cpf'], employee['name'], employee['email'], employee['address']))
		cur.execute("""
			INSERT INTO FUNCIONARIO (CPF, SALARIO, FUNCAO) VALUES (%s, %s, %s);
			""", (employee['cpf'], employee['salary'], employee['function']))
		conn.commit()
	except Exception as e:
		#print("Unable to execute table insertion. Exception: " + str(e))
		raise e	

def insertEspecialista(conn, specialist):
	try:
		cur = conn.cursor()

		#Checando consistência
		cur.execute("""SELECT * FROM FUNCIONARIO WHERE CPF = %s;""", (specialist['cpf'], ))
		if(len(cur.fetchall()) != 0):
			raise ValueError("O especialista não pode ser um funcionário.")

		# Inserindo tupla
		cur.execute("""
			INSERT INTO PESSOA (CPF, NOME, EMAIL, ENDERECO) VALUES (%s, %s, %s, %s);
			""", (specialist['cpf'], specialist['name'], specialist['email'], specialist['address']))
		cur.execute("""
			INSERT INTO ESPECIALISTA (CPF, ESPECIALIDADE, TAXA_HORA) VALUES (%s, %s, %s);
			""", (specialist['specialty'], specialist['hourFee']))
		conn.commit()
	except Exception as e:
		#print("Unable to execute table insertion. Exception: " + str(e))
		raise e

# graduation = {'client' : None, 'date' : None, 'value' : None, 'paymentMethod' : None, 'peopleNumber' : None, 'bartender' : None, 'cupbearer' : None, 'hall' : None}
def insertFormatura(conn, graduation):
	try:
		cur = conn.cursor()
		cur.execute("""
			INSERT INTO EVENTO (CLIENTE, DATAHORA, CATEGORIA, VALOR, METODOPAGAMENTO, NROPESSOAS)
				VALUES (%s, %s, %s, %s, %s, %s);
			""", (graduation['client'], graduation['date'], "FORMATURA", graduation['value'], graduation['paymentMethod'], graduation['peopleNumber']))
		cur.execute("""
			INSERT INTO FORMATURA (CLIENTE, DATAHORA, BARTENDER, COPEIRO, SALAO) VALUES (%s, %s, %s, %s, %s)
			""", (graduation['client'], graduation['date'], graduation['bartender'], graduation['cupbearer'], graduation['hall']))
		conn.commit()
	except Exception as e:
		#print("Unable to execute table insertion. Exception: " + str(e))
		raise e

# Não é possível alterar a chave da tabela, nem a categoria do evento
def updateFormatura(conn, graduation):
	try:
		cur = conn.cursor()
		cur.execute("""
			UPDATE EVENTO E SET E.VALOR = %s, E.METODOPAGAMENTO = %s, E.NROPESSOAS = %s
				WHERE E.CLIENTE = %s AND E.DATAHORA = %s
			""", (graduation['value'], graduation['paymentMethod'], graduation['peopleNumber'], graduation['client'], graduation['date']))
		cur.execute("""
			UPDATE FORMATURA F SET F.BARTENDER = %s, F.COPEIRO = %s, F.SALAO = %s 
				WHERE F.CLIENTE = %s AND F.DATAHORA = %s;
			""", (graduation['bartender'], graduation['cupbearer'], graduation['hall'], graduation['client'], graduation['date']))
		conn.commit()
	except Exception as e:
		#print("Unable to execute table update. Exception: " + str(e))
		raise e

def insertCasamento(conn, wedding):
	try:
		cur = conn.cursor()
		cur.execute("""
			INSERT INTO EVENTO (CLIENTE, DATAHORA, CATEGORIA, VALOR, METODOPAGAMENTO, NROPESSOAS)
				VALUES (%s, %s, %s, %s, %s, %s);
			""", (wedding['client'], wedding['date'], "CASAMENTO", wedding['value'], wedding['paymentMethod'], wedding['peopleNumber']))
		cur.execute("""
			INSERT INTO CASAMENTO (CLIENTE, DATAHORA, CHEF, MAITRE, LOCAL) VALUES (%s, %s, %s, %s, %s)
			""", (wedding['client'], wedding['date'], wedding['chef'], wedding['maitre'], wedding['hall']))
		conn.commit()
	except Exception as e:
		#print("Unable to execute table insertion. Exception: " + str(e))
		raise e

# Não é possível alterar a chave da tabela, nem a categoria do evento
def updateCasamento(conn, wedding):
	try:
		cur = conn.cursor()
		cur.execute("""
			UPDATE EVENTO E SET E.VALOR = %s, E.METODOPAGAMENTO = %s, E.NROPESSOAS = %s
				WHERE E.CLIENTE = %s AND E.DATAHORA = %s
			""", (wedding['value'], wedding['paymentMethod'], wedding['peopleNumber'], wedding['client'], wedding['date']))
		cur.execute("""
			UPDATE CASAMENTO C SET C.CHEF = %s, C.MAITRE = %s, C.LOCAL = %s 
				WHERE C.CLIENTE = %s AND C.DATAHORA = %s;
			""", (wedding['chef'], wedding['maitre'], wedding['hall'], wedding['client'], wedding['date']))
		conn.commit()
	except Exception as e:
		#print("Unable to execute table update. Exception: " + str(e))
		raise e


######### Na interface está previsto: #########
# 1)Adicionar Cliente, Funcionário, Especialista - 
# 2)Visualizar em uma tabela os dados de Cliente, Funcionário, Especialista juntos -- Pessoas - 
# 3)Adicionar e Atualizar Formatura e Casamento - 
# 4)Visualizar em uma tabela dos dados de Formatura e Casamento juntos -- Eventos
# 5)Visualizar em uma tabela dados de ContratoEvento e ContratoDeEspecialista -- Contratos
# 6)Visualizar em uma tabelas separadas Produtos, Fornecedores, Cardápios, Itens dos Cardápios 
# ---------------------------------------------
# Consultas: -- Estão em aberto ainda! Você pode escolher ...
# 1)
# 2)
# 3)
# 4)
# 5)
# 6)
###############################################



# Principais operações: 

# Inserção e atualização de dados de pessoas, incluindo clientes, funcionários e especialistas;

# Inserção de eventos e contratos;

# Inserção e atualização de dados relativos a fornecimento de produtos, fornecedores, pratos, bebidas e cardápio;

#Consultar quantas pessoas estão envolvidas em determinado evento;
# "Pessoas", neste contexto, são quaisquer tuplas da relação "Pessoa", conectadas de alguma maneira a um determinado evento (Cliente, Funcionário, ou especialista)

# Consultar quantas pessoas estão envolvidas em determinado evento;

# Consultar quais fornecedores estão envolvidos nos produtos de um item;

# Consultar quais são as melhores opções de fornecimento dos produtos necessários para formar todos os itens de um cardápio;

# Consultar quais são os fornecedores com maior volume de transações considerando os tipos de evento;

# Consultar contrato, local, cardápio, data, hora, tipo de festa e pessoas envolvidas em cada evento (cliente, funcionário e especialista).


