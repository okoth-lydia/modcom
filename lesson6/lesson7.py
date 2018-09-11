#inheritance
#one object can borrow properties/functions from another object


class Fish():
    def __init__(self, name, weight, age):

        self.name = name
        self.weight = weight
        self.age = age

    def swim(self):
        print("a fish can swim")

    def swim_backwards(self):
        print("it's moving backwards")

    def jump(self):
        print("look it just jumped")