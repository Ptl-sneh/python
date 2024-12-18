# Write a Python program to copy the contents of a file to another file

f1 = open("E:/Python/python/T3/Text Files/friends.txt")
f2 = open("E:/Python/python/T3/Text Files/friends_copy.txt","w")

for i in f1:
    f2.write(i)

f2.close()
f1.close()