"""Engineering practice: simple efficiency calculation."""

def calculate_efficiency(output_power, input_power):
    return output_power / input_power * 100


output_power = float(input("Output power: "))
input_power = float(input("Input power: "))

efficiency = calculate_efficiency(output_power, input_power)

print(f"Efficiency: {efficiency:.2f}%")
