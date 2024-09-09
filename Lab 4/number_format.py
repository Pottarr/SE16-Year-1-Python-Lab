num = eval(input("Enter a real number: "))

if type(num) == float :
    print("f = float")
    print("e = scientific notation")
    float_num_format = input("Enter format for this interger number:")
    if float_num_format == "f" :
        print(num)
    elif float_num_format == "e" :
        float_num = format(num, "e")
        print(float_num)
    else :
        print("Plz read the instruction")
elif type(num) == int :
    print("b = binary")
    print("o = octate")
    print("d = decimal")
    print("h = hexadecimal")
    int_num_format = input("Enter format for this interger number:")
    if int_num_format == "b" :
        int_num = format(int(num), "b")
        print(int_num)
    elif int_num_format == "o" :
        int_num = format(int(num), "o")
        print(int_num)
    elif int_num_format == "d" :
        print(int(num))
    elif int_num_format == "h" :
        int_num = format(int(num), "x")
        print(int_num)
    else :
        print("Plz read the instruction")
else :
    print("Number only")
        
    