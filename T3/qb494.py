# Write a python program that reads a text file and changes the file by capitalizing each character of file.

f1 = open("E:/Python/python/T3/Text Files/friends.txt")

for lines in f1:
    print(lines.title())