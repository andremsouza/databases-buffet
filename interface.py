from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

#dictionaries
client = {'name' : None, 'cpf' : None, 'address' : None, 'email' : None}
employee = {'name' : None, 'cpf' : None, 'address' : None, 'email' : None, 'salary' : None, 'function' : None}
specialist = {'name' : None, 'cpf' : None, 'address' : None, 'email' : None, 'specialty' : None, 'hourFee' : None}

textPeople = 'People info here'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(874, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, -20, 871, 101))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        MainWindow.setCentralWidget(self.centralwidget)
        

        ### Superior Menu ###
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        self.menuGerenciar_Pessoas = QtGui.QMenu(self.menubar)
        self.menuGerenciar_Pessoas.setObjectName(_fromUtf8("menuGerenciar_Pessoas"))
        
        self.menuAdicionar = QtGui.QMenu(self.menuGerenciar_Pessoas)
        self.menuAdicionar.setObjectName(_fromUtf8("menuAdicionar"))
        
        self.menuGerenciar_Eventos = QtGui.QMenu(self.menubar)
        self.menuGerenciar_Eventos.setObjectName(_fromUtf8("menuGerenciar_Eventos"))
        
        self.menuGerenciar_Contatos = QtGui.QMenu(self.menubar)
        self.menuGerenciar_Contatos.setObjectName(_fromUtf8("menuGerenciar_Contatos"))
        
        self.menuGerenciar_Produtos = QtGui.QMenu(self.menubar)
        self.menuGerenciar_Produtos.setObjectName(_fromUtf8("menuGerenciar_Produtos"))
        
        self.menuVisualizar = QtGui.QMenu(self.menuGerenciar_Produtos)
        self.menuVisualizar.setObjectName(_fromUtf8("menuVisualizar"))
        
        self.menuConsultas = QtGui.QMenu(self.menubar)
        self.menuConsultas.setObjectName(_fromUtf8("menuConsultas"))
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionVisualizar = QtGui.QAction(MainWindow)
        self.actionVisualizar.setObjectName(_fromUtf8("actionVisualizar"))
        
        self.actionCliente = QtGui.QAction(MainWindow)
        self.actionCliente.setObjectName(_fromUtf8("actionCliente"))
        
        self.actionFuncion_rios = QtGui.QAction(MainWindow)
        self.actionFuncion_rios.setObjectName(_fromUtf8("actionFuncion_rios"))
        
        self.actionEspecialista = QtGui.QAction(MainWindow)
        self.actionEspecialista.setObjectName(_fromUtf8("actionEspecialista"))
        
        self.actionRemover = QtGui.QAction(MainWindow)
        self.actionRemover.setObjectName(_fromUtf8("actionRemover"))
        
        self.actionAdicionar_2 = QtGui.QAction(MainWindow)
        self.actionAdicionar_2.setObjectName(_fromUtf8("actionAdicionar_2"))
        
        self.actionAlterar_2 = QtGui.QAction(MainWindow)
        self.actionAlterar_2.setObjectName(_fromUtf8("actionAlterar_2"))
        
        self.actionRemover_2 = QtGui.QAction(MainWindow)
        self.actionRemover_2.setObjectName(_fromUtf8("actionRemover_2"))
        
        self.actionVisualizar_2 = QtGui.QAction(MainWindow)
        self.actionVisualizar_2.setObjectName(_fromUtf8("actionVisualizar_2"))
        
        self.actionAlterar_3 = QtGui.QAction(MainWindow)
        self.actionAlterar_3.setObjectName(_fromUtf8("actionAlterar_3"))
        
        self.actionRemover_3 = QtGui.QAction(MainWindow)
        self.actionRemover_3.setObjectName(_fromUtf8("actionRemover_3"))
        
        self.actionAdicionar_3 = QtGui.QAction(MainWindow)
        self.actionAdicionar_3.setObjectName(_fromUtf8("actionAdicionar_3"))
        
        self.actionVisualizar_3 = QtGui.QAction(MainWindow)
        self.actionVisualizar_3.setObjectName(_fromUtf8("actionVisualizar_3"))
        
        self.actionAlterar_4 = QtGui.QAction(MainWindow)
        self.actionAlterar_4.setObjectName(_fromUtf8("actionAlterar_4"))
        
        self.actionRemover_4 = QtGui.QAction(MainWindow)
        self.actionRemover_4.setObjectName(_fromUtf8("actionRemover_4"))
        
        self.actionAdicionar_4 = QtGui.QAction(MainWindow)
        self.actionAdicionar_4.setObjectName(_fromUtf8("actionAdicionar_4"))
        
        self.actionAlterar_5 = QtGui.QAction(MainWindow)
        self.actionAlterar_5.setObjectName(_fromUtf8("actionAlterar_5"))
        
        self.actionRemover_5 = QtGui.QAction(MainWindow)
        self.actionRemover_5.setObjectName(_fromUtf8("actionRemover_5"))
        
        self.actionAdicionar_5 = QtGui.QAction(MainWindow)
        self.actionAdicionar_5.setObjectName(_fromUtf8("actionAdicionar_5"))
        
        self.actionVisualizar_5 = QtGui.QAction(MainWindow)
        self.actionVisualizar_5.setObjectName(_fromUtf8("actionVisualizar_5"))
        
        self.actionAlterar_6 = QtGui.QAction(MainWindow)
        self.actionAlterar_6.setObjectName(_fromUtf8("actionAlterar_6"))
        
        self.actionRemover_6 = QtGui.QAction(MainWindow)
        self.actionRemover_6.setObjectName(_fromUtf8("actionRemover_6"))
        
        self.actionProdutos = QtGui.QAction(MainWindow)
        self.actionProdutos.setObjectName(_fromUtf8("actionProdutos"))
        
        self.actionFornecedores = QtGui.QAction(MainWindow)
        self.actionFornecedores.setObjectName(_fromUtf8("actionFornecedores"))
        
        self.actionCard_pios = QtGui.QAction(MainWindow)
        self.actionCard_pios.setObjectName(_fromUtf8("actionCard_pios"))
        
        self.actionItens_de_Card_pios = QtGui.QAction(MainWindow)
        self.actionItens_de_Card_pios.setObjectName(_fromUtf8("actionItens_de_Card_pios"))
        
        self.menuAdicionar.addAction(self.actionCliente)
        self.menuAdicionar.addAction(self.actionFuncion_rios)
        self.menuAdicionar.addAction(self.actionEspecialista)
        
        self.menuGerenciar_Pessoas.addAction(self.menuAdicionar.menuAction())
        self.menuGerenciar_Pessoas.addAction(self.actionVisualizar)
        
        self.menuGerenciar_Eventos.addAction(self.actionAdicionar_2)
        self.menuGerenciar_Eventos.addAction(self.actionVisualizar_2)
        self.menuGerenciar_Eventos.addAction(self.actionAlterar_3)
        self.menuGerenciar_Eventos.addAction(self.actionRemover_3)
        
        self.menuGerenciar_Contatos.addAction(self.actionVisualizar_3)
        
        self.menuVisualizar.addAction(self.actionProdutos)
        self.menuVisualizar.addAction(self.actionFornecedores)
        self.menuVisualizar.addAction(self.actionCard_pios)
        self.menuVisualizar.addAction(self.actionItens_de_Card_pios)
        
        self.menuGerenciar_Produtos.addAction(self.menuVisualizar.menuAction())
        self.menubar.addAction(self.menuGerenciar_Pessoas.menuAction())
        self.menubar.addAction(self.menuGerenciar_Eventos.menuAction())
        self.menubar.addAction(self.menuGerenciar_Contatos.menuAction())
        self.menubar.addAction(self.menuGerenciar_Produtos.menuAction())
        self.menubar.addAction(self.menuConsultas.menuAction())
        ### --- ###

        #Add Client Box
        self.addClientBox = QtGui.QGroupBox(self.centralwidget)
        self.addClientBox.setGeometry(QtCore.QRect(0, 0, 871, 401))
        self.addClientBox.setObjectName(_fromUtf8("addClientBox"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.addClientBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 30, 871, 311))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        
        self.clientNameLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.clientNameLabel.setObjectName(_fromUtf8("clientNameLabel"))
        self.horizontalLayout_2.addWidget(self.clientNameLabel)
        self.clientNameLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.clientNameLine.setObjectName(_fromUtf8("clientNameLine"))
        self.horizontalLayout_2.addWidget(self.clientNameLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        
        self.clientCpfLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.clientCpfLabel.setObjectName(_fromUtf8("clientCpfLabel"))
        self.horizontalLayout_3.addWidget(self.clientCpfLabel)
        self.clientCpfLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.clientCpfLine.setObjectName(_fromUtf8("clientCpfLine"))
        self.horizontalLayout_3.addWidget(self.clientCpfLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        
        self.clientAddressLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.clientAddressLabel.setObjectName(_fromUtf8("clientAddressLabel"))
        self.horizontalLayout_4.addWidget(self.clientAddressLabel)
        self.clientAddressLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.clientAddressLine.setObjectName(_fromUtf8("clientAddressLine"))
        self.horizontalLayout_4.addWidget(self.clientAddressLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        
        self.clientEmailLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.clientEmailLabel.setObjectName(_fromUtf8("clientEmailLabel"))
        self.horizontalLayout_5.addWidget(self.clientEmailLabel)
        self.clientEmailLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.clientEmailLine.setObjectName(_fromUtf8("clientEmailLine"))
        self.horizontalLayout_5.addWidget(self.clientEmailLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        
        self.clientAddBtnSend = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.clientAddBtnSend.setObjectName(_fromUtf8("clientAddBtnSend"))
        self.verticalLayout_3.addWidget(self.clientAddBtnSend)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)

        self.clientSucessOrFail = QtGui.QLabel(self.addClientBox)
        self.clientSucessOrFail.setGeometry(QtCore.QRect(0, 320, 869, 49))
        self.clientSucessOrFail.setObjectName(_fromUtf8("clientSucessOrFail"))
        
        self.clientSucessOrFail.setVisible(0)
        self.addClientBox.setVisible(0)
        ### --- ###

        #Add Employee Box
        self.addEmployeeBox = QtGui.QGroupBox(self.centralwidget)
        self.addEmployeeBox.setGeometry(QtCore.QRect(0, 0, 871, 531))
        self.addEmployeeBox.setObjectName(_fromUtf8("addEmployeeBox"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.addEmployeeBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 871, 361))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        
        self.employeeNameLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.employeeNameLabel.setObjectName(_fromUtf8("employeeNameLabel"))
        self.horizontalLayout_2.addWidget(self.employeeNameLabel)
        self.employeeNameLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.employeeNameLine.setObjectName(_fromUtf8("employeeNameLine"))
        self.horizontalLayout_2.addWidget(self.employeeNameLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        
        self.employeeCpfLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.employeeCpfLabel.setObjectName(_fromUtf8("employeeCpfLabel"))
        self.horizontalLayout_3.addWidget(self.employeeCpfLabel)
        self.employeeCpfLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.employeeCpfLine.setObjectName(_fromUtf8("employeeCpfLine"))
        self.horizontalLayout_3.addWidget(self.employeeCpfLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        
        self.employeeAddressLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.employeeAddressLabel.setObjectName(_fromUtf8("employeeAddressLabel"))
        self.horizontalLayout_4.addWidget(self.employeeAddressLabel)
        self.employeeAddressLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.employeeAddressLine.setObjectName(_fromUtf8("employeeAddressLine"))
        self.horizontalLayout_4.addWidget(self.employeeAddressLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        
        self.employeeEmailLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.employeeEmailLabel.setObjectName(_fromUtf8("employeeEmailLabel"))
        self.horizontalLayout_5.addWidget(self.employeeEmailLabel)
        self.employeeEmailLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.employeeEmailLine.setObjectName(_fromUtf8("employeeEmailLine"))
        self.horizontalLayout_5.addWidget(self.employeeEmailLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        
        self.employeeSalaryLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.employeeSalaryLabel.setObjectName(_fromUtf8("employeeSalaryLabel"))
        self.horizontalLayout_6.addWidget(self.employeeSalaryLabel)
        self.employeeSalaryLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.employeeSalaryLine.setObjectName(_fromUtf8("employeeSalaryLine"))
        self.horizontalLayout_6.addWidget(self.employeeSalaryLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        
        self.employeeFunctionLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.employeeFunctionLabel.setObjectName(_fromUtf8("employeeFunctionLabel"))
        self.horizontalLayout_8.addWidget(self.employeeFunctionLabel)
        self.employeeFunctionLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.employeeFunctionLine.setObjectName(_fromUtf8("employeeFunctionLine"))
        self.horizontalLayout_8.addWidget(self.employeeFunctionLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        
        self.employeeAddBtnSend = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.employeeAddBtnSend.setObjectName(_fromUtf8("employeeAddBtnSend"))
        self.verticalLayout_3.addWidget(self.employeeAddBtnSend)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        
        self.employeeSucessOrFail = QtGui.QLabel(self.addEmployeeBox)
        self.employeeSucessOrFail.setGeometry(QtCore.QRect(0, 370, 869, 49))
        self.employeeSucessOrFail.setObjectName(_fromUtf8("employeeSucessOrFail"))

        self.employeeSucessOrFail.setVisible(0)
        self.addEmployeeBox.setVisible(0)
        ### --- ###

        #Add Specialist Box
        self.addSpecialistBox = QtGui.QGroupBox(self.centralwidget)
        self.addSpecialistBox.setGeometry(QtCore.QRect(0, 0, 871, 531))
        self.addSpecialistBox.setObjectName(_fromUtf8("addSpecialistBox"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.addSpecialistBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 871, 361))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        
        self.specialistNameLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.specialistNameLabel.setObjectName(_fromUtf8("specialistNameLabel"))
        self.horizontalLayout_2.addWidget(self.specialistNameLabel)
        self.specialistNameLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.specialistNameLine.setObjectName(_fromUtf8("specialistNameLine"))
        self.horizontalLayout_2.addWidget(self.specialistNameLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        
        self.specialistCpfLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.specialistCpfLabel.setObjectName(_fromUtf8("specialistCpfLabel"))
        self.horizontalLayout_3.addWidget(self.specialistCpfLabel)
        self.specialistCpfLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.specialistCpfLine.setObjectName(_fromUtf8("specialistCpfLine"))
        self.horizontalLayout_3.addWidget(self.specialistCpfLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        
        self.specialistAddressLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.specialistAddressLabel.setObjectName(_fromUtf8("specialistAddressLabel"))
        self.horizontalLayout_4.addWidget(self.specialistAddressLabel)
        self.specialistAddressLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.specialistAddressLine.setObjectName(_fromUtf8("specialistAddressLine"))
        self.horizontalLayout_4.addWidget(self.specialistAddressLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        
        self.specialistEmailLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.specialistEmailLabel.setObjectName(_fromUtf8("specialistEmailLabel"))
        self.horizontalLayout_5.addWidget(self.specialistEmailLabel)
        self.specialistEmailLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.specialistEmailLine.setObjectName(_fromUtf8("specialistEmailLine"))
        self.horizontalLayout_5.addWidget(self.specialistEmailLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        
        self.specialistSpecialtyLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.specialistSpecialtyLabel.setObjectName(_fromUtf8("specialistSpecialtyLabel"))
        self.horizontalLayout_6.addWidget(self.specialistSpecialtyLabel)
        self.specialistSpecialtyLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.specialistSpecialtyLine.setObjectName(_fromUtf8("specialistSpecialtyLine"))
        self.horizontalLayout_6.addWidget(self.specialistSpecialtyLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        
        self.specialistHourFeeLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.specialistHourFeeLabel.setObjectName(_fromUtf8("specialistHourFeeLabel"))
        self.horizontalLayout_8.addWidget(self.specialistHourFeeLabel)
        self.specialistHourFeeLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.specialistHourFeeLine.setObjectName(_fromUtf8("specialistHourFeeLine"))
        self.horizontalLayout_8.addWidget(self.specialistHourFeeLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        
        self.specialistAddBtnSend = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.specialistAddBtnSend.setObjectName(_fromUtf8("specialistAddBtnSend"))
        self.verticalLayout_3.addWidget(self.specialistAddBtnSend)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        
        self.specialistSucessOrFail = QtGui.QLabel(self.addSpecialistBox)
        self.specialistSucessOrFail.setGeometry(QtCore.QRect(0, 370, 869, 49))
        self.specialistSucessOrFail.setObjectName(_fromUtf8("specialistSucessOrFail"))

        self.specialistSucessOrFail.setVisible(0)
        self.addSpecialistBox.setVisible(0)
        ### --- ###

        ### Visualize People ###
        self.visualizePeopleBox = QtGui.QGroupBox(self.centralwidget)
        self.visualizePeopleBox.setGeometry(QtCore.QRect(0, 0, 871, 551))
        self.visualizePeopleBox.setObjectName(_fromUtf8("visualizePeopleBox"))
        self.textBrowserPeople = QtGui.QTextBrowser(self.visualizePeopleBox)
        self.textBrowserPeople.setGeometry(QtCore.QRect(10, 30, 851, 501))
        self.textBrowserPeople.setObjectName(_fromUtf8("textBrowserPeople"))
        self.visualizePeopleBox.setVisible(0)
        ### --- ###

        ### Auxiliar functions ###
        def clearDictionary(dict):
            for key in dict.keys():
                dict[key] = None

        def clearWindow():
            self.addClientBox.setVisible(0)
            self.addEmployeeBox.setVisible(0)
            self.addSpecialistBox.setVisible(0)
            self.clientSucessOrFail.setVisible(0)
            self.visualizePeopleBox.setVisible(0)

        ### --- ###

        ### Client functions ###
        def clientAdd():
            clearWindow()
            self.addClientBox.setVisible(1)

        def checkInputClientAdd(client):
            if(client['name']=='a'): return False
            else: return True

        def inputClientAdd():
            global client
            client['name'] = self.clientNameLine.text()
            client['cpf'] = self.clientCpfLine.text()
            client['email'] = self.clientEmailLine.text()
            client['address'] = self.clientAddressLine.text()
            print(client)
            if (checkInputClientAdd(client)):
                self.clientSucessOrFail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Cliente inserido com sucesso</p></body></html>", None))
            else:
                self.clientSucessOrFail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Alguma informação é inválida!</p></body></html>", None))
            self.clientSucessOrFail.setVisible(1)
            clearDictionary(client)
        ### --- ###

        ### Employee functions ###
        def employeeAdd():
            clearWindow()
            self.addEmployeeBox.setVisible(1)

        def checkInputEmployeeAdd(employee):
            if(employee['name']=='a'): return False
            else: return True

        def inputEmployeeAdd():
            global employee
            employee['name'] = self.employeeNameLine.text()
            employee['cpf'] = self.employeeCpfLine.text()
            employee['email'] = self.employeeEmailLine.text()
            employee['address'] = self.employeeAddressLine.text()
            employee['salary'] = self.employeeSalaryLine.text()
            employee['function'] = self.employeeFunctionLine.text()
            print(employee)
            if (checkInputEmployeeAdd(employee)):
                self.employeeSucessOrFail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Funcionário inserido com sucesso</p></body></html>", None))
            else:
                self.employeeSucessOrFail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Alguma informação é inválida!</p></body></html>", None))
            self.employeeSucessOrFail.setVisible(1)
            clearDictionary(employee)
        ### --- ###

        ### Specialist functions ###
        def specialistAdd():
            clearWindow()
            self.addSpecialistBox.setVisible(1)

        def checkInputSpecialistAdd(specialist):
            if(specialist['name']=='a'): return False
            else: return True

        def inputSpecialistAdd():
            global specialist
            specialist['name'] = self.specialistNameLine.text()
            specialist['cpf'] = self.specialistCpfLine.text()
            specialist['email'] = self.specialistEmailLine.text()
            specialist['address'] = self.specialistAddressLine.text()
            specialist['specialty'] = self.specialistSpecialtyLine.text()
            specialist['hourFee'] = self.specialistHourFeeLine.text()
            print(specialist)
            if (checkInputSpecialistAdd(specialist)):
                self.specialistSucessOrFail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Especialista inserido com sucesso</p></body></html>", None))
            else:
                self.specialistSucessOrFail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Alguma informação é inválida!</p></body></html>", None))
            self.specialistSucessOrFail.setVisible(1)
            clearDictionary(specialist)
        ### --- ###

        ### VisualizePeople Function ###
        def showPeople():
            global textPeople
            clearWindow()
            self.textBrowserPeople.setText(textPeople)
            self.visualizePeopleBox.setVisible(1)
        ### --- ###





        ##Link the Buttons with the actions 
        self.retranslateUi(MainWindow)
        self.actionCliente.triggered.connect(clientAdd)
        self.actionFuncion_rios.triggered.connect(employeeAdd)
        self.actionEspecialista.triggered.connect(specialistAdd)
        self.actionVisualizar.triggered.connect(showPeople)
        self.actionAdicionar_2.triggered.connect(clientAdd)
        QtCore.QObject.connect(self.clientAddBtnSend, QtCore.SIGNAL(_fromUtf8("clicked()")), inputClientAdd)
        QtCore.QObject.connect(self.employeeAddBtnSend, QtCore.SIGNAL(_fromUtf8("clicked()")), inputEmployeeAdd)
        QtCore.QObject.connect(self.specialistAddBtnSend, QtCore.SIGNAL(_fromUtf8("clicked()")), inputSpecialistAdd)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "EventManager", None))
        
        self.menuGerenciar_Pessoas.setTitle(_translate("MainWindow", "Gerenciar Pessoas", None))
        self.menuAdicionar.setTitle(_translate("MainWindow", "Adicionar", None))
        self.menuGerenciar_Eventos.setTitle(_translate("MainWindow", "Gerenciar Eventos", None))
        self.menuGerenciar_Contatos.setTitle(_translate("MainWindow", "Gerenciar Contratos", None))
        self.menuGerenciar_Produtos.setTitle(_translate("MainWindow", "Gerenciar Operação", None))
        
        self.menuVisualizar.setTitle(_translate("MainWindow", "Visualizar", None))
        self.menuConsultas.setTitle(_translate("MainWindow", "Consultas", None))
        self.actionVisualizar.setText(_translate("MainWindow", "Visualizar", None))
        self.actionCliente.setText(_translate("MainWindow", "Cliente", None))
        self.actionFuncion_rios.setText(_translate("MainWindow", "Funcionário", None))
        self.actionEspecialista.setText(_translate("MainWindow", "Especialista", None))
        self.actionRemover.setText(_translate("MainWindow", "Remover", None))
        self.actionAdicionar_2.setText(_translate("MainWindow", "Adicionar", None))
        self.actionAlterar_2.setText(_translate("MainWindow", "Alterar", None))
        self.actionRemover_2.setText(_translate("MainWindow", "Remover", None))
        self.actionVisualizar_2.setText(_translate("MainWindow", "Visualizar", None))
        self.actionAlterar_3.setText(_translate("MainWindow", "Alterar", None))
        self.actionRemover_3.setText(_translate("MainWindow", "Remover", None))
        self.actionAdicionar_3.setText(_translate("MainWindow", "Adicionar", None))
        self.actionVisualizar_3.setText(_translate("MainWindow", "Visualizar", None))
        self.actionAlterar_4.setText(_translate("MainWindow", "Alterar", None))
        self.actionRemover_4.setText(_translate("MainWindow", "Remover", None))
        self.actionAdicionar_4.setText(_translate("MainWindow", "Adicionar", None))
        self.actionAlterar_5.setText(_translate("MainWindow", "Alterar", None))
        self.actionRemover_5.setText(_translate("MainWindow", "Remover", None))
        self.actionAdicionar_5.setText(_translate("MainWindow", "Adicionar", None))
        self.actionVisualizar_5.setText(_translate("MainWindow", "Visualizar", None))
        self.actionAlterar_6.setText(_translate("MainWindow", "Alterar", None))
        self.actionRemover_6.setText(_translate("MainWindow", "Remover", None))
        self.actionProdutos.setText(_translate("MainWindow", "Produtos", None))
        self.actionFornecedores.setText(_translate("MainWindow", "Fornecedores", None))
        self.actionCard_pios.setText(_translate("MainWindow", "Cardápios", None))
        self.actionItens_de_Card_pios.setText(_translate("MainWindow", "Itens de Cardápios", None))
        
        self.addClientBox.setTitle(_translate("MainWindow", "Adicionar cliente:", None))
        self.clientNameLabel.setText(_translate("MainWindow", "Nome:       ", None))
        self.clientCpfLabel.setText(_translate("MainWindow", "CPF:           ", None))
        self.clientAddressLabel.setText(_translate("MainWindow", "Endereço:", None))
        self.clientEmailLabel.setText(_translate("MainWindow", "Email:       ", None))
        self.clientAddBtnSend.setText(_translate("MainWindow", "Enviar", None))
        self.clientSucessOrFail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">?</p></body></html>", None))

        self.addEmployeeBox.setTitle(_translate("MainWindow", "Adicionar Funcionário", None))
        self.employeeNameLabel.setText(_translate("MainWindow", "Nome:       ", None))
        self.employeeCpfLabel.setText(_translate("MainWindow", "CPF:           ", None))
        self.employeeAddressLabel.setText(_translate("MainWindow", "Endereço:", None))
        self.employeeEmailLabel.setText(_translate("MainWindow", "Email:       ", None))
        self.employeeSalaryLabel.setText(_translate("MainWindow", "Salário:    ", None))
        self.employeeFunctionLabel.setText(_translate("MainWindow", "Função:   ", None))
        self.employeeAddBtnSend.setText(_translate("MainWindow", "Enviar", None))
        self.employeeSucessOrFail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">?</p></body></html>", None))
        
        self.addSpecialistBox.setTitle(_translate("MainWindow", "Adicionar Especialista", None))
        self.specialistNameLabel.setText(_translate("MainWindow", "Nome:               ", None))
        self.specialistCpfLabel.setText(_translate("MainWindow", "CPF:                   ", None))
        self.specialistAddressLabel.setText(_translate("MainWindow", "Endereço:        ", None))
        self.specialistEmailLabel.setText(_translate("MainWindow", "Email:               ", None))
        self.specialistSpecialtyLabel.setText(_translate("MainWindow", "Especialidade:", None))
        self.specialistHourFeeLabel.setText(_translate("MainWindow", "Taxa/hora:      ", None))
        self.specialistAddBtnSend.setText(_translate("MainWindow", "Enviar", None))
        self.specialistSucessOrFail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">?</p></body></html>", None))

        self.visualizePeopleBox.setTitle(_translate("MainWindow", "Visualização de Pessoas", None))

        self.eventTypeBox.setTitle(_translate("MainWindow", "Escolha o tipo de evento:", None))
        self.btnMarriage.setText(_translate("MainWindow", "Formatura", None))
        self.btnGraduation.setText(_translate("MainWindow", "Casamento", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

