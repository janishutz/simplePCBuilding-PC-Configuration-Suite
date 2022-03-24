"""@package docstring
This module configures PCs but relies heavily on external modules that are included with the package.
"""
import bin.lib.csv_parsers


cvr = bin.lib.csv_parsers.CsvRead()
cvw = bin.lib.csv_parsers.CsvWrite()


class ConfigCreator:
    def __init__(self):
        self.__info_import = []

    def start_config(self, path):
        self.__info_import = cvr.importing(path)
