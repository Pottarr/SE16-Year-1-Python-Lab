def print_table(big_list) :
    element_of_table_count = len(big_list[0])
    longest_in_col = [0 for i in range(element_of_table_count)]
    
    for row in range(len(big_list)) :
        str_list = [str(i) for i in big_list[row]]
        for col in range(element_of_table_count) :
            if len(str_list[col]) > longest_in_col[col] :
                longest_in_col[col] = len(str_list[col])
            else :
                continue
            
    for row in range(len(big_list)) :
        str_list = [str(i) for i in big_list[row]]
        for col in range(element_of_table_count) :
            format_specifier = "<" + str(longest_in_col[col])
            format_str = format(str_list[col], format_specifier)
            print(format_str, end=" ")
        print()
            
                
    
    
print_table([["x", "y"],[0, 1],[100, 50],[10, 1000]])
print()
print_table([["ID", "Name", "Surname"], ["001", "Guido", "van Rossum"], ["002", "Donald", "Knuth"], ["003", "Gordon", "Moore"]])

