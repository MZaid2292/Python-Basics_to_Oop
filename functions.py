
# # 1. Write a function to calculate and return the square of a number
# def calculate_square(num):
#     return num ** 2

# result = calculate_square(10)
# print(result)

# # 2. Create a function that takes two number as a paramters and returns their sum

# def add_numbers(num1,num2):
#     return num1 + num2

# result = add_numbers(10,20)
# print("The Sum of two numbers is:", result) 

# # 3. (Polymorphism) Write a function multiply that multiplies two numbers but can also accept and multiply strings.
# # Polymorphism is use for the same function name but different behavior.

# def multiply(p1 , p2):
#     return p1 * p2

# print(multiply(10, 3))
# print(multiply("U",3))
# print(multiply(3, "Z"))

# # 4. Create a function that returns both the area and circumference of a circle when given the radius as a parameter.
# import math
# def circle_stats(radius):
#     area = round(math.pi * radius ** 2, 2)
#     circumference = round(2 * math.pi * radius , 2)
#     return area, circumference
    
# a , c = circle_stats(5)
# print("Area of Circle:", a, "\nCircumference of Circle:", c)   


# # 5. Write a function that greets a user. If no name is provided, it should greet with a default name.
# def greet_user(name="Muhammad Zaid"):
#     return "Hello " + name + "!"

# # print(greet_user("Umrah Zadi"))  #Name is provided
# print(greet_user())  #No name is provided, so it will use the default name


# # 6. Lambda Function: Create a lambda function to compute the cube of a number.
# cube = lambda x: x ** 3
# print(cube(3))


# # 7. Write a function that takes variable number of arguments and returns their sum.
# def sum_all(*args):
#     return sum(args)
# print(sum_all(1, 2, 3, 4, 5)) 
# print(sum_all(10, 20, 30))

# # -------------------------------------Loops & Functions-------------------------------------

# # 1. Greeting Multiple users.
# def greet(name):
#     return "Hello " + name

# names = ["Muhammad Zaid", "Umrah Zadi", "Umrah Zaid"]

# for name in names:
#     print(greet(name))


# # 2. Square of Numbers
# def square(num):
#     return num ** 2

# numbers = [1,2,3,4,5,6,7]

# for number in numbers:
#     print("Square of ", number, "is:", square(number))


# # 3. check Even and odd Numbers.
# def check_even(num):
#     if num % 2 == 0:
#         return "Even"
#     return "Odd"
# for i in range(1,11):
#     print(i, "is", check_even(i))


# # ----------Dictionary Looping with Functions----------
# def show_student(student):
#     # return student
#     print(student["name"], ":", student["age"])

# students = [
#     {"name":"Muhammad Zaid","age":23,"city":"Hyderabad"},
#     {"name":"Umrah Zadi","age":25,"city":"Khairpur"},
    
# ]

# for student in students:
#     # print(show_student(student))
#     show_student(student)




# # Print cube of 1-10 numbers using function and loop
# def cube(num):
#     return num ** 3

# numbers = [1,2,3,4,5,6,7,8,9,10]

# for number in numbers:
#     print("Cube of ", number, "is", cube(number))

# # Using Another way 
# def cube(num):
#     return num ** 3

# for i in range(1,11):
#     print("Cube of ", i, "is", cube(i))


 




# -----------------------------------*args Practice-----------------------------------
# def calculate_sum(*args):
#     total = 0

#     for num in args:
#         total += num
#     return total

# result = calculate_sum(10,20,30,40)
# print(f"The Sum of all numbers is: {result}")




# Calculate Product
# def calculate_product(*args):
#     product = 1

#     for num in args:
#         product *= num
#     return product

# result = calculate_product(2, 3, 4)
# print(f"The Product of all numbers is: {result}")


# Calculate Average
# def calculate_average(*args):
#     total = 0
#     count = len(args)

#     for num in args:
#         total += num
#     # return total
#     average = total / count
#     return average

# result = calculate_average(10, 20, 30, 40)
# print(f"The Average of all numbers is: {result}")
    


