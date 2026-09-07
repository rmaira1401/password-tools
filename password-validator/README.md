# Password Validator (CLI)

A simple command-line tool that checks whether a password meets a set of security rules, and tells the user exactly which rule failed.

## Features

- Validates a password against five rules:
  - At least 8 characters long
  - Contains at least 1 lowercase letter
  - Contains at least 1 uppercase letter
  - Contains at least 1 digit
  - Contains at least 1 special character
- Gives specific, rule-by-rule feedback instead of a generic pass/fail message
- Keeps prompting until a valid password is entered
- Handles unexpected interruptions gracefully (e.g. `Ctrl+C`, empty input, unexpected errors)

## How to Run

```bash
python password_validator.py
```

You'll be prompted to enter a password. If it fails validation, the program tells you which specific rule wasn't met and asks you to try again. Once a valid password is entered, it confirms and exits.

## Example

```
Please enter your password:
abc
Invalid Password! It should be atleast 8 characters long.
Please enter your password:
abcdefgh
Invalid Password! There should be atleast 1 uppercase letter.
Please enter your password:
Abcdefg1!
Your password'Abcdefg1!' is valid.
```

## What This Demonstrates

- String manipulation and character-type checks using Python's `string` module
- Control flow with loops and conditionals
- Exception handling (`try`/`except`) for interrupted or invalid input

## Possible Improvements

- Move the rule set into a shared module so it can be reused by a password generator
- Add unit tests for each validation rule
- Support reading passwords without echoing them to the terminal (`getpass`)
