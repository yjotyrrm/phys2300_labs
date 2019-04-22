# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from os import path
from magic_cabinet import *
from searchresults import Ui_Search_Results
from tagviewer import Ui_TagViewer
class Ui_MainWindow(object):

    def file_open(self):

        fname = QtWidgets.QFileDialog.getOpenFileName()
        fpath = path.relpath(fname[0])
        #add the relative path rather than absolute
        self.cabinet.add_file(fpath)

        #open a tagviewer for it, in order to add initial tags
        self.viewer = QtWidgets.QWidget()
        viewer = Ui_TagViewer()
        viewer.setupUi(self.viewer, fpath, self.cabinet)
        self.viewer.show()



    def show_suggestions(self):
        text = self.SearchBar.text()

        suggestions = self.cabinet.predict_tags(text)

        self.SuggestionBox.clear()
        for i in suggestions:
            self.SuggestionBox.addItem(i)

    def search(self):
        taglist = self.SearchBar.text().split()

        #use the primary class's search method to get a list of all entries with those tags
        names = self.cabinet.search(taglist)

        #create a new window with the search results
        results = Ui_Search_Results()
        self.window = QtWidgets.QWidget()
        results.setupUi(self.window, names, self.cabinet)
        self.window.show()

    def suggestion_clicked(self, suggestion):
        current_text = self.SearchBar.text()
        current_tags = current_text.split()
        #overwrite the last word, which is the incomplete suggestion, with the suggestion
        current_tags[-1] = suggestion.text()

        joiner = ' '
        self.SearchBar.setText(joiner.join(current_tags))

        self.SuggestionBox.clear()

    def backup(self):
        if self.cabinet.backupfile == '':
            print('no backup file was given on startup')
        else:
            confirm = QtWidgets.QDialog()
            buttonReply = QtWidgets.QMessageBox.question(confirm,'overwrite backup', "are you sure you want to overwrite the backup? \n this cannot be undone.", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if buttonReply == QtWidgets.QMessageBox.Yes:
                self.cabinet.update_file(self.cabinet.backupfile)
    def setupUi(self, MainWindow, cabinet):

        #save a reference to the primary class of the application
        self.cabinet = cabinet

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setObjectName("SearchButton")

        self.SearchButton.clicked.connect(self.search)

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

        self.SuggestionBox.itemClicked.connect(self.suggestion_clicked)

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

        self.actionAdd_File.triggered.connect(self.file_open)

        self.actionRemove_File = QtWidgets.QAction(MainWindow)
        self.actionRemove_File.setObjectName("actionRemove_File")
        self.actionUpdate_Backup = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Backup.setObjectName("actionUpdate_Backup")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionSave.triggered.connect(lambda: self.cabinet.update_file(self.cabinet.datafile))

        self.menuAdd_File.addAction(self.actionAdd_File)
        self.menuAdd_File.addAction(self.actionSave)
        self.menuAdd_File.addAction(self.actionUpdate_Backup)

        self.actionUpdate_Backup.triggered.connect(self.backup)

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

