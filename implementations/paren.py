OPENING = '('

def is_balanced(parentheses):
    stack  = []
    for paren in parentheses:
        if paren == OPENING:
            stack.append(paren)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0

print(is_balanced('((()))'))