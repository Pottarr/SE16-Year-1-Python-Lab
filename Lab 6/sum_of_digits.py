def sum_of_digits(num) :
    num_str = str(num)
    sum = 0
    for i in num_str :
        sum += int(i)
    return sum
        
        
print(sum_of_digits(123))
print(sum_of_digits(1203))
print(sum_of_digits(11))
print(sum_of_digits(2332))
    