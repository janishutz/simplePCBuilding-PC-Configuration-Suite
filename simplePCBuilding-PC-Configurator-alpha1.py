# This is the main runtime of the simplePCBuilding-PC-Configurator
# IMPORTS
import time


version = "alpha 1.0"
print("""
--------------------------------------------------------------------
        WELCOME TO THE simplePCBuilding PC CONFIGURATOR
        YOU ARE CURRENTLY RUNNING VERSION""", version, """
---------------------------------------------------------------------""")
time.sleep(1)
print("""

Please note that this software is developed and distributed by simplePCBuilding 
and as such you are not allowed to sell and / or distribute this software on
your own. If you want to share this project with others, please refer to our
guidelines and do only provide the official download-link.

""")
time.sleep(1)
print("""This software is split up into different modules you can use. 
Select the appropriate one:
MODULE LIST:
- Configurator (c)
- Updater (u)
- Package manager (p)
- Quit (q)

To select a module, please type the correct letter (found in brackets behind 
the module name in the above list) in through your keyboard
""")
i = input("please choose the module you want to use: ")
go = 1

while go == 1:
    if i == "c":
        print("starting configurator...")
        go = 0

    elif i == "u":
        print("starting updater...")
        go = 0

    elif i == "p":
        print("starting package manager...")
        go = 0

    elif i == "q":
        print("killing processes....")
        time.sleep(0.5)
        print("Terminating...")
        go = 0

    else:
        print("\nUnknown entry, please retry.\n ")
        time.sleep(0.5)
        print("""This software is split up into different modules you can use. 
Select the appropriate one:
    MODULE LIST:
        - Configurator (c)
        - Updater (u)
        - Package manager (p)
        - Quit (q)

    To select a module, please type the correct letter (found in brackets behind 
    the module name in the above list) in through your keyboard
    """)
        i = input("Please select a module and type in the corresponding letter: ")
