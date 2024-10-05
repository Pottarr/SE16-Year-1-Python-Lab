num_list = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]

def remove_the_thirds(num_list) :
    n = 0
    count = len(num_list) // 3
    for i in range(len(num_list) - count + 2) :
        if i % 3 == 2 :
            num_list.pop(i - n)
            n += 1
        else :
            continue

remove_the_thirds(num_list)
print(num_list)