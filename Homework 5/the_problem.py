n = input("Enter a number to find square root: ")

print()

if n.isnumeric() :
    n = float(n)
    
    guess = n/2

    real_ans = format(n ** 0.5, ".3f")

    is_equal_to_sqrt = True

    print("The real square root of", n, "is", real_ans)
    print()

    for i in range(7) :
        temp = n/guess
        guess = (guess + temp)/2
        
        if i >= 4 :
            guess_format = format(guess, ".3f")
            print("Guess for the", i + 1, "th time is", guess_format)
            if guess_format == real_ans :
                print("Guess is equal to the real square root")
                print()
            else :
                print("Guess is not equal to the real square root")
                is_equal_to_sqrt = False
                print()
    if is_equal_to_sqrt :
        print("From the the guesses above, we can conclude that the square root of", n, "is", guess_format)
    else :
        print("From the the guesses above, we can conclude that the square root of", n, "is not", guess_format)
        print("But if you are not sastisfied, you can do more time than that by yourself with the same algorhythm")

else :
    print("Error: Invalid input")
    print("Please enter a number")