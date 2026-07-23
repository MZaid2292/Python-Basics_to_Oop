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
student = {
    "name":"Muhamamd Zaid",
    "age":23,
    "city":"Hyderabad"
}

student.clear()
print(student)