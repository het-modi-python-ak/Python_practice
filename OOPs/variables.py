


x = 5
def fun1():
    global x  # we use global whne we want to access global var. here outpu twil;l be 7 7 . without global output will be 7 5
    x=7
    print(x)

fun1()
print(x)

y = 0
def f1():
    y  = 1
    def f2():
        y=2
        def f3():
            global y
            y=3
            print(y)
        f3()    
        print(y)
        
    f2()
    print(y)

f1()
print(y)  # output will be 3 2 1 3