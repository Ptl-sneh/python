# Write a python program to read line by line from a given files file1 & file2 and write into file3.

f1 = open("E:/Python/python/T3/Text Files/friends.txt")
f2 = open("E:/Python/python/T3/Text Files/city.txt")
f3 = open("E:/Python/python/T3/Text Files/file3.txt","w+")

l1 = f1.readlines()
l2 = f2.readlines()

length = len(l1) if len(l1) > len(l2) else len(l2)
for i in range(length):
    if l1[i] == "":
        f3.write(l2[i])
    elif l2[i] == "":
        f3.write(l1[i])
    else:
        if l1[i][0:len(l1[i])-1] != "\n" or l2[i][0:len(l2[i])-1] != "\n":
            f3.write(l1[i][0:len(l1[i])])
            f3.write("\n")
            f3.write(l2[i][0:len(l2[i])])
            f3.write("\n")
f3.close()