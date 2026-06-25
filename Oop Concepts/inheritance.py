# Inheritance: Inheritance allows a child class to use the attributes and methods of a parent class.

# class Animal:
#     def eat(self):
#         print("Eating")

#     def sleep(self):
#         print("Sleeping")


# class Dog(Animal):
#     pass #

# d = Dog()
# d.eat()
# d.sleep()

# --------------------------- Practice Questions-------------------------------------------
# 1. 
# class Person:

#     def walk(self):
#         print("walking")

# class Student(Person):
#     pass

# s1 = Student()
# s1.walk()


# 2.
# class Vehicle:

#     def start(self):
#         print("Vehicle Started")

# class Car(Vehicle):
#     pass

# car = Car()
# car.start()

# 3. 
# class Animal:

#     def eat(self):
#         print("Eating")

# class Dog(Animal):

#     def sound(self):
#         print("Dog is barking")

# d = Dog()
# d.eat()
# d.sound()

# 4. 
# class Person:
#     def __init__(self,name):
#         self.name = name

#     def print_name(self):
#         print("Hello ", self.name)

# class Student(Person):
#     pass

# s1 = Student("Muhammad Zaid")
# s1.print_name()

# 5. 
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#     def show_details(self):
#         print(f"Name: {self.name} \nSalary: {self.salary}") 

# class Manager(Employee):
#     pass

# manager = Manager("Muhammad Zaid", 100000)
# manager.show_details()

# 6. 
# class BankAccount:
#     def __init__(self,account_holder):
#         self.account_holder = account_holder

#     def name_account_holder(self):
#         print("Account Holder: ", self.account_holder)

# class SavingAccount(BankAccount):
#     pass

# savingaccount = SavingAccount("Muhammad Zaid")
# savingaccount.name_account_holder()


# -------------------------------------------Method Overriding Examples----------------------

# 1.
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog Barks")

# d = Dog()
# d.sound()

# 2.
# class Vehicle:
#     def start(self):
#         print("Vehicle started")

# class Car(Vehicle):
#     def start(self):
#         print("Car started")

# c = Car()
# c.start()

# 3. 
# class Person:
#     def intro(self):
#         print("I am a person")

# class Student(Person):
#     def intro(self):
#         print("I am a student")

# s1 = Student()
# s1.intro()        


# 4.
# class Employee:
#     def __init__(self,name):
#         self.name = name
#     def show_role(self):
#         print(f"Employee Name: {self.name}")

# class Manager(Employee):
#     def show_role(self):
#         print(f"Manager: {self.name}")

# manager = Manager("Muhammad Zaid")
# manager.show_role()


# --------------------------------------Super keyword---------------------------------------

# class Person:
#     def __init__(self,name,age,profession):
#         self.name = name
#         self.age = age
#         self.profession = profession

  

# class Student(Person):
#     def __init__(self,name,age,profession,cgpa):
#         super().__init__(name,age,profession)
#         self.cgpa = cgpa

#     def show_detail(self):
#         print(f"Name: {self.name} \nAge: {self.age} \nProfession: {self.profession} \nCGPA: {self.cgpa}")

# s1 = Student("Muhammad Zaid",23,"Student",3.2)
# s1.show_detail()


# 1.
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

# class Manager(Employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.department = department

#     def show_detail(self):
#         print(f"Name: {self.name} \nSalary: {self.salary} \nDepartment: {self.department}")

# manager = Manager("Muhammad Zaid", 100000, "Development")
# manager.show_detail()

# 2.
# class Product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

# class Mobile(Product):
#     def __init__(self,name,price,brand):
#         super().__init__(name,price)
#         self.brand = brand

#     def show_details(self):
#         print(f"Name: {self.name} \nPrice: {self.price} \nBrand: {self.brand}")

# mob = Mobile("Pixel 7", 65000, "Google")
# mob.show_details()

# class BankAccount:
#     def __init__(self, holder, balance):
#         self.holder = holder
#         self.balance = balance

# class SavingsAccount(BankAccount):
#     def __init__(self, holder, balance, interest):
#         super().__init__(holder,balance)
#         self.interest = interest

#     def show(self):
#         print(self.holder, self.balance, self.interest)

# acc = SavingsAccount("Zaid", 5000, 5)
# acc.show()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# class Manager(Employee):
#     def __init__(self, name, salary, dept):
#         super().__init__(name,salary)
#         self.dept = dept

#     def show(self):
#         print(self.name, self.salary, self.dept)

# m = Manager("Ali", 60000, "IT")
# m.show()