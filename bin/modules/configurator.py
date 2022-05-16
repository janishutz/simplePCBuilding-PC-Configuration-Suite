"""@package docstring
This module configures PCs but relies heavily on external modules that are included with the package.
"""
import bin.lib.csv_parsers
import bin.config.os
import bin.config.case


cvr = bin.lib.csv_parsers.CsvRead()
cvw = bin.lib.csv_parsers.CsvWrite()


class ConfigCreator:
    def __init__(self):
        self.__info_import = []
        self.__budget = 0
        self.__os_choice = ""
        self.__os_path = ""

    def start_config(self, path):
        self.__info_import = cvr.importing(path)
        self.__budget = bin.config.os.OSAssigner().os_chooser(self.__budget, self.__os_choice, self.__os_path)
        self.__budget = bin.config.case
