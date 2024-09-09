num = int(input("Enter a four-digit interger: "))
thousands = num//1000
thousands_str = str(thousands)
hundreds = (num-(thousands*1000))//100
hundreds_str = str(hundreds)
tens = (num-(thousands*1000)-(hundreds*100))//10
tens_str = str(tens)
ones = (num-(thousands*1000)-(hundreds*100)-(tens*10))
ones_str = str(ones)
rev_num = ones_str + tens_str + hundreds_str + thousands_str
print("The reversed form of", num, "is", rev_num)