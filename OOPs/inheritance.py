#single inhertance
class parent:
    name = "mahesh"
    def __init__(self):
        print("this is constructor of parent")
    
    def fun1(self):
        print("this is function 1")

class child(parent):
   name="raj " + parent.name
   def __init__(self):
        print("this is constructor of child")
   def fun1(self):
       print("this is child")
       return super().fun1()   # we use super keyword when we want to inherate parent function


a =child()
print(" name is ", a.name)
a.fun1()

print("--------")

#  multiple inheritance

class par1:
    def fun3(self):
        print("this is function of parent 3")
    

class par2:
    def fun3(self):
        print("this is function of parent 4")

class child2(par2,par1):
    def fun3(self):
        return super().fun3() # here which function is first inherited thats method will be applied.
    
ob1 = child2()
ob1.fun3()

print(" - - - - -")

 
class par1:            # ** important . same function with same name and variable gives the output whihc depends on the latest function defined
    def fun3(self):
        print("this is function of parent 67")
    
ob1 =par1()
ob1.fun3()       #ouput : this is function of parent 67



print(" - - --- - - - ")

print("Multilevel Iheritance")

# Base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self,grandfathername)

# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self,fathername,grandfathername)
        
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)


s1 = Son('jethalal', 'champklal', 'jyantilal')
print(s1.grandfathername)
s1.print_name()


print("---------------")
print("Heirical inheritance")
class a:
    def __init__(self,name):
        self.name=name
        print("name is the ",name)

class b(a):
    def __init__(self,name):
        super().__init__(name)


class c(a):
    def __init__(self,name):
        super().__init__(name)

obj = c("kaju")