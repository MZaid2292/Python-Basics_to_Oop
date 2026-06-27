
# Getters:A getter is a method used to access the value of a private variable.
# 1.
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

# Getter Method
    def get_balance(self):
        print("Balance: ", self.__balance)

bank = BankAccount(100000)
bank.get_balance()

# 2.
class Student:
    def __init__(self):
        self.__cgpa = 3.5

    def get_cgpa(self):
        print("CGPA: ",self.__cgpa) 

s1 = Student()
s1.get_cgpa()



# Setter:A setter is a method used to update the value of a private variable and can also perform
# validation before updating it.

class Student:
    def __init__(self):
        self.__cgpa = 3.2

    def set_cgap(self,cgpa):
        if 0 <= cgpa <= 4:
            self.__cgpa = cgpa
            print("CGPA Updated Successfully")
        else:
            print("Inavlid CGPA")

    def show_cgpa(self):
        print("CGPA: ",self.__cgpa)

s1 = Student()

# Show CGPA
s1.show_cgpa()

# Set CGPA
s1.set_cgap(3.5)

# Again show CGPA
s1.show_cgpa()

# Giving invalid input
s1.set_cgap(10)

s1.show_cgpa()   #Print Again 3.5

class BankAccount:
    def __init__(self):
        self.__balance = 50000
    
    def set_balance(self,balance):
        if balance >= 0:
            self.__balance = balance
            print("Balance Updated Successfully")
        else:
            print("Invalid Balance")

    def show_balance(self):
        print(f"Balance: {self.__balance}")

bank = BankAccount()

bank.show_balance()

bank.set_balance(100000)

bank.show_balance()



# -------------------------------------------Practice Questions-------------------------------

# 1. setter only
class Employee:
    def __init__(self):
        self.__salary = 50000

    def set_salary(self,salary):
        if salary >= 0:
            self.__salary = salary
            print("Salary Updated")
        else:
            print("Invalid Salary")

    def show_salary(self):
        print("Salary: ",self.__salary)

emp = Employee()

# Print Before Updated
emp.show_salary()

# Update Salary
emp.set_salary(80000)

# Print After Updated
emp.show_salary()

# Again Update
emp.set_salary(-1000)

# Print Again
emp.show_salary()

# 2. Getter only
class University:
    def __init__(self):
        self.__university_name = "Mehran University"

    def get_university_name(self):
        return self.__university_name

uni = University()
print(uni.get_university_name())


# 3. Combine setter and getter
class Mobile:
    def __init__(self):
        self.__price = 50000

# Setter Method
    def set_price(self,price):
        if price >= 0:
            self.__price = price
            print("Price Updated")
        else:
            print("Invalid Price")

# Getter Method
    def get_price(self):
        return self.__price 

mob = Mobile()

# Current Price
print("Price: ",mob.get_price())

# Price Updated
mob.set_price(80000)

# Again Print
print("Price: ",mob.get_price())


# 4. Combine Getter and Setter
class ExamResult:
    def __init__(self):
        self.__marks = 0

    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks Updated")
        else:
            print("Invalid Marks")

    def get_marks(self):
        return self.__marks

exam = ExamResult()

exam.set_marks(80)
print(exam.get_marks())

exam.set_marks(120)
print(exam.get_marks())


