from collections import deque

def is_palindrom(characters):
    character_deque = deque(characters) #initializing a deque with the string
    
    while(len(character_deque) > 1):
        first = character_deque.popleft()
        last = character_deque.pop()
        if first != last:
            return False
        return True
print(is_palindrom('lsdkjfskf'))
print(is_palindrom('radar'))   
        