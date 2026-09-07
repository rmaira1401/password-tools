import string
import random

def validate_rules(password):
    has_uppercase = any(c.isupper() for c in password )
    has_lowercase = any(c.islower() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_special = any (c in string.punctuation for c in password)

    if (not has_lowercase or not has_uppercase or not has_digits or not has_special):
        return False
    else:
        return password

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_char=string.punctuation

    req=input("Please select your requirements:\na. Lowercase letters\nb. Uppercase letters\nc. Digits\nd. Special Characters\ne. Combination of all\nEnter your options (a to d or e):")
    while (req!="e" and len(req)<2) or not any(letter in req for letter in "abcde"):
        req=input("Please select at least 2 valid options (e.g. 'ac'), or 'e' for all: ")

    pass_string = []
    pass_pool=""
    if "a" in req:
        pass_string.append(random.choice(lowercase))
        pass_pool+=lowercase
    if "b" in req:
        pass_string.append(random.choice(uppercase))
        pass_pool+=uppercase
    if "c" in req:
        pass_string.append(random.choice(digits))
        pass_pool+=digits
    if "d" in req:
        pass_string.append(random.choice(special_char))
        pass_pool+=special_char
    if "e" in req:
        pass_string.append(random.choice(lowercase))
        pass_string.append(random.choice(uppercase))
        pass_string.append(random.choice(digits))
        pass_string.append(random.choice(special_char))
        pass_pool=lowercase+uppercase+digits+special_char

    if length < len(pass_string):
        print(f"Length too short for {len(pass_string)} requirement(s). Using {len(pass_string)} instead.")
        length = len(pass_string)
    choice=length-len(pass_string)
    for x in range(choice):
        pass_string.append(random.choice(pass_pool))

    random.shuffle(pass_string)
    result="".join(pass_string)
    return result

def main():
    while True:
        x=int(input("Please select one option:\n1. Generate a random password\n2. Exit program\n"))
        if x == 1:
            length = int(input("What should be the password length? "))
            while length < 8:
                length = int(input("Please choose a length of at least 8: "))
            print("Here is your password:", generate_password(length))
            option=input("Would you like to generate another password? (yes/no) ")
            if option=="yes":
                continue
            else: break
        elif x==2:
                break
        else:
            print("Print select the right option\n1. Generate a random password\n2. Exit program")

# calling main function
main()