# Bad way
class Testing:
    def __init__(self, x, y):
        self.__set_x(x)
        self.__set_y(y)

    # Getters and Setters have to be private or else we have two ways -
    #  of doing something (not pythonic)
    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    def __get_y(self):
        return self.__y

    def __set_y(self, y):
        self.__y = y

    # Fix for bad setup to be able to call var.x -
    # instead of var.get_x()
    x = property(__get_x, __set_x)
    y = property(__get_y, __set_y)


testing = Testing(10001, 2)
print("Testing:", testing.x, testing.y)


# Proper Properties way
class Tester:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


tester = Tester(10001, 2)
print(type(tester.x))
print("Tester:", tester.x, tester.y)
