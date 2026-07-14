# Decorator
# A Decorator is a function that adds extra functionality to another function
# without changing its original code.
# Kisi function ke andar koi changes kiye bina usme extra kaam add karna.

# def hello():
#     print("Hello")

# def decorator(func):

#     print("Before Function")

#     func()

#     print("After Function")

# decorator(hello)


# Use multiple fucntions
# def hello():
#     print("Hello")
    
# def name():
#     print("Muhammad Zaid")

# def surname():
#     print("Nizamani")

# def decorator(func):

#     print("Before Function")

#     func()

#     print("After Function")

# functions = [hello, name, surname]
# for i in functions:
#     decorator(i)



# def add(a , b):
#     print(f"Sum: {a + b}")
    
# def sub(a , b):
#     print(f"Subtract: {a - b}" )

# def mul(a , b):
#     print(f"Multiplication: {a * b}")

# def divide(a , b):
#     print(f"Divide: {a / b}")

# def decorator(func , a , b):

#     print("Before Function")

#     func(a , b)

#     print("After Function")

# # functions = [add, sub ,  mul , divide]
# # for i in functions:
# #     decorator(i, 100 , 5)

# #without using list and loop  

# decorator(add , 100 , 5)
# decorator(sub , 100 , 5)
# decorator(mul , 100 , 5)
# decorator(divide , 100 , 5)  



#------------------------------------ Practice Questions-------------------------------------
# def cube(num):
#     print(f"Cube of {num} is: {num ** 3}")

# def decorator(func, num):
#     print("Starting Calulation")

#     func(num)

#     print("Calculation Completed")

# decorator(cube , 3)


def marks(english, math, science):
    print(f"English: {english}\nMath: {math}\nScience: {science}")
    print(f"Total Marks: {english + math + science}")

def decorator(func , english, math, science):
    print("Marks Calculation Started")

    func(english, math, science)

    print("Marks Calculation Finished")


decorator(marks, 70, 80 , 90)


