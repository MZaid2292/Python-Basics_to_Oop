# List comprehension is a short way to create a new list using a single line of code.
# example
# Normal Example
# numbers = [1,2,3,4,5]
# result = []
# for num in numbers:
#     result.append(num * num)

# print(result)


# Same with list comparison
# numbers = [1,2,3,4,5]
# result = [num * num for num in numbers]
# print(result)

# Double every number
# numbers = [1, 2, 3, 4, 5]
# result = [num + num for num in numbers]
# print(result)

# Square
# numbers = [2, 3, 4, 5, 6]
# result = [num * num for num in numbers]
# print(result)

# Only even numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# names = ["zaid", "ali", "ahmed", "sara"]
# result = [name.upper() for name in names]
# print(result)


# numbers = [1, 2, 3, 4, 5, 6]
# result = [num * 2 for num in numbers if num % 2 == 0]
# print(result)