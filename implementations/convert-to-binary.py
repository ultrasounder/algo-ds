DIGITS = '0123456789'

def convert_to_base(decimal_number, base):
    remainder_stack=[]
    
    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // 2
    new_digits = []
    while remainder_stack:
        new_digits.append(DIGITS[remainder_stack.pop()])
    return ''.join(new_digits)

print(convert_to_base(25, 2))
    
