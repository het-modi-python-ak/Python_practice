class Emp:
    emptot = 0
    lucknu = 4
    def __init__(self,name,age,salary):
        self.name = name
        self.age= age
        self.salry = salary
    
    def prt(self):
        print("name of emp is ", self.name)
        # print("age of ", self.name ," is ",self.age)
    

class Developer(Emp):
    lucknu = 9
    pass

emp1 = Emp("mahesh",12,90000)
emp1.prt()
print(Emp.lucknu)

emp2 = Developer("Raju",12,90000)
emp2.prt()
print(emp2.lucknu) #here lucku is changed in the developer class.


# multileve inheritance:

