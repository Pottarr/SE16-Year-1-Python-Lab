def LCS(s1, s2) :   
    if len(s1) < len(s2) :
        short_str = s1
        long_str = s2
    elif len(s1) >= len(s2) :
        short_str = s2
        long_str = s1
        

    longest_sub_str = ""
    temp = ""
    for i in range(0, len(short_str)) :
        for j in range(0, len(long_str)) :
            if short_str[i] == long_str[j] :
                for k in range(min(len(short_str) - i, len(long_str) - j)) :
                    if short_str[i + k] == long_str[j + k] :
                        temp += short_str[i + k]
                    else : 
                        break
                if len(longest_sub_str) < len(temp) :
                    longest_sub_str = temp
                temp = ""
    return longest_sub_str

print(LCS("ingenious", "intelligent"))
print(LCS("philosophically", "zoophilous"))
print(LCS("Love", "War"))
print(LCS("condition", "fictional"))
print(LCS("smart", "meter"))
print(LCS("back-end", "front-end"))
