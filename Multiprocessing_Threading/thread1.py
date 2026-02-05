import threading
import time
def hello_world():
    print("Hello, world!")
    time.sleep(1)
    print("End of function")

def hello_world2():
    print("Hello, world 2!")
    time.sleep(1)
    print("End of function 2")


t1 = threading.Thread(target=hello_world)
t2 = threading.Thread(target=hello_world2)
t1.run()
t2.run()

print("this is the end")