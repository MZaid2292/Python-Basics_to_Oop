# **kwargs allows a function to accept multiple keyword arguments (key-value pairs).


# def student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# student_info(
#     name = "Muhammad Zaid",
#     age = 23,
#     city= "Hyderabad",
#     field = "Software Engineering"
# )



# ---------------------------------Practice Questions--------------------------------------------
# def user_profile(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# user_profile(
#     username="zaid123",
#     email="zaid@gmail.com",
#     age=23
# )       

# def count_details(**kwargs):
#     count = len(kwargs)

#     print(f"Total Details: {count}")


# count_details(
#     name="Muhammad Zaid",
#     age=23,
#     city="Hyderabad",
#     skill="Python"
# )



# def student_info(**kwargs):
#     for key , value in kwargs.items():
#         print(f"{key} : {value}")
#     key = input("Enter Key:\n")
#     if key in kwargs:
#         print("Key Available")
#     else:
#         print("Key is not available")

# student_info(
#     name= "Muhammad Zaid",
#     age= 23,
#     email = "nizamanizaid99@gmail.com",
#     department= "Software Engineering"
# )

# def student_marks(**kwargs):
#     total = 0

#     for subject, marks in kwargs.items():
#         total += marks

#     return total

# result = student_marks(
#     english=80,
#     maths=90,
#     science=85,
#     computer=95
# )    

# print(f"Total Marks: {result}")