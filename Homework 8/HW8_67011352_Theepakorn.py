# Homework 8.1 Binary and Decimal Conversion

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

# Homework 8.2 Alphabet Frequency Table

input_str = input("Enter some text: ")

def find_aphabet_frequency(input_str) :
    chars = []
    for i in input_str :
        if i not in chars :
            chars.append(i)
        else :
            continue
    frequency_list = []
    for j in chars :
        frequency = input_str.count(j)
        frequency_list.append(frequency)
    return (chars, frequency_list)

result = find_aphabet_frequency(input_str)   
chars = result[0]
frequency_list = result[1]

print("-- Character Frequency Table --")
print("char percentage (character count / string length)")
for i in range(len(chars)) :
    print(chars[i], end="")
    print(format(frequency_list[i] / len(input_str) * 100, "8.2f"), end="")
    print("%")

# Homework 8.3 Alphabet Frequency Graph

import turtle as t

input_str = input("Enter some text: ")

def find_aphabet_frequency(input_str) :
    chars = []
    for i in input_str :
        if i not in chars :
            chars.append(i)
        else :
            continue
    frequency_list = []
    for j in chars :
        frequency = input_str.count(j)
        frequency_list.append(frequency)
    return (chars, frequency_list)

def draw_graph(result) :
    chars = result[0]
    frequency_list = result[1]
    block = 20
    initial_x = -1 * block * len(chars)
    initial_y = -1 * block * len(frequency_list)
    t1 = t.Turtle()
    t2 = t.Turtle()
    t3 = t.Turtle()
    t4 = t.Turtle()
    t1.penup()
    t2.penup()
    t3.penup()
    t4.penup()
    t1.goto(initial_x, initial_y)
    t2.goto(initial_x, initial_y)
    t3.goto(initial_x, initial_y)
    t4.goto(initial_x, initial_y)
    t1.pendown()
    t2.pendown()
    t3.pendown()
    t1.left(90)
    t1.forward(20 * max(frequency_list))
    t2.forward(20 * (len(chars) + 1) * 3)
    for i in range(len(frequency_list)) :
        t3.forward(2 * block)
        t3.left(90)
        t3.forward(frequency_list[i] * block)
        t3.right(90)
        t3.forward(block)
        t3.right(90)
        t3.forward(frequency_list[i] * block)
        t3.left(90)
    t3.hideturtle()
    t4.right(90)
    t4.forward(block)
    t4.left(90)
    for i in range(len(chars)) :
        t4.forward(2.5 * block)
        t4.write(chars[i])   
        t4.forward(0.5 * block)
    t4.hideturtle()
    

draw_graph(find_aphabet_frequency(input_str))

t.exitonclick()

# Homework 8.4 ISBN-10

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