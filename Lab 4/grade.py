score = int(input("Enter a score: "))

if score <= 100 and score >= 80 :
    print("Your Grade: A")
elif score < 80 and score >= 70 :
    print("Your Grade: B")
elif score < 70 and score >= 60 :
    print("Your Grade: C")
elif score < 60 and score >= 50 :
    print("Your Grade: D")
elif score < 50 and score >= 0 : 
    print("Your Grade: F")
else :
    print("This isn't your score")