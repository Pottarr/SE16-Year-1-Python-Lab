import turtle as t

print("Hello, Welcome to Turtle World!")
command = ""
while command != "quit" :
    command = input("turtle|>")
    
    
    if command == "fd" :
        arg = input("Please input its argument:")
        if arg.isnumeric() :
            int_arg = int(arg)
            t.forward(int_arg)
        else :
            print("Wrong argument, please try again.")
            
            
    elif command == "back" :
        arg = input("Please input its argument:")
        if arg.isnumeric() :
            int_arg = int(arg)
            t.backward(int_arg)
        else :
            print("Wrong argument, please try again.")
            
            
    elif command == "lt" :
        arg = input("Please input its argument:")
        if arg.isnumeric() :
            int_arg = int(arg)
            t.left(int_arg)
        else :
            print("Wrong argument, please try again.")
            
            
    elif command == "rt" :
        arg = input("Please input its argument:")
        if arg.isnumeric() :
            int_arg = int(arg)
            t.right(int_arg)
        else :
            print("Wrong argument, please try again.")
            
            
    elif command == "pu" :
        t.penup()
            
            
    elif command == "pd" :
        t.pendown()
            
            
    elif command == "reset" :
        t.reset()
            
    else :
        print("Wrong command, please try again.")
        