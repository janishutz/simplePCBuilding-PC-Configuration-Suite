"""@package docstring
This module asks the user questions so the software can configure the PC.
"""


class UserprofileCreator:
    def __init__(self):
        print("""First of all we need your name so we can match it with you.""")
        self.i = 0

    def chg_username(self):
        self.i = input("please enter your name")
        return self.i

    def chg_budget(self):
        self.i = input("Now, how big is your budget? ")
        return self.i

    def chg_use_case(self):
        """"""
        print("""Now we need some information regarding your intended use-case for this system.
        o = Office-PC (you are editing documents, creating pdfs, browsing the web
        c = Content Creation PC (you are editing videos, editing photos or other similarly intense workloads
        g = Gaming-PC (You are playing games, maybe streaming as well?)
        """)
        self.i = input("Choose your use-case from above")
        return self.i

    def chg_os(self):
        print("""simplePCBuilding offers the installation of different Operating Systems. You can choose from
        following: 
        W10 = Windows 10
        W11 = Windows 11
        L = any Linux-Distro""")
