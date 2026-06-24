# A class is a blueprint or template used to create objects. It defines the properties
# (variables) and behaviors (methods) that objects will have.


# Object: An object is an instance of a class. It is a real entity created from a class.

class Student:
    pass

s1 = Student()  #Object
s1.name = "Muhammad Zaid"
s1.age = 23

print(s1.name)
print(s1.age)



# What is Self?
# self refers to the current object of the class. It is used to access the
#  object's variables and methods.

class Student:
    def __init(self,name):
        self.name = name


# What is __init__
# __init__() is a constructor in Python. It is automatically called when an object is created.

class Student:  #Class
    def __init__(self,name):  #Constructor
        self.name = name

s1 = Student("Muhammad Zaid")  #Object
print(s1.name)


# What is a method
# A method is a function defined inside a class.

class Student:
    def greet(self):
        print("Hello Muhammad Zaid")

s1 = Student()
s1.greet()


class Student:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print("Hello " + self.name)

s1 = Student("Muhammad Zaid")
s1.greet()


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello " , self.name)

    def show_age(self):
        print("You're ", self.age, "years old")

s1 = Student("Muhammad Zaid",23)
s1.greet()
s1.show_age()


# Practice Questions
# 1. 
class Car:
    def __init__(self,brand):
        self.brand = brand

    def show_brand(self):
        print("The Car brand is", self.brand)

car = Car("Toyota")
car.show_brand()


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        # print("Name: ", self.name, "\nAge: ",self.age )   
        print(f"Name: {self.name}, Age: {self.age} ") 

s1 = Student("Muhammad Zaid", 23)
s1.show_info()


# Question 1: Print Car brand and color by using show_info method

class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def show_info(self):
        print(f"Brand: {self.brand} \nColor: {self.color}")

car = Car("Toyota Corolla", "Black Color")
car.show_info()   

# Question 2: Employee Class Requirements: Name and Salary
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_detail(self):
        print(f"Name: {self.name} \nSalary: {self.salary}")

employee = Employee("Muhammad Zaid", 100000)
employee.show_detail()

# Question Calculator Class Requirements 2 number(a,b) method add() multiply
class Calculator:
    def __init__(self, a , b):
        self.a = a
        self.b = b

    def add(self):
        print(f"Sum: {self.a + self.b}")

    def multiply(self):
        print(f"Multiply: {self.a * self.b}")

calculator = Calculator(10, 5)
calculator.add()
calculator.multiply()

class StudentMarks:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def result(self):
        print(f"Name: {self.name} \nMarks: {self.marks}")
        if self.marks >= 50:
            print("Pass")
        else:
            print("Fail")
       

s1 = StudentMarks("Muhammad Zaid",40)
s2 = StudentMarks("Umrah Zadi", 80)

s1.result()
s2.result()