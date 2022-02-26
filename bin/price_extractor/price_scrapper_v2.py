import bin.lib.csv_parsers
import requests
import datetime

cvr = bin.lib.csv_parsers.CsvRead()
cvw = bin.lib.csv_parsers.CsvWrite()

class PriceExtractor:
    def __init__(self):

    def update_all_prices(self, folder):
        self.digitec_extractor()


    def digitec_extractor(self):
        """Run through the entire list of links specified in the csv file that was selected either when loading the
        function or when specified through the method \"readfile\". NOTE: This method does not require any additional
        arguments and also does run through the entire file!"""
        while

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
