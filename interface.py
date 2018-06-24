import os
import re
import datetime
import psycopg2
import getpass
from dbCommands import *

#GLOBAL VARIABLES
#Connection with database
print("Tentando conectar a base de dados 'buffet': ")
passwd = getpass.getpass() # Get a password ('buffet01')
try:
	conn = psycopg2.connect("dbname = 'buffet' user = 'buffet' host = 'localhost' password = '"+passwd+"'")
	input("Conexão efetuada com sucesso. Pressione ENTER para continuar.")
except Exception as e:
	print("I am unable to connect to the database. Exception: " + str(e))
	exit(1)

#Dictionaries
client = {'name' : None, 'cpf' : None, 'address' : None, 'email' : None, 'phone' : None}
employee = {'name' : None, 'cpf' : None, 'address' : None, 'email' : None, 'phone' : None, 'salary' : None, 'function' : None}
specialist = {'name' : None, 'cpf' : None, 'address' : None, 'email' : None, 'phone' : None, 'specialty' : None, 'hourFee' : None}
graduation = {'client' : None, 'date' : None, 'value' : None, 'paymentMethod' : None, 'peopleNumber' : None, 'bartender' : None, 'cupbearer' : None, 'hall' : None}
wedding = {'client' : None, 'date' : None, 'value' : None, 'paymentMethod' : None, 'peopleNumber' : None, 'chef' : None, 'maitre' : None, 'hall' : None}

#Visualize Data Variables
peopleData = 'People info here'
eventsData = 'Events info here'
contractsData = 'Contracts info here'
productsData = 'Products info here'
providersData = 'Providers info here'
menuData = 'Menu info here'
menuItemsData = 'Menu Items info here'
query1Data = 'Query 1 info here'
query2Data = 'Query 2 info here'
query3Data = 'Query 3 info here'
query4Data = 'Query 4 info here'
query5Data = 'Query 5 info here'
query6Data = 'Query 6 info here'


def clearDictionary(dict):
	for key in dict.keys():
		dict[key] = None

def printMainMenu():
	os.system('clear')
	print("EventManager - Digite: ")
	print("'1' para Gerenciar Pessoas")
	print("'2' para Gerenciar Eventos")
	print("'3' para Gerenciar Contratos")
	print("'4' para Gerenciar Operação")
	print("'5' para realizar Consultas")
	print("'6' para Sair")

def printPeopleMenu():
	os.system('clear')
	print("Pessoas - Digite: ")
	print("'1' para Adicionar Cliente")
	print("'2' para Adicionar Funcionário")
	print("'3' para Adicionar Especialista")
	print("'4' para Visualizar Todas as Pessoas")
	print("'5' para Voltar ao Menu Principal")

def printEventsMenu():
	os.system('clear')
	print("Eventos - Digite: ")
	print("'1' para Adicionar Formatura")
	print("'2' para Alterar Formatura")
	print("'3' para Adicionar Casamento")
	print("'4' para Alterar Casamento")
	print("'5' para Visualizar Todos os Eventos")
	print("'6' para Deletar um Evento")
	print("'7' para Voltar ao Menu Principal")

def printContractsMenu():
	os.system('clear')
	print("Contratos - Digite: ")
	print("'1' para Visualizar Todos os Contratos")
	print("'2' para Voltar ao Menu Principal")

def printOperationMenu():
	os.system('clear')
	print("Operação - Digite: ")
	print("'1' para Visualizar Todos os Produtos")
	print("'2' para Visualizar Todos os Fornecedores")
	print("'3' para Visualizar Todos os Cardápios")
	print("'4' para Visualizar Todos os Itens de Cardápios")
	print("'5' para Voltar ao Menu Principal")

def printQueriesMenu():
	os.system('clear')
	print("Consultas - Digite: ")
	print("'1' para Consulta 1")
	print("'2' para Consulta 2")
	print("'3' para Consulta 3")
	print("'4' para Consulta 4")
	print("'5' para Consulta 5")
	print("'6' para Consulta 6")
	print("'7' para Voltar ao Menu Principal")

