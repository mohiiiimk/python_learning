"""Practice: while, for, range, list, index, break, continue, and combined logic."""

# While loop
temperature = 20

while temperature < 100:
    temperature += 10
    print(temperature)

# continue and break
for number in range(1, 11):
    if number == 5:
        continue
    if number == 8:
        break
    print(number)

# Input validation with while
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        continue
    if number == 0:
        break
    print(number)

# List and index
equipment = ["pump", "fan", "compressor", "turbine"]
print(equipment[0])
print(equipment[2])

for item in equipment:
    print(item)

# Loop + conditionals
temperatures = [72, 85, 91, 68, 100]

for temperature in temperatures:
    if temperature >= 90:
        print(f"{temperature} High")
    elif temperature >= 80:
        print(f"{temperature} Warning")
    else:
        print(f"{temperature} Normal")

# Pressure filtering
pressures = [1.2, 2.5, 3.8, 1.9, 4.1]

for pressure in pressures:
    if pressure > 4:
        print(f"{pressure} Critical")
    elif pressure > 2:
        print(pressure)

# continue with invalid values
pressures = [2.5, -1, 3.2, 0, 4.8, -0.5, 1.7]

for pressure in pressures:
    if pressure < 0:
        continue
    if pressure == 0:
        print("Zero Pressure")
    else:
        print(f"Pressure: {pressure}")

# Printing horizontally and vertically
for _ in range(5):
    print("*", end="")
print()

for _ in range(5):
    print("*")

# Function + loop + conditionals + return
def check_temperatures(temperatures):
    results = []

    for temperature in temperatures:
        if temperature < 0:
            continue
        if temperature >= 90:
            results.append("High")
        elif temperature >= 80:
            results.append("Warning")
        else:
            results.append("Normal")

    return results


sample_temperatures = [72, -5, 85, 93, 68]
print(check_temperatures(sample_temperatures))
