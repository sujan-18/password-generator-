#defining a function to check if the passowrd is dtong enough
def password_checker(password):
    #defining the crieteria for a strong password
    min_length=8
    has_uppercase=False
    has_lowercase=False
    has_digit=False
    has_special_char=False
    special_chars="!@#$%^&*()[{]}:;/?"

    #Check the length of th password
    if len(password)<min_length:
        print("password is too short!")
        return False
    
    #Check if the password contains an uppercase letter, lowercase letter, digit, and special character
    for char in password:
        if char.isupper():
            has_uppercase=True
        elif char.islower():
            has_lowercase=True
        elif char.isdigit():
            has_digit=True
        elif char in special_chars:
            has_special_char=True
    
#print an error message for each missing criteria
    if not has_uppercase:
        print("pasword must contain at least one uppercase letter!")
        return False
    if not has_lowercase:
        print("Pasword must contain at least one lowercase letter")
    if not has_digit:
        print("Password must contain at least one digit")

    if not has_special_char:
            print("Password must contain at least one special character!")
            return False
        
    #if all criiteria are met, print a success message
    print("Pasword is strong!")
    return True
    
    #promt the user to enter a password and check if it meets the crietria

password = input("Enter a password: ")
password_checker(password)
