import string


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_char=string.punctuation
while True:
    try:
        print("Please enter your password: ")
        password = input()

        has_uppercase = any(c.isupper() for c in password )
        has_lowercase = any(c.islower() for c in password)
        has_digits = any(c.isdigit() for c in password)
        has_special = any (c in string.punctuation for c in password)

        if len(password)<8:
            print("Invalid Password! It should be atleast 8 characters long.")
        elif not has_lowercase:
            print("Invalid Password! There should be atleast 1 lowercase letter.")
        elif not has_uppercase:
            print("Invalid Password! There should be atleast 1 uppercase letter.")
        elif not has_digits:
            print("Invalid Password! There should be atleast 1 digit.")
        elif not has_special:
            print("Invalid Password! There should be atleast 1 special character.")
        else:
            print(f"Your password'{password}' is valid.")
            break
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
        break
    except EOFError:
        print("\n\nNo input detected.")
        break
    except Exception as e:
        print(f"\n\nAn unexpected error occurred: ",{e})