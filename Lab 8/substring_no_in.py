short_str = input("Plese enter a short text:")
long_str = input("Plese enter a long text:")

def look_for_sub_str(short_str, long_str) :
    found_sub_str = False
    if len(short_str) > len(long_str) :
        return "The short text is longer than the long text."
    else :
        that_part = len(long_str) - (len(long_str) - len(short_str))
        for i in range(0, that_part) :
            if short_str == long_str[i:that_part] :
                found_sub_str = True
            else :
                continue
    return found_sub_str
        
if type(look_for_sub_str(short_str,long_str)) == str :
    print(look_for_sub_str(short_str,long_str))
elif look_for_sub_str(short_str,long_str) == True :
    print("Found", short_str, "in", long_str)
elif look_for_sub_str(short_str,long_str) == False :
    print("Couldn't find", short_str, "in", long_str)
    