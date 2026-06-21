
# 1. Write a function to calculate and return the square of a number
def calculate_square(num):
    return num ** 2

result = calculate_square(10)
print(result)

# 2. Create a function that takes two number as a paramters and returns their sum

def add_numbers(num1,num2):
    return num1 + num2

result = add_numbers(10,20)
print("The Sum of two numbers is:", result) 

# 3. (Polymorphism) Write a function multiply that multiplies two numbers but can also accept and multiply strings.
# Polymorphism is use for the same function name but different behavior.

def multiply(p1 , p2):
    return p1 * p2

print(multiply(10, 3))
print(multiply("U",3))
print(multiply(3, "Z"))

# 4. Create a function that returns both the area and circumference of a circle when given the radius as a parameter.
import math
def circle_stats(radius):
    area = round(math.pi * radius ** 2, 2)
    circumference = round(2 * math.pi * radius , 2)
    return area, circumference
    
a , c = circle_stats(5)
print("Area of Circle:", a, "\nCircumference of Circle:", c)   


# 5. Write a function that greets a user. If no name is provided, it should greet with a default name.
def greet_user(name="Muhammad Zaid"):
    return "Hello " + name + "!"

# print(greet_user("Umrah Zadi"))  #Name is provided
print(greet_user())  #No name is provided, so it will use the default name


# 6. Lambda Function: Create a lambda function to compute the cube of a number.
cube = lambda x: x ** 3
print(cube(3))


# 7. Write a function that takes variable number of arguments and returns their sum.
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4, 5)) 
print(sum_all(10, 20, 30))

# -------------------------------------Loops & Functions-------------------------------------

# 1. Greeting Multiple users.
def greet(name):
    return "Hello " + name

names = ["Muhammad Zaid", "Umrah Zadi", "Umrah Zaid"]

for name in names:
    print(greet(name))


# 2. Square of Numbers
def square(num):
    return num ** 2

numbers = [1,2,3,4,5,6,7]

for number in numbers:
    print("Square of ", number, "is:", square(number))


# 3. check Even and odd Numbers.
def check_even(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"
for i in range(1,11):
    print(i, "is", check_even(i))


# ----------Dictionary Looping with Functions----------
def show_student(student):
    # return student
    print(student["name"], ":", student["age"])

students = [
    {"name":"Muhammad Zaid","age":23,"city":"Hyderabad"},
    {"name":"Umrah Zadi","age":25,"city":"Khairpur"},
    
]

for student in students:
    # print(show_student(student))
    show_student(student)




# Print cube of 1-10 numbers using function and loop
def cube(num):
    return num ** 3

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    print("Cube of ", number, "is", cube(number))

# Using Another way 
def cube(num):
    return num ** 3

for i in range(1,11):
    print("Cube of ", i, "is", cube(i))


 