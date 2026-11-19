import re
text = "My Birhtday is on 2026-11-18"
pattern = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})") # naming groups
date = pattern.search(text)
print("Date:", date.group(0))
print("Year:", date.group("year")) # using group's name
print("Month:", date.group("month"))
print("Day:", date.group("day"))
## another wayu
date = date.groupdict()
print(date["year"])