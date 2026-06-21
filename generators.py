# Generators: A generator is a special function that uses yield instead of return and produces values  
# one at a time rather than creating all values at once, making it memory efficient.


def numbers():
    yield 10
    yield 20
    yield 30

for num in numbers():
    print(num)


# Print Even Numbers 
def even_numbers():

    for i in range(2, 11, 2):
        yield i

for num in even_numbers():
    print(num) 


# Print Odd Numbers
def odd_numbers():

    for i in range(1, 11, 2):
        yield i

for num in odd_numbers():
    print(num)



        