# Inheritance: Inheritance allows us to define a class that inherits all the methods
#  and properties from another class.

class Animal:
    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Dog(Animal):
    pass

d = Dog()
d.eat()
d.sleep()