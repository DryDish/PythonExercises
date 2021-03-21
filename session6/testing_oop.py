class Person:

    species = 'Mammal' 			# class variable

    def __init__(self, *args):
        # self.name = name  		# instance variable

        if len(args) == 1:
            self.name = args[0]

        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]

    def name_age(self):
        return self.name + str(self.age)


class Instructor:
    def __init__(self, course):
        self.course = course


class Student(Person, Instructor):

    def __init__(self, *args):
        Person.__init__(self, args[0], args[1])
        Instructor.__init__(self, args[2])
        super().__init__(args)


p = Person("Peter", 12)
p1 = Person("Anna", 14)


print("p.name: ", p.name)
print("p1.name: ", p.name)
print("All instances variables: ", Person.__dict__)

p.name = "Henning"
print("p.name is now : ", p.name)

p.age = 12      # adding a new variable, some how
print("p.__dict___ : ", p.__dict__)

p = Person("peter", 12)
print("person with extra args: ", p.__dict__)
print("person name_age() : ", p.name_age())

inherited = Student("peter", 12, 2)
print("inherited dict: ", inherited.__dict__)
print("inherited name", inherited.name)
# print("inherited age", inherited.age)  # this crashes currently
