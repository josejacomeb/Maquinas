# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Maquinas.ui'
#
# Created: Sat Jul 12 09:50:57 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(823, 760)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(470, 720, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 701, 20))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 201, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 141, 16))
        self.label_4.setObjectName("label_4")
        self.Onda = QtWidgets.QWidget(Dialog)
        self.Onda.setGeometry(QtCore.QRect(30, 120, 391, 300))
        self.Onda.setObjectName("Onda")
        self.Forma = QtWidgets.QLabel(Dialog)
        self.Forma.setGeometry(QtCore.QRect(30, 90, 391, 21))
        self.Forma.setTextFormat(QtCore.Qt.AutoText)
        self.Forma.setAlignment(QtCore.Qt.AlignCenter)
        self.Forma.setObjectName("Forma")
        self.Flujo = QtWidgets.QWidget(Dialog)
        self.Flujo.setGeometry(QtCore.QRect(30, 440, 401, 281))
        self.Flujo.setObjectName("Flujo")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 420, 391, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(480, 170, 161, 21))
        self.label_7.setObjectName("label_7")
        self.Frecuencia = QtWidgets.QSpinBox(Dialog)
        self.Frecuencia.setGeometry(QtCore.QRect(640, 160, 59, 31))
        self.Frecuencia.setMaximum(100)
        self.Frecuencia.setProperty("value", 60)
        self.Frecuencia.setObjectName("Frecuencia")
        self.FlujoTotal = QtWidgets.QLabel(Dialog)
        self.FlujoTotal.setGeometry(QtCore.QRect(620, 470, 66, 21))
        self.FlujoTotal.setObjectName("FlujoTotal")
        self.Direccion = QtWidgets.QLabel(Dialog)
        self.Direccion.setGeometry(QtCore.QRect(620, 500, 66, 21))
        self.Direccion.setObjectName("Direccion")
        self.Ingresar = QtWidgets.QPushButton(Dialog)
        self.Ingresar.setGeometry(QtCore.QRect(470, 270, 94, 29))
        self.Ingresar.setObjectName("Ingresar")
        self.Restablecer = QtWidgets.QPushButton(Dialog)
        self.Restablecer.setGeometry(QtCore.QRect(580, 270, 94, 29))
        self.Restablecer.setObjectName("Restablecer")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Flujo de un motor Trifásico"))
        self.buttonBox.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Evalua los valores ingresados</p></body></html>"))
        self.label.setText(_translate("Dialog", "PROGRAMA DE MAQUINAS ELECTRICAS"))
        self.label_2.setText(_translate("Dialog", "INTEGRANTES:"))
        self.label_3.setText(_translate("Dialog", "HIDROVO MAQUEAVELO"))
        self.label_4.setText(_translate("Dialog", "JACOME JOSE"))
        self.Forma.setText(_translate("Dialog", "Forma del Flujo"))
        self.label_6.setText(_translate("Dialog", "Flujo Total"))
        self.label_7.setText(_translate("Dialog", "Ingrese un periodo (Hz)"))
        self.FlujoTotal.setText(_translate("Dialog", "TextLabel"))
        self.Direccion.setText(_translate("Dialog", "TextLabel"))
        self.Ingresar.setText(_translate("Dialog", "Ingresar"))
        self.Restablecer.setText(_translate("Dialog", "Restablecer"))
