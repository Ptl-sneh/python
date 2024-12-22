f1 = open("E:/Python/python/T3/Text Files/friends.txt")

l = f1.readlines()
str = "Lif"
for i in l:
    if i.find(str) != -1:
        print("String is exists")
        print("line number:",l.index(i)+1,"index number:",i.index(str))