# Interactive Password Generator (CLI)

An interactive command-line tool that generates passwords based on user-selected requirements (character types) and a user-defined length, with input validation and a repeatable menu loop.

## Features

- Menu-driven interface: generate a password or exit
- User selects which character types to include (lowercase, uppercase, digits, special characters, or all)
- Requires at least 2 character-type selections to be chosen
- Enforces a minimum password length of 8 characters
- Automatically adjusts the length upward if it's too short to fit all selected character types
- Re-prompts on invalid menu choices or invalid requirement selections instead of crashing
- Lets the user generate multiple passwords in one session without restarting the program

## How to Run

```bash
python password_generator_interactive.py
```

## Example

```
Please select one option:
1. Generate a random password
2. Exit program
1
What should be the password length? 10
Please select your requirements:
a. Lowercase letters
b. Uppercase letters
c. Digits
d. Special Characters
e. Combination of all
Enter your options (a to d or e): ac
Here is your password: 9fT2pXq7v0
Would you like to generate another password? (yes/no) no
```

## How It Works

1. `main()` runs a loop that displays the menu and reads the user's choice.
2. If the user chooses to generate a password, they're asked for a length (minimum 8) and which character types to include.
3. `generate_password()` builds one guaranteed character for each selected type, then fills the remaining length randomly from the combined pool of selected types.
4. If the requested length is too short to fit every selected requirement, the length is automatically increased to fit.
5. The final list of characters is shuffled and joined into the returned password string.
6. The user is asked if they'd like to generate another password or exit; the loop repeats or ends accordingly.

## What This Demonstrates

- Separation of concerns: password-building logic (`generate_password`) is kept independent of the menu/input logic (`main`)
- Defensive input validation: guarding against invalid menu choices, too-few requirement selections, invalid/empty requirement input, and passwords too short for the chosen requirements
- Designing a repeatable CLI loop driven by user interaction

## Possible Improvements

- Replace the letter-based menu (`a`, `b`, `c`...) with `argparse` command-line flags for non-interactive use
- Consolidate the two separate length-validation checks (in `main` and `generate_password`) into a single place
- Add a "validate an existing password" option to the menu, reusing the rules from the standalone validator project
- Use `secrets` instead of `random` for stronger randomness guarantees
