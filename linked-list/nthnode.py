from LinkedList import LinkedList
from Node import Node

def find_nth(lst, n):
  end_node = lst.get_head()
  nthnode  = lst.get_head()
  count = 0
  
  while count < n:
    if end_node is None:
      return -1
    end_node = end_node.next_element
    count += 1
  while end_node is not None:
    end_node = end_node.next_element
    nthnode = nthnode.next_element
  return nthnode.data

lst = LinkedList()
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(8)
lst.insert_at_head(22)
lst.insert_at_head(15)

lst.print_list()

print(find_nth(lst, 19))
print(find_nth(lst, 5))

  
  
    