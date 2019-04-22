# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tagviewer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import magic_cabinet
import os

class Ui_TagViewer(object):
    def addTag(self):

        self.addTagDialog = QtWidgets.QDialog()
        text, okPressed = QtWidgets.QInputDialog.getText(self.addTagDialog, "Add Tag", "Add Tag:", QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '' and not (' ' in text):
            self.cabinet.add_tag(self.item, text)
            self.TagList.addItem(text)
        elif ' ' in text:
            print('tags must not have spaces in them, please use underscores instead')
        #as you have added a new tag, add the new tag to the taglist


    def removeTag(self):
        tag = self.TagList.currentItem().text()
        self.cabinet.remove_tag(self.item, tag)

        self.TagList.takeItem(self.TagList.row(self.TagList.currentItem()))

    def populate_tags(self):
        tags = self.cabinet.get_tags(self.item)
        for i in tags:
            self.TagList.addItem(i)



    def setupUi(self, TagViewer, item, cabinet):
        self.cabinet = cabinet
        self.item = item
        TagViewer.setObjectName("TagViewer")
        TagViewer.resize(669, 506)
        self.gridLayout = QtWidgets.QGridLayout(TagViewer)
        self.gridLayout.setObjectName("gridLayout")
        self.OpenFileButton = QtWidgets.QPushButton(TagViewer)
        self.OpenFileButton.setObjectName("OpenFileButton")


        self.OpenFileButton.clicked.connect(lambda: os.startfile(self.item))

        self.gridLayout.addWidget(self.OpenFileButton, 2, 0, 1, 1)
        self.AddTagButton = QtWidgets.QPushButton(TagViewer)
        self.AddTagButton.setObjectName("AddTagButton")

        self.AddTagButton.clicked.connect(lambda: self.addTag())

        self.gridLayout.addWidget(self.AddTagButton, 2, 1, 1, 1)
        self.RemoveTagButton = QtWidgets.QPushButton(TagViewer)
        self.RemoveTagButton.setObjectName("RemoveTagButton")

        self.RemoveTagButton.clicked.connect(self.removeTag)

        self.gridLayout.addWidget(self.RemoveTagButton, 2, 2, 1, 1)
        self.FilenameLabel = QtWidgets.QLabel(TagViewer)
        self.FilenameLabel.setMaximumSize(QtCore.QSize(300, 17))
        self.FilenameLabel.setObjectName("FilenameLabel")



        self.gridLayout.addWidget(self.FilenameLabel, 0, 0, 1, 1)
        self.TagList = QtWidgets.QListWidget(TagViewer)
        self.TagList.setObjectName("TagList")
        self.gridLayout.addWidget(self.TagList, 1, 0, 1, 3)

        self.populate_tags()

        self.retranslateUi(TagViewer)
        self.FilenameLabel.setText(self.cabinet.trunc_name(self.item))
        QtCore.QMetaObject.connectSlotsByName(TagViewer)

    def retranslateUi(self, TagViewer):
        _translate = QtCore.QCoreApplication.translate
        TagViewer.setWindowTitle(_translate("TagViewer", "Form"))
        self.OpenFileButton.setText(_translate("TagViewer", "Open"))
        self.AddTagButton.setText(_translate("TagViewer", "Add New Tags"))
        self.RemoveTagButton.setText(_translate("TagViewer", "Remove Selected Tag"))
        self.FilenameLabel.setText(_translate("TagViewer", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TagViewer = QtWidgets.QWidget()
    ui = Ui_TagViewer()
    ui.setupUi(TagViewer)
    TagViewer.show()
    sys.exit(app.exec_())

