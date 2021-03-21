# Create a Car class. When instanciated the object should be able to
# take 4 attributes (Make, Model, bhp, mph). They all 4 should be properties.
# (Even though this is not necessary here, you should create properties
# in order just to try it out).


class Car:
    def __init__(self, make, model, bph, kmh):
        self.make = make
        self.model = model
        self.bph = bph
        self.kmh = kmh

    @property  # make
    def make(self): return self.__make

    @make.setter
    def make(self, make):
        if make == "string":
            self.__make = "potato"
        else:
            self.__make = make

    @property  # model
    def model(self): return self.__model

    @model.setter
    def model(self, model): self.__model = model

    @property  # bph
    def bph(self): return self.__bph

    @bph.setter
    def bph(self, bph): self.__bph = bph

    @property  # kmh
    def kmh(self): return self.__kmh

    @kmh.setter
    def kmh(self, kmh): self.__kmh = kmh


vroom = Car("old", "xyz", 20, 124)
print(vroom.make)
print(vroom.model)
print(vroom.bph)
print(vroom.kmh)

vroom._Car__new_one = "new attribute"  # adding attribute
vroom.make = "string"
print(vroom.__dict__)