def getPeopleInput(type):
	os.system('clear')
	global client, employee, specialist, conn
	if(type.upper() == 'CLIENT'):
		print("Adicionando Cliente")
		person = client

	if(type.upper() == 'EMPLOYEE'):
		print("Adicionando Funcionário")
		person = employee

	if(type.upper() == 'SPECIALIST'):
		print("Adicionando Especialista")
		person = specialist

	while(True):
		try:
			if(type.upper() == 'CLIENT'): userInput = str(input("Digite o nome do Cliente: "))
			if(type.upper() == 'EMPLOYEE'): userInput = str(input("Digite o nome do Funcionário: "))
			if(type.upper() == 'SPECIALIST'): userInput = str(input("Digite o nome do Especialista: "))
			if(len(userInput)<128): break
			else: print("Entrada inválida - Nome muito longo")
		except:
			print("Entrada inválida")
			continue
	person['name'] = userInput

	while(True):
		try:
			if(type.upper() == 'CLIENT'): userInput = str(input("Digite o CPF(XXX.XXX.XXX-XX) do Cliente: "))
			if(type.upper() == 'EMPLOYEE'): userInput = str(input("Digite o CPF(XXX.XXX.XXX-XX) do Funcionário: "))
			if(type.upper() == 'SPECIALIST'): userInput = str(input("Digite o CPF(XXX.XXX.XXX-XX) do Especialista: "))
			cpfFormat = re.compile('[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}-[0-9]{2}')
			if(cpfFormat.match(userInput) and len(userInput)==14): 
				if(type.upper() == 'CLIENT'): break
				if(type.upper() == 'EMPLOYEE'):
					#TODO Pesquisar se já tem um especialista com este CPF e não permitir a inserção neste caso -- Prometemos tratar isto em Aplicação
					break
				if(type.upper() == 'SPECIALIST'):
					#TODO Pesquisar se já tem um funcionário com este CPF e não permitir a inserção neste caso -- Prometemos tratar isto em Aplicação
					break
				
			else: print("Entrada inválida - CPF inválido")
		except:
			print("Entrada inválida")
			continue
	person['cpf'] = userInput
	
	while(True):
		try:
			if(type.upper() == 'CLIENT'): userInput = str(input("Digite o endreço do Cliente: "))
			if(type.upper() == 'EMPLOYEE'): userInput = str(input("Digite o endreço do Funcionário: "))
			if(type.upper() == 'SPECIALIST'): userInput = str(input("Digite o endreço do Especialista: "))
			if(len(userInput)<128): break
			else: print("Entrada inválida - Endereço muito longo")
		except:
			print("Entrada inválida")
			continue
	person['address'] = userInput
	
	while(True):
		try:
			if(type.upper() == 'CLIENT'): userInput = str(input("Digite o email(nX@nX.nX) do Cliente: "))
			if(type.upper() == 'EMPLOYEE'): userInput = str(input("Digite o email(nX@nX.nX) do Funcionário: "))
			if(type.upper() == 'SPECIALIST'): userInput = str(input("Digite o email(nX@nX.nX) do Especialista: "))
			emailFormat = re.compile('^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
			if(emailFormat.match(userInput)): break
			else: print("Entrada inválida - Email inválido")
		except:
			print("Entrada inválida")
			continue
	person['email'] = userInput

	while(True):
		try:
			if(type.upper() == 'CLIENT'): userInput = str(input("Digite o Telefone('(XX) XXXXX-XXXX' ou '(XX) XXXX-XXXX') do Cliente ou '-1' se não desejar informar agora: "))
			if(type.upper() == 'EMPLOYEE'): userInput = str(input("Digite o Telefone('(XX) XXXXX-XXXX' ou '(XX) XXXX-XXXX') do Funcionário ou '-1' se não desejar informar agora: "))
			if(type.upper() == 'SPECIALIST'): userInput = str(input("Digite o Telefone('(XX) XXXXX-XXXX' ou '(XX) XXXX-XXXX') do Especialista ou '-1' se não desejar informar agora: "))
			phoneFormat = re.compile('^(\([0-9]{2}\) [0-9]{5}-[0-9]{4})|(\([0-9]{2}\) [0-9]{4}-[0-9]{4})$')
			if(phoneFormat.match(userInput)): break
			elif(userInput == '-1'): break
			else: print("Entrada inválida - Telefone inválido")
		except:
			print("Entrada inválida")
			continue
	if(userInput != '-1'): person['phone'] = userInput

	if(type.upper() == 'EMPLOYEE'):
		while(True):
			try:
				userInput = float(input("Digite o salário do Funcionário: "))
				if(userInput > 0): break
				else: print("Entrada inválida - Salário inválido")
			except:
				print("Entrada inválida")
				continue
		person['salary'] = userInput

		while(True):
			try:
				userInput = str(input("Digite a função('Garçom' ou 'Cozinheiro') do Funcionário: "))
				if(userInput.upper() != 'GARÇOM' and userInput.upper() != 'COZINHEIRO'): print("Entrada inválida - A função deve ser 'Garçom' ou 'Cozinheiro'")
				else: break
			except:
				print("Entrada inválida")
				continue
		person['function'] = userInput

	if(type.upper() == 'SPECIALIST'):
		while(True):
			try:
				userInput = float(input("Digite o taxa/hora do Especialista: "))
				if(userInput > 0): break
				else: print("Entrada inválida - Taxa/Hora inválida")
			except:
				print("Entrada inválida")
				continue
		person['hourFee'] = userInput

		while(True):
			try:
				userInput = str(input("Digite a função('Chef', 'Maître', 'Bartender' ou 'Copeiro') do Especialista: "))
				if(userInput.upper() != 'CHEF' and userInput.upper() != 'MAÎTRE' and userInput.upper() != 'BARTENDER' and userInput.upper() != 'COPEIRO'): 
					print("Entrada inválida - A função deve ser 'Chef', 'Maître', 'Bartender' ou 'Copeiro'")
				else: break
			except:
				print("Entrada inválida")
				continue
		person['specialty'] = userInput

	if(type.upper() == 'CLIENT'): client = person
	if(type.upper() == 'EMPLOYEE'): employee = person
	if(type.upper() == 'SPECIALIST'): specialist = person

def getEventsInput(type, operation):
	os.system('clear')
	global graduation, wedding, conn
	if(type.upper() == 'GRADUATION'):
		if(operation.upper() == 'ADD'): print("Adicionando Formatura")
		if(operation.upper() == 'UPDATE'): print("Atualizando Formatura")
		if(operation.upper() == 'DELETE'): print("Removendo Evento")
		event = graduation

	if(type.upper() == 'WEDDING'):
		if(operation.upper() == 'ADD'): print("Adicionando Casamento")
		if(operation.upper() == 'UPDATE'): print("Atualizando Casamento")
		event = wedding

	while(True):
		try:
			userInput = str(input("Digite o CPF(XXX.XXX.XXX-XX) do Cliente: "))
			cpfFormat = re.compile('[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}-[0-9]{2}')
			if(cpfFormat.match(userInput) and len(userInput)==14): break
			else: print("Entrada inválida - CPF inválido")
		except:
			print("Entrada inválida")
			continue
	event['cpf'] = userInput

	while(True):
		try:
			if(type.upper() == 'GRADUATION' and operation.upper() != 'DELETE'): userInput = str(input("Digite o data(AAAA-MM-DD-HH-MM) da Formatura: "))
			if(type.upper() == 'GRADUATION' and operation.upper() == 'DELETE'): userInput = str(input("Digite o data(AAAA-MM-DD-HH-MM) do Evento: "))
			if(type.upper() == 'WEDDING'): userInput = str(input("Digite o data(AAAA-MM-DD-HH-MM) do Casamento: "))
			dateFormat = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}')
			if(dateFormat.match(userInput) and len(userInput)==16):
				year = int(userInput[0:4])
				month = int(userInput[5:7])
				day = int(userInput[8:10])
				hour = int(userInput[11:13])
				minute = int(userInput[14:])
				if((month > 0 and month < 13) and (day > 0 and day < 32) and (hour > -1 and hour < 24) and (minute > -1 and minute < 61)): break
				else: print("Entrada inválida - Data inválida")
			else: print("Entrada inválida - Data inválida")
		except:
			print("Entrada inválida")
			continue
	event['date'] = datetime.datetime(year,month,day,hour,minute)

	if(operation.upper() == 'DELETE'): return

	while(True):
		try:
			if(type.upper() == 'GRADUATION'): userInput = float(input("Digite o valor acordado pela Formatura ou '-1' se não desejar informar agora: "))
			if(type.upper() == 'WEDDING'): userInput = float(input("Digite o valor acordado pelo Casamento ou '-1' se não desejar informar agora: "))
			if(userInput > 0): break
			elif(userInput == -1): break
			else: print("Entrada inválida - Valor inválido")
		except:
			print("Entrada inválida")
			continue
	if(userInput != -1): event['value'] = userInput

	while(True):
		try:
			if(type.upper() == 'GRADUATION'): userInput = str(input("Digite o método de pagamento('Dinheiro' ou 'Cartão') da Formatura ou '-1' se não desejar informar agora: "))
			if(type.upper() == 'WEDDING'): userInput = str(input("Digite o método de pagamento('Dinheiro' ou 'Cartão') do Casamento ou '-1' se não desejar informar agora: "))
			if(userInput.upper() != 'DINHEIRO' and userInput.upper() != 'CARTÃO' and userInput != '-1'): print("Entrada inválida - O método deve ser 'Dinheiro' ou 'Cartão'")
			else: break
		except:
			print("Entrada inválida")
			continue
	if(userInput != '-1'): event['paymentMethod'] = userInput

	while(True):
		try:
			if(type.upper() == 'GRADUATION'): userInput = float(input("Digite o número de pessoas que vão na Formatura: "))
			if(type.upper() == 'WEDDING'): userInput = float(input("Digite o número de pessoas que vão no Casamento: "))
			if(userInput > 0): break
			else: print("Entrada inválida - Número de Pessoas inválido")
		except:
			print("Entrada inválida")
			continue
	event['peopleNumber'] = userInput

	while(True):
		try:
			if(type.upper() == 'GRADUATION'): userInput = int(input("Digite o ID do local da Formatura: "))
			if(type.upper() == 'WEDDING'): userInput = int(input("Digite o ID do local do Casamento: "))
			if(userInput > 0): break
			else: print("Entrada inválida - ID inválido")
		except:
			print("Entrada inválida")
			continue
	event['hall'] = userInput

	if(type.upper() == 'GRADUATION'):
		while(True):
			try:
				userInput = str(input("Digite o CPF(XXX.XXX.XXX-XX) do Bartender da Formatura ou '-1' se não desejar informar agora: "))
				cpfFormat = re.compile('[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}-[0-9]{2}')
				if(cpfFormat.match(userInput) and len(userInput)==14): break
				elif(userInput == '-1'): break
				else: print("Entrada inválida - CPF inválido")
			except:
				print("Entrada inválida")
				continue
		if((userInput != '-1')): event['bartender'] = userInput

		while(True):
			try:
				userInput = str(input("Digite o CPF(XXX.XXX.XXX-XX) do Copeiro da Formaturaou '-1' se não desejar informar agora: "))
				cpfFormat = re.compile('[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}-[0-9]{2}')
				if(cpfFormat.match(userInput) and len(userInput)==14): break
				elif(userInput == '-1'): break
				else: print("Entrada inválida - CPF inválido")
			except:
				print("Entrada inválida")
				continue
		if((userInput != '-1')): event['cupbearer'] = userInput

	if(type.upper() == 'WEDDING'):
		while(True):
			try:
				userInput = str(input("Digite o CPF(XXX.XXX.XXX-XX) do Chef do Casamento ou '-1' se não desejar informar agora: "))
				cpfFormat = re.compile('[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}-[0-9]{2}')
				if(cpfFormat.match(userInput) and len(userInput)==14): break
				elif(userInput == '-1'): break
				else: print("Entrada inválida - CPF inválido")
			except:
				print("Entrada inválida")
				continue
		if((userInput != '-1')): event['chef'] = userInput

		while(True):
			try:
				userInput = str(input("Digite o CPF(XXX.XXX.XXX-XX) do Maître do Casamento ou '-1' se não desejar informar agora: "))
				cpfFormat = re.compile('[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}-[0-9]{2}')
				if(cpfFormat.match(userInput) and len(userInput)==14): break
				elif(userInput == '-1'): break
				else: print("Entrada inválida - CPF inválido")
			except:
				print("Entrada inválida")
				continue
		if((userInput != '-1')): event['maitre'] = userInput

	if(type.upper() == 'GRADUATION'): graduation = event
	if(type.upper() == 'WEDDING'): wedding = event

