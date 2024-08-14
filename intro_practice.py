import pandas as pd
import numpy as np

#number variable
num_var = 22

#string variable
string_var = "hello!"

#list
my_list = [1,2,4,5,6,7]

print("The assigned number is: ", num_var)
print ("The assigned string is: ", string_var)
print ("The list has the numbers: ", my_list)

#dictionary

my_dict = {
    'name': "Prabhakar",
    'age': 25,
    'hobbies': ["hiking", "music"],
    'school': {
        'name': "Stony Brook University",
        'program': "Masters in Applied Health Informatics"
    }
}

studentName = my_dict["name"]
program = my_dict["school"]["program"]
print("This student's name is ", studentName, "and he is enrolled in ", program )


def num_compare (num1, num2):
    if num1 > num2:
        result = f"{num1} is greater than {num2}"
    else:
        result = f"{num1} is smaller than {num2}"
    return result


check = num_compare(1,5)
print("The result is: ", check)
