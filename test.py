class Human():
    def __init__(self, price, name="n/a"):
        print("human created")
        self.age = 0
        self.numberOfLegs = 2
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        ret = " "
        ret += "\n Name: "
        ret += self.name
        ret += "\n Age:"
        ret += str(self.age)
        return ret

class Lumberjack(Human):
    def __init__(self):
        print("Lumberjack created")
        #ruft den Konstruktor der Oberklasse auf
        Human.__init__(self, 300)


myL = Lumberjack()

print(myL.name)


#doxygen --> For documentation