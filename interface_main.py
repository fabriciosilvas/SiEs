# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QRectF, QPointF)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDoubleSpinBox, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolBox, QVBoxLayout, QWidget, QGraphicsScene, QFormLayout)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(938, 593)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, -1, 0, -1)
        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, -1, 9)
        self.header = QFrame(self.main_container)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 9, 9)
        self.togle = QPushButton(self.header)
        self.togle.setObjectName(u"togle")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.togle.setIcon(icon)
        self.togle.setIconSize(QSize(32, 32))
        self.togle.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.togle, 0, Qt.AlignLeft)

        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.header)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_11 = QVBoxLayout(self.pg_home)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.pg_home)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_11.addWidget(self.label_4)

        self.label_9 = QLabel(self.pg_home)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_9)

        self.label_10 = QLabel(self.pg_home)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_11.addWidget(self.label_10, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.pg_home)
        self.pg_criar = QWidget()
        self.pg_criar.setObjectName(u"pg_criar")
        self.verticalLayout_6 = QVBoxLayout(self.pg_criar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.PROCESSOS = QTabWidget(self.pg_criar)
        self.PROCESSOS.setObjectName(u"PROCESSOS")
        self.PROCESSOS.setCursor(QCursor(Qt.PointingHandCursor))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(220,220,220);\n"
"\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"color:rgb(242,80,34);")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 2)

        self.lineEdit_6 = QLineEdit(self.frame_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 40))
        self.lineEdit_6.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout.addWidget(self.lineEdit_6, 4, 0, 1, 1)

        self.le_execucao = QLineEdit(self.frame_4)
        self.le_execucao.setObjectName(u"le_execucao")
        self.le_execucao.setMinimumSize(QSize(0, 40))
        self.le_execucao.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout.addWidget(self.le_execucao, 2, 0, 1, 1)

        self.le_qtdpaginas = QLineEdit(self.frame_4)
        self.le_qtdpaginas.setObjectName(u"le_qtdpaginas")
        self.le_qtdpaginas.setMinimumSize(QSize(0, 40))
        self.le_qtdpaginas.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout.addWidget(self.le_qtdpaginas, 1, 1, 1, 1)

        self.le_deadline = QLineEdit(self.frame_4)
        self.le_deadline.setObjectName(u"le_deadline")
        self.le_deadline.setMinimumSize(QSize(0, 40))
        self.le_deadline.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout.addWidget(self.le_deadline, 4, 1, 1, 1)

        self.le_chegada = QLineEdit(self.frame_4)
        self.le_chegada.setObjectName(u"le_chegada")
        self.le_chegada.setMinimumSize(QSize(0, 40))
        self.le_chegada.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout.addWidget(self.le_chegada, 2, 1, 1, 1)

        self.label_id = QLabel(self.frame_4)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setStyleSheet(u"background-color:rgb(255,255,255);")

        self.gridLayout.addWidget(self.label_id, 1, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.bt_criarprocesso = QPushButton(self.tab)
        self.bt_criarprocesso.setObjectName(u"bt_criarprocesso")
        self.bt_criarprocesso.setMinimumSize(QSize(160, 30))
        self.bt_criarprocesso.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_criarprocesso.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(242,80,34);\n"
"	border-radius: 15px;\n"
"	color:#fff;\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(197,197,197);\n"
"	border-radius: 15px;\n"
"}")

        self.verticalLayout_9.addWidget(self.bt_criarprocesso, 0, Qt.AlignHCenter)

        self.PROCESSOS.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"color:rgb(242,80,34);")

        self.verticalLayout_8.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	background-color:rgb(148,148,148);\n"
"	color:rgb(255,255,255);\n"
"	font:10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color:rgb(252,252,252);\n"
"}")
        self.tableWidget.setInputMethodHints(Qt.ImhDigitsOnly)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	border-radius:15px;\n"
