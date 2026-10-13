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


# Exercise 5: D+1 review — multiple exception handlers
def division_review():
    try:
        number_one, number_two = input("Give me two numbers: ").split()
        number_one = float(number_one)
        number_two = float(number_two)
        division = number_one / number_two
    except ValueError:
        print("Invalid input")
    except ZeroDivisionError:
        print("Number two cannot be zero")
    else:
        print(division)


# Exercise 6: Raising exceptions — age validator
def main_age_validator():
    try:
        age = get_valid_age("How old are you? ")
    except ValueError as error:
        print(error)
    else:
        print(age)


def get_valid_age(prompt):
    age = int(input(prompt))

    if age <= 0:
        raise ValueError("Age cannot be negative")
    elif age > 120:
        raise ValueError("Age is unrealistic")
    else:
        return age


# Exercise 7: Raising exceptions — username validator
def main_username():
    try:
        name = input("Type your username: ")
        validate_username(name)
    except ValueError as error:
        print(error)
    else:
        print(f"Username accepted: {name}")


def validate_username(username):
    if len(username) < 4:
        raise ValueError("Username is too short")
    elif " " in username:
        raise ValueError("Username cannot contain spaces")
    elif not username.isalnum():
        raise ValueError("Username must be alphanumeric")
    else:
        return username


if __name__ == "__main__":
    # Run one exercise at a time by uncommenting it.
    # main_point()
    # main_cost()
    # main_grade()
    # division_review()
    # main_age_validator()
    # main_username()
    pass
