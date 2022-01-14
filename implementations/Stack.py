class Stack:
    
    def __init__(self):
        self._items = [] # create an empty stack
        
    def is_empty(self): # check if list is empty
        return not bool(self._items)
    
    def push(self, item):  # append item to the list 
        self._items.append(item)
    
    def pop(self): # remove the last element from the list
        return self._items.pop()
        
    def peek(self): # look at the last element from the list without  removing it
        return self._items[-1]
    
    def size(self):  # size of list len()
        return len(self._items)
        