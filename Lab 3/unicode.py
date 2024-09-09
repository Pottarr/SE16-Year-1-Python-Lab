char = input("Please enter a character: ")
ascii_dec = ord(char)
ascii_hex = str(format(ascii_dec, "04x"))
unicode_hex = "u" + ascii_hex

print('''The unicode of "''', end = "")
print(char, end = "")
print('''" is ''', end = "")
print(unicode_hex, end = "")
print('''.''', end = "")
