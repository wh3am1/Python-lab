
data = [10, 4, 5, 10, 5, 4, 4, 4, 4, 3, 7, 8]
## then sort and delete repeated num
unique_sorted = sorted(set(data))
## empty dic to store the final info
result = {}

## check if number is odd or even
for num in unique_sorted:
    if num % 2 == 0:
        result[num] = "even"
    else:
        result[num] = "odd"

match len(result):
    case 3:
        status = "low"
    case 4:
        status = "medium"
    case _:
        status = "high"
print(result)
print(status)