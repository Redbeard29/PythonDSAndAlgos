"""
Convert an integer to its binary equivalent. The easiest way to do this is with the division
by 2 method, which can be implemented by taking a number, dividing it by 2, and saving the remaineder.
Then, take the answer the number that you got when you divided the starting number by 2 (minus its remainder)
and divide THAT by two, and again save the remainder. Keep following this pattern until you can't divide anymore, 
saving all of the remainders. Once you have all saved remainders, your binary equivalent can be found by putting
all of your remainders together from the MOST RECENT to LEAST RECENT. Ex:
242 / 2 = 121 R0
121 / 2 = 60 R1
60 / 2 = 30 R0
30 / 2 = 15 R0
15 / 2 = 7 R1 
7 / 2 = 3 R1
3 / 2 = 1 R1
1 / 2 = 0 R1

Now, to get your binary equivalent, read the remainders from top to bottom - 11110010
Note: Your solution should return the correct binary equivalent of dec_num as a string
in order to pass the tests.
"""

from Stack import Stack


def convert_int_to_bin(num):

    if num == 0:
        return 0

    my_stack = Stack()
    bin_string = ""
    current_num = num

    while current_num > 0:
        remainder = current_num % 2
        my_stack.push(remainder)
        current_num = current_num // 2
    
    while not my_stack.is_empty():
        bin_string += str(my_stack.pop())

    return bin_string

print(convert_int_to_bin(242))