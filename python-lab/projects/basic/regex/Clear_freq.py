import re
from collections import Counter
txt = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text)
def most_frequent(text):
    words = text.split()
    top_three = Counter(words).most_common(3)
    return [(count, word) for word, count in top_three]

cleaned_text = clean_text(txt)
print(cleaned_text)
print(most_frequent(cleaned_text))