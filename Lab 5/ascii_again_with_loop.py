ascii_num = None
while ascii_num != 9 :
    char = input("Enter a character: ")
    ascii_num = ord(char)
    if ascii_num >= 48 and ascii_num <= 57 :
        print(char, "is a numeric number.")
        continue
    elif ascii_num >= 59 and ascii_num <= 90 :
        print(char, "is a capital letter and its  small-case letter is", chr(ascii_num+32))
        continue
    elif ascii_num >= 97 and ascii_num <= 122 :
        print(char, "is a small-case letter and its  capital letter is", chr(ascii_num-32))
        continue
    else :
        print("This is a special character")
        continue