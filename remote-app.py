"""
The application is responsible for identifying the keys entered while searching for an input string.

You have your a keyboard as below
[
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', 'n', 'o'],
    ['p', 'q', 'r', 's', 't'],
    ['u', 'v', 'w', 'x', 'y'],
    ['z']
]

remote = ["down", "up", "left", "right", "enter"

Let's say, you are searching for a string("netflix")

Do you know what keys you will enter in your remote to search for "netflix"? If not, No problem. I got you covered!!! :).

Use the below script to find out.
"""

import string
keys = string.ascii_lowercase	#### Create as string of lowercase letter
keys_list = [i for i in keys]	#### Convert the string to list
output = []

def keys_sp_finder(keys_list, input_string, keys_dict={}):
    initial_position = [0,0]
    for i in keys:
        index = keys_list.index(i)
        row = index / 5 #Find the row of the string
        column = index % 5 #Find the column of the string
        let_position = [row, column]
        keys_dict[i] = {'position': let_position}

    while len(input_string) > 0:
        let = input_string[0]
        let_position = keys_dict[let]["position"]
        cursor = [let_position[0] - initial_position[0], let_position[1] - initial_position[1]]
        down = ["down"]*cursor[0]
        right = ["right"]*cursor[1]
        up = ["up"]*-cursor[0]
        left = ["left"]*-cursor[1]
        enter = ["enter"]
        while initial_position[0] != let_position[0]:
            if cursor[0] > 0:
                output.extend(down)
                initial_position[0] = let_position[0]
            elif cursor[0] < 0:
                output.extend(up)
                initial_position[0] = let_position[0]
            while initial_position[1] != let_position[1]:
                if cursor[1] > 0:
                    output.extend(right)
                    initial_position[1] = let_position[1]
                elif cursor[1] < 0:
                    output.extend(left)
                    initial_position[1] = let_position[1]
        else:
            output.extend(enter)
        input_string = input_string[1:]

keys_sp_finder(keys_list, "whatis")
print(output)
