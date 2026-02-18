import array as ar

pq =ar.array('i',[2,3,4,45,6,32,4])
print(*pq)


pq.remove(3)   # removes particular element from array

print(*pq)   
 
pq.pop(-1)     # removes element from particular position
print(*pq)

tp = pq     # point as the reference any changes made in pq will be same for tp 
 
print(tp)

pq.extend([23,5,6,4])

pq.insert(3,534)
print(pq)
print(tp)