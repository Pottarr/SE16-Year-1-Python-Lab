def reverse(num):
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num = num // 10
    return reverse_num

result1 = reverse(3456)
result2 = reverse(1232)
result3 = reverse(37775)
result4 = reverse(2387)
result5 = reverse(19)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)