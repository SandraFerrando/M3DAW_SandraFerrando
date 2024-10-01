class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.abilities = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def info(self):
        return f"{self.firstname} {self.lastname}"

class Candidate(Person):
    def __init__(self, firstname, lastname, gender):
        super().__init__(firstname, lastname)
        self.gender = gender

    def info(self):
        pronoun = "He" if self.gender == 'male' else "She"
        return f"{pronoun} is {self.firstname} {self.lastname}."


# Test Input
c1 = Candidate('Manel', 'Cantells', 'male')
c1.add_ability('JavaScript')
c1.add_ability('Python')

c2 = Candidate('Maria', 'Gironés', 'female')
c2.add_ability('PHP')

# Test Output
print(c1.info())
print(c1.abilities)

print(c2.info())
print(c2.abilities)
