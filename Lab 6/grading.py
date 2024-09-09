
def grading(score) :
    if  score <= 100 and score >= 80 :
        return "A"
    elif score < 80 and score >= 70 :
        return "B"
    elif score < 70 and score >= 60 :
        return "C"
    elif score < 60 and score >= 50 :
        return "D"
    elif score < 50 and score >= 0 :
        return "F"
    else :
        return "Your score is invalid"
        
    
print(grading(0))
print(grading(54))
print(grading(66))
print(grading(79))
print(grading(80))
print(grading(101))
print(grading(-69))