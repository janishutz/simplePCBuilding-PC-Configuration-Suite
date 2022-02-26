import datetime
import csv
"""@package docstring
This software / package is used to easily manage the available products. This software will automatically update
whenever there is an update for the reader available on the website. 
--------

NOTE: This software changes files in the directory in which it is located and as such is not made for 
inexperienced users. Please read the readme.txt file for further notice. 

NOTE: This software does not feature a standard gui (Graphical User Interface) currently and as such is 
based on commands. You cna find a full lists of commands on the wiki.

NOTE: The simplePCBuilding-Configurator comes with an Update service for the component list. In the event of 
an Update, there is a script installed with your software that merges the new updates to the components file
with the changes you made. 

NOTE: Changing the CSV-File containing the component information with any other editor other than this one,
the file might get unreadable for the software. Do always use this software here to change something. 
"""
version = str("alpha 1.0")
print("""
================================================================
Welcome to the simplePCBuilding PC-Configurator-Package-Manager!
You are currently running""", version, """!
================================================================

This software is used to easily manage the available products. This software will automatically update
whenever there is an update for the reader available on the website. 
--------

NOTE: This software changes files in the directory in which it is located and as such is not made for 
inexperienced users. Please read the readme.txt file for further notice. 

NOTE: This software does not feature a standard gui (Graphical User Interface) currently and as such is 
based on commands. You cna find a full lists of commands on the wiki.

NOTE: The simplePCBuilding-Configurator comes with an Update service for the component list. In the event of 
an Update, there is a script installed with your software that merges the new updates to the components file
with the changes you made. 

NOTE: Changing the CSV-File containing the component information with any other editor other than this one,
might result in loss of correct operation of the software. Do always use this software here to change something. 
""")



i = input("Please read above carefully and type a y to continue, a \"n\" to exit the software:")

if i == "y":
    print("Starting...")

else:
    print("Leaving...")

