import string
import getpass

def check_pwd():
    password = getpass.getpass("Enter Password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0
    password_length = len(password)

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase: 
            upper_count +=1
        elif char in string.digits: 
            num_count += 1
        elif char == ' ':
            wspace_count +=1
        else: 
            special_count +=1

    if password_length < 6:
        remarks += "Password should have at least 6 characters.\n"
    elif password_length > 12:
        remarks += "Your Password has 12 characters or more thats great!\n"
    else:
        strength += 1

    if lower_count >= 1:
        strength +=1
    if upper_count >= 1:
        strength +=1
    if num_count >= 1:
        strength +=1
    if wspace_count>=1:
        strength +=1
    if special_count>=1:
        strength +=1

    if strength == 1:
        remarks += "This Password is Very Weak"
    elif strength == 2: 
        remarks += "This Password is Weak"
    elif strength == 3:
        remarks += "This Password is Good"
    elif strength == 4: 
        remarks += "This Password is Strong"
    elif strength == 5: 
        remarks += "This Password is Very Strong!"

    print('Your password has: ')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    print(f"Password is: {strength}")
    print(f"Hint: {remarks}")

def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
        choice=input('Do you want to change your password? (y/n): ')
    else:
        choice=input('Do you want to check your password? (y/n): ')

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid, Try Again')
    
if __name__ == '__main__':
    print('Welcome to Password Checker!')
    print('Your password will be checked on a scale of 1 to 5. 1 being the Weakest and 5 being the Strongest.')
    ask_pw = ask_pwd()
    while check_pwd:
        check_pwd()
        ask_pw = ask_pwd(True)