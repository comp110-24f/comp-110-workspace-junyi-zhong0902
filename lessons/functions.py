"""Practice with functions."""

from random import randint

print(randint(1, 10))


# Define a function
def sum(num_1: int, num_2: int) -> int:
    """return num1 + num2"""
    return num_1 + num_2


# Call the function
print(sum(num_1=1, num_2=10))  # 1 and 10 are arguments
