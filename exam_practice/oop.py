kirk = {"James Kirk", 34, "Captain", 2265}


class SpaceMan():
    # Class Attribute
    type = "Human"

    def __init__(self, name, age, position, id):
        # Instance attribute
        self.name = name
        self.age = age
        self.__position = position
        self.id = id

    def catchphrase(self, speech):
        return f"{self.name}'s catchphrase is :' '{speech}'"

    def __str__(self):
        return f"SpaceMan < name {self.name}, age {self.age}, position {self.__position}, id {self.id}  >"


class Captain(SpaceMan):
    type = "Alien"

    def catchphrase(self, speech="Live long and prosper"):
        return super().catchphrase(speech)


class Sargent(SpaceMan):

    def catchphrase(self, speech="Live long and prosper"):
        return super().catchphrase(speech)


class Corporal(SpaceMan):
    def catchphrase(self, speech="Live long and prosper"):
        return super().catchphrase(speech)


peter = Sargent("Peter Point", 45, "Sargent", 1001)
anders = Corporal("Anders Andersen", 28, "Corporal", 1002)
kirk = Captain("James T. Kirk", 34, "Captain", 2265)

print(kirk.catchphrase())
print(peter.catchphrase("Oh hi mark"))
print(peter)
