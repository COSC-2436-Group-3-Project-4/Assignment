# Doubly Linked List Queue
''' In the Queue
        Adjust the tail when adding item
        Adjust the head when removing item
'''
#n1 = bldg.head #lowest floor
#n10 = bldg.tail #highest floor
from node import DNode

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    # This method adds item to the queue
    def add(self,item):
        if self.head == None: #If the queue is empty
            self.head = item
            self.tail = item
        else:
            self.tail.next = item
            # establish the link from this item to the current tail item
            item.previous = self.tail
            # change the tail to point to this item
            self.tail = item

    def append(self, data):
        if self.head is None:
            new_node = DNode(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = DNode(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    # This method removes the item to the queue
    def remove(self,item):
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
        
##    def delete(self,item):
##        item = self.getItem(DNode(item))
##        nodep = item.previous
##        noden = item.next
##        nodep.next = noden
##        noden.previous = nodep
##        return item
    
    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None 
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None 
                    nxt.previous = None
                    cur = None
                    self.head = nxt
                    return 

            elif cur.data == key:
                # Case 3:
                if cur.next:
                    nxt = cur.next 
                    previous = cur.previous
                    previous.next = nxt
                    nxt.previous = previous
                    cur.next = None 
                    cur.previous = None
                    cur = None
                    return

                # Case 4:
                else:
                    previous = cur.previous 
                    previous.next = None 
                    cur.previous = None 
                    cur = None 
                    return 
            cur = cur.next

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None 
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None 
                    nxt.previous = None
                    cur = None
                    self.head = nxt
                    return 

            elif cur == node:
                # Case 3:
                if cur.next:
                    nxt = cur.next 
                    previous = cur.previous
                    previous.next = nxt
                    nxt.previous = previous
                    cur.next = None 
                    cur.previous = None
                    cur = None
                    return

                # Case 4:
                else:
                    previous = cur.previous 
                    previous.next = None 
                    cur.previous = None 
                    cur = None 
                    return 
            cur = cur.next
            
    def remove_duplicates(self):
        cur = self.head 
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt

                
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

class Building():
    def __init__(self,floors):
        self.__floors = floors
    def getFloors(self):
        return self.__floors



class Elevator():
    def __init__(self):
        self.currentfloor=0
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


queue = Queue()
#bldg = Building()


floors=int(input("How many floors does this bulding have?"))
#Sets floor 1 as lobby, floor will be range
total_floors=Building(floors)
new_node = DNode(int(1))
queue.sortedInsert(new_node)#This will be the lobby
flag = 'y'
while flag == 'y':
     

    floorrequest=int(input("What floor do you want to go to?"))
    #Conditional Statement to remove redundancies
    #   if floorrequest == data
    #Conditonal Statement for request to not be higher than number than floors
    #   if floorrequest >> floor... return try again.
    new_node = DNode(int(floorrequest))
    queue.append(int(floorrequest))
    queue.sortedInsert((new_node))
    #queue.remove_duplicates()
    flag = input("Do you want to add a floor request :")

print ("Create Linked List")
queue.printList()
queue.remove_duplicates()
print ("Create Linked List After Removing Duplicates")
queue.printList()
print("Sort Request and add top floor")
queue.sortedInsert(int(floors))
queue.printList()
marshall=queue.getCount()
print("Number of Nodes", marshall)
