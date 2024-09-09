import random

print("0 scissor")
print("1 rock")
print("2 paper")
choice = int(input("Input 0-2: "))
bot_choice = random.randint(0,2)

if bot_choice == 0 :
    if choice == 0 :
        print("Bot chose scissor, and you also chose scissor: Draw")
    elif choice == 1 :
        print("Bot chose scissor, but you chose rock: Won")
    elif choice == 2 :
        print("Bot chose scissor, but you chose paper: Lose")
    else :
        print("WTF")
elif bot_choice ==1 :
    if choice == 0 :
        print("Bot chose rock, but you chose scissor: Lose")
    elif choice == 1 :
        print("Bot chose rock, and you also chose rock: Draw")
    elif choice == 2 :
        print("Bot chose rock, but you chose paper: Won")
    else :
        print("WTF")
elif bot_choice ==2 :
    if choice == 0 :
        print("Bot chose paper, but you chose scissor: Won")
    elif choice == 1 :
        print("Bot chose paper, but you chose rock: Lose")
    elif choice == 2 :
        print("Bot chose paper, and you also chose paper: Draw")
    else :
        print("WTF")
else :
    print("WTF")