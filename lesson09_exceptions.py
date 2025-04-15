# Exception Handling Example

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input types!")
    else:
        print("Result:", result)
    finally:
        print("Execution completed.\n")

# Examples
divide_numbers(10, 2)
divide_numbers(5, 0)
divide_numbers("10", 2)
