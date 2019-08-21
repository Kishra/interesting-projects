import string
x = string.ascii_lowercase
keys = [i for i in x]

def finder(initial, input_list):
    if input_list:
        i = input_list[0]
        index = keys.index(i)
        row = index / 5
        column = index % 5
        cursor = [row, column]
        while initial != cursor:
            if cursor[0] - initial[0] > 0:
                print("down "*(cursor[0]-initial[0]))
                initial[0] = cursor[0]
                if cursor[1] - initial[1] > 0:
                    print("right "*(cursor[1] - initial[1]))
                    print("Enter")
                    initial[1]=cursor[1]
                elif cursor[1] - initial[1] < 0:
                    print("left "*((cursor[1] - initial[1])*-1))
                    print("Enter ")
                    initial[1]=cursor[1]
                else:
                    print("Enter ")
                    initial[1] = cursor[1]
            elif cursor[0] - initial[0] < 0:
                print("up "*((initial[0]-cursor[0])*1))
                initial[0] = cursor[0]
                if cursor[1] - initial[1] > 0:
                    print("right "*(cursor[1] - initial[1]))
                    print("Enter ")
                    initial[1] = cursor[1]
                elif cursor[1] - initial[1] < 0:
                    print("left "*((cursor[1] - initial[1])*-1))
                    print("Enter ")
                    initial[1] = cursor[1]
                else:
                    print("Enter ")
                    initial[1]=cursor[1]
            else:
                if cursor[1] - initial[1] > 0:
                    print("right "*(cursor[1] - initial[1]))
                    print("Enter ")
                    initial[1] = cursor[1]
                elif cursor[1] - initial[1] < 0:
                    print("left "*((cursor[1] - initial[1])*-1))
                    print("Enter")
                    initial[1] = cursor[1]
                else:
                    print("Enter ")
                    initial[1] = cursor[1]
        finder(initial, input_list[1:])

finder([0,0], "qfeyp")


















'''
keys = [
["a", "b", "c", "d", "e"],
["f", "g", "h", "i", "j"],
["k", "l", "m", "n", "o"],
["p", "q", "r", "s", "t"],
["u", "v", "w", "x", "y"],
["z"]
]

input = "zam"
cursor = []
i = 0

def key_input(keys, input_list, rows=0, columns=0):
    for row, column in enumerate(keys):
        for i in input_list:
            if i in column:
                a, b = finder((rows, columns), (row, column.index(i)))
                while a != 0:
                    if a > 0:
                        print("u")
                        a -= 1
                    elif a < 0:
                        print("d")
                        a += 1






def finder(list1, list2):
    row = list1[0] - list2[0]
    column = list1[1] - list2[1]
    return [row, column]




print(key_input(keys, "fch"))
'''
