"""Junyi (Johnny) Zhong's first Code Challenge"""

__author__ = "730776350"

"""Write my own function. This function will repeat my input"""


def mimic(message: str) -> str:
    return message


"""Main function pulls together the functinons that I previously wrote.
It implements high level logic of my program"""


def main() -> None:
    # Nested function call: because it calls a function in
    # a function(arguement from mimic has been passed to the print function)
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
