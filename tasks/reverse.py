"""
Two methods are used to reverse the input string
First enter your number and then choose how you want to return the string.
"""


import emoji

input_number = input("Please enter your number : ")

method  = input("How do you want to return your number? \n 1) list \n 2) method python \n add : ")

if method == 1:
    print(revers_one(input_number))
elif method == 2:
    print(revers_two(input_number))
else:
    print("Please choose the appropriate number !!!" + "  " + emoji.emojize(":zipper-mouth_face:"))


# method one
def revers_one(add):
    string = str(add)
    return string[::-1]

# method two
def reverse_two(string):
    return "".join(reversed(string))
