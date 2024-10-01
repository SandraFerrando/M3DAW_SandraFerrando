class Dad:
    def __init__(self, firstName, lastName, name):
        self.dad_firstName = firstName
        self.dad_lastName = lastName
        self.dad_name = name

    def getDadFirstName(self):
        return self.dad_firstName

    def getDadFullName(self):
        return f"El nom complet del meu pare és {self.dad_name} {self.dad_firstName} {self.dad_lastName}"

class Mom:
    def __init__(self, firstName, lastName, name):
        self.mom_firstName = firstName
        self.mom_lastName = lastName
        self.mom_name = name

    def getMomFirstName(self):
        return self.mom_firstName

    def getMomFullName(self):
        return f"El nom complet de la meva mare és {self.mom_name} {self.mom_firstName} {self.mom_lastName}"

class Child(Dad, Mom):
    def __init__(self, name, dad_firstName="Ferrando", mom_firstName="Espuny", dad_lastName="Galcera", mom_lastName="Escriba", dad_name="Marc", mom_name="Teresa"):
        Dad.__init__(self, dad_firstName, dad_lastName, dad_name)
        Mom.__init__(self, mom_firstName, mom_lastName, mom_name)
        self.name = name

    def getFullName(self):
        return f"El meu nom complert és {self.name} {self.getDadFirstName()} {self.getMomFirstName()}"

# Test
child = Child("Sandra")
print(child.getFullName())
print(child.getDadFullName())
print(child.getMomFullName())