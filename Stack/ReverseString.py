#Reverse a string using a stack:

def reverse_string(string):
    stack = []
    rev_string = ""

    for char in string:
        stack.append(char)

    while len(stack) > 0:
        rev_string += stack.pop()

    return rev_string


#Reverse a string using a single for loop:

def reverse_string_one_loop(string):
    str_type = 'even' if len(string) % 2 == 0 else 'odd'
    center = round(len(string) / 2) - 1
    rev_string_list = [x for x in string]
    
    if str_type == 'even':
        left = center
        right = center + 1
    
    else:
        left = center - 1
        right = center + 1
    
    while left >= 0 and right <= len(string):
        temp = string[left]
        rev_string_list[left] = string[right]
        rev_string_list[right] = temp
        left -= 1
        right += 1

    return ''.join(rev_string_list)
