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
    
def generate_password():
    length=12
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_char=string.punctuation
    pass_string=[]
    pass_string.append(random.choice(lowercase))
    pass_string.append(random.choice(uppercase))
    pass_string.append(random.choice(digits))
    pass_string.append(random.choice(special_char))

    password = lowercase+uppercase+digits+special_char
    for x in range(length-4):
        pass_string.append(random.choice(password))

    random.shuffle(pass_string)
    result="".join(pass_string)
    validated_pass=validate_rules(result)
    if validated_pass:
        return validated_pass
    else:
        return generate_password()


print("Here is your password: ",generate_password())