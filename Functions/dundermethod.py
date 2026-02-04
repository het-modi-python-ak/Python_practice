class String:
    
    def __init__(self, string):
        self.string = string 
        
    def __repr__(self):
        return 'Object: {}'.format(self.string)
        
    def __len__(self):
        print("I will not give length")
        return 5
        

    def __add__(self, other):
        print("helo")
        return self.string + other


    
string1 = String('Hello')
len(string1)
print(string1 +' Geeks','dfu')