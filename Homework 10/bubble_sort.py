def bubble_sort(that_list):
    n = len(that_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if that_list[j] > that_list[j+1]:
                temp = that_list[j]
                that_list[j] = that_list[j+1]
                that_list[j+1] = temp


list1 = [3, 2, 9, 7, 8]
print("Before sort:", list1)
bubble_sort(list1)
print("After sort:", list1)

list2 = [3, 44, 33, 11, 8, 57, 87, 12]
print("Before sort:", list2)
bubble_sort(list2)
print("After sort:", list2)