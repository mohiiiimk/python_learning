"""Practice: exceptions, input validation, try/except/else, pass, and return."""


# Exercise 1: Age entry
while True:
    try:
        age = int(input("How old are you? "))
        print(f"Age accepted: {age}")
        break
    except ValueError:
        print("Please enter a whole number")


# Exercise 2: Coordinate reader
def main_point():
    x, y = get_point("Point? ")
    print(f"Point: ({x}, {y})")


def get_point(prompt):
    while True:
        try:
            x, y = input(prompt).split(",")
            x = float(x)
            y = float(y)
            return x, y
        except ValueError:
            pass


# Exercise 3: Discount calculator
def main_cost():
    total = cost_calculator("How much is the price? And how many? ")
    print(f"Final price is: {total:.2f}")


def cost_calculator(prompt):
    while True:
        try:
            price, quantity = input(prompt).split()
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            print("Invalid input")
        else:
            total = price * quantity
            if total >= 100:
                total = 0.9 * total
            return total


# Exercise 4: Grade parser
def main_grade():
    grade = get_grade("What is your grade? ")

    if grade is not None:
        if grade >= 60:
            print(f"Score: {grade:.1f}%", "Result: pass", sep="\n")
        else:
            print(f"Score: {grade:.1f}%", "Result: fail", sep="\n")


def get_grade(prompt):
    try:
        up, down = input(prompt).split("/")
        grade = (int(up) / int(down)) * 100
        return grade
    except ValueError:
        print("Invalid format")
    except ZeroDivisionError:
        print("Total cannot be zero")


if __name__ == "__main__":
    # Run one exercise at a time by uncommenting it.
    # main_point()
    # main_cost()
    # main_grade()
    pass
