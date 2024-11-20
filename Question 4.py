import _thread
import time


# Reference: https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm
def calculate(number1, number2, operation):
    """ Function to perform the specified operation on the two numbers given.
        Returns the result.
    """
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        return number1 / number2


def print_result(number1, number2, operation):
    """ Function to call calculate() and print the result in proper statement.
    """
    result = calculate(number1, number2, operation)
    print(f'\n{number1} {operation} {number2} = {int(result)}', end='')


# Get 2 numbers from the user
number_1 = int(input("Enter number 1: "))
number_2 = int(input("Enter number 2: "))

# Create one thread for each operation
_thread.start_new_thread(print_result, (number_1, number_2, "+",))
_thread.start_new_thread(print_result, (number_1, number_2, "-",))
_thread.start_new_thread(print_result, (number_1, number_2, "*",))
_thread.start_new_thread(print_result, (number_1, number_2, "/",))

# Delay the main process so that it finishes after all threads finished
time.sleep(10)
