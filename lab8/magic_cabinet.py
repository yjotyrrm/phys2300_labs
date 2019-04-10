import argparse
import csv


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

def add_tags(filename, tags, data):

    #get the first column of data, which is a list of the filenames
    filenames = column(data, 0)
    if filename in filenames:
        row = data[filenames.index(filename)]

        for i in tags:
            row.append(i)

    else:
        row = data.append([filename])

        for i in tags:
           row.append(i)

def remove_tags(filename, tags, data):

    filenames = column(data, 0)
    if not (filename in filenames):
        print('that filename does not exist')
    else:
        row = data[filenames.index(filename)]
        for tag in tags:
            if tag in row:
                row.remove(tag)
            else:
                print(tag +' is not a tag for ' + filename)


def get_tags(filename, data):
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
def search(tags, data):
    """

    :param tags: the tags you want
    :param data: the 2d list of data
    :return: all filenames which are attatched to that list of tags
    """
    names = []
    for row in data:
        match = True
        for tag in tags:
            if not (tag in row):
                match = False

        if match:
            names.append(row[0])

    return names




def update_file(data, file):
    """
    writes the data with updates to the csv file
    :param data: the 2d list of all data
    """

    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)

        f.close()




def main():

    parser = argparse.ArgumentParser(description= 'get_data')
    parser.add_argument('--file', required=True)
    parser.parse_args()
    data = []
    with open(parser.file) as file:

        for line in file:

            data.append(line.split(sep=','))

        file.close()

if __name__ == '__main__':
    main()