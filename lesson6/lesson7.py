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

#  Trout inherits from Fish
#  fish is a parent class -


class Trout(Fish):  #  IS A - Relationship
    def singing(self):
        print("a trout can sing")


class Shark(Fish):
    def eat(self):
        print("Sharks eat anything literally")

#inherits from Trout/ Fish

class Omena(Trout):
    def small_size(self):
        print("it's very small")

#  method overriding
    def swim(self):
        print("shhhhhhhhhh")


# create a class BrownFish that extends Omena class

class BrownFish(Omena):
    def guggle(self):
        print("I can guggle")



object = Omena("BrownFish", 56, 8)
object.swim()

