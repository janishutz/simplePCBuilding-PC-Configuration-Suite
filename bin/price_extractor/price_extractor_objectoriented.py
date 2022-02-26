"""@package docstring
This package extracts prices from websites. Currently, the package only allows for extraction of prices from
https://digitec.ch/"""

import requests
import csv
import datetime


class PriceExtractor:
    def __init__(self):
        with open("../../data/prices.csv", "w") as pricedata:
            self.__writing = csv.writer(pricedata, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            self.__writing.writerow(["version from", datetime.datetime.now()])
        self.__imp = open("../../data/products.csv", "r")
        self.__raw_imp = csv.reader(self.__imp, delimiter=',')
        self.__raw_list = list(self.__raw_imp)
        self.__productcount = len(self.__raw_list)
        print("needing to update", self.__productcount, "prices")
        self.__productnumber = 0
        self.__website = ""
        self.__ingest = ""
        self.__res = ""
        self.__priceIdx = 0
        self.__check = 0
        self.__request_done = ""
        self.__raw_price = ""
        self.__price = 0
        self.__price_extract = 0

    def readfile(self, filename):
        """Reads a new file that contains links in csv format. Arguments:
        Filename. Either specify full path (e.g. /home/[username]/price_extractor/prices.csv), relative path when
        inside the folder of the executable (e.g. /pricedata/prices2.csv) or inside another folder that is located in
        the parent folder (e.g. ../pricedata/prices3.csv).
        Returns the content of the file inside of a list.

        Example: prices = PriceExtractor.readfile(/pricedata/prices2.csv) (NOTE: prices is a list in this case!)"""
        with open(filename, "w") as pricedata:
            self.__writing = csv.writer(pricedata, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            self.__writing.writerow(["version from", datetime.datetime.now()])
        self.__imp = open("../../data/products.csv", "r")
        self.__raw_imp = csv.reader(self.__imp, delimiter=',')
        self.__raw_list = list(self.__raw_imp)
        self.__productcount = len(self.__raw_list)
        print("needing to update", self.__productcount, "prices")
        self.__productnumber = 0
        return self.__raw_list

    def chg_website(self, website):
        """Change the website (exact URL to product on https://digitec.ch/ only currently). Arguments:
        Website. Only put direct link to product on digitec. Will return an error if a link other than digitec is
        specified, though might work if the website structure is similar.

        Example: PriceExtractor.chg_website(https://www.digitec.ch/de/s1/product/asus-radeon-rx-6600-dual-8-gb-grafikkarte-16833213)"""
        self.__website = website

    def digitec_extractor(self):
        """Run through the entire list of links specified in the csv file that was selected either when loading the
        function or when specified through the method \"readfile\". NOTE: This method does not require any additional
        arguments and also does run through the entire file!"""
        while self.__productnumber < self.__productcount:
            self.__ingest = self.__raw_list.pop(0)
            self.__website = self.__ingest.pop(1)
            self.__productnumber = int(self.__ingest.pop(0))
            print("fetching data... This step might take a couple of seconds")
            self.__res = requests.get(self.__website)
            print("recieved data from", self.__website)
            self.__check = str(self.__res)
            if self.__check == "<Response [404]>":
                print("Ressource unavailable, skipping..")
            else:
                self.__request_done = self.__res.text
                self.__priceIdx = self.__request_done.index('property="product:price:amount')
                self.__raw_price = self.__request_done[self.__priceIdx + 41:self.__priceIdx + 60]
                self.__price_extract = ""
                for buchstabe in self.__raw_price:
                    if buchstabe == "\"":
                        break
                    else:
                        self.__price_extract += buchstabe
                self.__price = float(self.__price_extract)
                print("The price is following: ", self.__price, "CHF\n")
                with open("../../data/prices.csv", "a") as pricedata:
                    writing = csv.writer(pricedata, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                    writing.writerow([self.__productnumber, self.__price])


digitec_ext = PriceExtractor()
digitec_ext.digitec_extractor()
