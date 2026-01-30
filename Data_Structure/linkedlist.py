class Node:
    def __init__(self,data):
        self.data = data
        self.next=None


n1 = Node(4)
n2 = Node(8)
n3 = Node(12)

n1.next =  n2
n2.next=n3
n3.next=None

head = n1
current = head

while current != None :
    print(current.data,end=" ")
    
    current=current.next


#insert at start
print("\n")
new = Node(1)
new.next = n1
head = new
current = head
while current != None :
    print(current.data,end=" ")
    current=current.next
                            


#insert at any position
def insert(head,pos=3):
    new = Node(100)
    
    curr = head
    for i in range(1,pos-1):
     if curr is None:
        return head
     curr = curr.next

    if curr is None:
     return head
   
    new.next = curr.next
    curr.next = new
    
head = Node(3)
head.next = Node(34)
head.next.next = Node(54)
insert(head,4)
print("\n")

current = head
while current != None :
    print(current.data,end=" ")
    current=current.next
                            
#delete head from front
def deletehd(head):
   if head == None:
      return None
   tp = head
   head = head.next
   tp = None



#delete from any position 
def deletfun(head,pos):
   if pos == 1:
      tem = head
      head = head.next
      tem = None
   
   prev =None
   for i in range(1, pos):
        prev = temp
        temp = temp.next

   prev.next = temp.next
   return head


      