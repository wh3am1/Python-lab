import math
from fractions import Fraction
from unittest import result

history = []
def calculate_sqrt():
    n = int(input("Number: "))
    r = math.sqrt(n)
    result = math.trunc(r)
    print(f"Result: {result}")
    history.append(result)
def calculate_factorial():
    n = int(input("Number: "))
    result = math.factorial(n)
    print(f"Result: {result}")
    history.append(result)

def calculate_gcd():
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    result = math.gcd(n1, n2)
    print(f" Square Root: {result}")
    history.append(result)

def calcualte_lcm():
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    result = math.lcm(n1, n2)
    print(f"LCM: {result}")
    history.append(result)

def calcualte_sin_cos_tan():
    n = int(input("Number: "))
    rs = math.sin(n)
    rc = math.cos(n)
    rt = math.tan(n)
    sin = math.trunc(rs)
    cos = math.trunc(rc)
    tan = math.trunc(rt)
    print("\n--- The Angles ---")
    print(f"Sin: {sin}")
    print(f"Cos: {cos}")
    print(f"Tan: {tan}")
    print("------------------------")
    history.append(sin)
    history.append(cos)
    history.append(tan)
def calcualte_fraction():

    print("\n1. add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Select the Operation: ")

    n1 = int(input("Fraction 1 numerator: "))
    d1 = int(input("Fraction 1 Denominator: "))

    n2 = int(input("Fraction 2 numerator: "))
    d2 = int(input("Fraction 2 Denominator: "))

    f1 = Fraction(n1, n2)
    f2 = Fraction(n1, n2)

    if choice == "1":
        result = f1 + f2
    elif choice == "2":
        result = f1 - f2
    elif choice == "3":
        result = f1 * f2
    elif choice == "4":
        result = f1 / f2
    else:
        print("Invalid error")
        return
    print(f"Result: {result}")
    history.append(result)

def show_history():
    for item in history:
        print(item)

while True:
    print("\n1. Sqrt")
    print("2. Factorial")
    print("3. GCD")
    print("4. LCM")
    print("5. Sin, Cos && Tan")
    print("6. Fraction")
    print("7. History")
    print("8. Exit")

    choice = input("Select an option: ")
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid Option")
    elif choice == "8":
        print("Good Bye")
        break
    elif choice == "1":
        calculate_sqrt()
    elif choice == "2":
        calculate_factorial()
    elif choice == "3":
        calculate_gcd()
    elif choice == "4":
        calcualte_lcm()
    elif choice == "5":
        calcualte_sin_cos_tan()
    elif choice == "6":
        calcualte_fraction()
    elif choice == "7":
        show_history()
    else:
        pass
