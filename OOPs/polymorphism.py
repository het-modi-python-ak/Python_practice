
#compile time poly
class c1:
    def add(self,a=1,b=3,*args):
        sum = a+b
        for i in args:
            sum+=i
        
        return sum

a = c1()
print(a.add())
print(a.add(4.3,4534,56,545,545,3))


#runtime poly

class animal:
    def __init__(self):
        print("Hello")
    def sound(self):
        print("make some noise")

class dog(animal):
    def __init__(self):
        print("dogs hello")
        super().__init__()
    def sound(self):
        print("Barks")

class cat(animal):
    def __init__(self):  # if this cat construcotr is removed then it will print animals constructor automatically,but if it is there it will not print animal const
        print("Cats Hello")
        
    def sound(self):
        print("Meow")

ob1 = cat()
ob1.sound()