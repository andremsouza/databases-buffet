import psycopg2
import getpass

# Basic search in table "Pessoa"
# Returns column names in strout[0], and query results in strout[1]
def searchPessoa(conn, constraint):
	strout = []
	try:
		cur = conn.cursor()
		cur.execute("""SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE UPPER(TABLE_NAME) = 'PESSOA';""")
		strout.append(cur.fetchall())
		cur.execute("""SELECT * FROM PESSOA WHERE %s;""", (constraint, ))
		strout.append(cur.fetchall())
		return strout
	except Exception as e:
		print("Unable to execute table search. Exception: " + str(e))
		return None

######### Na interface está previsto: #########
# 1)Adicionar Cliente, Funcionário, Especialista
# 2)Visualizar em uma tabela os dados de Cliente, Funcionário, Especialista juntos -- Pessoas
# 3)Adicionar e Atualizar Formatura e Casamento
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


