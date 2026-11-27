import random
import string

def random_id_by_usr():
    length = int(input("How many characters ?"))
    count = int(input("How many IDs?"))
    characters = string.ascii_letters + string.digits
    for _ in range(count):
        user_id = ""
        for _ in range(length):
            user_id += random.choice(characters)
        print(user_id)
print(random_id_by_usr())