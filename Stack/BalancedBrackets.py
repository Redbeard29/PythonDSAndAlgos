#Solve the balanced brackets algorithm using a stack:

def balanced_brackets(string):
    stack = []
    opening_brackets = '([{'
    closing_brackets = '}])'
    bracket_pairs = {'(' : ')', '[' : ']', '{' : '}'}

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            else:
                top_elem = stack.pop()
                if not bracket_pairs[top_elem] == char:
                    return False
 
    return len(stack) == 0

