name = "Muhammad Zaid"
age  = 23
print("My name is " + name + " and I am " + str(age) + " years old.")


num1 = int(input("Enter first Number"))
num2 = int(input("Enter second Number"))

sum = num1 + num2

print("The Sum of", num1, "and", num2, "is", sum)



num = int(input("Enter a number:\n"))

if num % 2 == 0:
    print("The number is even")
else:
    print("the number is odd")    

if num > 18:
    print("you can drive")
else:
    print("You cannot drive")        



#List: order collection of items, mutable, allows duplicate values, allows indexing and slicing 

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.append(11)
numbers.insert(11,12)
numbers.pop(1)
numbers.remove(3)
print(numbers)


# Tuple: ordered collection of items, immutable, allows duplicate values, allows indexing and slicing
numbers = (1,2,3,4,5,6,7,8,9,10)
print(numbers)

# Set: unordered collection of unique items, mutable, does not allow duplicate values, does not allow indexing and slicing
numbers = {1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10}
print(numbers)


# Dictionary: unordered collection of key-value pairs, mutable, does not allow duplicate keys, allows indexing and slicing

student= {
    "name":"Muhammad Zaid",
    "age":23,
    "city":"Hyderabad",
    "profession":"Software Engineer"
}

student2 = {
    "name":"Umrah Zadi",
    "age":25,
    "city":"Khairpur",
    "profession":"Software Engineer",
}

print(student)
print(student2)