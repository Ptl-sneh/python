# Write a python program to create and read the city.txt file in one go and print the contents on the output screen.

f1 = open("E:/Python/python/T3/Text Files/city.txt","w")
cities = ["Ahmedabad\n","Banglore\n","Mumbai\n","Surat"]
f1.writelines(cities)
f1.close()
f2 = open("E:/Python/python/T3/Text Files/city.txt")
city = f2.read()
print(city)