#from PreProj import Building
#building=Building()

from node import DNode

class Building:
	number_of_floors = 0                                                                                                                # sets number_of_floors variable to 0
    customer_list = []                                                                                                                  # creates an empty array for customer_list
    elevator = 0                                                                                                                        # sets elevator variable to 0
    def __init__(self):
        self.head = None
        self.tail = None
    # This method adds floors to the queue
    def floors(self,item):
        if self.head == None: #If the bldg is empty
            self.head = item
            self.tail = item
        else:
            self.tail.next = item
            # establish the link from this item to the current tail item
            item.previous = self.tail
            # change the tail to point to this item
            self.tail = item
    # This method removes the item to the queue
    def remove(self):
        item = self.head # temporarily save the head to item
        print('Removing ...',item.data)
        # adjust the head to point to the next item in Queue
        self.head = item.next
        #self.head.previous = None
        return item
    # This method checks if the queue is empty
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def insert(self, item, position):        
        nodeN = self.getItem(DNode(position))
        nodeP = nodeN.previous
        item.next = nodeN
        nodeP.next = item
        nodeN.previous = item
        item.previous = nodeP


    def getCount(self): 
        temp = self.head # Initialise temp 
        count = 0 # Initialise count 
  
        # Loop while end of linked list is not reached 
        while (temp): 
            count += 1
            temp = temp.next
        return count

    def sortedInsert(self, new_node): 
          
        # Special case for the empty linked list  
        if self.head is None: 
            new_node.next = self.head 
            self.head = new_node 
  
        # Special case for head at end 
        elif int(self.head.data) >= int(new_node.data): 
            new_node.next = self.head 
            self.head = new_node 
  
        else : 
  
            # Locate the node before the point of insertion 
            current = self.head 
            while(current.next is not None and
                 int(current.next.data) < int(new_node.data)): 
                current = current.next
              
            new_node.next = current.next
            current.next = new_node 
        
    def delete(self,item):
        item = self.getItem(DNode(item))
        nodep = item.previous
        noden = item.next
        nodep.next = noden
        noden.previous = nodep
        return item

    def getItem(self, item):
        node = self.head
        while node.next != None:
            if node.data == item.data:
                return node 
            node = node.next
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = DNode(new_data) 
        new_node.next = self.head 
        self.head = new_node
        
    # Utility function to print it the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data) 
            temp = temp.next

class Elevator():
    def __init__(self):
        self.elevatorstatus= bldg.head.data
    def set_elevatorStatus(self,s):
        self.elevatorstatus=s
    def get_elevatorStatus(self):
        return self.elevatorstatus

class Request():
    def __init__(self):
#        super.__init__(self)
        self.direction= 0
        self.requestedfloor=0
        self.currentfloor=0
    def set_currentFloor(self,c):
        self.currentfloor=c
    def get_currentFloor(self):
        return self.currentfloor
    def set_Direction(self,d):
        self.direction=d
    def get_Direction(self):
        #0=down , 1=up
        if self.direction == 0:
            return "down"
        if self.direction == 1:
            return "up"
    def set_RequestedFloor(self,f):
        self.requestedfloor =f
    def get_RequestedFloor(self):
        return self.requestedfloor



bldg = Building()

bldg.floors(DNode(1))
bldg.floors(DNode(2))
bldg.floors(DNode(3))
bldg.floors(DNode(4))
bldg.floors(DNode(5))
bldg.floors(DNode(6))
bldg.floors(DNode(7))
bldg.floors(DNode(8))
bldg.floors(DNode(9))
bldg.floors(DNode(10))


n1 = bldg.head #lowest floor
n2 = n1.next #next item
n3 = n2.next #next item
n4 = n3.next #next item
n5 = n4.next #next item
n6 = n5.next #next item
n7 = n6.next #next item
n8 = n7.next #next item
n9 = n8.next #next item
n10 = bldg.tail #highest floor

print(bldg.tail.data)

print(n1.data)
print(n2.data)
print(n3.data)

el=Elevator()
#el.set_currentFloor(5)
print("Elevator Status",el.get_elevatorStatus())

req=Request()
req.set_currentFloor(bldg.tail.data)
req.set_Direction(0)
req.set_RequestedFloor(3)

print("Current Floor",req.get_currentFloor())
print("Requested Direction",req.get_Direction())
print("Requested Floor", req.get_RequestedFloor())


queue = Queue()

#Push n number of items in the stack

queue.add(DNode('1'))
queue.add(DNode('3'))
queue.add(DNode('5'))
queue.add(DNode('7'))
queue.add(DNode('8'))
queue.add(DNode('9'))



#marshalling through the queue
n1 = queue.head #head item
n2 = n1.next #next item
n3 = n2.next #next item
n4 = n3.next #next item
n5 = n4.next #next item
n6 = n5.next #next item


print("Traversing the queue")
print(n1.data)
print(n2.data)
print(n3.data)
print("Insert Sort")
queue.sortedInsert(DNode('9'))

print(n1.data)
print(n2.data)
print(n3.data)
print(n4.data)
print(n5.data)
print(n6.data)

print("Queue Count")
print(queue.getCount())


#insert Doug
queue.insert(DNode('4'),'5')
#Deleting Doug
queue.delete('4')

# marshalling backwards through double link
print("Traversing reverse the queue")
print(n3.data)
print(n3.previous.data)
print(n2.previous.data)
# removing 
n1 = queue.remove()
print(n1.data)
n2 = queue.remove()
print(n2.data)
n3 = queue.remove()
print(n3.data)
print("Sorted Insert")
# Driver program 
new_node = DNode(5) 
queue.sortedInsert(new_node) 
new_node = DNode(10) 
queue.sortedInsert(new_node) 
new_node = DNode(7) 
queue.sortedInsert(new_node) 
new_node = DNode(3) 
queue.sortedInsert(new_node) 
new_node = DNode(1) 
queue.sortedInsert(new_node) 
new_node = DNode(9) 
queue.sortedInsert(new_node) 
print ("Create Linked List")
queue.printList()             
        
        
