def get_the_difference(list1, list2) :
    # print("find list1_found")
    list1_found = []
    for i in range(len(list1)) :
        if list1[i] not in list1_found :
            list1_found.append(list1[i])
            # print(list1_found)
        else :
            continue
    # print("find list2_found")
    list2_found = []
    for i in range(len(list2)) :
        if list2[i] not in list2_found :
            list2_found.append(list2[i])
            # print(list2_found)
        else :
            continue
        
    # print("find num in common")
    num_in_common = []
    for i in range(len(list1_found)) :
        if i in list2_found :
            num_in_common.append(i)
            # print(num_in_common)
        else :
            continue
    
    # print("remove num in common")
    for i in range(len(num_in_common)) :
        list1_found.remove(num_in_common[i])
        # print(list1_found)
        list2_found.remove(num_in_common[i])
        # print(list2_found)
    
    for i in range(len(list2_found)) :
        list1_found.append(list2_found[i])
        
    print(list1_found)
    
get_the_difference([3, 1, 1, 1, 2, 7], [4, 1, 1, 2, 2, 5])