"""
Give an input string and get the number of uppercase and lowercase letters and ... at the end.
"""

# method one
def method_one(string_input):
    "Total number of characters : "
    n_chars = len(string_input)

    "Number of lowercase letters : "
    n_lower_chars =  sum(map(str.islower, string_input))

    "Number of capital letters : "
    n_upper_chars = sum(map(str.isupper, string_input))


    all_add = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    n_number = 0
    for i in string_input:
        if i in all_add:
            n_number += 1

    n_char = n_chars - n_upper_chars - n_lower_chars - n_number

    "PRINT : "
    print("count string input : " + str(n_chars))
    print("count number input : " + str(n_number))
    print("count string lower : " + str(n_lower_chars))
    print("count string upper : " + str(n_upper_chars))
    print("count string char : " + str(n_char))

# method two
import re

def method_two(string_input):
    n_number = len(re.findall('[0-9]', string_input))
    n_upper = len(re.findall('[A-Z]', string_input))
    n_lower = len(re.findall('[a-z]', string_input))
    n_char = len(string_input) - n_number - n_upper - n_lower

    "PRINT : "
    print("count string lower : " + str(n_lower))
    print("count string upper : " + str(n_upper))
    print("count string char : " + str(n_char))
    print("count number input : " + str(n_number))



string = input("Please enter your field : ")

method_one(string)
print("------------------------")
method_two(string)