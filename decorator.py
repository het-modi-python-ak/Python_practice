class emp:
    def __init__(self,name,age,lname):
        self.name= name
        self.age = age
        self.lname = name+lname

e1 = emp("harsh",25,"patel")
print(e1.lname)
e1.name="raj"
print("first name is ",e1.name)
print("full name ",e1.lname )