"	background-color:rgb(197,197,197);\n"
"	font:11pt \"MS Shell Dig 2\";\n"
"}\n"
"QFrame{\n"
"	background-color:rgb(220,220,220);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(242,80,34);\n"
"	border-radius: 15px;\n"
"	color:#fff;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 15, 5, -1)
        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(160, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.PROCESSOS.addTab(self.tab_2, "")

        self.verticalLayout_6.addWidget(self.PROCESSOS)

        self.stackedWidget.addWidget(self.pg_criar)
        self.pg_executar = QWidget()
        self.pg_executar.setObjectName(u"pg_executar")
        self.gridLayout_4 = QGridLayout(self.pg_executar)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_5 = QFrame(self.pg_executar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Panel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_12.addWidget(self.label_11)

        self.slt_escalonamento = QComboBox(self.frame_7)
        self.slt_escalonamento.addItem("")
        self.slt_escalonamento.addItem("")
        self.slt_escalonamento.addItem("")
        self.slt_escalonamento.addItem("")
        self.slt_escalonamento.addItem("")
        self.slt_escalonamento.setObjectName(u"slt_escalonamento")
        self.slt_escalonamento.setStyleSheet(u"\n"
"QComboBox {\n"
"	background-color:rgb(220,220,220);\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color:rgb(127,186,0);\n"
"}\n"
"\n"
"\n"
"")

        self.slt_escalonamento.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.slt_escalonamento)


        self.gridLayout_3.addWidget(self.frame_7, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_13.addWidget(self.label_12)

        self.slt_paginacao = QComboBox(self.frame_8)
        self.slt_paginacao.addItem("")
        self.slt_paginacao.addItem("")
        self.slt_paginacao.addItem("")
        self.slt_paginacao.setObjectName(u"slt_paginacao")
        self.slt_paginacao.setCursor(QCursor(Qt.PointingHandCursor))
        self.slt_paginacao.setStyleSheet(u"\n"
"QComboBox {\n"
"	background-color:rgb(220,220,220);\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color:rgb(127,186,0);\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_13.addWidget(self.slt_paginacao)


        self.gridLayout_3.addWidget(self.frame_8, 0, 1, 1, 1)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.le_quantum = QLineEdit(self.frame_9)
        self.le_quantum.setObjectName(u"le_quantum")
        self.le_quantum.setStyleSheet(u"background-color:rgb(220,220,220);")
        self.le_quantum.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.le_quantum, 0, 0, 1, 1)

        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color:rgb(220,220,220);")
        self.lineEdit_2.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 0, 1, 1)

        self.box_delay = QDoubleSpinBox(self.frame_9)
        self.box_delay.setObjectName(u"box_delay")
        self.box_delay.setCursor(QCursor(Qt.PointingHandCursor))
        self.box_delay.setMinimum(0.250000000000000)
        self.box_delay.setMaximum(5.000000000000000)
        self.box_delay.setSingleStep(0.250000000000000)
        self.box_delay.setValue(0.250000000000000)
        self.box_delay.setStyleSheet(u"QDoubleSpinBox {\n"
"background-color:rgb(220,220,220);\n"
"    padding-right: 15px; /* make room for the arrows */\n"
"    border-width: 3;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::up-arrow {\n"
"	\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_2.addWidget(self.box_delay, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_9, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.pg_executar)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Panel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.bt_executar = QPushButton(self.frame_6)
        self.bt_executar.setObjectName(u"bt_executar")
        self.bt_executar.setMinimumSize(QSize(160, 30))
        self.bt_executar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_executar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(128,204,40);\n"
"	border-radius: 15px;\n"
"	color:#fff;\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(197,197,197);\n"
"	border-radius: 15px;\n"
"}")

        self.verticalLayout_19.addWidget(self.bt_executar)
        
        self.bt_reiniciar = QPushButton(self.frame_6)
        self.bt_reiniciar.setObjectName(u"bt_reiniciar")
        self.bt_reiniciar.setMinimumSize(QSize(160, 30))
        self.bt_reiniciar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(128,204,40);\n"
"	border-radius: 15px;\n"
"	color:#fff;\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(197,197,197);\n"
"	border-radius: 15px;\n"
"}")

        self.verticalLayout_19.addWidget(self.bt_reiniciar)


        self.gridLayout_4.addWidget(self.frame_6, 0, 1, 1, 1)

        self.cpu = QFrame(self.pg_executar)
        self.cpu.setObjectName(u"cpu")
        self.cpu.setFrameShape(QFrame.Panel)
        self.cpu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.cpu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_10 = QFrame(self.cpu)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_17 = QLabel(self.frame_10)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_14.addWidget(self.label_17)

        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_14.addWidget(self.label_14, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.pgs_execucao = QProgressBar(self.frame_10)
        self.pgs_execucao.setObjectName(u"pgs_execucao")
        self.pgs_execucao.setStyleSheet(u" QProgressBar {\n"
"        border: 2px solid rgba(33, 37, 43, 180);\n"
"        border-radius: 5px;\n"
"        text-align: center;\n"
"        background-color: rgba(33, 37, 43, 180);\n"
"        color: black;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: #7FBA00;\n"
"    }")
        self.pgs_execucao.setValue(0)
        self.pgs_execucao.setTextVisible(False)

        self.verticalLayout_14.addWidget(self.pgs_execucao)

        self.lb_cpu_id_e = QLabel(self.frame_10)
        self.lb_cpu_id_e.setObjectName(u"lb_cpu_id_e")

        self.verticalLayout_14.addWidget(self.lb_cpu_id_e)

        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_14.addWidget(self.label_15)

        self.pgs_bloqueado = QProgressBar(self.frame_10)
        self.pgs_bloqueado.setObjectName(u"pgs_bloqueado")
        self.pgs_bloqueado.setStyleSheet(u" QProgressBar {\n"
"        border: 2px solid rgba(33, 37, 43, 180);\n"
"        border-radius: 5px;\n"
"        text-align: center;\n"
"        background-color: rgba(33, 37, 43, 180);\n"
"        color: black;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: #FFB900;\n"
"    }")
        self.pgs_bloqueado.setValue(0)
        self.pgs_bloqueado.setTextVisible(False)

        self.verticalLayout_14.addWidget(self.pgs_bloqueado)

        self.lb_cpu_id_b = QLabel(self.frame_10)
        self.lb_cpu_id_b.setObjectName(u"lb_cpu_id_b")

        self.verticalLayout_14.addWidget(self.lb_cpu_id_b)

        self.label_20 = QLabel(self.frame_10)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_14.addWidget(self.label_20)

        self.pgs_sobrecarga = QProgressBar(self.frame_10)
        self.pgs_sobrecarga.setObjectName(u"pgs_sobrecarga")
        self.pgs_sobrecarga.setStyleSheet(u" QProgressBar {\n"
"        border: 2px solid rgba(33, 37, 43, 180);\n"
"        border-radius: 5px;\n"
"        text-align: center;\n"
"        background-color: rgba(33, 37, 43, 180);\n"
"        color: black;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: #F25022;\n"
"    }")
        self.pgs_sobrecarga.setValue(0)
        self.pgs_sobrecarga.setTextVisible(False)

        self.verticalLayout_14.addWidget(self.pgs_sobrecarga)


        self.horizontalLayout.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.cpu)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lb_tempo = QLabel(self.frame_11)
        self.lb_tempo.setObjectName(u"lb_tempo")

        self.verticalLayout_15.addWidget(self.lb_tempo)

        self.label_16 = QLabel(self.frame_11)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_15.addWidget(self.label_16)

        self.lista_prontos = QTableWidget(self.frame_11)
        if (self.lista_prontos.columnCount() < 6):
            self.lista_prontos.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.lista_prontos.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.lista_prontos.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.lista_prontos.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.lista_prontos.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.lista_prontos.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.lista_prontos.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.lista_prontos.setObjectName(u"lista_prontos")
        self.lista_prontos.setStyleSheet(u"QHeaderView::section{\n"
"	background-color:rgb(197,197,197);\n"
"	color:rgb(0,0,0);\n"
"	font:10pt \"MS Shell Dig 2\";\n"
"}")
        self.lista_prontos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lista_prontos.horizontalHeader().setMinimumSectionSize(45)
        self.lista_prontos.horizontalHeader().setDefaultSectionSize(45)

        self.verticalLayout_15.addWidget(self.lista_prontos)


        self.horizontalLayout.addWidget(self.frame_11)


        self.gridLayout_4.addWidget(self.cpu, 0, 2, 2, 1)

        self.ram = QFrame(self.pg_executar)
        self.ram.setObjectName(u"ram")
        self.ram.setMinimumSize(QSize(0, 140))
        self.ram.setFrameShape(QFrame.Panel)
        self.ram.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.ram)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.label_18 = QLabel(self.ram)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_16.addWidget(self.label_18, 0, Qt.AlignVCenter)

        self.tabela_ram = QTableWidget(self.ram)
        if (self.tabela_ram.columnCount() < 10):
            self.tabela_ram.setColumnCount(10)
        if (self.tabela_ram.rowCount() < 5):
            self.tabela_ram.setRowCount(5)
        self.tabela_ram.setObjectName(u"tabela_ram")
        self.tabela_ram.setMaximumSize(QSize(16777192, 16777215))
        self.tabela_ram.setFrameShape(QFrame.NoFrame)
        self.tabela_ram.setLineWidth(-1)
        self.tabela_ram.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tabela_ram.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tabela_ram.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tabela_ram.setAutoScroll(True)
        self.tabela_ram.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_ram.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tabela_ram.setShowGrid(True)
        self.tabela_ram.setRowCount(5)
        self.tabela_ram.setColumnCount(10)
        self.tabela_ram.horizontalHeader().setVisible(False)
        self.tabela_ram.horizontalHeader().setMinimumSectionSize(46)
        self.tabela_ram.horizontalHeader().setDefaultSectionSize(46)
        self.tabela_ram.verticalHeader().setVisible(False)
        self.tabela_ram.verticalHeader().setMinimumSectionSize(24)
        self.tabela_ram.verticalHeader().setDefaultSectionSize(24)
        self.tabela_ram.verticalHeader().setHighlightSections(True)

        self.verticalLayout_16.addWidget(self.tabela_ram, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridLayout_4.addWidget(self.ram, 1, 0, 2, 2, Qt.AlignVCenter)

        '''self.graantgrafico = QFrame(self.pg_executar)
        self.graantgrafico.setObjectName(u"graantgrafico")
        self.graantgrafico.setFrameShape(QFrame.Panel)
        self.graantgrafico.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.graantgrafico)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_22 = QLabel(self.graantgrafico)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_18.addWidget(self.label_22)

        self.fm_graficograant = QGraphicsView(self.graantgrafico)
        self.fm_graficograant.setObjectName(u"fm_graficograant")'''
        
        self.graantgrafico = QFrame(self.pg_executar)
        self.graantgrafico.setObjectName(u"graantgrafico")
        self.graantgrafico.setFrameShape(QFrame.Panel)
        self.graantgrafico.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.graantgrafico)
        self.formLayout.setObjectName(u"formLayout")
        self.label_22 = QLabel(self.graantgrafico)
        self.label_22.setObjectName(u"label_22")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_22)

        self.fm_graficograant = QGraphicsView(self.graantgrafico)
        self.fm_graficograant.setObjectName(u"fm_graficograant")

        self.fm_idsvisu = QGraphicsView(self.graantgrafico)
        self.fm_idsvisu.setObjectName(u"fm_idsvisu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fm_idsvisu.sizePolicy().hasHeightForWidth())
        self.fm_idsvisu.setSizePolicy(sizePolicy1)
        self.fm_idsvisu.setMinimumSize(QSize(40, 0))
        self.fm_idsvisu.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_4.addWidget(self.graantgrafico, 2, 2, 2, 1)
        
        
        
        
        #self.cena = QGraphicsScene(0,0,460,230) 
        self.rect = QRectF(0,0,400,250)
        #self.rect.al
        self.cena = QGraphicsScene(self.rect) 
        
        #self.fm_graficograant.setAlignment(Qt.AlignTop) 
        
        self.rect1 = QRectF(0,0,18,250)
        #self.rect.al
        self.cena1 = QGraphicsScene(self.rect1) 
         
        self.fm_graficograant.setScene(self.cena)
        self.fm_idsvisu.setScene(self.cena1)
        
        self.fm_graficograant.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.fm_idsvisu.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        

        self.fm_idsvisu.verticalScrollBar().setMaximumSize(QSize(3, 16777215))
        self.fm_idsvisu.setLayoutDirection(Qt.RightToLeft)
        
        
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.fm_graficograant)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.fm_idsvisu)
        


        self.gridLayout_4.addWidget(self.graantgrafico, 2, 2, 2, 1)

        self.disco = QFrame(self.pg_executar)
        self.disco.setObjectName(u"disco")
        self.disco.setFrameShape(QFrame.Panel)
        self.disco.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.disco)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.label_19 = QLabel(self.disco)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_17.addWidget(self.label_19)

        self.tb_disco = QTableWidget(self.disco)
        if (self.tb_disco.columnCount() < 15):
            self.tb_disco.setColumnCount(15)
        if (self.tb_disco.rowCount() < 10):
            self.tb_disco.setRowCount(10)
        self.tb_disco.setObjectName(u"tb_disco")
        self.tb_disco.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tb_disco.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tb_disco.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tb_disco.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_disco.setRowCount(10)
        self.tb_disco.setColumnCount(15)
        self.tb_disco.horizontalHeader().setVisible(False)
        self.tb_disco.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_disco.horizontalHeader().setMinimumSectionSize(36)
        self.tb_disco.horizontalHeader().setDefaultSectionSize(36)
        self.tb_disco.verticalHeader().setVisible(False)
        self.tb_disco.verticalHeader().setDefaultSectionSize(25)

        self.verticalLayout_17.addWidget(self.tb_disco)


        self.gridLayout_4.addWidget(self.disco, 3, 0, 1, 2, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.pg_executar)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_10 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.pg_sobre)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_10.addWidget(self.label_7)

        self.label_8 = QLabel(self.pg_sobre)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_10.addWidget(self.label_8)

        self.stackedWidget.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer = QFrame(self.main_container)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, 0)
        self.label_2 = QLabel(self.footer)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer)


        self.gridLayout_5.addWidget(self.main_container, 0, 1, 1, 1)

        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMinimumSize(QSize(0, 0))
        self.left_container.setMaximumSize(QSize(9, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 0, -1)
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, -1, 0, 9)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(220,220,220);\n"
"}\n"
"QToolBox{\n"
"	text-align: left;\n"
"	background-color:rgb(211,211,211);\n"
"}\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	background-color:rgb(220,220,220);\n"
"	text-align: left;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 9, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(8)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0,164,239);\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"QPushButton{\n"
"	border-radius:15px;\n"
"	background-color:rgb(255,255,255);\n"
"	font:11pt \"MS Shell Dig 2\";\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 160, 437))
        self.page.setMinimumSize(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(60, 30))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dig 2"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setIconSize(QSize(16, 16))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_criar = QPushButton(self.page)
        self.btn_criar.setObjectName(u"btn_criar")
        self.btn_criar.setMinimumSize(QSize(0, 30))
        self.btn_criar.setFont(font1)
        self.btn_criar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_criar)

        self.btn_executar = QPushButton(self.page)
        self.btn_executar.setObjectName(u"btn_executar")
        self.btn_executar.setMinimumSize(QSize(0, 30))
        self.btn_executar.setFont(font1)
        self.btn_executar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_executar)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setFont(font1)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 16, 437))
        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.gridLayout_5.addWidget(self.left_container, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.PROCESSOS.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.togle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/nome10.png\"/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/ln4.png\"/></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/><span style=\" font-size:11pt;\">Bem-vindo ao SiEs!</span></p><p align=\"justify\"><br/></p><p align=\"justify\"><span style=\" font-size:11pt; font-style:italic;\">Para uma melhor experi\u00eancia, execute o programa em tela cheia.</span></p><p align=\"justify\"><span style=\" font-size:11pt;\"><br/></span></p><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">INSTRU\u00c7\u00d5ES:</span><span style=\" font-size:11pt;\"><br/></span></p><p align=\"justify\"><span style=\" font-size:11pt;\">1. Para criar processos, v\u00e1 at\u00e9 a aba Criar e preencha todas as informa\u00e7\u00f5es necess\u00e1rias;</span></p><p align=\"justify\"><span style=\" font-size:11pt;\">2. Ap\u00f3s adicionar todos os processos, v\u00e1 at\u00e9 a aba Executar;</span></p><p align=\"justify\"><span style=\" font-size:11pt;\">3. Preencha as informa\u00e7\u00f5es restantes, al\u00e9m de selecionar os respectivos algoritmos de escalonamento e substitui\u00e7\u00e3o de p\u00e1"
                        "gina;</span></p><p align=\"justify\"><span style=\" font-size:11pt;\">4. Por fim, aperte no bot\u00e3o Executar para visualizar o funcionamento da aplica\u00e7\u00e3o;</span></p><p align=\"justify\"><span style=\" font-size:11pt;\">5. Ao fim da execu\u00e7\u00e3o, uma janela ser\u00e1 aberta exibindo o turnaround. Caso n\u00e3o a visualize, verifique se ela n\u00e3o aparece por detr\u00e1s da janela principal.</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Desenvolvido por Fabr\u00edcio Silva.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">CRIA\u00c7\u00c3O DE PROCESSOS</span></p></body></html>", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prioridade", None))
        self.le_execucao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tempo de execu\u00e7\u00e3o", None))
        self.le_qtdpaginas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantidade de p\u00e1ginas", None))
        self.le_deadline.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Deadline", None))
        self.le_chegada.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tempo de chegada", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bt_criarprocesso.setText(QCoreApplication.translate("MainWindow", u"Criar processo", None))
        self.PROCESSOS.setTabText(self.PROCESSOS.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Criar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">PROCESSOS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T. CHEGADA", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"T.EXECU\u00c7\u00c3O", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"DEADLINE", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"PRIORIDADE", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"N\u00ba P\u00c1GINAS", None));
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.PROCESSOS.setTabText(self.PROCESSOS.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Processos criados", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Escalonamento</p></body></html>", None))
        self.slt_escalonamento.setItemText(0, QCoreApplication.translate("MainWindow", u"- Selecione -", None))
        self.slt_escalonamento.setItemText(1, QCoreApplication.translate("MainWindow", u"FIFO", None))
        self.slt_escalonamento.setItemText(2, QCoreApplication.translate("MainWindow", u"SJF", None))
        self.slt_escalonamento.setItemText(3, QCoreApplication.translate("MainWindow", u"Round Robin", None))
        self.slt_escalonamento.setItemText(4, QCoreApplication.translate("MainWindow", u"EDF", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Subs. de p\u00e1gina</p></body></html>", None))
        self.slt_paginacao.setItemText(0, QCoreApplication.translate("MainWindow", u"- Selecione -", None))
        self.slt_paginacao.setItemText(1, QCoreApplication.translate("MainWindow", u"FIFO", None))
        self.slt_paginacao.setItemText(2, QCoreApplication.translate("MainWindow", u"LRU", None))

        self.le_quantum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantum", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Delay</p></body></html>", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sobrecarga", None))
        self.bt_executar.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.bt_reiniciar.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">CPU</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Executando", None))
        self.lb_cpu_id_e.setText(QCoreApplication.translate("MainWindow", u"ID: ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Bloqueado</p></body></html>", None))
        self.lb_cpu_id_b.setText(QCoreApplication.translate("MainWindow", u"ID: ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Sobrecarga</p></body></html>", None))
        self.lb_tempo.setText(QCoreApplication.translate("MainWindow", u"Tempo:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Prontos</span></p></body></html>", None))
        ___qtablewidgetitem6 = self.lista_prontos.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem7 = self.lista_prontos.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"CGD", None));
        ___qtablewidgetitem8 = self.lista_prontos.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"EXE", None));
        ___qtablewidgetitem9 = self.lista_prontos.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"PRD", None));
        ___qtablewidgetitem10 = self.lista_prontos.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"DDL", None));
        ___qtablewidgetitem11 = self.lista_prontos.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"PGS", None));
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">RAM</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Gr\u00e1fico de Graant</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">DISCO</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">SOBRE</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><span style=\" font-size:12pt;\">SiEs \u00e9 uma aplica\u00e7\u00e3o que simula o escalonamento de processos em um sistema operacional.</span></p><p><span style=\" font-size:12pt;\">Ele suporta os seguintes algoritmos de escalonamento de processos:</span></p><p><span style=\" font-size:12pt;\">- FIFO</span></p><p><span style=\" font-size:12pt;\">- SJF</span></p><p><span style=\" font-size:12pt;\">- Round-Robin</span></p><p><span style=\" font-size:12pt;\">- EDF</span></p><p><span style=\" font-size:12pt;\"><br/></span></p><p><span style=\" font-size:12pt;\">Para a substitui\u00e7\u00e3o de p\u00e1ginas s\u00e3o utilizados os seguintes algoritmos:</span></p><p><span style=\" font-size:12pt;\">- FIFO</span></p><p><span style=\" font-size:12pt;\">- LRU (Menos recentemente utilizada)</span></p><p><br/></p><p><br/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/nome10.png\"/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/ln3.png\"/></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_criar.setText(QCoreApplication.translate("MainWindow", u"Criar", None))
        self.btn_executar.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
    # retranslateUi

