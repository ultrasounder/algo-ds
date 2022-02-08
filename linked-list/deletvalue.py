from Node import Node
from LinkedList import LinkedList

def delete(lst, value):
    deleted = False
    if lst.is_empty():
        print("List is empty")
        return deleted
    current_node = lst.get_head()
    previous_node = None
    if current_node.data is value:
        lst.delete_at_head()
        deleted = True
        return deleted
    
    #traversing/searching for node to Delete
    while current_node is not None:
        # Node to delet is found
        if value is current_node.data:
            previous_node.next_element = current_node.next_element
            current_node.next_element = None
            deleted = True
            break
        previous_node = current_node
        current_node = current_node.next_element
        
    if deleted == False:
        print(str(value) + " is not in list!")
    else:
        print(str(value) + " deleted!")
        
    return deleted

lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
delete(lst, 4)
lst.print_list()