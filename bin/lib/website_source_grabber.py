import requests


class WebsiteSourceGrabber:
    def __init__(self):
        self.__website = ""
        self.__res = ""
        self.__request_done = ""

    def grabber(self):
        self.__website = "https://store.steampowered.com/search/?filter=topsellers"
        self.__res = requests.get(self.__website)
        self.__request_done = self.__res.text
        return self.__request_done
