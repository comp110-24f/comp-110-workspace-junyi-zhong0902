"""My first exercise in COMP110."""

__author__ = "730776350"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


"""function call expression."""
greet(name="Johnny")


def total_cost(price: int, tax_rate: float):
    return price + (price * tax_rate)


print(total_cost(price=100, tax_rate=0.07))
