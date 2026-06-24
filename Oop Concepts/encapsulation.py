# Encapsulation: Encapsulation is used to hide and protect data by making variables private.

# 1.
class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.__cgpa = cgpa

    def show_details(self):
        print(f"Name: {self.name} \nCGPA: {self.__cgpa}")

s1 = Student("Muhammad Zaid",3.2)
s1.show_details()

# 2.
class Employee:
    def __init__(self):
        self.__salary = 100000

    def show_salary(self):
        print(f"Salary: {self.__salary}")

emp = Employee()
emp.show_salary()


# 3.
# class BankAccount:
#     def __init__(self,name):
#         self.name = name
#         self.__balance = 100000 #We can write it like or we can use it inside object 

#     def show_details(self):
#         print(f"Name: {self.name} \nBalance: {self.__balance}")

# bank = BankAccount("Muhammad Zaid")
# bank.show_details()

# Same Question but different way 
class BankAccount:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def show_details(self):
        print(f"Name: {self.name} \nSalary: {self.__salary}") 

bank = BankAccount("Muhammad Zaid", 100000)
bank.show_details() #But isko bhe access sirf method ke through kar sakty direct nh 


# 4.
class User:
    def __init__(self):
        self.__password = "12345"

    def show_password(self):
        print("Password: ", self.__password)

user = User()
user.show_password()


# --------------------------------------Practice Questions-------------------------------

print("\n\nPractice Qusestions\n\n")

# 1.
class ExamResult:
    def __init__(self,student_name,marks):
        self.student_name = student_name
        self.__marks = marks

    def show_result(self):
        print(f"Student Name: {self.student_name} \nMakrs: {self.__marks}")
        if self.__marks >= 50:
            print("Pass")
        else:
            print("Fail")

s1 = ExamResult("Muhammad Zaid", 80)
s1.show_result()


# 2.
class Product:
    def __init__(self,name,price):
        self.name = name
        self.__price = price
    def product_detail(self):
        print(f"Product Name: {self.name} \nPrice: {self.__price}")

product = Product("Laptop",120000)
product.product_detail()


# 3. 
class Patient:
    def __init__(self,name,disease):
        self.name = name
        self.__disease = disease

    def show_patient(self):
        print(f"Name: {self.name} \nDisease: {self.__disease}")

patient = Patient("Muskan", "Kidney Stone")
patient.show_patient()

# 4.
class YoutubeChannel:
    def __init__(self,name):
        self.name = name
        self.__subscribers = 12000

    def show_channel(self):
        print(f"Name: {self.name} \nSubscribers: {self.__subscribers}")

youtube = YoutubeChannel("Muhammad Zaid")
youtube.show_channel()
