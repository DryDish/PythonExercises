
# Create a Machine class that takes care of powering on and off a the machine.
# Create a printer class that is a subclass of the Machine super class.
# The printer should be able to print to console.
# The printer should have a papertray, which should be in its own class.
# The papertray class should keep track of the paper,
#   it should have the ability to use paper and
#   load new paper in the tray if empty.

# Machine : On - Off
# Printer: Print(ifHasPaper) to console
# Papertray: list(paper), load new paper

# Machine -> Printer -> Papertray

class Machine():
    def __init__(self):
        self.is_powered = False

    def toggle_power(self):
        if self.__is_powered:
            self.__is_powered = False
            print("The Machine is now: Off")
        else:
            self.__is_powered = True
            print("the machine is now: On")

    @property
    def is_powered(self):
        return self.__is_powered

    @is_powered.setter
    def is_powered(self, status):
        self.__is_powered = status

    def __repr__(self):
        return "\n" + str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)


class Papertray():
    def __init__(self, paper):
        self.paper = paper

    def print(self, pages):
        if pages > self.paper:
            print("Not enough paper remaining, please refill.")
            return self.__paper
        else:
            self.paper -= pages
            print("Print successful, remaining pages", self.__paper)

    def refill_paper(self, quantity):
        self.paper += quantity
        print("Paper refilled by", quantity, ".")
        print("Paper is now at:", self.paper)

    @property
    def paper(self):
        return self.__paper

    @paper.setter
    def paper(self, quantity):
        self.__paper = quantity

    def __repr__(self):
        return "\n" + str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)


class Printer(Machine, Papertray):
    def __init__(self, paper, status):
        Papertray.__init__(self, paper)
        Machine.__init__(self)

    def print(self, print_quant):
        if (self.is_powered):
            Papertray.print(self, print_quant)
        else:
            raise ConnectionError("Printer is not powered")


heward_packard = Printer(100, False)  # created printer with 100 pages in tray
try:  # it will crash if the printer is not powered
    print("Printer is on? :", heward_packard.is_powered)
    heward_packard.toggle_power()
    heward_packard.print(90)
    heward_packard.refill_paper(150)
    heward_packard.print(140)
    print("-- attempting to print 30 pages --")
    heward_packard.print(30)  # this should not work
    print("-- adding 199 pages to tray --")
    heward_packard.refill_paper(199)
    heward_packard.print(30)  # now should work
except ConnectionError:
    print("You need to power on the machine before you can print.")
    print("You can do that by calling <printername>.toggle_power")


class Papertray():
    def __init__(self, text=""):
        self.paper_list = [text]
        self.current_paper = self.paper_list[0]

    def load_paper(self, text=""):
        self.current_paper = text
        self.paper_list.append(self.current_paper)

    def use_paper(self, pos=0):
        self.current_paper = self.paper_list[pos % len(self.paper_list)]

    @property
    def paper_list(self):
        return self.__paper_list

    @property
    def current_paper(self):
        return self.__current_paper

    @paper_list.setter
    def paper_list(self, paper_list):
        self.__paper_list = paper_list

    @current_paper.setter
    def current_paper(self, current_paper):
        self.__current_paper = current_paper
