import random
import string
length = int(input("How many character shou procude ?:"))
def random_user_id(length):
    if length <= 0:
        return "Length must be greater than zero"
    characters = string.ascii_letters + string.digits
    user_id = ""
    for _ in range(length):
        user_id += random.choice(characters)
    return user_id
print(random_user_id(length))