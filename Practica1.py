class Dad:
    def __init__(self, firstName, lastName, name):
        self.firstName = firstName
        self.lastName = lastName
        self.name = name

    def getDadFirstName(self):
        return "El meu nom es " + self.firstName
    
    def getDadFullName(self):
        return "El meu nom complet es " + self.name + " " + self.firstName + " " + self.lastName

class Mom:
    def __init__(self, firstName, lastName, name):
        self.firstName = firstName
        self.lastName = lastName
        self.name = name

    def getMomFirstName(self):
        return "El teu nom es " + self.firstName

    def getMomFullName(self):
        return "El teu nom complet es " + self.name + " " + self.firstName + " " + self.lastName

class Child(Dad, Mom):
    def __init__(self, name, firstName, lastName):
        Dad.__init__(self, firstName, lastName, name)
        Mom.__init__(self, firstName, lastName, name)
        self.name = name

    def getFullName(self):
        return "El teu nom complet es " + self.name + " " + Dad.firstName + " " + Mom.firstName



#Test

child = Child("Sandra")
print(child.getFullName())
print(child.getDadFullName())
print(child.getMomFullName())