from numbers import Number
from math import sqrt
from math import trunc
from datetime import datetime

# an empty list to store history data
history = []

""" A function that analyze the number 
and save the resutls into history list """
def analyze(num):
    root = trunc(sqrt(num))
    #if isinstance(root, float) and root.is_integer():
        #root = int(root)
    if not isinstance(num, Number):
        return "Not Number"
    result = {
        "number": num,
        "square": num ** 2,
        "sqrt": root,
        "time": datetime.now()
    }
    print("\n ======  RESULT  ======")
    print(f"Number : {result['number']}")
    print(f"Square : {result['square']}")
    print(f"Sqrt   : {result['sqrt']}")
    print(f"Time : {result['time']}")
    print("=========================")
    history.append(result)

## Function that show history to user
def show_history():
    for item in history:
        print(item)


while True:
    print("\n1. Analyze Number")
    print("2. Show History")
    print("3. Exit")
    choice = input("Choice: ")


    if choice not in ["1", "2", "3"]:
        print("Invalid error")

    elif choice == "1":
        try:
            num = float(input("Enter Number: "))
            result = analyze(num)
            print("\nResult")
            print(result)
        except ValueError:
            print("Invalid Number")
    elif choice == "2":
       show_history()
    elif choice == "3":
        break