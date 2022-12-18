# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sessionPlanUploaderUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 456)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.leUserName = QtWidgets.QLineEdit(self.centralwidget)
        self.leUserName.setGeometry(QtCore.QRect(130, 10, 113, 20))
        self.leUserName.setObjectName("leUserName")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lePassword.setGeometry(QtCore.QRect(130, 50, 113, 20))
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lePassword.setObjectName("lePassword")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.leCourseCode = QtWidgets.QLineEdit(self.centralwidget)
        self.leCourseCode.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.leCourseCode.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leCourseCode.setObjectName("leCourseCode")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 220, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cbLectureHours = QtWidgets.QComboBox(self.centralwidget)
        self.cbLectureHours.setGeometry(QtCore.QRect(140, 220, 69, 22))
        self.cbLectureHours.setObjectName("cbLectureHours")
        self.cbLectureHours.addItem("")
        self.cbLectureHours.addItem("")
        self.cbLectureHours.addItem("")
        self.cbLectureHours.addItem("")
        self.cbLectureHours.addItem("")
        self.cbLectureHours.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 220, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.cbTutHours = QtWidgets.QComboBox(self.centralwidget)
        self.cbTutHours.setGeometry(QtCore.QRect(340, 220, 69, 22))
        self.cbTutHours.setObjectName("cbTutHours")
        self.cbTutHours.addItem("")
        self.cbTutHours.addItem("")
        self.cbTutHours.addItem("")
        self.cbTutHours.addItem("")
        self.cbTutHours.addItem("")
        self.cbTutHours.addItem("")
        self.cbPracticalHours = QtWidgets.QComboBox(self.centralwidget)
        self.cbPracticalHours.setGeometry(QtCore.QRect(530, 220, 69, 22))
        self.cbPracticalHours.setObjectName("cbPracticalHours")
        self.cbPracticalHours.addItem("")
        self.cbPracticalHours.addItem("")
        self.cbPracticalHours.addItem("")
        self.cbPracticalHours.addItem("")
        self.cbPracticalHours.addItem("")
        self.cbPracticalHours.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 220, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 220, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cbSkillingHours = QtWidgets.QComboBox(self.centralwidget)
        self.cbSkillingHours.setGeometry(QtCore.QRect(720, 220, 69, 22))
        self.cbSkillingHours.setObjectName("cbSkillingHours")
        self.cbSkillingHours.addItem("")
        self.cbSkillingHours.addItem("")
        self.cbSkillingHours.addItem("")
        self.cbSkillingHours.addItem("")
        self.cbSkillingHours.addItem("")
        self.cbSkillingHours.addItem("")
        self.pbRun = QtWidgets.QPushButton(self.centralwidget)
        self.pbRun.setGeometry(QtCore.QRect(280, 360, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pbRun.setFont(font)
        self.pbRun.setObjectName("pbRun")
        self.pbClear = QtWidgets.QPushButton(self.centralwidget)
        self.pbClear.setGeometry(QtCore.QRect(370, 360, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pbClear.setFont(font)
        self.pbClear.setObjectName("pbClear")
        self.pbExit = QtWidgets.QPushButton(self.centralwidget)
        self.pbExit.setGeometry(QtCore.QRect(460, 360, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pbExit.setFont(font)
        self.pbExit.setObjectName("pbExit")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 170, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.cbSem = QtWidgets.QComboBox(self.centralwidget)
        self.cbSem.setGeometry(QtCore.QRect(350, 170, 69, 22))
        self.cbSem.setObjectName("cbSem")
        self.cbSem.addItem("")
        self.cbSem.addItem("")
        self.cbSem.addItem("")
        self.cbAcademicYear = QtWidgets.QComboBox(self.centralwidget)
        self.cbAcademicYear.setGeometry(QtCore.QRect(140, 170, 69, 22))
        self.cbAcademicYear.setObjectName("cbAcademicYear")
        self.cbAcademicYear.addItem("")
        self.cbAcademicYear.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 170, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.leFilePath = QtWidgets.QLineEdit(self.centralwidget)
        self.leFilePath.setGeometry(QtCore.QRect(140, 280, 311, 20))
        self.leFilePath.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leFilePath.setObjectName("leFilePath")
        self.pbBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.pbBrowse.setGeometry(QtCore.QRect(460, 280, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pbBrowse.setFont(font)
        self.pbBrowse.setObjectName("pbBrowse")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 330, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.leStartingSession = QtWidgets.QLineEdit(self.centralwidget)
        self.leStartingSession.setGeometry(QtCore.QRect(140, 330, 113, 20))
        self.leStartingSession.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leStartingSession.setObjectName("leStartingSession")
        self.leOfferedTo = QtWidgets.QLineEdit(self.centralwidget)
        self.leOfferedTo.setGeometry(QtCore.QRect(130, 130, 113, 20))
        self.leOfferedTo.setText("")
        self.leOfferedTo.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leOfferedTo.setObjectName("leOfferedTo")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 130, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 390, 921, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(580, 0, 341, 121))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("G:/My Drive/avinash.s.vaidya@klh.edu.in 2020-10-09 10 05/KLH_Logo.png"))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(590, 130, 261, 16))
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInstructions = QtWidgets.QAction(MainWindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionSample_Session_Plan = QtWidgets.QAction(MainWindow)
        self.actionSample_Session_Plan.setObjectName("actionSample_Session_Plan")
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addAction(self.actionSample_Session_Plan)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "User Name"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Course code"))
        self.label_4.setText(_translate("MainWindow", "Lecture Hours"))
        self.cbLectureHours.setItemText(0, _translate("MainWindow", "0"))
        self.cbLectureHours.setItemText(1, _translate("MainWindow", "1"))
        self.cbLectureHours.setItemText(2, _translate("MainWindow", "2"))
        self.cbLectureHours.setItemText(3, _translate("MainWindow", "3"))
        self.cbLectureHours.setItemText(4, _translate("MainWindow", "4"))
        self.cbLectureHours.setItemText(5, _translate("MainWindow", "5"))
        self.label_5.setText(_translate("MainWindow", "Tutorial Hours"))
        self.cbTutHours.setItemText(0, _translate("MainWindow", "0"))
        self.cbTutHours.setItemText(1, _translate("MainWindow", "1"))
        self.cbTutHours.setItemText(2, _translate("MainWindow", "2"))
        self.cbTutHours.setItemText(3, _translate("MainWindow", "3"))
        self.cbTutHours.setItemText(4, _translate("MainWindow", "4"))
        self.cbTutHours.setItemText(5, _translate("MainWindow", "5"))
        self.cbPracticalHours.setItemText(0, _translate("MainWindow", "0"))
        self.cbPracticalHours.setItemText(1, _translate("MainWindow", "1"))
        self.cbPracticalHours.setItemText(2, _translate("MainWindow", "2"))
        self.cbPracticalHours.setItemText(3, _translate("MainWindow", "3"))
        self.cbPracticalHours.setItemText(4, _translate("MainWindow", "4"))
        self.cbPracticalHours.setItemText(5, _translate("MainWindow", "5"))
        self.label_6.setText(_translate("MainWindow", "Practical Hours"))
        self.label_7.setText(_translate("MainWindow", "Skilling Hours"))
        self.cbSkillingHours.setItemText(0, _translate("MainWindow", "0"))
        self.cbSkillingHours.setItemText(1, _translate("MainWindow", "1"))
        self.cbSkillingHours.setItemText(2, _translate("MainWindow", "2"))
        self.cbSkillingHours.setItemText(3, _translate("MainWindow", "3"))
        self.cbSkillingHours.setItemText(4, _translate("MainWindow", "4"))
        self.cbSkillingHours.setItemText(5, _translate("MainWindow", "5"))
        self.pbRun.setText(_translate("MainWindow", "Run"))
        self.pbClear.setText(_translate("MainWindow", "Clear"))
        self.pbExit.setText(_translate("MainWindow", "Exit"))
        self.label_8.setText(_translate("MainWindow", "Semester"))
        self.cbSem.setItemText(0, _translate("MainWindow", "Odd Sem"))
        self.cbSem.setItemText(1, _translate("MainWindow", "Even Sem"))
        self.cbSem.setItemText(2, _translate("MainWindow", "Summer Term"))
        self.cbAcademicYear.setItemText(0, _translate("MainWindow", "2021-2022"))
        self.cbAcademicYear.setItemText(1, _translate("MainWindow", "2022-2023"))
        self.label_9.setText(_translate("MainWindow", "Academic Year"))
        self.label_10.setText(_translate("MainWindow", "Session Plan File:"))
        self.pbBrowse.setText(_translate("MainWindow", "Browse..."))
        self.label_11.setText(_translate("MainWindow", "Starting Session:"))
        self.label_12.setText(_translate("MainWindow", "Offered to:"))
        self.label_14.setText(_translate("MainWindow", "Created by Dr. Avinash S Vaidya, Dept. of ECE, KLH"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions"))
        self.actionSample_Session_Plan.setText(_translate("MainWindow", "Sample Session Plan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
