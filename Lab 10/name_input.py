def name_list() :
    stop = False
    count = 1
    names = []
    while stop == False :
        msg = "Enter name " + str(count) + ": "
        name_input = input(msg)
        count += 1
        if name_input == "" :
            stop = True
        else :
            names.append(name_input)
    return names

print(name_list())