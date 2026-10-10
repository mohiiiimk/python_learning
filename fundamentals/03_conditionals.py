"""Practice: if/elif/else, and/or, bool, match, and parity."""

# Temperature status
temperature = float(input("What is the temperature? "))

if temperature >= 100:
    print("High")
elif temperature >= 80:
    print("Warning")
else:
    print("Normal")

# Temperature and pressure status
temperature = int(input("Temperature? "))
pressure = int(input("Pressure? "))

if temperature > 120 or pressure > 5:
    print("Critical")
elif temperature >= 80 and pressure >= 2:
    print("Warning")
else:
    print("Normal")

# Parity
number_of_blades = int(input("Number of blades? "))

if number_of_blades % 2 == 0:
    print("Even")
else:
    print("Odd")


def is_hot(temperature):
    return temperature > 80


temperature = int(input("What is the temperature? "))

if is_hot(temperature):
    print("Hot")
else:
    print("Not hot")

# match/case
equipment = input("What equipment? ").strip().lower()

match equipment:
    case "pump":
        print("Liquid machine")
    case "fan":
        print("Air-moving machine")
    case "compressor":
        print("Gas compression machine")
    case _:
        print("Unknown equipment")
