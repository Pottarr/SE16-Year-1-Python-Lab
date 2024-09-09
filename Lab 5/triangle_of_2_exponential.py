n = int(input("Enter rows: "))
if n % 2 == 1 :
    for i in range(0, ((n + 1) // 2) - 1) :
        for j in range(i, -1, -1) :
            print(2**j, end=" ")
        print()
    for k in range(((n + 1) // 2) -1, -1, -1) :
        for l in range(k, -1, -1) :
            print(2**l, end=" ")
        print()
else :
    for i in range(0, ((n + 1) // 2)):
        for j in range(i, -1, -1) :
            print(2**j, end=" ")
        print()
    for k in range(((n + 1) // 2) - 1, -1, -1) :
        for l in range(k, -1, -1) :
            print(2**l, end=" ")
        print()