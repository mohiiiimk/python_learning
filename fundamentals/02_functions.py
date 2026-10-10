"""Practice: functions, parameters, return values, scope, and formatting."""

def calculate_efficiency(output_power, input_power):
    efficiency = output_power / input_power * 100
    return efficiency


def convert_pressure(pressure_pa):
    pressure_kpa = pressure_pa / 1000
    return pressure_kpa


def get_positive_number():
    while True:
        number = int(input("Enter a positive number: "))
        if number > 0:
            return number


def meow(number):
    for _ in range(number):
        print("meow")


def main():
    efficiency = calculate_efficiency(875, 1000)
    print(efficiency)
    print(round(efficiency, 1))
    print(f"{efficiency:.2f}")

    pressure = convert_pressure(2000)
    rounded_pressure = round(pressure, 2)
    formatted_pressure = f"{pressure:.2f}"

    print(pressure)
    print(rounded_pressure)
    print(formatted_pressure)

    number = get_positive_number()
    meow(number)


if __name__ == "__main__":
    main()
