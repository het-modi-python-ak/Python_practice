from queue import Queue
q = Queue(maxsize=3)

q.put("hi")
q.put_nowait(34)
q.put(324)

print(type(q))
print(list(q.queue))



print(q.full())
x =q.get()
print(x)
print(q.full())



# using deque
from collections import deque
a = deque()
a.append(34)
a.append(34)
a.append(5)
a.append(65)
a.append(76)

print(a)
a.popleft()
print(a)


