# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from game import Game
import time
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(657, 516)
        self.B00 = QtWidgets.QPushButton(Dialog)
        self.B00.setGeometry(QtCore.QRect(230, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.B00.setFont(font)
        self.B00.setText("")
        self.B00.setObjectName("B00")
        self.B01 = QtWidgets.QPushButton(Dialog)
        self.B01.setGeometry(QtCore.QRect(290, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.B01.setFont(font)
        self.B01.setText("")
        self.B01.setObjectName("B01")
        self.B02 = QtWidgets.QPushButton(Dialog)
        self.B02.setGeometry(QtCore.QRect(350, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.B02.setFont(font)
        self.B02.setText("")
        self.B02.setObjectName("B02")
        self.B12 = QtWidgets.QPushButton(Dialog)
        self.B12.setGeometry(QtCore.QRect(350, 160, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.B12.setFont(font)
        self.B12.setText("")
        self.B12.setObjectName("B12")
        self.B11 = QtWidgets.QPushButton(Dialog)
        self.B11.setGeometry(QtCore.QRect(290, 160, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.B11.setFont(font)
        self.B11.setText("")
        self.B11.setObjectName("B11")
        self.B10 = QtWidgets.QPushButton(Dialog)
        self.B10.setGeometry(QtCore.QRect(230, 160, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.B10.setFont(font)
        self.B10.setText("")
        self.B10.setObjectName("B10")
        self.B22 = QtWidgets.QPushButton(Dialog)
        self.B22.setGeometry(QtCore.QRect(350, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.B22.setFont(font)
        self.B22.setText("")
        self.B22.setObjectName("B22")
        self.B21 = QtWidgets.QPushButton(Dialog)
        self.B21.setGeometry(QtCore.QRect(290, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.B21.setFont(font)
        self.B21.setText("")
        self.B21.setObjectName("B21")
        self.B20 = QtWidgets.QPushButton(Dialog)
        self.B20.setGeometry(QtCore.QRect(230, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.B20.setFont(font)
        self.B20.setText("")
        self.B20.setObjectName("B20")
        self.ButtonStart = QtWidgets.QPushButton(Dialog)
        self.ButtonStart.setGeometry(QtCore.QRect(170, 380, 141, 41))
        self.ButtonStart.setObjectName("ButtonStart")
        self.ButtonSecond = QtWidgets.QPushButton(Dialog)
        self.ButtonSecond.setGeometry(QtCore.QRect(360, 380, 141, 41))
        self.ButtonSecond.setObjectName("ButtonSecond")
        self.Title = QtWidgets.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(210, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.Mensagem = QtWidgets.QLabel(Dialog)
        self.Mensagem.setGeometry(QtCore.QRect(180, 290, 261, 31))
        self.Mensagem.setObjectName("Mensagem")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(52, 390, 56, 24))
        self.spinBox.setMaximum(3)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 370, 81, 20))
        self.label.setObjectName("label")
        # Events
        self.B00.clicked.connect(self.ButtonB00)
        self.B01.clicked.connect(self.ButtonB01)
        self.B02.clicked.connect(self.ButtonB02)
        self.B10.clicked.connect(self.ButtonB10)
        self.B11.clicked.connect(self.ButtonB11)
        self.B12.clicked.connect(self.ButtonB12)
        self.B20.clicked.connect(self.ButtonB20)
        self.B21.clicked.connect(self.ButtonB21)
        self.B22.clicked.connect(self.ButtonB22)
        # Events
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ButtonStart.setText(_translate("Dialog", "Começar Primeiro"))
        self.ButtonSecond.setText(_translate("Dialog", "Começar Depois"))
        self.Title.setText(_translate("Dialog", "JOGO DA VELHA"))
        self.Mensagem.setText(_translate("Dialog", "Mensagem"))
        self.label.setText(_translate("Dialog", "Profundidade"))

    # Functions
    def ButtonB00(self):
        self.makeBoard(0,0,"O")
        self.Play()

    def ButtonB01(self):
        self.makeBoard(0,1,"O")
        self.Play()

    def ButtonB02(self):
        self.makeBoard(0,2,"O")
        self.Play()

    def ButtonB10(self):
        self.makeBoard(1,0,"O")
        self.Play()

    def ButtonB11(self):
        self.makeBoard(1,1,"O")
        self.Play()

    def ButtonB12(self):
        self.makeBoard(1,2,"O")
        self.Play()

    def ButtonB20(self):
        self.makeBoard(2,0,"O")
        self.Play()

    def ButtonB21(self):
        self.makeBoard(2,1,"O")
        self.Play()

    def ButtonB22(self):
        self.makeBoard(2,2,"O")
        self.Play()

    def Play(self):
        table_before = self.takeBoard()
        game = Game()
        flag, msg = game.alguem_ganhou(table_before)
        if(flag):
            print(flag)
            self.Mensagem.setText(msg)
            #time.sleep(2)
            self.reset()
        else:
            self.Mensagem.setText("Minha Vez")
            line, colm = game.my_time(table_before)
            self.makeBoard(line, colm, "X")
            table_before = self.takeBoard()
            flag, msg = game.alguem_ganhou(table_before)
            if(flag):
                print(flag)
                self.Mensagem.setText(msg)
                #time.sleep(1)
                self.reset()
            else:
                self.Mensagem.setText("Sua Vez")


    def takeBoard(self):
        B00 = self.B00.text()
        B01 = self.B01.text()
        B02 = self.B02.text()
        B10 = self.B10.text()
        B11 = self.B11.text()
        B12 = self.B12.text()
        B20 = self.B20.text()
        B21 = self.B21.text()
        B22 = self.B22.text()

        board = [
            [B00, B01, B02],
            [B10, B11, B12],
            [B20, B21, B22]
        ]
        
        return board
    def reset(self):
        self.makeBoard(0,0,"")
        self.makeBoard(0,1,"")
        self.makeBoard(0,2,"")
        self.makeBoard(1,0,"")
        self.makeBoard(1,1,"")
        self.makeBoard(1,2,"")
        self.makeBoard(2,0,"")
        self.makeBoard(2,1,"")
        self.makeBoard(2,2,"")

 #   def cpu_start(self):
        #kkkkk

    def makeBoard(self, lin, col,flag):
        if (lin == 0):
            if(col == 0):
                self.B00.setText(flag)
            elif(col == 1):
                self.B01.setText(flag)
            elif(col == 2):
                self.B02.setText(flag)
        elif (lin == 1):
            if(col == 0):
                self.B10.setText(flag)
            elif(col == 1):
                self.B11.setText(flag)
            elif(col == 2):
                self.B12.setText(flag)
        elif (lin == 2):
            if(col == 0):
                self.B20.setText(flag)
            elif(col == 1):
                self.B21.setText(flag)
            elif(col == 2):
                self.B22.setText(flag)
        else:
            print('Errow!')

    # Functions end

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

