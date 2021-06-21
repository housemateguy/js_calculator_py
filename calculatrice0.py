#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:28:13 2020

@author: houssemh
"""


from PyQt5 import QtCore, QtGui, QtWidgets
import res
import logging as log
import js2py as js

class Ui_MainWindow(object):
    
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 449)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget { background-image: url(:/background.jpg);  \n"
"  }\n"
"")
        self.bb = QtWidgets.QWidget(MainWindow)
        self.bb.setObjectName("bb")
        self.pushButton_9 = QtWidgets.QPushButton(self.bb)
        self.pushButton_9.setGeometry(QtCore.QRect(290, 110, 61, 51))
        self.pushButton_9.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
"background-color:  rgba(17, 221, 45, 123);\n"
"\n"
" color: rgb(238, 238, 236);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda: self.buttonClick(self.pushButton_9))

        self.pushButton_8 = QtWidgets.QPushButton(self.bb)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 110, 61, 51))
        self.pushButton_8.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda: self.buttonClick(self.pushButton_8))

        self.pushButton_7 = QtWidgets.QPushButton(self.bb)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 110, 61, 51))
        self.pushButton_7.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: self.buttonClick(self.pushButton_7))

        self.pushButton_6 = QtWidgets.QPushButton(self.bb)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 170, 61, 51))
        self.pushButton_6.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: self.buttonClick(self.pushButton_6))


        self.pushButton_5 = QtWidgets.QPushButton(self.bb)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 170, 61, 51))
        self.pushButton_5.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.buttonClick(self.pushButton_5))

        
        self.pushButton_4 = QtWidgets.QPushButton(self.bb)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 170, 61, 51))
        self.pushButton_4.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.buttonClick(self.pushButton_4))

        self.pushButton_3 = QtWidgets.QPushButton(self.bb)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 230, 61, 51))
        self.pushButton_3.setStyleSheet(" border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\"; ")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.buttonClick(self.pushButton_3))

        self.pushButton_2 = QtWidgets.QPushButton(self.bb)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 230, 61, 51))
        self.pushButton_2.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.buttonClick(self.pushButton_2))

        self.pushButton_1 = QtWidgets.QPushButton(self.bb)
        self.pushButton_1.setGeometry(QtCore.QRect(150, 230, 61, 51))
        self.pushButton_1.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(lambda: self.buttonClick(self.pushButton_1))

        self.label = QtWidgets.QLabel(self.bb)
        self.label.setGeometry(QtCore.QRect(10, 10, 341, 81))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label.setWhatsThis("Chouia Houssem lol")
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("#label {border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:   rgba(68, 58, 58, 154);\n"
"font: 75 35pt \"Wozcott\";\n"
"text-align: center;  }")
        self.label.setObjectName("label")
        self.pushButton_plus = QtWidgets.QPushButton(self.bb)
        self.pushButton_plus.setGeometry(QtCore.QRect(80, 110, 61, 51))
        self.pushButton_plus.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_plus.clicked.connect(lambda: self.buttonClick(self.pushButton_plus))
        
        
        self.pushButton_divide = QtWidgets.QPushButton(self.bb)
        self.pushButton_divide.setGeometry(QtCore.QRect(80, 170, 61, 51))
        self.pushButton_divide.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_divide.clicked.connect(lambda: self.buttonClick(self.pushButton_divide))        

        self.pushButton_egal = QtWidgets.QPushButton(self.bb)
        self.pushButton_egal.setGeometry(QtCore.QRect(10, 230, 131, 51))
        self.pushButton_egal.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_egal.setObjectName("pushButton_egal")
        self.pushButton_egal.clicked.connect(lambda: self.egalClick(self.pushButton_egal))        

        self.pushButton_minus = QtWidgets.QPushButton(self.bb)
        self.pushButton_minus.setGeometry(QtCore.QRect(10, 110, 61, 51))
        self.pushButton_minus.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_minus.clicked.connect(lambda: self.buttonClick(self.pushButton_minus))        

        self.pushButton_x = QtWidgets.QPushButton(self.bb)
        self.pushButton_x.setGeometry(QtCore.QRect(10, 170, 61, 51))
        self.pushButton_x.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_x.setObjectName("pushButton_x")
        self.pushButton_x.clicked.connect(lambda: self.buttonClick(self.pushButton_x))        

        self.pushButton_dot = QtWidgets.QPushButton(self.bb)
        self.pushButton_dot.setGeometry(QtCore.QRect(290, 290, 61, 51))
        self.pushButton_dot.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_dot.clicked.connect(lambda: self.buttonClick(self.pushButton_dot))        

        self.pushButton_closebraket = QtWidgets.QPushButton(self.bb)
        self.pushButton_closebraket.setGeometry(QtCore.QRect(220, 290, 61, 51))
        self.pushButton_closebraket.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_closebraket.setObjectName("pushButton_closebraket")
        self.pushButton_closebraket.clicked.connect(lambda: self.buttonClick(self.pushButton_closebraket))        


        self.pushButton_openbraket = QtWidgets.QPushButton(self.bb)
        self.pushButton_openbraket.setGeometry(QtCore.QRect(150, 290, 61, 51))
        self.pushButton_openbraket.setStyleSheet("QPushButton { border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\"; } ")
        self.pushButton_openbraket.setObjectName("pushButton_openbraket")
        self.pushButton_openbraket.clicked.connect(lambda: self.buttonClick(self.pushButton_openbraket))        

        self.pushButton_oss = QtWidgets.QPushButton(self.bb)
        self.pushButton_oss.setGeometry(QtCore.QRect(80, 290, 61, 51))
        self.pushButton_oss.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
" font: 75 italic 11pt \"\";\n"
" \n"
"font: 19pt \"Ubuntu\";")
        self.pushButton_oss.setObjectName("pushButton_oss")
        self.pushButton_oss.clicked.connect(lambda: self.buttonClick(self.pushButton_oss))        

        self.pushButton_chouiahoussem_git_housemateguy = QtWidgets.QPushButton(self.bb)
        self.pushButton_chouiahoussem_git_housemateguy.setGeometry(QtCore.QRect(220, 350, 131, 51))
        self.pushButton_chouiahoussem_git_housemateguy.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 29pt \"Vaporwave\";")
        self.pushButton_chouiahoussem_git_housemateguy.setObjectName("pushButton_chouiahoussem_git_housemateguy")
        self.pushButton_C = QtWidgets.QPushButton(self.bb)
        self.pushButton_C.setGeometry(QtCore.QRect(10, 290, 61, 51))
        self.pushButton_C.setStyleSheet("border: 0px solid white; border-radius:10px; \n"
" color: rgb(238, 238, 236);\n"
"background-color:  rgba(17, 221, 45, 123);\n"
"font: 75 15pt \"\";\n"
"font: 75 11pt \"Game of \";\n"
"font: 75 italic 11pt \"\";\n"
"font: 75 19pt \"Wozcott\";")
        self.pushButton_C.setObjectName("pushButton_C")
        self.pushButton_C.clicked.connect(lambda: self.deleteClick(self.pushButton_C))        

        MainWindow.setCentralWidget(self.bb)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JS Calculator in Python"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_divide.setText(_translate("MainWindow", "/"))
        self.pushButton_egal.setText(_translate("MainWindow", "="))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_x.setText(_translate("MainWindow", "x"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_closebraket.setText(_translate("MainWindow", ")"))
        self.pushButton_openbraket.setText(_translate("MainWindow", "("))
        self.pushButton_oss.setText(_translate("MainWindow", "^"))
        self.pushButton_chouiahoussem_git_housemateguy.setText(_translate("MainWindow", "Ch"))
        self.pushButton_C.setText(_translate("MainWindow", "C"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        
        
    def buttonClick(self, button):
        if (self.label.text()=="0"):
         self.label.setText("")
        print("'"+button.text()+"' was clicked!")
        log.basicConfig(filename='history.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        log.info("'"+button.text()+"' was clicked!")
        self.label.setText(self.label.text()+button.text())
        
    def egalClick(self, button):
        log.basicConfig(filename='history.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        log.info("'"+button.text()+"' was clicked!")
        print("'"+button.text()+"' was clicked!")
        #the magical eval javascript command
        js1 = ''+self.label.text().replace("x","*")+''
        print("result = "+str(js.eval_js(js1))+" was found!")
        log.info("result = "+str(js.eval_js(js1))+" was found!")
        self.label.setText(str(js.eval_js(js1)))
        
    def deleteClick(self, button):
        print("'"+button.text()+"' was clicked!")
        log.basicConfig(filename='history.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        log.info("'"+button.text()+"' was clicked!")
        log.info("erased!")

        self.label.setText("0")
        
    
if __name__ == "__main__":
        import sys
        app= QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
        
 