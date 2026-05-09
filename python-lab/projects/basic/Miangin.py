number = int(input("Enter your number: "))

jam_a = 0
tedda_a = 0

while number != -1:
    jam_a += number
    tedda_a += 1

    number = int(input("Enter your number: "))

miangin = jam_a / tedda_a

print(miangin)