class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linked_List(Node):
    def __init__(self):
        super().__init__()
        self.first = None
        self.len = 0
    
    def insertLast(self,key):
        newNode = Node(key)
        
        if self.first == None:
            self.first = newNode
            
        else:
            temp = self.first
            
            while(temp.next != None):
                temp = temp.next
            
            temp.next = newNode
            
    def insertFirst(self,key):
        newNode = Node(key)
        
        if self.first == None:
            self.first = newNode
            
        else:
            newNode.next = self.first
            self.first = newNode
    
    def insert_after(self,key,pos):
        """
        Insert at a given position(pos)
        """
        newNode = Node(key)
        
        if self.first == None:
            self.first = newNode
            
        elif self.len == 1:
            if pos == 1:
                self.insertFirst(self,key)
            else:
                self.insertLast(self,key)
        elif pos == 1:
            self.insertFirst(self,key)
        else:
            temp = self.first
            length = 1
            while length != pos - 1:
                temp = temp.next
                length += 1
            
            newNode.next = temp.next
            temp.next = newNode       
    
    
    def length(self):
        if self.first == None:
            return "Empty Linked List"
        else:
            temp = self.first
            while(temp != None):
                self.len += 1
                temp = temp.next
                
        return self.len        
    
    def deleteFirst(self):
        if self.first == None:
            return "No node to delete"
        elif self.len == 1:
            self.first = None
        else:
            self.first = self.first.next
            
    def delete_after(self,pos):
        """
        delete the node at a given specific position
        This function takes arguments as pos and delete the element present in that position and return the deleted value
        """
        if self.first == None:
            return "Nothing to delete"
        elif self.first.next == None:
            self.first = None
            return "There was only one element in the list and that is deleted"
        
        else:
            temp = self.first
            curr = self.first
            length = 1
            while length != pos:
                temp = temp.next
                length += 1
                
            temp_data = temp.data
            
            while curr.next != temp:
                curr = curr.next
            
            curr.next = temp.next
            del temp
            
    def deleteLast(self):
        if self.first == None:
            return "No node to delete"
        
        elif self.len == 1:
            self.first = None
            return "Their was only one node to delete"
        
        else:
            temp = self.first
            while temp.next != None:
                temp = temp.next
                
            temp_data = temp.data
            curr = self.first
            
            while curr.next != temp:
                curr = curr.next
            
            del temp
            curr.next = None
            
            return temp_data
            
    def display(self):
        if self.first != None:
            temp = self.first
            
            while temp != None:
                print(temp.data)
                temp = temp.next
        else:
            return "Nothing to return"
        
    def display_first_data(self):
        return self.first.data