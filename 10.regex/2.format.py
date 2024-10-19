import re  # Importing the 're' module to work with regular expressions.

name = input("Whats your Name? ").strip()
# Prompting the user to input their name, and 'strip()' is used to remove any leading or trailing whitespace.

if matches := re.search(r"^(.+), *(.+)$", name):
    # Using a regular expression to match the input in the format 'Last, First'.
    # - ^ asserts the beginning of the string.
    # - (.+) matches one or more of any characters (except newline) and captures this as the last name before the comma.
    # - , matches the literal comma.
    # - * matches zero or more spaces after the comma.
    # - (.+) captures the first name after the spaces.
    # - $ asserts the end of the string.
    # The 're.search()' function finds this pattern in the string. If found, 'matches' holds the result.
    
    last, first = matches.groups()
    # The 'groups()' method extracts the matched groups.
    # The first group (matches.group(1)) is the last name, and the second group (matches.group(2)) is the first name.

    name = matches.group(2) + " " + matches.group(1)
    # Reformatting the name to "First Last" by swapping the order of the matched groups.
    # 'matches.group(2)' is the first name, and 'matches.group(1)' is the last name.

print(f"hello,{name}")
# Printing a greeting with the newly formatted name (first name followed by last name).
