#IMPORTS
import requests
import csv
import datetime

with open("prices.csv", "w") as pricedata:
    writing = csv.writer(pricedata, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writing.writerow(["version from", datetime.datetime.now()])

#reading of Product-CSV-File; Variable definition
imp = open("products.csv","r")
raw_imp = csv.reader(imp, delimiter=',')
raw_list = list(raw_imp)
productcount = len(raw_list)
print("needing to update",productcount, "prices")
productnumber =  0

#DATA-RECIEVING
while productnumber < productcount:
    ingest = raw_list.pop(0)
    website = ingest.pop(1)
    productnumber = int(ingest.pop(0))
    print("fetching data... This step might take a couple of seconds")
    res = requests.get(website)
    print("recieved data from", website)
    check = str(res)
    if check == "<Response [404]>":
        print("Ressource unavailable, skipping..")

    else:
        request_done = res.text
        priceIdx = request_done.index('property="product:price:amount')
        raw_price = request_done[priceIdx+41:priceIdx+60]
        price_extract = ""
        for buchstabe in raw_price:
            if buchstabe == "\"":
                break
            else:
                price_extract += buchstabe

        price = float(price_extract)
        print("The price is following: ", price, "CHF\n")
        with open("prices.csv", "a") as pricedata:
            writing = csv.writer(pricedata, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writing.writerow([productnumber, price])