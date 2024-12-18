# Write a Python program to read a text file and do following: 1. Print no. of words 2. Print no. statements

f1 = open("E:/Python/python/T3/Text Files/friends.txt")
w_count = 0
l = f1.readlines()
sen_count = len(l)
for i in l:
    w_count += len(i.split()) 
print(f"Word count: {w_count} and sentence count: {sen_count}")