# Count even
# def count_even(*args):
#     count = 0

#     for num in args:
#         if num % 2 == 0:
#             count += 1
#     return count


# result = count_even(10, 15, 20, 25, 30)
# print(f"Total Even Numbers: {result}")



# Largest Number:
# def largest_num(*args):
#     large = [0]

#     for num in args:
#         if num > large[0]:
#             large[0] = num
#     return large[0]

# result = largest_num(15, 80, 25, 100, 45)        
# print(f"Largest Number: {result}")















# ----------------------------------Lambda functions----------------------------------------
# square = lambda num: num * num
# print(square(5))


# add = lambda a , b: a + b

# result = add(10, 20)
# print(result)


# Practice Questions:
# 1.
# cube = lambda num: num ** 3
# print(cube(4))

# maximum = lambda a , b: a if a > b else b
# result = maximum(10, 15)
# print(result)



# check_number = lambda num: "Positive" if num > 0 else "Zero" if num == 0 else "Negative"
# print(check_number(-5))


# Even odd
# even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
# print(even_odd(9))



# final_price = lambda price, discount_price: price - (price * discount_price / 100)
# print(final_price(1000, 20))




# -----------------------------Map() function-------------------------------------------
# map() is used to apply a function to every item in a list and return the transformed values.
# numbers = [1,2,3,4]

# result = list(map(lambda num: num * 2, numbers))
# print(result)


# --------------------Practice Question-------------------------------------
# numbers = [2, 4, 6, 8, 10]
# result = list(map(lambda num: num * 2, numbers))
# print(result)

# numbers = [1, 2, 3, 4, 5]
# result = list(map(lambda num: num * num, numbers))
# print(result)

# names = ["zaid", "ali", "ahmed"]
# result = list(map(lambda name: name.upper(), names))
# print(result)

# # numbers = [5, 10, 15, 20]
# # result = list(map(lambda num: num + 10, numbers))
# # print(result)


# celsius = [0, 10, 20, 30]
# result = list(map(lambda temp: (temp * 9/5) + 32, celsius))
# print(result)



# ----------------------------------Filter()------------------------------------------
# filter() is used to select only those items from a list that match a condition.

# Example
# numbers = [1,2,3,4,5,6]
# result = list(filter(lambda num: num % 2 == 0, numbers))
# print(result)


# -------------------------------Practice Questions-----------------------------------------
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# result = list(filter(lambda num: num % 2 == 0, numbers))
# print(result)


# numbers = [-10, 5, -3, 8, 0, 12, -7]
# result = list(filter(lambda num: num >= 0, numbers))
# print(result)


# numbers = [20, 55, 10, 80, 45, 100, 30]
# result = list(filter(lambda num: num > 50, numbers))
# print(result)


# names = ["Ali", "Zaid", "Ahmed", "Bilal"]
# result = list(filter(lambda name: name.startswith("A"), names))
# print(result)


# ages = [12, 18, 25, 16, 30, 15, 21]
# result = list(filter(lambda age: age >= 18, ages))
# print(result)



# --------------------------reduce()---------------------------------------------------
# reduce() is used to combine all items of a list and return one final value.

# map()     → Har item ko transform karta hai
# filter()  → Condition ke according items select karta hai
# reduce()  → Sab items combine karke ek final value deta hai

# Example
# from functools import reduce
# numbers = [2 , 3 , 4]
# result = reduce(lambda x, y: x * y,numbers)
# print(result)


# --------------------------------Practice Questions------------------------------------------
# 1.
# from functools import reduce
# numbers = [10, 20, 30, 40]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)

# 2.
# from functools import reduce
# numbers = [2, 5, 3, 4]
# result = reduce(lambda a, b: a * b, numbers)
# print(result)

# 3.
# from functools import reduce
# numbers = [15, 80, 25, 100, 45]
# result = reduce(lambda x , y: x if x > y else y, numbers)
# print(result)


# 4.
# from functools import reduce
# numbers = [15, 80, 25, 100, 45]
# result = reduce(lambda x , y: x if x < y else y, numbers)
# print(result)

# 5.
