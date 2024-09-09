width = int(input("Enter width of the biggest pyramid: "))

if width > 1 :
    print("*")
for n in range(width, 0, -1):

    for i in range(2, n):
        for j in range(i):
            print("*", end="")
        print()
    for k in range(n + 1, 1, -1) :
        for l in range(k, 1, -1) :
            print("*", end="")
        print()