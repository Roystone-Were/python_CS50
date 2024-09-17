# Python Code Example

This document contains a simple Python code snippet that demonstrates how to:

1. Prompt the user for their name.
2. Remove any leading or trailing whitespace from the input.
3. Capitalize the first letter of the name.
4. Print a greeting message with the formatted name.

## Code Snippet

```python
# --\n-- prints to Next line
name = input("What is your Name?\n") 

#-.strip()-- removes whitespaces on strings and --.title()-- capitalizes The First letters of Each Name String
name = name.strip().title()

print(f"Hello, {name}")