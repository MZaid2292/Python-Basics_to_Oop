# name = "Muhammad Zaid"
# age  = 23
# print("My name is " + name + " and I am " + str(age) + " years old.")


# num1 = int(input("Enter first Number"))
# num2 = int(input("Enter second Number"))

# sum = num1 + num2

# print("The Sum of", num1, "and", num2, "is", sum)



# num = int(input("Enter a number:\n"))

# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("the number is odd")    

# if num > 18:
#     print("you can drive")
# else:
#     print("You cannot drive")        



# #List: order collection of items, mutable, allows duplicate values, allows indexing and slicing 

# numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers.append(11)
# numbers.insert(11,12)
# numbers.pop(1)
# numbers.remove(3)
# print(numbers)


# # Tuple: ordered collection of items, immutable, allows duplicate values, allows indexing and slicing
# numbers = (1,2,3,4,5,6,7,8,9,10)
# print(numbers)

# # Set: unordered collection of unique items, mutable, does not allow duplicate values, does not allow indexing and slicing
# numbers = {1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10}
# print(numbers)


# # Dictionary: unordered collection of key-value pairs, mutable, does not allow duplicate keys, allows indexing and slicing

# student= {
#     "name":"Muhammad Zaid",
#     "age":23,
#     "city":"Hyderabad",
#     "profession":"Software Engineer"
# }

# student2 = {
#     "name":"Umrah Zadi",
#     "age":25,
#     "city":"Khairpur",
#     "profession":"Software Engineer",
# }

# print(student)
# print(student2)


# login = {
#     "username": "admin",
#     "password": "admin123"
# }

# user_name = input("Enter Username:\n")
# user_pass = input("Enter user password:\n")

# if user_name == login["username"] and user_pass == login["password"]:
#     print("Login Successful")
# else:
#     print("Invalid username or password")
    


# student = {
#     "name": "Zaid",
#     "age": 23,
#     "city": "Hyderabad"
# }

# for key in student.keys():
#     print(key)
# for value in student.values():
#     print(value)
# for key, value in student.items():
#     print(key, ":", value)        


# student = {
#     "name": "Muhammad Zaid",
#     "age": 23,
#     "city": "Hyderabad",
#     "CGPA": 3.2
# }

# for key, value in student.items():
#     print(f"Key = {key} | Value = {value}")



# get()  concept
# student = {
#     "name": "Muhammad Zaid",
#     "age": 23
# }

# # print(student.get("city"))

# # output - None (error nh aega agr get() use na karen to error hoga Q ke city exist nh karta)
# print(student.get("city", "Not Found"))
# print(student.get("name"))



# Update dictionary concept
# student = {
#     "name": "Muhammad Zaid",
#     "age": 22,
#     "city": "Khairpur"
# }

# student.update({
#     "age":23,
#     "city":"Hyderabad"
# })

# print(student)


# employee = {
#     "name": "Ali",
#     "department": "QA"
# }

# employee.update({
#     "department":"Automation QA",
#     "salary":80000,
#     "city":"Karachi"

# })

# print(employee)



# pop(): pop() removes a specific key from a dictionary and returns its value.
# student = {
#     "name": "Zaid",
#     "age": 23,
#     "city": "Hyderabad"
# }

# student.pop("city")

# print(student)

# student = {
#     "name": "Zaid",
#     "age": 23,
#     "city": "Hyderabad"
# }

# removed = student.pop("city")

# print(removed) #print removed key
# print(student)



# popitem(): popitem() removes and returns the last inserted key-value pair from a dictionary.
# pop() ➜ Tum khud key batate ho.
# popitem() ➜ Python last item ko remove karta hai.

# student = {
#     "name":"Muhammad Zaid",
#     "age":23,
#     "city":"Hyderabad"
# }
# student.popitem()
# print(student)

# output {"name":"Muhammad Zaid","age":23}



# copy(): copy() creates a copy of a dictionary.

# student = {
#     "name": "Zaid",
#     "age": 23
# }

# student2 = student.copy()

# student2["age"] = 25

# print(student)
# print(student2)

# clear(): clear() removes all items from a dictionary.
# student = {
#     "name":"Muhamamd Zaid",
#     "age":23,
#     "city":"Hyderabad"
# }

# student.clear()
# print(student)



# Scenario Question asked in interview
# api1 = {
#     "v1": "a1",
#     "v2": "a2",
#     "v3": "a3"
# }

# api2 = {
#     "a1": 1,
#     "a2": 2,
#     "a3": 3
# }

# result = {}

# for key, value in api1.items():
#     result[key] = api2[value]

# print(result)


# students = {
#     "student1":{
#         "name":"Muhammad Zaid",
#         "age":23
#     },
#     "student2":{
#         "name":"Umrah Zaid",
#         "age":23
#     }
# }

