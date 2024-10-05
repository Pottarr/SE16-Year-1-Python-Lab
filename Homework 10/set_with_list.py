
def my_union(list1, list2) :
    found_num = []
    for i in list1 :
        if i not in found_num :
            found_num.append(i)
        else :
            continue
    for j in list2 :
        if j not in found_num :
            found_num.append(j)
        else :
            continue
    found_num.sort()
    return found_num

def my_intersection(list1, list2) :
    merge_list = list1 + list2
    found_num = []
    for i in merge_list :
        if i not in found_num :
            found_num.append(i)
        else :
            continue
    intersection_list = []
    for n in found_num :
        if merge_list.count(n) == 2 :
            intersection_list.append(n)
    intersection_list.sort()
    return intersection_list

def my_difference(list1, list2) :
    extend_list = list1 + my_intersection(list1, list2)
    difference_list = []  
    for m in extend_list :
        if extend_list.count(m) < 2 :
            difference_list.append(m)
    difference_list.sort()
    return difference_list

list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

list3 = my_union(list1, list2)
list4 = my_intersection(list1, list2)
list5 = my_difference(list1, list2)

print("Llist1:", list1)
print("Llist2:", list2)
print("Llist3 (list1 union list2):", list3)
print("Llist4 (list1 intersection list2):", list4)
print("Llist5 (list1 intersection list2):", list5)