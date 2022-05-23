"""@package docstring
This module configures PCs but relies heavily on external modules that are included with the package.
"""
import bin.lib.csv_parsers
import bin.config.os
import bin.config.psu
import bin.config.storage
import bin.config.cpu
import bin.config.gpu
import bin.config.mbd
import bin.config.cooler
import bin.config.case


cvr = bin.lib.csv_parsers.CsvRead()
cvw = bin.lib.csv_parsers.CsvWrite()


class ConfigCreator:
    def __init__(self):
        self.__info_import = []
        self.__budget = 0
        self.__os_choice = ""
        self.__os_path = ""
        self.__psu_path = ""
        self.__config = ""
        self.__storage_path = ""
        self.__cpu_path = ""
        self.__gpu_path = ""
        self.__mbd_path = ""
        self.__cooler_path = ""
        self.__case_path = ""
        self.__storage_amount = 0
        self.__storage_config = []
        self.__usage_infos = []

    def start_config(self, path):
        self.__info_import = cvr.importing(path)
        self.__budget = bin.config.os.OSAssigner().os_chooser(self.__budget, self.__os_choice, self.__os_path)
        self.__budget = bin.config.psu.PSUAssigner().psu_chooser(self.__budget, self.__psu_path)
        self.__budget = bin.config.storage.StorageAssigner().storage(self.__budget, self.__storage_amount, self.__storage_config, self.__storage_path)
        self.__budget = bin.config.cpu.CPUAssigner().cpu_chooser(self.__budget, self.__cpu_path, self.__usage_infos)
        self.__budget = bin.config.gpu.GPUAssigner().gpu_assigner(self.__budget, self.__gpu_path, self.__usage_infos)
        self.__budget = bin.config.mbd.MBDAssigner().mbd_chooser(self.__budget, self.__mbd_path, self.__config)
        self.__budget = bin.config.cooler.CoolerAssigner().cooler_chooser(self.__budget, self.__cooler_path, self.__config)
        self.__budget = bin.config.case.CaseAssigner().case_chooser(self.__budget, self.__case_path, self.__config)
