class Dad:
    def __init__(self, firstName="Galcera", lastName="Ferrando", name="Marc"):
        self.firstName = firstName
        self.lastName = lastName
        self.name = name

    def getDadFirstName(self):
        return self.firstName

    def getDadFullName(self):
        return f"{self.firstName} {self.lastName} {self.name}"

class Mom:
    def __init__(self, firstName="Escriba", lastName="Espuny", name="Teresa"):
        self.firstName = firstName
        self.lastName = lastName
        self.name = name

    def getMomFirstName(self):
        return self.firstName

    def getMomFullName(self):
        return f"{self.firstName} {self.lastName} {self.name}"

class Child(Dad, Mom):
    def __init__(self, name):
        Dad.__init__(self)
        Mom.__init__(self)
        self.name = name

    def getFullName(self):
        return f"{self.name} {Dad.lastName} {Mom.lastName}"

    def getDadFullName(self):
        return Dad.getDadFullName(self)

    def getMomFullName(self):
        return Mom.getMomFullName(self)

# Test
child = Child("Sandra")
print(child.getFullName())
print(child.getDadFullName())
print(child.getMomFullName())
