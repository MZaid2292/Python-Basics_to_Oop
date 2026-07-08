# JSON (JavaScript Object Notation) is a lightweight format used to store and exchange data.

# | Python Dictionary                         | JSON                                            |
# | ----------------------------------------- | ----------------------------------------------- |
# | Python object                             | File/Data format                                |
# | Single & Double quotes dono ho sakte hain | Keys aur strings **double quotes** me hote hain |
# | Python ke andar use hota hai              | Data exchange ke liye use hota hai              |





# import json

# file = open("student.json", "r")
# data =  json.load(file)
# # print(data)

# # Access Individually
# print(data["name"])
# print(data["age"])
# print(data["department"])

# file.close()



# ------------------------------------Practice Questions------------------------------------------
# Question 1:
# import json

# file = open("company.json", "r")
# data = json.load(file)
# print(data["company"])
# print(data["location"])
# print(data["employees"])
# file.close()


# Question 2
# import json

# file = open("book.json", "r")
# data = json.load(file)
# print("Title: ",data["title"])
# print("Author: ",data["author"])
# print("Price: ",data["price"])
# file.close()


# Question 3
# import json

# file = open("laptop.json", "r")
# data = json.load(file)
# print("Brand: ",data["brand"])
# print("Model: ",data["model"])
# print("Ram: ",data["ram"])
# print("Price: ",data["price"])
# file.close()



# Question 4
# import json
 
# file = open("university.json", "r")
# data = json.load(file)
# print("University: ",data["university"])
# print("Department: ",data["department"])
# print("Semester: ",data["semester"])
# file.close() 


# Question 5
# import json

# file = open("car.json", "r")
# data = json.load(file)
# print(data["brand"])
# print(data["year"])
# file.close()


# json.loads:json.loads() converts a JSON string into a Python Dictionary.
# import json

# text = '{"name":"Zaid","age":23}'

# data = json.loads(text)

# Difference between json.load and json.loads
# json.load()                                  |json.loads()
# Used to read data from a JSON file.	       | Used to read data from a JSON string.
# Takes a file object as input.                |Takes a string as input.
# Converts a JSON file into a Python dictionary.|Converts a JSON string into a Python dictionary.

# import json

# employee = '{"name":"Muhammad Zaid","department":"QA","salary":50000}'

# data = json.loads(employee)

# print("Name: ",data["name"])
# print("Department: ",data["department"])
# print("Salary: ",data["salary"])



# -------------------------------JSON DUMP------------------------------------------------
# json.dump() is used to write python data into a json file.
# import json

# info = {
#     "name":"Muhammad Zaid",
#     "age":23,
#     "department":"Software Engineering"
# }

# file = open("info.json", "w")
# json.dump(info, file, indent = 4) #indent=4 → JSON ko readable format me save karega.
# file.close()

# withour indent Output
# {"name":"Muhammad Zaid","age":23, "department":"Software Engineering"}



# json.dumps(): json.dumps() converts a Python object into a JSON string.
# import json

# zaid_info = {
#     "name":"Muhammad Zaid",
#     "age":23,
#     "profession":"Software Engineer"
# }

# data = json.dumps(zaid_info, indent = 4)
# print(data) 


# Difference between json.dump() and json.dumps() 
# json.dump() alag se file create karta hai wahan json ka code hota hai
# json.dumps() file create nh karta sirf string banegi



# Difference between json.dump() and json.dumps()
# json.dump()                               |json.dumps()
# -------------------------------------------------------------------------------------------
# Used to write data into a JSON file.	    |Used to convert Python data into a JSON string.
# Takes a file object as input.	            |Does not use a file.
# Saves Python dictionary into a JSON file.	|Returns a JSON string.



