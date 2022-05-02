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

    def updater(self):
        self.__get_source = bin.lib.website_source_grabber.WebsiteSourceGrabber().grabber()
        print("ok")
        self.list_generator()
        # while self.__go == 1:
            # self.list_generator()

    def list_generator(self):
        self.__source = self.__get_source[self.__index + 100:]
        try:
            self.__index = self.__source.index("<div class=\"col search_name ellipsis\">")
            self.__extracted = self.__source[self.__index + 80:self.__index + 200]
            for self.letter in self.__extracted:
                if self.letter == "<":
                    break
                else:
                    self.__output += self.letter
            print(self.__output)
        except ValueError:
            self.__go = 0


TopGamesUpdater().updater()
