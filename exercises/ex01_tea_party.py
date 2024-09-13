"""Junyi (Johnny) Zhong's tea party exercise."""

__author__ = "730776350"


"""This function calculates the number of tea bags 
needed given how many people will attend the tea party"""


def tea_bags(people: int) -> int:
    """return how many bags needed"""
    return people * 2


"""This function calculates the number of treat needed 
given how many people will attend the tea party"""


def treats(people: int) -> int:
    """return how many treats needed"""
    return int(tea_bags(people=people) * 1.5)


"""This function calculates the total cost of the tea 
party given the number of bags and treats."""


def cost(tea_count: int, treat_count: int) -> float:
    """return total costs"""
    return tea_count * 0.5 + treat_count * 0.75


def main_planner(guests: int) -> None:
    """Print out the number of people that is planned attend the party"""
    print("A Cozy Tea Party for", guests, "People!")
    """Print out the expected number of tea bags needed for the party"""
    print("Tea Bags:", tea_bags(people=guests))
    """Print out the expected number of treat needed for the party"""
    print("Treats:", treats(people=guests))
    """Print out the expected cost for the party"""
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
