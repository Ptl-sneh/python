# Write a function count_lines() to count and display the total number of lines from the file. Consider the following lines for the file – friends.txt

def count_lines():
    f1 = open("E:/Python/python/T3/Text Files/friends.txt")
    l = f1.readlines()
    print("Total number of lines in the file: ", len(l))

count_lines()