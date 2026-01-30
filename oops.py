class animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound = sound
    
    def prt(self):
        print(self.name , " : " ,self.sound)


a = animal("dog","barks")
a.prt()


