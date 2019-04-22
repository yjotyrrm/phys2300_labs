import argparse
import sys
import csv
from main_window import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MagicCabinet:

    def __init__(self):
        parser = argparse.ArgumentParser(description='get_data')
        parser.add_argument('--file', required=True)
        parser.add_argument('--backup', default='')
        args = parser.parse_args()

        self.datafile = args.file
        self.backupfile = args.backup
        self.tags = []
        self.data = []

        with open(args.file) as file:
            reader = csv.reader(file)

            for row in reader:
                self.data.append(row)

            file.close()

        self.update_tags()

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow, self)
        MainWindow.show()
        sys.exit(app.exec_())

    def column(self, list, index):
        """

        :param list: a 2d list
        :param index: the index of the column you want
        :return: a list which contains all the values of the column at index
        """

        column = []
        for i in list:
            if index < len(i):
                column.append(i[index])

        return column

    def trunc_name(self,filename):
        """
        truncates a full path to just the name of the file
        :param filename:
        :return:
        """
        if '\\' in filename:
            start = filename.index('\\')
            trunc = filename[start+1:]
            return trunc
        else:
            return filename

    def add_tag(self, filename, tag):

        #get the first column of data, which is a list of the filenames
        filenames = self.column(self.data, 0)
        if not (filename in filenames):
            print('that filename does not exist', 'eee')
        else:
            row = self.data[filenames.index(filename)]
            if tag in row:
                print('that tag is already there')
            else:
                row.append(tag)
                # added a tag, recompute the list of unique tags
                self.update_tags()


    def remove_tag(self, filename, tag):

        filenames = self.column(self.data, 0)
        if not (filename in filenames):
            print('that filename does not exist', 'ggg')
        else:
            row = self.data[filenames.index(filename)]
            if tag in row:
                row.remove(tag)
                self.update_tags()
            else:
                print(tag +' is not a tag for ' + filename)


    def add_file(self, filename):
        filenames = self.column(self.data,0)
        if filename in filenames:
            print('that file is already in the system')
        else:
            self.data.append([filename])

    def remove_file(self, filename):
        filenames = self.column(self.data,0)
        if filename in filenames:
            del self.data[filenames.index(filename)]
        else:
            print('that file is not in the system')

    def get_tags(self, filename):
        """

        :param filename: the filename for which you want associated tags
        :param data: the 2d list of data
        :return: all tags associated with the given file
        """
        filenames = self.column(self.data, 0)
        if not (filename in filenames):
            print('that filename does not exist')
        else:
            row = self.data[filenames.index(filename)]

            return row[1:]

    def search(self, taglist):
        """

        :param tags: the tags you want
        :param data: the 2d list of data
        :return: all filenames which are attatched to that list of tags
        """
        names = []
        for row in self.data:
            match = True
            for tag in taglist:
                if not (tag in row):
                    match = False

            if match:
                names.append(row[0])

        return names




    def update_file(self, file):
        """
        writes the data with updates to the csv file
        :param data: the 2d list of all data
        """

        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)

            f.close()

    def update_tags(self):
        """
        get a list of each unique tag in the database
        :param data:
        :return:
        """
        temp =  []
        for i in self.data:
            #cut off the first index, which is the filename, not a path
            e = i[1:]

            temp = temp + e

        self.tags = list(set(temp))

    def predict_tags(self, text):
        """
        :param text: the raw text in the textbox
        :param tags: the list of applicable tags
        :return: a list of up to seven possible tags
        """
        possibles = []
        words = text.split()

        #if the search bar is empty there should be no suggestions
        if words == []:
            return []
        else:
            snippet = words[-1]

            #if the final snippet is a complete tag, no suggestions are necessary
            if snippet in self.tags:
               return []
            else:
                length = len(snippet)

                for i in self.tags:
                    if i[:length] == snippet:
                        possibles.append(i)

                return possibles[:7]




if __name__ == '__main__':

    #code pulled from stackoverflow, makes PyQt actually print its errors, don't know how
    sys._excepthook = sys.excepthook


    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    sys.excepthook = exception_hook

    #initialize the primary class
    MagicCabinet()