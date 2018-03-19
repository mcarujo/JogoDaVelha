# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Interface(object):
    def setupUi(self, Interface):
        Interface.setObjectName(_fromUtf8("Interface"))
        Interface.resize(400, 300)
        self.pushButton_5 = QtGui.QPushButton(Interface)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 70, 41, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Interface)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 70, 41, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Interface)
        self.pushButton_7.setGeometry(QtCore.QRect(120, 170, 41, 31))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(Interface)
        self.pushButton_8.setGeometry(QtCore.QRect(120, 120, 41, 31))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(Interface)
        self.pushButton_9.setGeometry(QtCore.QRect(180, 120, 41, 31))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.B21 = QtGui.QPushButton(Interface)
        self.B21.setGeometry(QtCore.QRect(180, 170, 41, 31))
        self.B21.setObjectName(_fromUtf8("B21"))
        self.B02 = QtGui.QPushButton(Interface)
        self.B02.setGeometry(QtCore.QRect(240, 70, 41, 31))
        self.B02.setObjectName(_fromUtf8("B02"))
        self.B12 = QtGui.QPushButton(Interface)
        self.B12.setGeometry(QtCore.QRect(240, 120, 41, 31))
        self.B12.setObjectName(_fromUtf8("B12"))
        self.B22 = QtGui.QPushButton(Interface)
        self.B22.setGeometry(QtCore.QRect(240, 170, 41, 31))
        self.B22.setObjectName(_fromUtf8("B22"))
        self.BotaoComecar = QtGui.QPushButton(Interface)
        self.BotaoComecar.setGeometry(QtCore.QRect(40, 250, 131, 31))
        self.BotaoComecar.setObjectName(_fromUtf8("BotaoComecar"))
        self.BotaoDepois = QtGui.QPushButton(Interface)
        self.BotaoDepois.setGeometry(QtCore.QRect(210, 250, 151, 31))
        self.BotaoDepois.setObjectName(_fromUtf8("BotaoDepois"))
        self.Titulo = QtGui.QLabel(Interface)
        self.Titulo.setGeometry(QtCore.QRect(70, 10, 321, 36))
        self.Titulo.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Titulo.setFont(font)
        self.Titulo.setMouseTracking(False)
        self.Titulo.setObjectName(_fromUtf8("Titulo"))

        self.retranslateUi(Interface)
        QtCore.QMetaObject.connectSlotsByName(Interface)

    def retranslateUi(self, Interface):
        Interface.setWindowTitle(_translate("Interface", "Jogo da Velha Controle Inteligente", None))
        self.pushButton_5.setText(_translate("Interface", "#", None))
        self.pushButton_6.setText(_translate("Interface", "#", None))
        self.pushButton_7.setText(_translate("Interface", "#", None))
        self.pushButton_8.setText(_translate("Interface", "#", None))
        self.pushButton_9.setText(_translate("Interface", "#", None))
        self.B21.setText(_translate("Interface", "#", None))
        self.B02.setText(_translate("Interface", "#", None))
        self.B12.setText(_translate("Interface", "#", None))
        self.B22.setText(_translate("Interface", "#", None))
        self.BotaoComecar.setText(_translate("Interface", "Começar Primeiro", None))
        self.BotaoDepois.setText(_translate("Interface", "Começar Depois", None))
        self.Titulo.setWhatsThis(_translate("Interface", "<html><head/><body><p>A</p></body></html>", None))
        self.Titulo.setText(_translate("Interface", " JOGO DA VELHA ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Interface = QtGui.QDialog()
    ui = Ui_Interface()
    ui.setupUi(Interface)
    Interface.show()
    sys.exit(app.exec_())

