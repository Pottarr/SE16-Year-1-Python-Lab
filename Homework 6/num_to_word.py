str_num = input("Enter an interger from 0 to 999: ")

def convert_num_to_word_single_digit(str_digit) :
    digit = int(str_digit)
    if digit == 1 :
        return "one"
    elif digit == 2 :
        return "two"
    elif digit == 3 :
        return "three"
    elif digit == 4 :
        return "four"
    elif digit == 5 :
        return "five"
    elif digit == 6 :
        return "six"
    elif digit == 7 :
        return "seven"
    elif digit == 8 :
        return "eight"
    elif digit == 9 :
        return "nine"
    else :
        return ""
    
def convert_num_to_word_tens_and_ones(str_digits) :
    tens = int(str_digits[1])
    ones = int(str_digits[2])

    if tens == 1 :
        if ones == 0 :
            return "ten"
        elif ones == 1 :
            return "eleven"
        elif ones == 2 :
            return "twelve"
        elif ones == 3 :
            return "thirteen"
        elif ones == 4 :
            return "fourteen"
        elif ones == 5 :
            return "fifteen"
        else :
            return convert_num_to_word_single_digit(ones) + "teen"
    elif tens == 2 :
        if ones == 0 :
            return "twenty"
        else :
            return "twenty-" + convert_num_to_word_single_digit(ones)
    elif tens == 3 :
        return "thirty-" + convert_num_to_word_single_digit(ones)
    elif tens == 4 :
        return "forty-" + convert_num_to_word_single_digit(ones)
    elif tens == 5 :
        return "fifty-" + convert_num_to_word_single_digit(ones)
    else :
        return convert_num_to_word_single_digit(tens) + "ty-" + convert_num_to_word_single_digit(ones)
    
def read_num(num) :
    if  len(num) == 3 :
        hundreds = convert_num_to_word_single_digit(num[0])
        tens_and_ones = convert_num_to_word_tens_and_ones(num)
        print(hundreds, "hundred and", tens_and_ones)
    elif len(num) == 2 :
        print(2)
    elif len(num) == 1 :
        print(1)
    else :
        print("Error")
    
    
    
    
if str_num.isnumeric() == True :
    for i in str_num :
        if i == "." :
            print("PLease enter interger!")
        else :
            if len(str_num) > 1 and len(str_num) < 4 :
                is_valid_to_read = False
                for i in str_num :
                    if int(i) != 0 :
                        is_valid_to_read = True
                        break
                    else :
                        print("Please enter the interger without 0 in the front.")
                        break
                if is_valid_to_read == True :
                    read_num(str_num)
            elif len(str_num) == 1 :
                read_num(str_num)
            else :
                print("I don't know")
        break
else :
    print("Please enter interger!")