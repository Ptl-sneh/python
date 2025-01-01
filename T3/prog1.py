# 9 marker Question 1

class CustomError(Exception):
    pass
class SQ:
    def __init__(self,list1):
        self.list1 = list1
    def shift(self):
        try:
            if self.list1 == []:
                raise CustomError("There is no element! List is empty")
        except CustomError as e:
            print(e)
        else:
            removed = self.list1.pop(0)
            return (f"{removed} is removed")
    def unshift(self,n):
        self.list1.insert(0,n)
        return (f"{n} is added at front")
    def push(self,n):
        self.list1.append(n)
        return (f"{n} is added at end")
    def display(self):
        for i in self.list1:
            print(i,end = " ")


l1 = [1,2,3,4,5]
Stack_Que = SQ(l1)

Stack_Que.shift()
Stack_Que.display()
print()

Stack_Que.unshift(18)
Stack_Que.display()
print()

Stack_Que.push(45)
Stack_Que.display()
print()