class Parent:
    def __init__(self, first_name, last_name, second_last_name=None):
        self.first_name = first_name
        self.last_name = last_name
        self.second_last_name = second_last_name

    def getFullName(self):
        if self.second_last_name:
            return f"{self.first_name} {self.last_name} {self.second_last_name}"
        return f"{self.first_name} {self.last_name}"

class Child:
    def __init__(self, first_name, dad_first_name="Marc", dad_last_name="Ferrando", dad_second_last_name="Galcera", mom_first_name="Teresa", mom_last_name="Espuny", mom_second_last_name="Escriba"):
        self.first_name = first_name
        self.dad = Parent(dad_first_name, dad_last_name, dad_second_last_name)
        self.mom = Parent(mom_first_name, mom_last_name, mom_second_last_name)

    def getFullName(self):
        return f"{self.first_name} {self.dad.last_name} {self.mom.last_name}"

    def getDadFullName(self):
        return f"El nom complet del meu pare és {self.dad.getFullName()}"

    def getMomFullName(self):
        return f"El nom complet de la meva mare és {self.mom.getFullName()}"

# Test
child = Child("Sandra")
print(child.getFullName())
print(child.getDadFullName())
print(child.getMomFullName())
