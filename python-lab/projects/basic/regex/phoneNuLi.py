import re
import phonenumbers
#from phonenumbers import timezone
#from phonenumbers.carrier import name_for_number


text = input("Enter your text here :")
#text = """
# Contact:
# +93782280415
# +12025550123
# +447911123456
# """
pattern = re.compile(r'\+\d{7,15}')
numbers = re.findall(pattern, text)
for number in numbers:
    n = phonenumbers.parse(number, None)
    r = phonenumbers.parse(number, "Ro")

    coutry_code = n.country_code
    country = phonenumbers.region_code_for_number(n)
    is_valid = phonenumbers.is_valid_number(n)
    #carr = carrier.name_for_number(r, "en")
    #timezone.time_zones_for_number(t)
    print("Number:", number)
    print("Country Code:", coutry_code)
    print("Country:", country)
    print("Valid:", is_valid)
    print("Carrier:", carr)
    print("-" * 30)


