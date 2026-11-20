import re
email = input("Enter your text here to find emails :")
pattern = re.compile(r"[a-zA-Z0-9_.+*%]+@[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,4})", re.VERBOSE)
match = re.search(pattern, email)

if match:
    print("Email:", match.group())
