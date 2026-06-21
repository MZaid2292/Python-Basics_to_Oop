
# 1. Counting positive numbers
# Proble: Give a list of numbers, count how many of them are positive.
# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]

# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# positive_num_count = 0

# for num in numbers:
#     if num > 0:
#         positive_num_count += 1
# print("Final count of positive numbers:", positive_num_count)    


# 2. Sum of even numbers
# n = 100
# sum = 0

# for num in range(1, n+1):
#     if num % 2 == 0:
#         sum += num
#         print(num)
# print("sum of even numbers:", sum)        


# 3. Print a multiplication table for a given number upto 10 but skip the fifth iteration.
# n = 10

# for i in range(1, n+1):
#     if i == 5:
#         continue
#     print(n, "*", i, "=", n*i)


# 4. Print Right Triangle Star pattern
# rows = 5

# for i in range(1, rows+1):
#     for j in range(1, i+1):
#         print("*",end="")
#     print()    

# 5. Print Reverse Triangle Star pattern
# rows = 5

# for i in range(rows,0,-1):
#     for j in range(1, i+1):
#       print("*",end=" ")
#     print()    


# # 6. Reverse a String 
# input_string = "idaz"
# reversed_string = ""

# for char in input_string:
#     reversed_string = char + reversed_string
# print("Reversed String:", reversed_string)    



# rows = 5

# # Upper part of Diamond Shape
# for row in range(rows):
#     for space in range(rows - row - 1):
#         print(" ",end="")
#     for star in range(2 * row + 1):
#         print("*",end="")
#     print()

# # Lower part of Diamond Shape
# for row in range(rows - 2, -1, -1):
#     for space in range(rows - row - 1):
#         print(" ",end="")
#     for star in range(2 * row + 1):
#         print("*",end="")
#     print()    



# Loop and List tupples and set 

# numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers_tuple = (1,2,3,4,5,6,7,8,9,10)
# numbers_set = {1,2,3,4,5,6,7,8,9,10}

# for num in numbers:
#     print("List:",num)

# for num in numbers_tuple:
#     print("Tuple:",num)

# for num in numbers_set:
#     print(num)



# Loops with dictionary
student = {
    "name":"Muhammad Zaid",
    "name1":"Umrah Zaid",
    "city":"Hyderabad",
    "profession":"Software Engineer",
}

for key, value in student.items():
    print(key, ":", value)


num  = 5
fact = 1

for i in range(1, num + 1):
    fact *= i
    print("Factorial of,", num, "is", fact  )