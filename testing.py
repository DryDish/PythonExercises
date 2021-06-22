

def function(**kwargs):
    name = kwargs["name"]
    lastname = kwargs["lastname"]
    person = {"name": name, "lastname": name}
    return person


class Person:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.lastname = kwargs["lastname"]


functionPerson = function(name="peter", lastname="griffin")
personPerson = Person(name="Jens", lastname="Jensen")

print(functionPerson["name"])
print(personPerson.name)
