input_num = input("Enter your positive interger: ")

def binary_to_decimal(dec_num) :
    i = 0
    while 2 ** i <= dec_num :
        i += 1
    bin_string = []
    for j in range(i-1, -1, -1) :
        bin_digit = dec_num // 2 ** j
        dec_num -= bin_digit * 2 ** j
        bin_string.append(str(bin_digit))
    bin_num = ""
    for k in bin_string :
        bin_num = bin_num + k
    return bin_num
    
def decimal_to_binary(bin_num) :
    bin_digit = []
    for i in bin_num :  
        bin_digit.append(int(i))
    bin_len = len(bin_digit)
    dec_string = []
    for j in range(bin_len) :
        dec_digit = bin_digit[j] * 2 ** (bin_len - j - 1)
        dec_string.append(dec_digit)
    dec_num = 0
    for k in dec_string :
        dec_num += k
    return dec_num
    
try :
    if int(input_num) > 0 :
        print("We can convert", input_num, "from decimal to ", end="")
        bin_num = binary_to_decimal(int(input_num))
        print(bin_num, end="")
        print(" in binary.")
        
        print("We can also convert", bin_num, "from binary to ", end="")
        dec_num = decimal_to_binary(str(bin_num))
        print(dec_num, end="")
        print(" in decimal.")
    elif int(input_num) == 0 :
        print("It's 0.")
    else :
        print(input_num, " is a negative number.") 
except :
    print("Please insert positive interger only.")