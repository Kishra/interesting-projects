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

def finder(start_value, input_list):
    if input_list:
        i = input_list[0]
        index = keys_list.index(i) 
        row = index / 5 #Find the row of the string
        column = index % 5 #Find the column of the string
        dst_value = [row, column]

	#### Our start_value is at "a". Hence we started with [0,0] (Row=0 and Column=0).
        while start_value != dst_value:
            if dst_value[0] - start_value[0] > 0:
                print("down " * (dst_value[0]-start_value[0]))
                start_value[0] = dst_value[0]
                if dst_value[1] - start_value[1] > 0:
                    print("right "*(dst_value[1] - start_value[1]))
                    print("Enter")
                    start_value[1]=dst_value[1]
                elif dst_value[1] - start_value[1] < 0:
                    print("left "*((dst_value[1] - start_value[1])*-1))
                    print("Enter ")
                    start_value[1]=dst_value[1]
                else:
                    print("Enter ")
                    start_value[1] = dst_value[1]
            elif dst_value[0] - start_value[0] < 0:
                print("up "*((start_value[0]-dst_value[0])*1))
                start_value[0] = dst_value[0]
                if dst_value[1] - start_value[1] > 0:
                    print("right "*(dst_value[1] - start_value[1]))
                    print("Enter ")
                    start_value[1] = dst_value[1]
                elif dst_value[1] - start_value[1] < 0:
                    print("left "*((dst_value[1] - start_value[1])*-1))
                    print("Enter ")
                    start_value[1] = dst_value[1]
                else:
                    print("Enter ")
                    start_value[1]=dst_value[1]
            else:
                if dst_value[1] - start_value[1] > 0:
                    print("right "*(dst_value[1] - start_value[1]))
                    print("Enter ")
                    start_value[1] = dst_value[1]
                elif dst_value[1] - start_value[1] < 0:
                    print("left "*((dst_value[1] - start_value[1])*-1))
                    print("Enter")
                    start_value[1] = dst_value[1]
                else:
                    print("Enter ")
                    start_value[1] = dst_value[1]
        finder(start_value, input_list[1:])

finder([0,0], "netflix")
