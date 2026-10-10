"""Engineering practice: pressure conversion."""

def convert_pressure(pressure_pa):
    return pressure_pa / 1000


pressure_pa = float(input("Pressure in Pa: "))
pressure_kpa = convert_pressure(pressure_pa)

rounded_pressure = round(pressure_kpa, 2)
formatted_pressure = f"{pressure_kpa:.2f}"

print(f"Pressure: {rounded_pressure} kPa")
print(f"Formatted display: {formatted_pressure} kPa")
