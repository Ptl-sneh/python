# Write a function display_oddLines() to display odd number lines from the text file. Consider the following lines for the file – friends.txt.

def display_oddLines():
    f1 = open("E:/Python/python/T3/Text Files/friends.txt")
    l = f1.readlines()
    for i in range(len(l)):
        if i % 2 == 0:
            print(l[i])

display_oddLines()