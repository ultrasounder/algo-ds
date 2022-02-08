
from Node import Node

from LinkedList import LinkedList
def length(lst):
    # start from the first element
    curr = lst.get_head()
    length = 0
    
    #Traverse the list and count number of nodes
    while curr:
        length += 1
        curr = curr.current.next_element
    return length

lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.insert_at_head(1)
lst.insert_at_head(0)
print(length(lst))