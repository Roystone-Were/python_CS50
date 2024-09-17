# Python Code Example

This document contains a simple Python code snippet that demonstrates how to:

1. Prompt the user for their name.
2. Remove any leading or trailing whitespace from the input.
3. Capitalize the first letter of the name.
4. Print a greeting message with the formatted name.

## Code Snippet

```python
name = input("What is your Name?\n")  # Prompts the user for their name

# Removes leading and trailing whitespaces from the input string
name = name.strip()

# Capitalizes the first letter of the string
name = name.capitalize()

# Prints a greeting message with the formatted name
print(f"Hello, {name}")
