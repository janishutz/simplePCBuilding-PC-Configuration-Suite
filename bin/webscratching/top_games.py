import bin.lib.website_source_grabber


class TopGamesUpdater:
    def __init__(self):
        self.__get_source = ""
        self.__index = 0
        self.__extracted = ""
        self.letter = ""
        self.__output = ""
        self.__source = ""
        self.__go = 1
        self.__location = 0
        self.err = ""
        self.__return_value = []

    def updater(self):
        self.__source = bin.lib.website_source_grabber.WebsiteSourceGrabber().grabber("https://store.steampowered.com/search/?filter=topsellers")
        self.list_generator()
        return self.__return_value

    def list_generator(self):
        while self.__go == 1:
            try:
                self.__index = self.__source[self.__location:].index("<div class=\"col search_name ellipsis\">")
                self.__index += 80
                self.__location += self.__index
                self.__extracted = self.__source[self.__location:self.__location + 120]
                self.__output = ""
                for self.letter in self.__extracted:
                    if self.letter == "<":
                        break
                    else:
                        self.__output += self.letter
                self.__return_value.append(self.__output)

            except ValueError:
                self.__go = 0


TopGamesUpdater().updater()
