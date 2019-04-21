import argparse
import sys
import csv
from main_window import *
from PyQt5 import QtCore, QtGui, QtWidgets

data = []
tags = []
datafile = 'tagdata.csv'

def column(list, index):
    """

    :param list: a 2d list
    :param index: the index of the column you want
    :return: a list which contains all the values of the column at index
    """

    column = []
    for i in list:
        column.append(i[index])

    return column

def add_tag(filename, tag):

    #get the first column of data, which is a list of the filenames
    filenames = column(data, 0)
    if not (filename in filenames):
        print('that filename does not exist')
    else:
        row = data[filenames.index(filename)]
        if tag in row:
            print('that tag is already there')
        else:
            row.append(tag)


def remove_tag(filename, tag):

    filenames = column(data, 0)
    if not (filename in filenames):
        print('that filename does not exist')
    else:
        row = data[filenames.index(filename)]
        if tag in row:
            row.remove(tag)
        else:
            print(tag +' is not a tag for ' + filename)


def add_file(filename):
    filenames = column(data,0)
    if filename in filenames:
        print('that file is already in the system')
    else:
        data.append([filename])

def remove_file(filename):
    filenames = column(data,0)
    if filename in filenames:
        del data[filenames.index(filename)]
    else:
        print('that file is not in the system')

def get_tags(filename):
    """

    :param filename: the filename for which you want associated tags
    :param data: the 2d list of data
    :return: all tags associated with the given file
    """
    filenames = column(data, 0)
    if not (filename in filenames):
        print('that filename does not exist')
    else:
        row = data[filenames.index(filename)]

        return row[1:]

def search(taglist):
    """

    :param tags: the tags you want
    :param data: the 2d list of data
    :return: all filenames which are attatched to that list of tags
    """
    names = []
    for row in data:
        match = True
        for tag in taglist:
            if not (tag in row):
                match = False

        if match:
            names.append(row[0])

    return names




def update_file():
    """
    writes the data with updates to the csv file
    :param data: the 2d list of all data
    """

    with open(datafile, 'w') as f:
        writer = csv.writer(f)

        writer.writerows(data)

        f.close()

def update_tags(data, tags):
    """
    get a list of each unique tag in the database
    :param data:
    :return:
    """
    temp =  []
    for i in data:
        #cut off the first index, which is the filename, not a path
        e = i[1:]

        temp = temp + e

    tags = list(set(tags))

def predict_tags(text):
    """
    :param text: the raw text in the textbox
    :param tags: the list of applicable tags
    :return: a list of up to seven possible tags
    """
    possibles = []
    words = text.split()
    if words == []:
        return []
    else:
        snippet = words[-1]
        length = len(snippet)

        for i in tags:
            if i[:length] == snippet:
                possibles.append(i)

        return possibles[:7]


def main():

    parser = argparse.ArgumentParser(description= 'get_data')
    parser.add_argument('--file', required=True)
    args = parser.parse_args()

    global datafile
    datafile = args.file

    with open(args.file) as file:

        for line in file:

            data.append(line.split(sep=','))

        file.close()

    update_tags(data, tags)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    sys._excepthook = sys.excepthook


    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    sys.excepthook = exception_hook
    main()