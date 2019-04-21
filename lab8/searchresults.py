# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchresults.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Search_Results(object):
    def setupUi(self, Search_Results):
        Search_Results.setObjectName("Search_Results")
        Search_Results.resize(724, 442)
        self.gridLayout = QtWidgets.QGridLayout(Search_Results)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Search_Results)
        self.label.setMaximumSize(QtCore.QSize(59, 17))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ExitButton = QtWidgets.QPushButton(Search_Results)
        self.ExitButton.setObjectName("ExitButton")
        self.gridLayout.addWidget(self.ExitButton, 1, 1, 1, 1)
        self.ResultList = QtWidgets.QListWidget(Search_Results)
        self.ResultList.setObjectName("ResultList")
        self.gridLayout.addWidget(self.ResultList, 0, 1, 1, 1)

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

