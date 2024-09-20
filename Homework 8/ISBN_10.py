nine_dig = input("Enter the first 9 digits of an ISBN-10 as a string: ")

if nine_dig.isnumeric() == True :
    if len(nine_dig) == 9 :
        
        dig_list = []
        for i in nine_dig :
            dig_list.append(int(i))
        
        sum = 0
        
        for i in range(len(dig_list)) :
            sum += (dig_list[i] * (i + 1))
        
        tenth_dig = sum % 11
        
        if tenth_dig == 10 :
            tenth_dig = "X"
        else :
            tenth_dig = str(tenth_dig)
        
        result = nine_dig + tenth_dig
        print("Your ISBN-10 number is ", result)
        
    else :
        print("Please enter 9 digit of number only.")
else :
    print("Please enter 9 digit of number only.")