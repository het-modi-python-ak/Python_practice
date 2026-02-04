def greet(fun):    # the outer first function greet is use for keyword. w he oriinal function is abc which we want to play before and after the hi funciton
    def abc():
        print("This is before the function")
        fun()
        print("this is after the function")
    return abc()
    

@greet
def hi():
    print("hello")

hi()