import enum from Enum
class color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

color = color(input("Enter your color"))

match color:
    case color.RED:
        print("I am red")
    case color.BLUE:
        print("I am blue")
    case color.GREEN:
        print("I am green")