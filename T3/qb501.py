f1 = open("E:/Python/python/T3/Text Files/friends.txt")
f2 = open("E:/Python/python/T3/Text Files/reverse.txt","w")
f3 = open("E:/Python/python/T3/Text Files/upper.txt","w")
f4 = open("E:/Python/python/T3/Text Files/vowels_count.txt","w")
f5 = open("E:/Python/python/T3/Text Files/secondline.txt","w")
vowel = ["a","e","i","o","u"]
l = f1.readlines()
vowel_count = 0
for i in l:
    f2.write(i[::-1]+ "\n")
    f3.write(i[::-1].upper() + "\n")
    if l[1] == i:
        f5.write(i)
    for j in range(len(i)):
        if i[j].lower() in vowel:
            vowel_count += 1
f4.write(f"Vowel count is: {vowel_count}")