firstname = input("Enter your first name:")
lastname = input("Enter your last name:")
gender = input("Enter your gender (m/f):")

if gender == "m" or gender == "f" :
    formated_gender = gender
    formated_lastname = lastname[0]
    formated_firstname = firstname[0:6]
    username = formated_gender + formated_lastname + formated_firstname
    username = username.upper()
    print(username)
else :
    print("Please enter the gender correctly. m or f only")