# print(students["student1"]["name"])

# employees = {
#     "emp1": {
#         "name": "Zaid",
#         "salary": 80000
#     },
#     "emp2": {
#         "name": "Usman",
#         "salary": 60000
#     }

# }

# employees["emp1"]["salary"] = 100000

# print(employees)


# 1.
# students = {
#     "student1": {
#         "name": "Ali",
#         "age": 20,
#         "city": "Karachi"
#     },
#     "student2": {
#         "name": "Zaid",
#         "age": 23,
#         "city": "Hyderabad"
#     }
# }

# print(students["student1"]["name"])
# print(students["student2"]["age"])
# print(students["student2"]["city"])


# 2.
# employee = {
#     "emp1": {
#         "name": "Ahmed",
#         "department": "QA",
#         "salary": 50000
#     }
# }

# employee["emp1"]["salary"] = 70000
# employee["emp1"]["city"] = "karachi"

# print(employee)


3.
# company = {
#     "employee1": {
#         "name": "Ali",
#         "age": 25,
#         "department": "QA"
#     },
#     "employee2": {
#         "name": "Zaid",
#         "age": 23,
#         "department": "Developer"
#     }
# }
# # print(f"Name: {company['employee1']['name']}")
# # print(f"Department: {company['employee1']['department']}")
# # print("\n")
# # print(f"Name: {company['employee2']['name']}")
# # print(f"Department: {company['employee2']['department']}")

# for key, value in company.items():
#     print(key)
#     print(value)


# students = {
#     "student1": {
#         "name": "Ali",
#         "marks": 85
#     },
#     "student2": {
#         "name": "Zaid",
#         "marks": 35
#     },
#     "student3": {
#         "name": "Ahmed",
#         "marks": 72
#     }
# }

# for key, value in students.items():
#     if value['marks'] >= 40:
#         print(f"{value['name']} Passed")
#     else:
#         print(f"{value['name']} Failed")    









# ----------------------Sets Advanced-------------------------------------
# 1.
# names = ["Ali", "Ahmed", "Ali", "Zaid", "Ahmed", "Usman"]

# # Making the list to set
# unique_names = set(names)
# # print in sorted way according to the alphabets
# print(sorted(unique_names))


# 2.
# python_students = {"Ali", "Ahmed", "Zaid", "Usman"}

# qa_students = {"Ahmed", "Zaid", "Hamza", "Bilal"}

# print(python_students)
# print(qa_students)


# 3.
# emails = [
#     "zaid@gmail.com",
#     "ali@gmail.com",
#     "zaid@gmail.com",
#     "ahmed@gmail.com",
#     "ali@gmail.com"
# ]

# unique_emails = set(emails)
# print(unique_emails)


# students = [
#     {"name": "Ali", "course": "Python"},
#     {"name": "Ahmed", "course": "QA"},
#     {"name": "Ali", "course": "Python"},
#     {"name": "Zaid", "course": "QA"}
# ]



# for _ , value in students:
#     print(value)



# -------------------------------Sets Practice---------------------------------------
# names = {"Ali", "Ahmed", "Zaid"}

# names.add("Usman")
# names.remove("Ahmed")

# print(names)

# numbers = {10, 20, 30, 40, 50, 60}

# for i in numbers:
#     if i > 30:
#         print(i)


# emails = {
#     "zaid@gmail.com",
#     "ali@gmail.com",
#     "hamza@gmail.com"
# }

# user = input("Enter an email\n")

# if user in emails:
#     print("Email Found")
# else:
#     print("Email not found")    



# numbers = {5, 10, 15, 20, 25, 30, 35, 40}
# even_num = 0
# odd_num = 0

# for i in numbers:
#     if i % 2 == 0:
#         even_num += 1
#     else:
#         odd_num += 1

# print(f"Even Numbers: {even_num}")
# print(f"Odd Numbers: {odd_num}")
          


# api1 = {101, 102, 103, 104, 105}
# api2 = {103, 104, 105, 106, 107}


# Common id
# print(f"Common Id: {api1.intersection(api2)}")
# # only api1 jo api2 men na ho 
# print(f"Only Api1: {api1.difference(api2)}")
# # only api2 jo api1 men na ho
# print(f"Only Api2{api2.difference(api1)}")


# # total unique ids
# print(f"Unique Ids: {api1.union(api2)}")
# different way 
# unique_api = api1.union(api2)
# print(unique_api)
# print(len(unique_api))



# fruits = {"Apple", "Banana", "Mango", "Orange", "Kiwi"}

# for i in fruits:
#     if len(i) > 5:
#         print(i)



# numbers = {11, 22, 33, 44, 55, 66, 77, 88}
# divisible_by_2 = 0
# not_divisible_by_2 = 0

