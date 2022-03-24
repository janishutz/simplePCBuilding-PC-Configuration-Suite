"""@package docstring
This is a simplification of the csv module"""

import csv


class CsvRead:
    """This is a class that reads csv files and depending on the module selected does do different things with it"""
    def __init__(self):
        self.__imp = ""
        self.__raw = ""
        self.__raw_list = ""

    def importing(self, path):
        """Returns a list of the imported csv-file, requires path, either direct system path or relative path"""
        self.__imp = open(path)
        self.__raw = csv.reader(self.__imp, delimiter=',')
        self.__raw_list = list(self.__raw)
        return self.__raw_list


class CsvWrite:
    """This is a class that modifies csv files"""
    def __init__(self):
        self.__impl = []
        self.__strpop = []
        self.__removed = []
        self.__removing = 0
        self.__change = 0
        self.__appending = 0

    def rem_str(self, path, row):
        """Opens the csv-file in write mode which is specified as an argument either as direct or relative path"""
        self.__impl = CsvRead.importing(path)
        self.__removed = self.__impl.pop(row)
        with open(path, "w") as removedata:
            self.__removing = csv.writer(removedata, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            self.__removing.writerow(self.__removed)

    def chg_str(self, path, row, pos, new_value):
        """Opens the csv-file in write mode to change a value, e.g. if a recipes is changed."""
        self.__impl = CsvRead.importing(path)
        self.__strpop = self.__impl.pop(row)
        self.__strpop.remove(pos)
        self.__strpop.insert(pos, new_value)
        self.__impl.insert(row, self.__strpop)
        with open(path, "w") as changedata:
            self.__change = csv.writer(changedata, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            self.__change.writerow(self.__impl)

    def app_str(self, path, value):
        """Opens the csv-file in append mode and writes given input. CsvWrite.app_str(path, value).
        Path can be specified both as direct or relative. value is a list. Will return an error if type of value is
        not a list."""
        with open(path, "a") as appenddata:
            self.__appending = csv.writer(appenddata, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            self.__appending.writerow(value)
