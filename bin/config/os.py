import bin.lib.csv_parsers


cvr = bin.lib.csv_parsers.CsvRead()


class OSAssigner:
    def __init__(self):
        self.__budget = 0
        self.__import = []
        self.__extracted = ""
        self.__price = []

    def os_chooser(self, budget, os_choice, os_price_file, availability=False):
        self.__budget = budget
        self.__import = cvr.importing(os_price_file)
        for self.item in self.__import:
            self.__price.append(self.item.pop(1))

        if os_choice == "Windows 10 Home" or "Windows 11 Home" and availability is False:
            self.__budget -= self.__price.pop(0)
        elif os_choice == "Windows 10 Pro" or "Windows 11 Pro" and availability is False:
            self.__budget -= self.__price.pop(1)
        else:
            pass

        return self.__budget
