from LinkedList import LinkedList
from Node import Node

def reverse(lst):
    #To reverse a linked list we need to keep track of three things
    previous = None #Maintain a track of the previous Node
    current = lst.get_head() # The current node set to head
    next = None # The next node in the list
    
    #reversal
    while current:
        next = current.next_element
        current.next_element = previous
        previous = current
        current = next
        
        #set the last element as the new head node
        lst.head_node = previous
    return lst

lst = LinkedList()
lst.insert_at_head(6)
lst.insert_at_head(4)
lst.insert_at_head(9)
lst.insert_at_head(10)
lst.print_list()

reverse(lst)
lst.print_list()

    

