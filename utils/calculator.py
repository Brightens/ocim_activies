def calc(operator: str, num_1: int, num_2: int):
    """
    Basic Calculator.
    """
    operations = {
        "+": num_1 + num_2,
        "-": num_1 - num_2,
        "*": num_1 * num_2,
        "/": num_1 / num_2 if num_2 != 0 else "Cannot divide by zero"
    }

    output = operations.get(operator, "Invalid operator")

    print(f"Result: {output}")
    return output