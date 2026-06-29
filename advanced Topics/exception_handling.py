
# # Exception: Exception is an error that comes during execution of program.

# # Exception Q handle karty hain? Like we have a code
 
# num = int(input("Enter Number: ")) #hamne input abc diya
# print(num) 
# print("Program End")

# # Output: value error aega because ham integer input le rahe hain or de string rahe hain
# # Program wahi stop hojaega lekin if ham exception handling use karen to 

# try:
#     num = int(input("Enter Number: "))
#     print(num)
# except:
#     print("Invalid Number")

# print("program end")


# # Try: is code ko try karo. Agr error ae to program stop nh karo 
# # Except: Agr error ae to ye code chala do 

# # Example:
# # 1.
# try:
#     number = int(input("Enter Number: "))
#     print(number)

# except:
#     print("Please Enter a valid number")

# # 2.
# try:
#     a = 10
#     b = 0
#     print(a / b)
# except:
#     print("Can not divide by zero")    

# # 3.
# try:
#     numbers = [10,20,30]
#     print(numbers[5])
# except:
#     print("Index doesn't exist.")    


# # 4. Multiple Exceptions
# try:
#     num1 = int(input("Enter first number"))
#     num2 = int(input("Enter second number"))
#     print(num1 / num2)

# except ValueError:
#     print("Only numbers are allowed")

# except ZeroDivisionError:
#     print("Cannot divide by zero")


# try:
#     numbers = int(input("Enter Number: "))

# except Exception as e:
#     print(e) 


# # except: → Catches the error, but does not give you the actual error message.
# # except Exception as e: → Catches the error and stores the actual error message in e.


# # -------------------------------Practice Questions----------------------------------------------
# 1.
# try:
#     age = int(input("Enter your age: "))
#     print("Your age is: ",age)

# except:
#     print("Please enter a valid age")

# # 2.
# try:
#     num1 = int(input("Enter First Number: "))
#     num2 = int(input("Enter Second Number: "))
#     print(num1 / num2)
# except ValueError:
#     print("Enter a valid numbers")

# except ZeroDivisionError:
#     print("Cannot divide zero")

# # 3.
# try:
#     numbers = [10,20,30,40]
#     index = int(input("Enter Index"))
#     print(numbers[index])

# except:
#     print("Index doesn't exist. ")


# # 4.
# try:
#     student = {
#         "name":"Muhammad Zaid",
#         "age":23
#     }
#     key = input("Enter Key")
#     print(student[key])

# except KeyError:
#     print("Enter a valid key")


# try:
#     num1 = int(input("Enter First Number"))
#     num2 = int(input("Enter Second Number"))

#     result = num1 / num2

# except ValueError:
#     print("Only numbers are allowed")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result: ",result)

# try:
#     pin = int(input("Enter PIN: "))

# except ValueError:
#     print("Invalid PIN")

# else:
#     print("Login Successful")



# # The else block executes only if no exception occurs in the try block.
    


# try:
#     subjects = ["Python", "Java", "Flutter", "React"]

#     index = int(input("Enter index:"))
#     subject = subjects[index]

# except ValueError:
#     print("Please enter a valid number.")

# except IndexError:
#     print("Subject not found.")

# else:
#     print("Selected Subject:", subject)
    


# # Finally Keyword: The finally block always executes, whether an exception occurs or not.


# try:
#     student = {
#         "name":"Muhammad Zaid",
#         "age":23,
#         "profession":"Software Engineer"
#     }

#     key = input("Enter Key: ")
#     print(student[key])

# except KeyError:
#     print("Please enter a valid key")

# finally:
#     print("Program Finished")


# # 1.
# try:
#     id = int(input("Enter Student ID: "))
    

# except ValueError:
#     print("Invalid Student ID.")

# else:
#     print("Login Successful")
#     print("Student ID: ",id)

# finally:
#     print("Session Closed")


# # 2.
# try:
#     products = {
#         "laptop":120000,
#         "mouse":2500,
#         "keyboard":5000
#     }

#     product_name = input("Enter a product name: ")
#     product = products[product_name]

# except KeyError:
#     print("Product not available")

# else:
#     print("Good choice")
#     print("Your selected product is: ",product)

# finally:
#     print("Thank you for visiting our store")


# # 3.
# try:
#     books = ["Python","Flutter","Java","React"]

#     index = int(input("Enter an index"))
#     book = books[index]

# except ValueError:
#     print("Only numbers are allowed")

# except IndexError:
#     print("Index doesn't exist. ")

# else:
#     print("Selected Book is: ",book)

# finally:
#     print("Library session ended")



# # 4.
# try:
#     balance = 100000

#     withdrawl_amount = int(input("Enter Withdrawl Amount: "))

# except ValueError:
#     print("Invalid Amount")

# else:
#     if withdrawl_amount <= balance:
#         print("Withdrawl Amount: ",withdrawl_amount)
#         remaining_balance = balance - withdrawl_amount
#         print("Remaining Balance: ",remaining_balance)

#     else:
#         print("Insufficient Balance")

# finally:
#     print("Thank you for banking with us.")
    
# # 5.
# try:
#     num1 = int(input("Enter First Number: "))
#     num2 = int(input("Enter second Number: "))
#     operator = input("Enter an operator (+, -, *, /): ")
#     print("Selected Operator: ",operator)

#     if operator == "+":
#         result = num1 + num2

#     elif operator == "-":
#         result = num1 - num2
        
#     elif operator == "*":
#         result = num1 * num2
        
#     elif operator == "/":
#         result = num1 / num2
       

#     else:
#         print("Invalid Operator")

# except ValueError:
#     print("Only numbers are allowed")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result: ",result)
    

# finally:
#     print("Calculator Closed")



# Raise: raise is used to manually generate an exception when a condition is not acceptable.

# try:
#     age = int(input("Enter your age: "))

#     if age < 0:
#         raise ValueError("Age cannot be negeative")
#     print("Your age is: ",age)

# except Exception as e:
#     print(e)


# try:
#     amount = int(input("Enter Amount: "))

#     if amount <= 0:
#         raise ValueError("Amount must be greater than 0")
    
#     print("Amount is: ",amount)

# except Exception as e:
#     print(e)

try:
    marks = int(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")
    
    print("Marks: ",marks)

except Exception as e:
    print(e)