# Write a “pager” program. Your solution should prompt for a filename, and display the text file 25 lines at a time, pausing each time to ask the user to enter the word “continue”, in order to show the next 25 lines or enter the word “stop” to close the file.

f1 = open("E:/Python/python/T3/Text Files/hello.txt","w")

for i in range(1000):
    if i < 999:
        f1.write("Hello \n")
    else:
        f1.write("Hello")

f1.close()
f2 = open("E:/Python/python/T3/Text Files/hello.txt")
num = int(input("Enter number"))
for i,j in enumerate(f2,1):
    print(str(i) + ":" + j)
    if i % num == 0:
        ans = input("Enter continue to continue or enter anything to exit:")
        if ans.lower() != "continue":
            break