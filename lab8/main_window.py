# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from magic_cabinet import *
class Ui_MainWindow(object):

    def show_suggestions(self):
        print('gothere')
        text = self.SearchBar.text()
        suggestions = predict_tags(text)
        for i in suggestions:
            self.SuggestionBox.addItem(i)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setObjectName("SearchButton")
        self.gridLayout.addWidget(self.SearchButton, 4, 0, 1, 1)
        self.SearchLabel = QtWidgets.QLabel(self.centralwidget)
        self.SearchLabel.setObjectName("SearchLabel")
        self.gridLayout.addWidget(self.SearchLabel, 2, 0, 1, 1)
        self.SearchBar = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchBar.setObjectName("SearchBar")
        self.SearchBar.textChanged.connect(self.show_suggestions)
        self.gridLayout.addWidget(self.SearchBar, 2, 1, 1, 1)
        self.SuggestionBox = QtWidgets.QListWidget(self.centralwidget)
        self.SuggestionBox.setObjectName("SuggestionBox")
        self.gridLayout.addWidget(self.SuggestionBox, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 26))
        self.menubar.setObjectName("menubar")
        self.menuAdd_File = QtWidgets.QMenu(self.menubar)
        self.menuAdd_File.setObjectName("menuAdd_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_File = QtWidgets.QAction(MainWindow)
        self.actionAdd_File.setObjectName("actionAdd_File")
        self.actionRemove_File = QtWidgets.QAction(MainWindow)
        self.actionRemove_File.setObjectName("actionRemove_File")
        self.actionUpdate_Backup = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Backup.setObjectName("actionUpdate_Backup")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuAdd_File.addAction(self.actionAdd_File)
        self.menuAdd_File.addAction(self.actionSave)
        self.menuAdd_File.addAction(self.actionUpdate_Backup)
        self.menubar.addAction(self.menuAdd_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SearchButton.setText(_translate("MainWindow", "Enter"))
        self.SearchLabel.setText(_translate("MainWindow", "Search"))
        self.menuAdd_File.setTitle(_translate("MainWindow", "File"))
        self.actionAdd_File.setText(_translate("MainWindow", "Add File"))
        self.actionRemove_File.setText(_translate("MainWindow", "Remove File"))
        self.actionUpdate_Backup.setText(_translate("MainWindow", "Update Backup"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

