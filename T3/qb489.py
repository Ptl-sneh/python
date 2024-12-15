# Write a function cust_data() to ask user to enter their names and age to store data in customer.txt file.

def cust_data(name , age):
    f1 = open("E:\python\PYTHON\T3\Text Files\qb489.txt","a")
    f1.write("name: " + name +" age: " +age + "\n")

name = input("Enter your name: ")
age = input("Enter your age: ")
cust_data(name,age)