def handleMenu():
	exit = False
	global conn
	while(exit == False):
		printMainMenu()
		while(True):
			try:
				option = int(input("Selecione sua opção: "))
				if(option>0 and option<7): break
				else: print("Comando inválido")
			except:
				print("Comando inválido")
				continue

		#Manage People
		if(option == 1):
			printPeopleMenu()
			while(True):
				try:
					option = int(input("Selecione sua opção: "))
					if(option>0 and option<6): break
					else: print("Comando inválido")
				except:
					print("Comando inválido")
					continue
			#Add Client
			if(option == 1):
				global client
				getPeopleInput('CLIENT')
				try: insertCliente(conn, client)
				except:
					print("Desculpe, mas houve um problema na inserção! Tente novamente com outros dados!")
				else:
					print("Cliente adicionado com sucesso!")
				clearDictionary(client)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Add Employee
			if(option == 2):
				global employee
				getPeopleInput('EMPLOYEE')
				try: insertFuncionario(conn, employee)
				except:
					print("Desculpe, mas houve um problema na inserção! Tente novamente com outros dados!")
				else:
					print("Funcionário adicionado com sucesso!")
				clearDictionary(employee)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Add SPECIALIST
			if(option == 3):
				global specialist
				getPeopleInput('SPECIALIST')
				try: insertFuncionario(conn, specialist)
				except:
					print("Desculpe, mas houve um problema na inserção! Tente novamente com outros dados!")
				else:
					print("Especialista adicionado com sucesso!")
				clearDictionary(specialist)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Visualize People Data
			if(option == 4):
				os.system('clear')
				global peopleData
				try: peopleData = searchPessoaAll(conn)
				except:
					print("Desculpe, mas houve um problema na pesquisa!")
				else:
					print(peopleData)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1
			option = -1


		#Manage Events
		if(option == 2):
			printEventsMenu()
			while(True):
				try:
					option = int(input("Selecione sua opção: "))
					if(option>0 and option<8): break
					else: print("Comando inválido")
				except:
					print("Comando inválido")
					continue

			#Add Graduation
			if(option == 1):
				global graduation
				getEventsInput('GRADUATION', 'ADD')
				try: insertFormatura(conn, graduation)
				except:
					print("Desculpe, mas houve um problema na inserção! Tente novamente com outros dados!")
				else:
					print("Formatura adicionada com sucesso!")
				clearDictionary(graduation)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Update Graduation
			if(option == 2):
				global graduation
				getEventsInput('GRADUATION', 'UPDATE')
				try: updateFormatura(conn, graduation)
				except:
					print("Desculpe, mas houve um problema na alteração! Tente novamente com outros dados!")
				else:
					print("Formatura alterada com sucesso!")
				clearDictionary(graduation)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Add Wedding
			if(option == 3):
				global wedding
				getEventsInput('WEDDING', 'ADD')
				try: insertCasamento(conn, wedding)
				except:
					print("Desculpe, mas houve um problema na inserção! Tente novamente com outros dados!")
				else:
					print("Casamento adicionado com sucesso!")
				clearDictionary(wedding)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Update Wedding
			if(option == 4):
				global wedding
				getEventsInput('WEDDING', 'UPDATE')
				try: updateCasamento(conn, wedding)
				except:
					print("Desculpe, mas houve um problema na alteração! Tente novamente com outros dados!")
				else:
					print("Casamento alterado com sucesso!")
				clearDictionary(wedding)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Visualize Events Data
			if(option == 5):
				os.system('clear')
				global eventsData
				try: eventsData = searchEventoAll(conn)
				except:
					print("Desculpe, mas houve um problema na pesquisa!")
				else:
					print(eventsData)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Delete Event
			if(option == 6):
				global graduation #Used to receive graduation['client'] and graduation['date'], but it serves to Wedding Events data either
				getEventsInput('GRADUATION', 'DELETE') #Here we use 'GRADUATION', but this is used to Wedding events either
				#TODO Link with database
				print("Evento removido com sucesso!")
				clearDictionary(graduation)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1
			option = -1

		#Manage Contracts
		if(option == 3):
			printContractsMenu()
			while(True):
				try:
					option = int(input("Selecione sua opção: "))
					if(option>0 and option<3): break
					else: print("Comando inválido")
				except:
					print("Comando inválido")
					continue

			#Visualize Contracts Data
			if(option == 1):
				os.system('clear')
				global contractsData
				try: contractsData = searchContrato(conn)
				except:
					print("Desculpe, mas houve um problema na pesquisa!")
				else:
					print(contractsData)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1
			option = -1

		#Manage Operation
		if(option == 4):
			printOperationMenu()
			while(True):
				try:
					option = int(input("Selecione sua opção: "))
					if(option>0 and option<6): break
					else: print("Comando inválido")
				except:
					print("Comando inválido")
					continue

			#Visualize Products Data
			if(option == 1):
				os.system('clear')
				global productsData
				try: productsData = searchProduto(conn)
				except:
					print("Desculpe, mas houve um problema na pesquisa!")
				else:
					print(productsData)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Visualize Providers Data
			if(option == 2):
				os.system('clear')
				global providersData
				try: providersData = searchFornecedor(conn)
				except:
					print("Desculpe, mas houve um problema na pesquisa!")
				else:
					print(providersData)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Visualize Menu Data
			if(option == 3):
				os.system('clear')
				global menuData
				try: menuData = searchCardapio(conn)
				except:
					print("Desculpe, mas houve um problema na pesquisa!")
				else:
					print(menuData)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Visualize Menu Items Data
			if(option == 4):
				os.system('clear')
				global menuItemsData
				try: menuItemsData = searchCardapioItem(conn)
				except:
					print("Desculpe, mas houve um problema na pesquisa!")
				else:
					print(menuItemsData)
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1
			option = -1

		#Queries
		if(option == 5):
			printQueriesMenu()
			while(True):
				try:
					option = int(input("Selecione sua opção: "))
					if(option>0 and option<8): break
					else: print("Comando inválido")
				except:
					print("Comando inválido")
					continue

			#Visualize Query 1 Data
			if(option == 1):
				os.system('clear')
				global query1Data
				print(query1Data)
				#TODO Link with database
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Visualize Query 2 Data
			if(option == 2):
				os.system('clear')
				global query2Data
				print(query2Data)
				#TODO Link with database
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Visualize Query 3 Data
			if(option == 3):
				os.system('clear')
				global query3Data
				print(query3Data)
				#TODO Link with database
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Visualize Query 4 Data
			if(option == 4):
				os.system('clear')
				global query4Data
				print(query4Data)
				#TODO Link with database
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Visualize Query 5 Data
			if(option == 5):
				os.system('clear')
				global query5Data
				print(query5Data)
				#TODO Link with database
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1

			#Visualize Query 6 Data
			if(option == 6):
				os.system('clear')
				global query6Data
				print(query6Data)
				#TODO Link with database
				wait =input("Pressione 'Enter' para continuar ... ")
				option = -1
			option = -1

		if(option == 6): exit = True
		option = -1

if __name__ == "__main__":
	handleMenu()