import re  # Import the regular expressions (regex) module

# Take user input for email and remove any leading/trailing spaces
email = input("What's your Email? ").strip()

# Check if the email matches the specified pattern using regex
# ^        : Ensures that the pattern starts at the beginning of the string
# \w+      : Matches one or more word characters (letters, digits, or underscores) before the @
# @        : The literal "@" symbol separating the local part from the domain
# (\w+\.)? : Optional part (due to ?) that matches a subdomain (e.g., sub.domain.com) before the main domain
# \w+      : Matches the domain part (letters, digits, or underscores)
# \.       : Escapes the dot, which separates the domain and the extension
# (com|edu|gov|net): Matches one of the allowed domain extensions: com, edu, gov, or net
# $        : Ensures the pattern matches until the end of the string
# re.IGNORECASE : Makes the regex case-insensitive (so "EMAIL@EXAMPLE.COM" is treated the same as "email@example.com")
if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net)$", email, re.IGNORECASE):
    print("valid")  # If the regex pattern matches, the email is valid
else:
    print("Invalid")  # If the pattern doesn't match, the email is invalid
