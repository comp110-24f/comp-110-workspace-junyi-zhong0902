"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730776350"


def input_word() -> str:
    """this function takes input from the user
    the input has to be a 5 letter word"""
    input_word: str = input("Enter a 5-character world:")  # take input
    if (
        len(input_word) == 5
    ):  # use if statement to check if the input is a 5 letters word
        return input_word
    else:
        print("Error: Word must contain 5 characters.")
        return input_word


def input_letter() -> str:
    """this function takes input from the user,
    the letter has to be a single letter"""
    input_letter: str = input("Enter a single character:")  # take input
    if (
        len(input_letter) == 1
    ):  # use if statement to check if the input is only one letter
        return input_letter
    else:
        print("Error: Character must be a single character.")
        return input_letter


def contains_char(word: str, letter: str) -> None:
    """this function takes the word and the letter from user input in previous function
    and then compare if the letter exist in the word"""
    found_letter: int = (
        0  # declare a local variable for counting purpose (how many letters are found)
    )
    print("Searching for", letter, "in", word)
    """following if statements are used to compare inputted letter to each letter in the word"""
    if letter == word[0]:
        print(letter, "found at index 0.")
        found_letter = found_letter + 1
    if letter == word[1]:
        print(letter, "found at index 1.")
        found_letter = found_letter + 1
    if letter == word[2]:
        print(letter, "found at index 2.")
        found_letter = found_letter + 1
    if letter == word[3]:
        print(letter, "found at index 3.")
        found_letter = found_letter + 1
    if letter == word[4]:
        print(letter, "found at index 4.")
        found_letter = found_letter + 1
    if found_letter == 0:  # print result
        print(
            "No instances of",
            letter,
            "found in",
            word,
        )
    else:
        print(found_letter, "instance of", letter, "found in", word)

    return None


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
