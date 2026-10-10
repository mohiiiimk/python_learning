"""Engineering practice: Blade Passing Frequency calculator."""

def calculate_bpf(rpm, number_of_blades):
    bpf = rpm / 60.0 * number_of_blades
    return bpf


rpm, number_of_blades = input("Enter RPM and number of blades: ").split()

frequency = calculate_bpf(float(rpm), int(number_of_blades))
print(f"BPF: {frequency:.2f} Hz")
