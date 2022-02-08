from Node import Node
from LinkedList import LinkedList
#recursive solution
# def search(node, value):
#     if(not node):
#         return False
#     if(node.data is value):
#         return True
#     return search(node.next_element, value)

#Iterative solution
def search(lst, value):
    
    #start from the first element
    current_node = lst.get_head()
    
    #traverse the list till you reach end
    while current_node:
        if current_node.data == value:
            return True
        current_node = current_node.next_element
    return False

lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(10)
lst.insert_at_head(40)
lst.insert_at_head(5)
lst.length()
print(search(lst.get_head(), 4))
    
