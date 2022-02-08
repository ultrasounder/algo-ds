from Node import Node

class LinkedList:
    def __init__(self):
        self.head_node = None
        
    def get_head(self):
        return self.head_node
    
    def is_empty(self):
        if(self.head_node is None): #check if the head is empty 
            return True
        else:
            return False
        
    def insert_at_head(self, dt):
        temp_node = None(dt)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node
    
    def insert_at_tail(self, value):
        new_node = Node(value)
        
        if self.get_head() is None:
            
            self.head_node = new_node
            return
        
        #if the list is not empty traverse the entire list
        temp = self.get_head()
        
        while temp.next_element is not None:
            temp = temp.next_element
        #set the nextElement of the previous node to new node
        temp.next_element = new_node
        return
    
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True
    


    
    