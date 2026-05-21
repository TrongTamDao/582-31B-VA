class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius # we have our private property

    # this helps our class to understand that celsius is a private property and calling
    # celsius function basically allows access to the private property
    @property
    def celsius(self):
        return self.__celsius
    # write as a method, but use it like a field/attribute!

    # now we need a setter
    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self._celsius = value
        else:
            print("Invalid temperature")

print("======")
t = Temperature(-25)
print(t.celsius)

t.celsius = 30
print(t.celsius)

t.celsius = -500
print(t.celsius)