# for i in numbers:
#     if i % 2 == 0:
#         divisible_by_2 += 1
#     else:
#         not_divisible_by_2 += 1

# print(f"Divisible by 2 = {divisible_by_2}")
# print(f"Not Divisible by 2 = {not_divisible_by_2}")



# Question 
# Print the following:
# Common users.
# Users only in API 1.
# Users only in API 2.
# Total unique users.
# Total number of unique users.


# api1 = {
#     "Ali",
#     "Ahmed",
#     "Zaid",
#     "Usman",
#     "Hamza"
# }

# api2 = {
#     "Ahmed",
#     "Hamza",
#     "Bilal",
#     "Ayan",
#     "Usman"
# }


# # Common Users
# print(f"Common users: {api1.intersection(api2)}")
# # Only Api1 users jo api2 men na ho 
# print(f"Api1 users: {api1.difference(api2)}")
# # # Only Api2 users jo api1 men na ho 
# print(f"Api2 users: {api2.difference(api1)}")

# # total unique users
# unique_users = api1.union(api2)
# print(f"Unique Users: {unique_users}")
# print(f"Total Numbers of unique users: {len(unique_users)}")


# students = {
#     "Ali",
#     "Ahmed",
#     "Zaid",
#     "Hamza",
#     "Bilal",
#     "Usman"
# }


# name = input("Enter Name:\n").title() #agr alphabet men changes ho to osy fark nh parega

# if name in students:
#     print("Student Found")
# else:
#     print("Student not found")    



# ----------------------------------------------Tupple Practice---------------------------------------------

# 1.
# api1 = ("Ali", "Ahmed", "Zaid", "Usman", "Hamza")
# api2 = ("Ahmed", "Hamza", "Bilal", "Ayan", "Usman")

# print("Common Names")
# for name in api1:    
#     if name in api2:
#         print(name) 


# 2.
# api1 = ("Ali", "Ahmed", "Zaid", "Usman", "Hamza")
# api2 = ("Ahmed", "Hamza", "Bilal", "Ayan", "Usman")

# print("Names only in API 1")
# for name in api1:
#     if name not in api2:
#         print(name)


# 3.
# students = (
#     "Ali",
#     "Ahmed",
#     "Zaid",
#     "Usman",
#     "Hamza"
# )

# name = input("Enter Name:\n").title()
# if name in students:
#     print("Student Found")
# else:
#     print("Student not found")



# 4.
# fruits = (
#     "Apple",
#     "Banana",
#     "Mango",
#     "Orange",
#     "Kiwi",
#     "Guava"
# )

# count = 0

# for i in fruits:
#     if len(i) >= 5:
#         count += 1

# print(f"Total Fruits: {count}")





# --------------------------------------Functions Practice------------------------------------
# 1.
# def greet():
#     print("Welcome Muhammad Zaid")


# greet()

# 2.
# def student(name):
#     print(f"Welcome {name}")

# student("Muhammad Zaid")
# student("Ali")
# student("Ahmed")


# 3.
# def add(a,b):
#     return a + b

# print(add(10,20))
# print(add(50,25))


# 4.
# def multiply(a,b):
#     return a * b

# result = multiply(10,5)
# print(result)


# 5.
# def check_marks(marks):
#     if marks >= 40:
#         return "Pass"
#     else:
#         return "Fail"

# print(check_marks(90))
# print(check_marks(25))
# print(check_marks(40))    


# 5.
# def even_odd(num):
#     if num % 2 ==0:
#         print("Even")
#     else:
#         print("Odd")

# print(even_odd(10))
# print(even_odd(7))
# print(even_odd(24))



# def login(username, password):
#     if username == "admin" and password == "admin123":
#         print("Login Successful")
#     else:
#         print("Invalid Credentials")

# login("admin", "admin123")
# login("Zaid", "Zaid123")


# def welcome(name = "Greet"):
#     print(f"Welcome {name}")

# welcome("Muhammad Zaid")


# def student(name, age, city):
#     print(f"Name: {name}\nAge: {age}\nCity: {city} ")

# student("Muhammad Zaid", 23, "Hyderabad")


# def calculation(a,b):
#     return a + b, a * b

# sum_result, mul_result = calculation(10,5)
# print(f"Sum: {sum_result}\nMultiplication: {mul_result}")


# def largest(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# print(f" Largest: {largest(10,20,30)}")




# def calcualation(a,b):
#     return a + b, a - b, a * b, a / b

# add, sub, mul, div = calcualation(10,5)
# print(f"Addition: {add}\nSubtraction: {sub}\nMultiplication: {mul}\nDivision: {div}")



def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg


numbers = [10, 20, 30, 40, 50]

result = average(numbers)

print(f"Average = {result}")