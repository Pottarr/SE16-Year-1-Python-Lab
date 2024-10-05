list1_str = input("Enter list1: ")
list2_str = input("Enter list2: ")

list1 = list1_str.split(" ")
list2 = list2_str.split(" ")

def merge(list1, list2) :
    lista = []
    for i in list1 :
        lista.append(int(i))
    listb = []
    for i in list2 :
        listb.append(int(i))
    
    result = []
    i = 0
    j = 0
    while i < len(lista) and j < len(listb) :
        if lista[i] < listb[j] :
            result.append(lista[i])
            i += 1
        else :
            result.append(listb[j])
            j += 1
    if i < len(lista) :
        for k in range(i, len(lista)) :
            result.append(lista[k])
    if j < len(listb) :
        for k in range(j, len(listb)) :
            result.append(listb[k])
    print("The merged list is", result)


        
        
    
merge(list1, list2)