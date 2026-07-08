
# CSV Handling: CSV (Comma Separated Values) is a file format used to store data in rows and columns.

# Example:

# Reading
# import csv

# file = open("students.csv", "r")
# reader = csv.reader(file)

# for row in reader:
#     print(row)

# file.close()


# 2. Writing into a CSV File
# import csv

# file = open("info.csv", "w", newline= "")

# writer = csv.writer(file)

# writer.writerow(["Name", "Age", "Department"])
# writer.writerow(["Muhammad Zaid", 23, "Software Engineering"])

# file.close()



# Writing Multiple Rows
# import csv

# file = open("students_info.csv", "w", newline= "")

# writer = csv.writer(file)

# data = [
#     ["Name" , "Age", "Department"],
#     ["Muhammad Zaid", 23, "Software Engineering"],
#     ["Umrah Zadi", 25, "Software Engineering"],
#     ["Athar Hussain", 28, "Civil Engineering"]
# ]

# writer.writerows(data)

# file.close()



# Appending Data
# import csv 
# file = open("students_info.csv", "a", newline= "")

# writer = csv.writer(file)

# writer.writerow(["Umrah Zaid", 26, "Computer Science"])

# file.close()



# Reading row by row
# import csv
# file = open("students_info.csv", "r")

# reader = csv.reader(file)

# for row in reader:
#     print("Name: ",row[0])
#     print("Age: ",row[1])
#     print("Department: ",row[2])

# file.close()    



# Pratice Questions
# # 1.
# import csv
# file = open("movies.csv", "r")

# reader = csv.reader(file)

# for row in reader:
#     print(row)

# file.close()


# 2. write row
# import csv
# file = open("employees.csv", "w", newline= "")

# writer = csv.writer(file)

# data = [
#     ["Name", "Department"],
#     ["Muhammad Zaid", "Software Engineering"],
#     ["Ali", "QA Engineer"],
#     ["Ahmed", "Devops"]
# ]

# writer.writerows(data)

# Different way
# writer.writerow(["Muhammad Zaid", "Software Engineering"])
# writer.writerow(["Ali", "QA Engineer"])
# writer.writerow(["Ahmed", "Devops"])

# file.close()



#3. Append
# import csv
# file = open("employees.csv", "a", newline= "")

# writer = csv.writer(file)


# writer.writerow(["Usman", "Flutter Developer"])

# file.close()



# 4.Write multiple rows
 
# import csv

# file = open("hardware_assets.csv", "w", newline= "")

# writer = csv.writer(file)

# data = [
#     ["Product", "Price"],
#     ["Laptop", 1200000],
#     ["Mouse", 2500],
#     ["Keyboard", 5000]
# ]

# writer.writerows(data)

# file.close()



# 5. Row by Row
import csv
# file = open("students.csv", "r")

# reader = csv.reader(file)

# for row in reader:
#     print("Name: ",row[0])
#     print("Age: ", row[1])
#     print("Department: ",row[2])

# file.close()    

file = open("zaid.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow(["Muhammad Zaid", "Nizamani", 23])
file.close()
