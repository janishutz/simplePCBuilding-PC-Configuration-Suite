import requests


class WebsiteSourceGrabber:
    def __init__(self):
        self.__website = ""
        self.__res = ""
        self.__request_done = ""

    def grabber(self, website):
        self.__res = requests.get(website).text
        return self.__res
