# Password Tools

A small collection of command-line Python tools for validating and generating passwords, built as a progression: starting with a basic rule-based validator, then a simple random generator, and finally an interactive generator that combines both ideas with user-driven requirements.

## Projects

| Project | Description |
|---|---|
| [1. Password Validator](./1-password-validator) | Checks a password against a set of security rules and reports exactly which rule failed. |
| [2. Random Password Generator](./2-random-password-generator) | Generates a random, rule-compliant password with no user input required. |
| [3. Interactive Password Generator](./3-password-generator-with-preferences) | Menu-driven tool where the user chooses password length and which character types to include, with input validation and a repeatable session loop. |

Each subfolder has its own README with setup instructions, usage examples, and notes on how that project works.

## Why These Three Together

These projects build on each other and were developed in this order:

1. **Validation first** — establishing the rule set (length, character types) that defines what a "strong" password looks like.
2. **Generation second** — reusing that same rule set to produce compliant passwords automatically, with a retry mechanism to guarantee correctness.
3. **User control third** — extending generation so the user can choose their own requirements and length, with defensive input handling throughout.

## Requirements

- Python 3.x (no external dependencies — uses only the standard library: `string`, `random`)

## Running Any Project

```bash
cd <project-folder>
python <script-name>.py
```

See each project's own README for exact filenames and example output.

## Skills Demonstrated

- Core Python: string manipulation, loops, conditionals, functions, recursion
- Input validation and defensive programming (handling invalid, missing, or malformed user input)
- Exception handling
- Iterative development and refactoring (separating input/menu logic from core logic as the project grew)
- Writing project documentation

## Possible Future Additions

- Convert to `argparse`-based CLIs for non-interactive/scriptable use
- Add unit tests (`pytest`) covering the validation rules and generator output
- Merge shared rule logic into a single reusable module imported by all three tools
- Replace `random` with `secrets` for cryptographically secure password generation
