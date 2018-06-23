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

graduation = {'client' : None, 'date' : None, 'value' : None, 'paymentMethod' : None, 'peopleNumber' : None, 'bartender' : None, 'cupbearer' : None, 'hall' : None}


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
        
        self.actionAlterar_2 = QtGui.QAction(MainWindow)
        self.actionAlterar_2.setObjectName(_fromUtf8("actionAlterar_2"))
        
        self.actionRemover_2 = QtGui.QAction(MainWindow)
        self.actionRemover_2.setObjectName(_fromUtf8("actionRemover_2"))
        
        self.actionVisualizar_2 = QtGui.QAction(MainWindow)
        self.actionVisualizar_2.setObjectName(_fromUtf8("actionVisualizar_2"))
        
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

        self.actionFormatura = QtGui.QAction(MainWindow)
        self.actionFormatura.setObjectName(_fromUtf8("actionFormatura"))
        
        self.actionCasamento = QtGui.QAction(MainWindow)
        self.actionCasamento.setObjectName(_fromUtf8("actionCasamento"))

        self.menuAdicionar_2 = QtGui.QMenu(self.menuGerenciar_Eventos)
        self.menuAdicionar_2.setObjectName(_fromUtf8("menuAdicionar_2"))

        self.menuAdicionar_2.addAction(self.actionFormatura)
        self.menuAdicionar_2.addAction(self.actionCasamento)

        self.menuGerenciar_Eventos.addAction(self.menuAdicionar_2.menuAction())

        self.actionFormatura_2 = QtGui.QAction(MainWindow)
        self.actionFormatura_2.setObjectName(_fromUtf8("actionFormatura_2"))
        
        self.actionCasamento_2 = QtGui.QAction(MainWindow)
        self.actionCasamento_2.setObjectName(_fromUtf8("actionCasamento_2"))

        self.menuAlterar = QtGui.QMenu(self.menuGerenciar_Eventos)
        self.menuAlterar.setObjectName(_fromUtf8("menuAlterar"))

        self.menuAlterar.addAction(self.actionFormatura_2)
        self.menuAlterar.addAction(self.actionCasamento_2)

        self.menuGerenciar_Eventos.addAction(self.menuAlterar.menuAction())
        
        self.menuAdicionar.addAction(self.actionCliente)
        self.menuAdicionar.addAction(self.actionFuncion_rios)
        self.menuAdicionar.addAction(self.actionEspecialista)
        
        self.menuGerenciar_Pessoas.addAction(self.menuAdicionar.menuAction())
        self.menuGerenciar_Pessoas.addAction(self.actionVisualizar)
        
        self.menuGerenciar_Eventos.addAction(self.actionVisualizar_2)
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

        ### Add Graduation ###
        self.addGraduationBox = QtGui.QGroupBox(self.centralwidget)
        self.addGraduationBox.setGeometry(QtCore.QRect(0, 0, 871, 581))
        self.addGraduationBox.setObjectName(_fromUtf8("addGraduationBox"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.addGraduationBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 871, 421))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        
        self.clientGraduation = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.clientGraduation.setObjectName(_fromUtf8("clientGraduation"))
        self.horizontalLayout_2.addWidget(self.clientGraduation)
        self.clientGraduationLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.clientGraduationLine.setObjectName(_fromUtf8("clientGraduationLine"))
        self.horizontalLayout_2.addWidget(self.clientGraduationLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        
        self.valueGraduation = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.valueGraduation.setObjectName(_fromUtf8("valueGraduation"))
        self.horizontalLayout_11.addWidget(self.valueGraduation)
        self.valueGraduationLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.valueGraduationLine.setObjectName(_fromUtf8("valueGraduationLine"))
        self.horizontalLayout_11.addWidget(self.valueGraduationLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        
        self.methodGraduation = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.methodGraduation.setObjectName(_fromUtf8("methodGraduation"))
        self.horizontalLayout_5.addWidget(self.methodGraduation)
        self.methodGraduationLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.methodGraduationLine.setObjectName(_fromUtf8("methodGraduationLine"))
        self.horizontalLayout_5.addWidget(self.methodGraduationLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        
        self.nPeopleGraduation = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.nPeopleGraduation.setObjectName(_fromUtf8("nPeopleGraduation"))
        self.horizontalLayout_6.addWidget(self.nPeopleGraduation)
        self.nPeopleGraduationLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.nPeopleGraduationLine.setObjectName(_fromUtf8("nPeopleGraduationLine"))
        self.horizontalLayout_6.addWidget(self.nPeopleGraduationLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        
        self.bartenderGraduation = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.bartenderGraduation.setObjectName(_fromUtf8("bartenderGraduation"))
        self.horizontalLayout_8.addWidget(self.bartenderGraduation)
        self.bartenderGraduationLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.bartenderGraduationLine.setObjectName(_fromUtf8("bartenderGraduationLine"))
        self.horizontalLayout_8.addWidget(self.bartenderGraduationLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        
        self.cupbearerGraduation = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.cupbearerGraduation.setObjectName(_fromUtf8("cupbearerGraduation"))
        self.horizontalLayout_10.addWidget(self.cupbearerGraduation)
        self.cupbearerGraduationLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.cupbearerGraduationLine.setObjectName(_fromUtf8("cupbearerGraduationLine"))
        self.horizontalLayout_10.addWidget(self.cupbearerGraduationLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        
        self.hallGraduation = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.hallGraduation.setObjectName(_fromUtf8("hallGraduation"))
        self.horizontalLayout_9.addWidget(self.hallGraduation)
        self.hallGraduationLine = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.hallGraduationLine.setObjectName(_fromUtf8("hallGraduationLine"))
        self.horizontalLayout_9.addWidget(self.hallGraduationLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        
        self.dateGraduation = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.dateGraduation.setObjectName(_fromUtf8("dateGraduation"))
        self.horizontalLayout_4.addWidget(self.dateGraduation)
        self.dateGraduationLine = QtGui.QDateTimeEdit(self.verticalLayoutWidget_2)
        self.dateGraduationLine.setObjectName(_fromUtf8("dateGraduationLine"))
        self.horizontalLayout_4.addWidget(self.dateGraduationLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        
        self.graduationAddBtnSend = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.graduationAddBtnSend.setObjectName(_fromUtf8("graduationAddBtnSend"))
        self.verticalLayout_3.addWidget(self.graduationAddBtnSend)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.graduationSucessOrFail = QtGui.QLabel(self.addGraduationBox)
        self.graduationSucessOrFail.setGeometry(QtCore.QRect(-10, 430, 869, 49))
        self.graduationSucessOrFail.setObjectName(_fromUtf8("label"))

        self.graduationSucessOrFail.setVisible(0)
        self.addGraduationBox.setVisible(0)
        ### --- ###

        ### Update Graduation ###
        self.updateGraduationBox = QtGui.QGroupBox(self.centralwidget)
        self.updateGraduationBox.setGeometry(QtCore.QRect(0, 0, 871, 581))
        self.updateGraduationBox.setObjectName(_fromUtf8("updateGraduationBox"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.updateGraduationBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 871, 421))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        
        self.clientGraduationUpdate = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.clientGraduationUpdate.setObjectName(_fromUtf8("clientGraduationUpdate"))
        self.horizontalLayout_2.addWidget(self.clientGraduationUpdate)
        self.clientGraduationLineUpdate = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.clientGraduationLineUpdate.setObjectName(_fromUtf8("clientGraduationLineUpdate"))
        self.horizontalLayout_2.addWidget(self.clientGraduationLineUpdate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        
        self.valueGraduationUpdate = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.valueGraduationUpdate.setObjectName(_fromUtf8("valueGraduationUpdate"))
        self.horizontalLayout_11.addWidget(self.valueGraduationUpdate)
        self.valueGraduationLineUpdate = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.valueGraduationLineUpdate.setObjectName(_fromUtf8("valueGraduationLineUpdate"))
        self.horizontalLayout_11.addWidget(self.valueGraduationLineUpdate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        
        self.methodGraduationUpdate = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.methodGraduationUpdate.setObjectName(_fromUtf8("methodGraduationUpdate"))
        self.horizontalLayout_5.addWidget(self.methodGraduationUpdate)
        self.methodGraduationLineUpdate = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.methodGraduationLineUpdate.setObjectName(_fromUtf8("methodGraduationLineUpdate"))
        self.horizontalLayout_5.addWidget(self.methodGraduationLineUpdate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        
        self.nPeopleGraduationUpdate = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.nPeopleGraduationUpdate.setObjectName(_fromUtf8("nPeopleGraduationUpdate"))
        self.horizontalLayout_6.addWidget(self.nPeopleGraduationUpdate)
        self.nPeopleGraduationLineUpdate = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.nPeopleGraduationLineUpdate.setObjectName(_fromUtf8("nPeopleGraduationLineUpdate"))
        self.horizontalLayout_6.addWidget(self.nPeopleGraduationLineUpdate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        
        self.bartenderGraduationUpdate = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.bartenderGraduationUpdate.setObjectName(_fromUtf8("bartenderGraduationUpdate"))
        self.horizontalLayout_8.addWidget(self.bartenderGraduationUpdate)
        self.bartenderGraduationLineUpdate = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.bartenderGraduationLineUpdate.setObjectName(_fromUtf8("bartenderGraduationLineUpdate"))
        self.horizontalLayout_8.addWidget(self.bartenderGraduationLineUpdate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        
        self.cupbearerGraduationUpdate = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.cupbearerGraduationUpdate.setObjectName(_fromUtf8("cupbearerGraduationUpdate"))
        self.horizontalLayout_10.addWidget(self.cupbearerGraduationUpdate)
        self.cupbearerGraduationLineUpdate = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.cupbearerGraduationLineUpdate.setObjectName(_fromUtf8("cupbearerGraduationLineUpdate"))
        self.horizontalLayout_10.addWidget(self.cupbearerGraduationLineUpdate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        
        self.hallGraduationUpdate = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.hallGraduationUpdate.setObjectName(_fromUtf8("hallGraduationUpdate"))
        self.horizontalLayout_9.addWidget(self.hallGraduationUpdate)
        self.hallGraduationLineUpdate = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.hallGraduationLineUpdate.setObjectName(_fromUtf8("hallGraduationLineUpdate"))
        self.horizontalLayout_9.addWidget(self.hallGraduationLineUpdate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        
        self.dateGraduationUpdate = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.dateGraduationUpdate.setObjectName(_fromUtf8("dateGraduationUpdate"))
        self.horizontalLayout_4.addWidget(self.dateGraduationUpdate)
        self.dateGraduationLineUpdate = QtGui.QDateTimeEdit(self.verticalLayoutWidget_2)
        self.dateGraduationLineUpdate.setObjectName(_fromUtf8("dateGraduationLineUpdate"))
        self.horizontalLayout_4.addWidget(self.dateGraduationLineUpdate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        
        self.graduationUpdateBtnSend = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.graduationUpdateBtnSend.setObjectName(_fromUtf8("graduationUpdateBtnSend"))
        self.verticalLayout_3.addWidget(self.graduationUpdateBtnSend)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.graduationSucessOrFailUpdate = QtGui.QLabel(self.updateGraduationBox)
        self.graduationSucessOrFailUpdate.setGeometry(QtCore.QRect(-10, 430, 869, 49))
        self.graduationSucessOrFailUpdate.setObjectName(_fromUtf8("graduationSucessOrFailUpdate"))

        self.graduationSucessOrFailUpdate.setVisible(0)
        self.updateGraduationBox.setVisible(0)
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
            self.graduationSucessOrFail.setVisible(0)
            self.addGraduationBox.setVisible(0)
            self.updateGraduationBox.setVisible(0)

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

        ### Graduation functions ###
        def graduationAdd():
            clearWindow()
            self.addGraduationBox.setVisible(1)

        def checkInputGraduationAdd(graduation):
            if(graduation['client'] =='a'): return False
            else: return True

        def inputGraduationAdd():
            global graduation
            graduation['client'] = self.clientGraduationLine.text()
            graduation['date'] = self.dateGraduationLine.text()
            graduation['value'] = self.valueGraduationLine.text()
            graduation['paymentMethod'] = self.methodGraduationLine.text()
            graduation['peopleNumber'] = self.nPeopleGraduationLine.text()
            graduation['bartender'] = self.bartenderGraduationLine.text()
            graduation['cupbearer'] = self.cupbearerGraduationLine.text()
            graduation['hall'] = self.hallGraduationLine.text()
            print(graduation)
            if (checkInputGraduationAdd(graduation)):
                self.graduationSucessOrFail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Formatura inserida com sucesso</p></body></html>", None))
            else:
                self.graduationSucessOrFail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Alguma informação é inválida!</p></body></html>", None))
            self.graduationSucessOrFail.setVisible(1)
            clearDictionary(graduation)

        def graduationUpdate():
            clearWindow()
            self.updateGraduationBox.setVisible(1)

        def checkInputGraduationUpdate(graduation):
            if(graduation['client'] =='a'): return False
            else: return True

        def inputGraduationUpdate():
            global graduation
            graduation['client'] = self.clientGraduationLineUpdate.text()
            graduation['date'] = self.dateGraduationLineUpdate.text()
            graduation['value'] = self.valueGraduationLineUpdate.text()
            graduation['paymentMethod'] = self.methodGraduationLineUpdate.text()
            graduation['peopleNumber'] = self.nPeopleGraduationLineUpdate.text()
            graduation['bartender'] = self.bartenderGraduationLineUpdate.text()
            graduation['cupbearer'] = self.cupbearerGraduationLineUpdate.text()
            graduation['hall'] = self.hallGraduationLineUpdate.text()
            print(graduation)
            if (checkInputGraduationUpdate(graduation)):
                self.graduationSucessOrFailUpdate.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Formatura atualizada com sucesso</p></body></html>", None))
            else:
                self.graduationSucessOrFailUpdate.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Alguma informação é inválida!</p></body></html>", None))
            self.graduationSucessOrFailUpdate.setVisible(1)
            clearDictionary(graduation)
        ### --- ###





        ##Link the Buttons with the actions 
        self.retranslateUi(MainWindow)
        self.actionCliente.triggered.connect(clientAdd)
        self.actionFuncion_rios.triggered.connect(employeeAdd)
        self.actionEspecialista.triggered.connect(specialistAdd)
        self.actionVisualizar.triggered.connect(showPeople)
        self.actionFormatura.triggered.connect(graduationAdd)
        self.actionFormatura_2.triggered.connect(graduationUpdate)
        self.actionCasamento.triggered.connect(clientAdd)
        self.actionCasamento_2.triggered.connect(clientAdd)

        QtCore.QObject.connect(self.clientAddBtnSend, QtCore.SIGNAL(_fromUtf8("clicked()")), inputClientAdd)
        QtCore.QObject.connect(self.employeeAddBtnSend, QtCore.SIGNAL(_fromUtf8("clicked()")), inputEmployeeAdd)
        QtCore.QObject.connect(self.specialistAddBtnSend, QtCore.SIGNAL(_fromUtf8("clicked()")), inputSpecialistAdd)
        QtCore.QObject.connect(self.graduationAddBtnSend, QtCore.SIGNAL(_fromUtf8("clicked()")), inputGraduationAdd)
        QtCore.QObject.connect(self.graduationUpdateBtnSend, QtCore.SIGNAL(_fromUtf8("clicked()")), inputGraduationUpdate)
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
        self.actionAlterar_2.setText(_translate("MainWindow", "Alterar", None))
        self.actionRemover_2.setText(_translate("MainWindow", "Remover", None))
        self.actionVisualizar_2.setText(_translate("MainWindow", "Visualizar", None))
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

        self.menuAdicionar_2.setTitle(_translate("MainWindow", "Adicionar", None))
        self.menuAlterar.setTitle(_translate("MainWindow", "Alterar", None))
        self.actionFormatura.setText(_translate("MainWindow", "Formatura", None))
        self.actionCasamento.setText(_translate("MainWindow", "Casamento", None))
        self.actionFormatura_2.setText(_translate("MainWindow", "Formatura", None))
        self.actionCasamento_2.setText(_translate("MainWindow", "Casamento", None))

        self.addGraduationBox.setTitle(_translate("MainWindow", "Adicionar Formatura", None))
        self.clientGraduation.setText(_translate("MainWindow", "Cliente:                                   ", None))
        self.valueGraduation.setText(_translate("MainWindow", "Valor:                                     ", None))
        self.methodGraduation.setText(_translate("MainWindow", "Metodo de Pagamento:    ", None))
        self.nPeopleGraduation.setText(_translate("MainWindow", "Número de Pessoas:         ", None))
        self.bartenderGraduation.setText(_translate("MainWindow", "Bartender:                          ", None))
        self.cupbearerGraduation.setText(_translate("MainWindow", "Copeiro:                              ", None))
        self.hallGraduation.setText(_translate("MainWindow", "Salão:                                  ", None))
        self.dateGraduation.setText(_translate("MainWindow", "Data:", None))
        self.graduationAddBtnSend.setText(_translate("MainWindow", "Enviar", None))
        
        self.graduationSucessOrFail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">?</p></body></html>", None))
        self.updateGraduationBox.setTitle(_translate("MainWindow", "Alterar Formatura", None))
        self.clientGraduationUpdate.setText(_translate("MainWindow", "Cliente:                                   ", None))
        self.valueGraduationUpdate.setText(_translate("MainWindow", "Valor:                                     ", None))
        self.methodGraduationUpdate.setText(_translate("MainWindow", "Metodo de Pagamento:    ", None))
        self.nPeopleGraduationUpdate.setText(_translate("MainWindow", "Número de Pessoas:         ", None))
        self.bartenderGraduationUpdate.setText(_translate("MainWindow", "Bartender:                          ", None))
        self.cupbearerGraduationUpdate.setText(_translate("MainWindow", "Copeiro:                              ", None))
        self.hallGraduationUpdate.setText(_translate("MainWindow", "Salão:                                  ", None))
        self.dateGraduationUpdate.setText(_translate("MainWindow", "Data:", None))
        self.graduationSucessOrFailUpdate.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">?</p></body></html>", None))
        self.graduationUpdateBtnSend.setText(_translate("MainWindow", "Enviar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())