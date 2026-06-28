# Abstraction: Abstraction is the process of hiding implementation details and showing only 
# essential functionality.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        print("Animal Move")

class Dog(Animal):
    def move(self):
        print("Dog Runs")

class Bird(Animal):
    def move(self):
        print("Bird flies")

class Fish(Animal):
    def move(self):
        print("Fish Swims")

animals = [Animal(),Dog(),Bird(),Fish()]
for animal in animals:
    animal.move()


# 2.
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

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

# 3.
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @abstractmethod
    def show_details(self):
        pass    

class Student(Person):
    def __init__(self,name,age,department,cgpa):
        super().__init__(name,age)
        self.department = department
        self.cgpa = cgpa 

    def show_details(self):
        print(f"Name: {self.name} \nAge: {self.age} \nDepartment: {self.department} \nCGPA: {self.cgpa}")


s1 = Student("Muhammad Zaid",23,"Software Engineer",3.2)
s1.show_details()


# ------------------------------Practice Questions--------------------------------------
# 1.
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")

class Bike(Vehicle):
    def start(self):
        print("Bike Started")

vehicles = [Car(), Bike()]

for vehicle in vehicles:
    vehicle.start()


# 2.
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Tester(Employee):
    def work(self):
        print("Tester tests Software")

employees = [Developer(), Tester()]
for employee in employees:
    employee.work()


# 3.
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_basic_info(self):
        print(f"Name: {self.name} \nAge: {self.age}")

    @abstractmethod
    def show_details(self):
        pass

class Student(Person):
    def __init__(self,name,age,rollno,department,cgpa):
        super().__init__(name,age)
        self.rollno = rollno
        self.department = department
        self.cgpa = cgpa

    def show_details(self):
        print(f"Name: {self.name} \nAge: {self.age} \nRoll No: {self.rollno} \nDepartment: {self.department} \nCGPA: {self.cgpa}")

s1 = Student(
    "Muhammad Zaid",
    23,
    "K22SW019",
    "Software Engineering",
    3.2
)  


s1.show_details()


# 4.
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    @abstractmethod
    def show_details(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self,account_holder,balance,account_type):
        super().__init__(account_holder,balance)
        self.account_type = account_type

    def show_details(self):
        print(f"Account Holder: {self.account_holder} \nBalance: {self.balance} \nAccount Type: {self.account_type}")

class CurrentAccount(BankAccount):
    def __init__(self,account_holder,balance,account_type):
        super().__init__(account_holder,balance)
        self.account_type = account_type

    def show_details(self):
        print(f"Account Holder: {self.account_holder} \nBalance: {self.balance} \nAccount Type: {self.account_type}")


accounts = [
    SavingsAccount("Muhammad Zaid", 100000, "Savings Account"),
    CurrentAccount("Zaid Nizamani", 200000, "Current Account")
    ]

for account in accounts:
    account.show_details()


# 5.
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_person(self):
        print(f"Name: {self.name} \nAge: {self.age}")

    @abstractmethod
    def show_profile(self):
        pass

class Student(Person):
    def __init__(self,name,age,rollno,cgpa,department):
        super().__init__(name,age)
        self.rollno = rollno
        self.cgpa = cgpa
        self.department = department

    def show_profile(self):
        print(f"Name: {self.name} \nAge: {self.age} \nRoll No: {self.rollno} \nCGPA: {self.cgpa} \Department: {self.department}")

class Employee(Person):
    def __init__(self,name,age,employee_id,subject,salary):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.subject = subject
        self.salary = salary

    def show_profile(self):
        print(f"Name: {self.name} \nAge: {self.age} \nEmployee Id: {self.employee_id} \nSubject: {self.subject} \nSalary: {self.salary}")

peoples = [
    Student("Muhammad Zaid", 23, "K22SW019", 3.2, "Software Engineering"),
    Employee("Zaid Nizamani", 25 , 123 , "Developer", 100000)

]

for people in peoples:
    people.show_profile()