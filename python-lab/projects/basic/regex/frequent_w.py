import re
from collections import Counter
paragraph = "    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
match = re.findall(r"\w+", paragraph, re.I)
result = Counter(match)
print(result.most_common(1))