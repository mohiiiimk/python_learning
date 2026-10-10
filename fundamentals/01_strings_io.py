"""Practice: input/output, strings, formatting, split, type conversion."""

# Welcome message
name = input("What is your name? ")
print(f"Welcome, {name}!")

# First and last name
first_name = input("What is your first name? ").strip().capitalize()
last_name = input("What is your last name? ").strip().capitalize()
print(f"{first_name} {last_name}")

# Equipment name
equipment = input("What is your selected equipment? ").strip().title()
print(f"Selected equipment: {equipment}")

# Lowercase a sentence
sentence = input("What sentence do you want in lowercase? ")
print(sentence.lower())

# Temperature label
label = input("Temperature label: ").strip().lower()
print(f"Temperature label: {label}")

# Fluid name
fluid = input("Selected fluid: ").strip().title()
print(f"Selected Fluid: {fluid}")

# Split into two variables
equipment_type, equipment_name = input(
    "Enter equipment type and equipment name: "
).split()
print(f"Type: {equipment_type}")
print(f"Equipment: {equipment_name}")

# Two input values
temperature, pressure = input("Enter temperature and pressure: ").split()
print(f"Temperature is: {temperature}")
print(f"Pressure is: {pressure}")

# Integer temperature change
temperature, delta = input(
    "Enter integer temperature and temperature change: "
).split()
print(f"New temperature is: {int(temperature) + int(delta)}")

# Float temperature change
temperature, delta = input(
    "Enter decimal temperature and temperature change: "
).split()
print(f"New temperature is: {float(temperature) + float(delta)}")

# Number formatting
value = 1234567.895
print(f"{value:,.2f}")
