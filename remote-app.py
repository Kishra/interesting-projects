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
