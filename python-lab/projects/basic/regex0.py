#! python3
# PhoneandEmail.py
# Find phone numbers and email addresses on the clipboard
import re
import pyperclip
# ==========================
#   PHONE NUMBER REGEX
# =========================

phoneRegex = re.compile(r'''(
     (\d{3}|\(\d{3}\))?
     (\s|-|\.)?
     (\d{3})
     (\s|-|\.)
     (\d{4})
     (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

#=========================
# EMAIL ADDRESS REGEX
#=========================
emailRegex = re.compile(r'''(
    [a-zA-Z0-9.+%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

#  GETTING TEXT FROM CLIPBOAD
text = str(pyperclip.paste())

# FIND ALL MATCHES
match = []
for grups in phoneRegex.findall(text):
    phoneNum = '_'.join([
        groups[1],
        groups[3],
        groups[5]
    ])
    if grups[8] != '':
        phoneNum += ' x' + groups[8]
        matche.append(groups[0])
# FIND EMAIL ADDRESSES
for groups in emailRegex.findall(text):
    match.append(group[0])

print(match)