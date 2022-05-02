import requests
import pyperclip as pc

while True:
    website = str(input("Website to get the sourcecode from: "))
    print(website)

    if website == "q":
        print("Leaving")
        break
    else:
        res = requests.get(website)
        print(res.text)
        try:
            pc.copy(res.text)
            print("""
        
--------------------------
        
        COPIED
        
--------------------------
""")
        except:
            pass
