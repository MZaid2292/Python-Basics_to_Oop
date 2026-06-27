# Polymorphism means one interface, many implementations.
#  The same method can behave differently for different objects.

# 1.
class Shape:
    def draw(self):
        print("The Shape")


class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")


c = Circle()
c.draw()

r = Rectangle()
r.draw()


# 2.
class Animal:
    def move(self):
        print("Moving")

class Dog(Animal):
    def move(self):
        print("Dog runs")

class Bird(Animal):
    def move(self):
        print("Bird Flies")

class Fish(Animal):
    def move(self):
        print("Fish Swims")

d = Dog()
d.move()

b = Bird()
b.move()

f = Fish()
f.move()


# 3.
class Account:
    def account_type(self):
        print("Account Type")

class SavingsAccount(Account):
    def account_type(self):
        print("Savings Account")

class CurrentAccount(Account):
    def account_type(self):
        print("Current Account")

s = SavingsAccount()
s.account_type()

c = CurrentAccount()
c.account_type()

# 4.
class Browser:
    def open_browser(self):
        print("Open Browser")

class Chrome(Browser):
    def open_browser(self):
        print("Opening Chrome")

class Firefox(Browser):
    def open_browser(self):
        print("Opening Firefox")

class Edge(Browser):
    def open_browser(self):
        print("Opening Edge")

c = Chrome()
c.open_browser()

f = Firefox()
f.open_browser()

e = Edge()
e.open_browser()



# 5. loop plus polymorphism
class Employee:
    def work(self):
        print("Employees Work")

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Tester(Employee):
    def work(self):
        print("Tester tests software")

class Designer(Employee):
    def work(self):
        print("Designer creates UI")


employees = [Developer(), Tester(), Designer()]

for employee in employees:
    employee.work()


# ---------------------------------More Questions using loops---------------------------------------

# 1.
class Food:
    def prepare(self):
        print("Prepare Food")

class Pizza(Food):
    def prepare(self):
        print("Prepare Pizza")

class Burger(Food):
    def prepare(self):
        print("Prepare Burger")

class Biryani(Food):
    def prepare(self):
        print("Prepare Biryani")

foods = [Pizza(), Burger(), Biryani()]

for food in foods:
    food.prepare()



# 2.
class Payment:
    def pay(self):
        print("Pay")

class JazzCash(Payment):
    def pay(self):
        print("Payment through JazzCash")

class EasyPaisa(Payment):
    def pay(self):
        print("Payment through EasyPaisa")

class CreditCard(Payment):
    def pay(self):
        print("Payment through Credit Card")

payments = [JazzCash(), EasyPaisa(), CreditCard()]

for payment in payments:
    payment.pay()


























class Person:
    def intro(self):
        print("I'm a person")

class Student(Person):
    def intro(self):
        print("I'm a student")

class Teacher(Person):
    def intro(self):
        print("I'm a Teacher")

persons = [Person(), Student(), Teacher()]

for person in persons:
    person.intro()
