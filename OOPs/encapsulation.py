class bank:
    def __init__(self,name,age,amount):
        self.name=name
        self._age=age
        self.__amount=amount

    def getamout(self):
        print("Amount in the bank is ",self.__amount)
    def setamount(self,amt):
        self.__amount+=amt

    
a1 = bank("raj",23,30000)
a1.setamount(4000)
print(a1.getamout())