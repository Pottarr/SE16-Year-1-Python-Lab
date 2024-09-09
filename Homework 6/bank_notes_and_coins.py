str_input = input("Enter the amount of money: ")

def bank_notes_and_coins(num) :
    bank1000 = num // 1000
    num -= bank1000 * 1000
    bank500 = num // 500
    num -= bank500 * 500
    bank100 = num // 100
    num -= bank100 * 100
    bank50 = num // 50
    num -= bank50 * 50
    bank20 = num // 20
    num -= bank20 * 20
    coin10 = num // 10
    num -= coin10 * 10
    coin5 = num // 5
    num -= coin5 * 5
    coin2 = num // 2
    num -= coin2 * 2
    coin1 = num // 1
    print("1000-Baht notes:", bank1000)
    print("500-Baht notes:", bank500)
    print("100-Baht notes:", bank100)
    print("50-Baht notes:", bank50)
    print("20-Baht notes:", bank20)
    print("10-Baht coins:", coin10)
    print("5-Baht coins:", coin5)
    print("2-Baht coins:", coin2)
    print("1-Baht coins:", coin1)

if str_input.isnumeric() == True : 
    bank_notes_and_coins(int(str_input))
else :
    print("Error: Please enter interger.")