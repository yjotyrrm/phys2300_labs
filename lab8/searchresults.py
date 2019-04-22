# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchresults.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tagviewer import Ui_TagViewer
import sys

class Ui_Search_Results(object):

    def populate_results(self):
        if(self.filenames != []):
            for i in self.filenames:
                self.ResultList.addItem(i)
        else:
            self.ResultList.addItem('there are no documents with that combination of tags')
    def open_tagviewer(self, item):

        self.window = QtWidgets.QWidget()
        viewer = Ui_TagViewer()
        viewer.setupUi(self.window, item, self.cabinet)
        self.window.show()


    def setupUi(self, Search_Results, filenames, cabinet):
        self.filenames = filenames
        self.cabinet = cabinet
        Search_Results.setObjectName("Search_Results")
        Search_Results.resize(742, 453)
        self.verticalLayout = QtWidgets.QVBoxLayout(Search_Results)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ResultList = QtWidgets.QListWidget(Search_Results)
        self.ResultList.setObjectName("ResultList")

        #no idea why I can't just pass open_tagviewer directly, but I can't and this works
        self.ResultList.itemClicked.connect(lambda: self.open_tagviewer(self.ResultList.currentItem().text()))

        self.verticalLayout.addWidget(self.ResultList)
        self.ExitButton = QtWidgets.QPushButton(Search_Results)
        self.ExitButton.setObjectName("ExitButton")

        self.ExitButton.clicked.connect(Search_Results.close)

        self.verticalLayout.addWidget(self.ExitButton)

        self.populate_results()

        self.retranslateUi(Search_Results)
        QtCore.QMetaObject.connectSlotsByName(Search_Results)

    def retranslateUi(self, Search_Results):
        _translate = QtCore.QCoreApplication.translate
        Search_Results.setWindowTitle(_translate("Search_Results", "Form"))
        self.ExitButton.setText(_translate("Search_Results", "Back"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Search_Results = QtWidgets.QWidget()
    ui = Ui_Search_Results()
    ui.setupUi(Search_Results)
    Search_Results.show()
    sys.exit(app.exec_())

