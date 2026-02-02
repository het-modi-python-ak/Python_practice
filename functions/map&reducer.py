list1 = [1,2,3,4,5]

# map
pq =list(map(lambda x:x*x , list1))
print(pq)

# filter 

lp = list(filter(lambda x : x>2,list1))
print(lp)


#reduce

# print(list(reduce(lambda x,y:x*y,list1 )))