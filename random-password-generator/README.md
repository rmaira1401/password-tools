# Random Password Generator (CLI)

A command-line tool that generates a strong, random 12-character password and guarantees it satisfies a defined set of security rules before returning it.

## Features

- Generates a random password using a mix of lowercase letters, uppercase letters, digits, and special characters
- Guarantees at least one character from each required category
- Randomizes character order using `random.shuffle` so output isn't predictable
- Validates every generated password against the same rule set before returning it, automatically retrying if a generated password doesn't pass

## How to Run

```bash
python password_generator.py
```

Running the script immediately prints a randomly generated, rule-compliant password.

## Example

```
Here is your password:  qT9$mLp2Xz!k
```

## How It Works

1. One character is randomly chosen from each required category (lowercase, uppercase, digit, special character) to guarantee all rules can be met.
2. The remaining characters are filled in randomly from the combined pool of all categories.
3. The full character list is shuffled so the guaranteed characters aren't always in the same position.
4. The result is validated against the rule set; if it somehow fails, the function calls itself again to generate a fresh password.

## What This Demonstrates

- Use of Python's `random` module for secure-feeling randomization
- Function design: separating "build a password" logic from "check a password" logic
- Recursive retry logic to guarantee output correctness

## Possible Improvements

- Use the `secrets` module instead of `random` for cryptographically stronger randomness
- Replace the recursive retry with a `while` loop
- Make password length configurable instead of hardcoded
