try:
    # Code that might raise an exception
    number = 4
    result = 10 / number
except ValueError:
    # Handles invalid input type
    print("Invalid input! Please enter a numeric value.")
except ZeroDivisionError:
    # Handles division by zero
    print("You cannot divide by zero!")
else:
    # Code that runs ONLY if no exceptions were raised in the try block
    print(f"Division successful! Result is: {result}")
finally:
    # Code that ALWAYS runs, regardless of success or failure (often used for cleanup)
    print("Program execution completed.")

