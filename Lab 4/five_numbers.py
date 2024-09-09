sum = 0
last_num = 0
for _ in range(5) :
    num = int(input("Enter an interger: "))
    if num >= 0 and last_num <= 0 :
        sum = num
        last_num = num
        print("Current sum:", sum)
    elif num <= 0 and last_num >= 0 :
        sum = num
        last_num = num
        print("Current sum:", sum)
    elif num >= 0 and last_num >= 0 :
        sum += num
        last_num = num
        print("Current sum:", sum)
    elif num <= 0 and last_num <= 0 :
        sum += num
        last_num = num
        print("Current sum:", sum)
    else :
        print("WTF")

