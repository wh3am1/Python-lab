names = ["ali", "Masoud", "Mostafa", "Mahmood"]
ports = range(20, 26)
for i, name in enumerate(names, start=1):
    print(i, name)
for i, port in enumerate(ports, start=1):
    print(f"Try: {port}; port {ports}")