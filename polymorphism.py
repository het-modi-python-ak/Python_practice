class c1:
    def add(self,a=1,b=3,*args):
        sum = a+b
        for i in args:
            sum+=i
        
        return sum

a = c1()
print(a.add())
print(a.add(4.3,4534,56,545,545,3))
