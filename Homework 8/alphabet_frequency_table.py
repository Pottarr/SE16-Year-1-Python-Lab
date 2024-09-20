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