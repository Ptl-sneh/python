# Write a function cust_data() to ask user to enter their names and age to store data in customer.txt file.

f1 = open("E:\python\PYTHON\T3\Text Files\qb489.txt","a")
name = input("Enter your name: ")
age = input("Enter your age: ")
f1.writelines("name: " + name +" age: " +age + "\n")