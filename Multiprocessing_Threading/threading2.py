import threading
import time

start = time.perf_counter()

def fun1():
    print("Before fu1")
    time.sleep(1)
    print("After fu1")

def fun2():
    print("Before fu2")
    time.sleep(1)
    print("After fu2")

# t1 = threading.Thread(target=fun1)
# t2 = threading.Thread(target=fun2)
# t1.start()

# t2.start()

# t1.join()
# t2.join()


for  _ in range(10):
    t = threading.Thread(target=fun1)
    t.start()
    t.join()




 
        
finish = time.perf_counter()
print("finished in " , (round(finish-start)))

print("helo this is last")




