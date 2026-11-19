import re
PhoneNum = input("Enter your Number with Country code :")
pattern = re.compile(r"^(?:0093|\+93)(7[1-9])\d{7}$")
operators = {
    "78": {"name": "Etisalat", "Price": 250},
    "79": {"name": "Roshan", "Price": 100},
    "76": {"name": "MTN", "Price": 58}
}

match = pattern.match(PhoneNum)

if match:
    code = match.group(1)
    print("PhoneNumber:", match.group())
    info = operators.get(code)
    if info:
        print("operator:", info["name"])
        print("Price:", info["Price"])
    else:
        print("Unknown Code Number")
else:
    print("Phone Number Not Found.")